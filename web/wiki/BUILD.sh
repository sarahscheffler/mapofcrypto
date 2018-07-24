# BUILD SCRIPT FOR IMPORTING DATA TO THE WIKI
NODES=../../objects/Nodes
EDGES=../../objects/Edges
BIBFILE=../../objects/Citations/Citations.bib
NEWBIBFILE=_includes/bib/citations.bib
RELS=_includes/relationships
SCHEMA_FILE=../../schema.json
PAGES=pages

echo "Cleaning previous build..."
jekyll clean

echo "Removing old relationship files..."
rm $RELS/*

# Build pages for nodes
# TODO this is not terribly elegant.  Find a better way.
echo "Creating files..."
for node_file in $NODES/*; do
    uid="$(grep -w \"uid\"\: $node_file | sed -e 's/[\ \t]*\"uid\"\:\ //; s/,//')"
    echo "           Creating file for $node_file, uid=$uid"
    python3 convert_node_to_page.py $node_file "$PAGES/$uid.html" $SCHEMA_FILE
done

# Build pages for edges AFTER building the edge files
# This also adds the relevant edges to the nodes' pages.
for edge_file in $EDGES/*; do
    uid="$(grep -w \"uid\"\: $edge_file | sed -e 's/[\ \t]*\"uid\"\:\ //; s/,//')"
    echo "           Creating file for $edge_file, uid=$uid"
    python3 convert_edge_to_page.py $edge_file "$PAGES/$uid.html" $SCHEMA_FILE
    python3 create_relationships.py $edge_file
done

echo "Creating bibliography files..."
cp $BIBFILE $NEWBIBFILE
python3 create_bib_includes.py

echo "Done!  Run with \`jekyll serve\`"




