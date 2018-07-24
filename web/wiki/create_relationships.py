from convert_edge_to_page import get_nodename_by_uid
import os.path
import json
import sys

INCLUDESPATH = "_includes/relationships"

def write_rels_from_edge(edge_filename):
    with open(edge_filename, "r") as edge_file:
        edge = json.load(edge_file)
        #TODO validate edge
        link_type = edge["link_type"]
        dest_node_uid = edge["dest_node"]
        dest_name = get_nodename_by_uid(dest_node_uid)
        dest_rel_filename = "".join([INCLUDESPATH, "/", str(dest_node_uid), "_rel.html"])
        for source_node_uid in edge["source_nodes"]:
            node_rel_filename = "".join([INCLUDESPATH, "/", str(source_node_uid), "_rel.html"])
            source_name = get_nodename_by_uid(source_node_uid)
            relationship = "%s %s %s\n" % (source_name, link_type, dest_name)
            write_to_rel_file(node_rel_filename, relationship)
            write_to_rel_file(dest_rel_filename, relationship)

def write_to_rel_file(rel_filename, relationship):
    """Write relationship to uid_rel.html file, creating it if necessary"""
    if not os.path.isfile(rel_filename):
        with open(rel_filename, "w") as f:
            f.write("<h4>Relationships with other nodes</h4>\n")
    with open(rel_filename, "a") as f:
        f.write("".join(["<p>", relationship, "</p>\n"]))

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_relationships.py edge_file.json")
    else:
        write_rels_from_edge(sys.argv[1])




