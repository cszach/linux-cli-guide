#!/usr/bin/env python3
# Script used to generate image credits table in CREDITS.md.
# Data is extracted from a CSV file named "img-credits.csv"
# in the same directory as this script.
#
# NOTE: The output of this program may be incorrect. Please check to make sure
# that the rendered output of the Markdown content produced by this program is
# correct before commiting the changes.
#
# NOTE: This program should not be executed manually. It is now invoked in
# the Shell script alias-credits.sh. Please run alias-credits.sh instead.

from os.path import isfile, basename
from csv import DictReader
import logging

csvfname = "../data/img-credits.csv"

logging.basicConfig(format="%(message)s")

if not isfile(csvfname):
    logging.critical("fatal: %s not found" % csvfname)
    exit(1)

print("<!-- This table was generated using script/%s -->\n" % basename(__file__))
print("|Image|Metadata|")
print("|:---:|---|")

with open(csvfname, newline='', encoding='utf-8') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        # Set variables to make it easier to work with them later
        # fname: File name of the image (including the extension)
        # source: Possible SVG source of the image
        # authors: (Python) List of authors
        # org_authors: (Python) List of original authors
        # links: (Python) List of links to authors and original authors
        # lics: Python dictionary containing licenses' name and links to them,
        # correspondingly

        fname = row['File name']
        source = "svg/%s/%s" % (row['Subfolder'], row['Source'])
        authors = row['Author'].split(', ')
        org_authors = row['Original author'].split(', ')
        links = row['Link to author'].split(', ')
        lics = {lic_name: lic_link
                for lic_name, lic_link in zip(row['License'].split(", "), row['Link to license'].split(", "))}

        # First, work on the left cell of the row.
        # This contains the thumbnail of the image (found in /img/thumb/), and
        # links to different formats which the image is available under

        if fname[-3:].lower() != "gif":
            print("|![](img/thumb/{0})<br/><br/>[{1}](img/{2}/{0})"
                  .format(fname, fname[fname.rfind('.') + 1:].upper(), row['Subfolder']),
                  end='')
        else:
            print("<img src=\"img/{1}/{0}\" width=\"300px\"/><br/><br/>[GIF](img/{1}/{0})"
                  .format(fname, row['Subfolder']),
                  end='')
        if isfile("../" + source):
            print(" &mdash; [SVG](%s)" % source, end='')
        print("|", end='')

        # Work on the second cell

        if row['Title'] != "":
            print("**Title**: %s <br/> " % row['Title'], end='')
        print("**Shown in**: %s <br/> " % row['Shown in'], end='')
        print("**Originality**: %s <br/> " % row['Originality'], end='')

        print("**Author**: ", end='') if len(authors) == 1 \
            else print("**Authors**: ", end='')
        for author, link in zip(authors, links[:len(authors)]):
            print("[%s](%s), " % (author, link), end='') if link != "" \
                else print("%s, " % author, end='')
        print("\b\b <br/> ", end='')

        if row['Original author'] != "":
            print("**Original author%s**: " %
                  ("" if len(org_authors) == 1 else "s"), end='')
            for author, link in zip(org_authors, links[len(authors):]):
                print("%s, " % author, end='') if link == "" \
                    else print("[%s](%s), " % (author, link), end='')
            print("\b\b <br/> ", end='')

        print("**License%s**: " % ("" if len(lics) == 1 else "s"), end='')
        for lic_name, lic_link in lics.items():
            print("%s, " % lic_name, end='') if lic_link == "" \
                else print("[%s](%s), " % (lic_name, lic_link), end='')
        print("\b\b", end='')
        if row['Note'] != "":
            print("<br/> **Note**: %s" % row['Note'], end='')
        print("|")
