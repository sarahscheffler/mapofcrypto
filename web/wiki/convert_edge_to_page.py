from jsonschema import validate, ValidationError
import sys
import json
import os
import re

REPLACEMENT_TEXT = "!!!ADDEDGES!!!"
PAGES = "pages"

def edge_to_html(edge_filename, output_filename, schema_filename):
    """Convert an edge verified with check_schema.py into a page about the
    edge for the jekyll site"""

    ### Validate schema
    with open(edge_filename, "r") as edge_file:
        edge = json.load(edge_file)
        with open(schema_filename, "r") as schema_file:
            sch = json.load(schema_file)
            try:
                validate(edge, sch["edge_schema"])
            except ValidationError as e:
                print("File %s did not validate as edge against schema %s" %
                        (edge_filename, schema_filename))
                print(e)
                return 1
        with open(output_filename, "w") as out:
            # Header
            out.write("---\n")
            out.write("layout: page\n")
            out.write("categories: edges\n")
            out.write("permalink: edges/%s.html\n" % edge["uid"])
            out.write("title: %s %s %s\n" %
                    (get_nodename_by_uid(edge["source_nodes"][0]),
                edge["link_type"], get_nodename_by_uid(edge["dest_node"])))
            for k in edge.keys():
                if k != "long_description":
                    out.write("%s: %s\n" % (k, edge[k]))
            out.write("---\n")
            out.write("%s" % edge.get("long_description", "No long description.  Contribute one?"))

        
def get_nodename_by_uid(uid):
    with open("".join([PAGES, "/", str(uid), ".html"]), "r") as f:
        for line in f:
            if "display_name" in line:
                return re.match(r"display_name: (.+)\n", line).group(1)



if __name__=="__main__":
    if len(sys.argv) != 4:
        print("Usage: python convert_edge_to_page.py edge_filename output_filename schema_filename")
        exit()
    else:
        edge_to_html(sys.argv[1], output_filename=sys.argv[2], schema_filename=sys.argv[3])

