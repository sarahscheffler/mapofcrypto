import pybtex.database
import sys

BIBFILE = "_includes/bib/citations.bib"
INCLUDES = "_includes/bib"
FORMAT = "bibtex"

def create_bib_includes(filename):
    d = pybtex.database.parse_file(filename, bib_format=FORMAT)
    for k in d.entries.keys():
        with open("".join([INCLUDES, "/", k]), "w") as f:
            f.write(pybtex.database.BibliographyData(entries={k:
                d.entries[k]}).to_string(FORMAT))

if __name__=="__main__":
    if len(sys.argv) < 2:
        create_bib_includes(BIBFILE)
    else:
        create_bib_includes(sys.argv[1])



