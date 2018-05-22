from jsonschema import validate, ValidationError
import json
import sys

def check(to_check, schema="schema.json"):
    with open("schema.json", "r") as schema_file:
        d = json.load(schema_file)
        print(d)
        node_schema = d["node_schema"]
        edge_schema = d["edge_schema"]
        with open(to_check, "r") as to_check_file:
            data = json.load(to_check_file)
            try:
                validate(data, edge_schema) # edge schema more restrictive; check this first
            except ValidationError as edge_except:
                try:
                    validate(data, node_schema)
                except ValidationError as node_except:
                    print("File not valid")
                    print(edge_except)
                    print(node_except)
                    return
                print("Valid node")
                return
            print("Valid edge")
            return
    print("Something went wrong.")
            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_schema file_to_check.json [schema.json]")
        exit(0)
    if len(sys.argv) == 3:
        check(sys.argv[1], sys.argv[2])
    else:
        check(sys.argv[1])

