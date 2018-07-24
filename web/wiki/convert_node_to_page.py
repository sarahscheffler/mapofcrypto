from jsonschema import validate, ValidationError
import sys
import json
import os

def node_to_html(node_filename, output_filename, schema_filename):
    """Convert a node verified with check_schema.py into a page about the
    node for the jekyll site"""

    ### Validate schema
    with open(node_filename, "r") as node_file:
        node = json.load(node_file)
        with open(schema_filename, "r") as schema_file:
            sch = json.load(schema_file)
            try:
                validate(node, sch["node_schema"])
            except ValidationError as e:
                print("File %s did not validate as node against schema %s" %
                        (node_filename, schema_filename))
                print(e)
                return 1
        with open(output_filename, "w") as out:
            # Header
            out.write("---\n")
            out.write("layout: page\n")
            out.write("categories: nodes\n")
            out.write("title: %s\n" % node.get("full_name", node["display_name"]))
            out.write("permalink: nodes/%s.html\n" % node["uid"])
            for k in node.keys():
                if k != "long_description":
                    out.write("%s: %s\n" % (k, node[k]))
            out.write("---\n")
            out.write("%s\n" % node.get("long_description", "No long description yet.  Contribute one?"))
            # End header
            # All actual formatting should happen within _layouts/node.html

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("Usage: python convert_node_to_page.py node_filename output_filename schema_filename")
        exit()
    else:
        node_to_html(node_filename=sys.argv[1], output_filename=sys.argv[2], schema_filename=sys.argv[3])

