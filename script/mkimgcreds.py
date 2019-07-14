#!/usr/bin/env python3
# Script used to generate image credits table in CREDITS.md.
# Data is extracted from /data/img-credits.csv (CSV file).
#
# NOTE: The output of this program may be incorrect. Please check to make sure
# that the rendered output of the Markdown content produced by this program is
# correct before commiting the changes.

from os.path import isfile, basename
from csv import DictReader
import logging

# ============== DATA FILES ==============

csvfname = "../data/img-credits.csv"
alias_fpath = "../data/aliases"

# ========================================

logging.basicConfig(format="%(message)s")

if not isfile(csvfname):
    logging.critical("fatal: %s not found" % csvfname)
    exit(1)

# First, get the defined aliases for links to later replace full links with
# their aliases, correspondingly
aliases = {}  # Links are keys, their corresponding aliases are values
if isfile(alias_fpath):
    with open(alias_fpath, "r") as alias_f:
        for line in alias_f:
            aliases[line[:].split("|")[1][:-1]] = line[:].split("|")[0]
    del alias_f, alias_fpath


def link_md(url):
    """
    Given a URL, return its address defined in Markdown format (excluding the
    display text). If an alias is available, use the alias instead of the full
    link.

    :param url: Input URL
    :return: The link as partially formatted in Markdown
    """
    return "(%s)" % url if url not in aliases.keys() else "[%s]" % aliases[url]


print("<!-- This table was generated using script/%s -->" % basename(__file__))
print()
print("|Image|Metadata|")
print("|:---:|---|")

with open(csvfname, newline='', encoding='utf-8') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        # Set variables to make it easier to work with them later
        # fname: File name of the image (including the extension)
        # subf: Path of subfolders combined together where the image is placed
        # source: Possible SVG source of the image
        # authors: (Python) List of authors
        # org_authors: (Python) List of original authors
        # links: (Python) List of links to authors and original authors
        # lics: Python dictionary containing licenses' name and links to them,
        # correspondingly

        fname = row['File name']
        subf = row['Subfolder']
        source = "svg/%s/%s" % (subf, row['Source'])
        authors = row['Author'].split(', ')
        org_authors = row['Original author'].split(', ')
        links = row['Link to author'].split(', ')
        lics = {lic_name: lic_link
                for lic_name, lic_link in zip(row['License'].split(", "), row['Link to license'].split(", "))}

        # ========== LEFT CELL ==========
        # First, work on the left cell of the row.
        # This contains the thumbnail of the image (found in /img/thumb/), and
        # links to different formats which the image is available under

        if fname[-3:].lower() != "gif":
            print("|![](img/thumb/{0})<br/><br/>[{1}](img/{2}/{0})"
                  .format(fname, fname[fname.rfind('.') + 1:].upper(), subf),
                  end='')
        else:
            # Currently we cannot generate thumbnails for GIFs, so just link to
            # the actual GIFs themselves and set width to 300px
            print("<img src=\"img/{1}/{0}\" width=\"300px\"/><br/><br/>[GIF](img/{1}/{0})"
                  .format(fname, subf),
                  end='')

        if isfile("../" + source):
            print(" &mdash; [SVG](%s)" % source, end='')
        print("|", end='')

        del fname, subf, source

        # ===============================


        # ======== RIGHT CELL ========

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
                    else print("[%s]%s, " % (author, link_md(link)), end='')
            print("\b\b <br/> ", end='')

        print("**License%s**: " % ("" if len(lics) == 1 else "s"), end='')
        for lic_name, lic_link in lics.items():
            print("%s, " % lic_name, end='') if lic_link == "" \
                else print("[%s]%s, " % (lic_name, link_md(lic_link)), end='')

        print("\b\b", end='')
        if row['Note'] != "":
            print("<br/> **Note**: %s" % row['Note'], end='')

        print("|")

        # ============================
