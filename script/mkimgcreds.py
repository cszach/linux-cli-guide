#!/usr/bin/env python3
# Script used to generate image credits table in CREDITS.md.

from os.path import isfile

# Authors
author_01 = {
    "name": "Nguyen Hoang Duong",
    "profile": "http://github.com/NOVAglow",
}

# Licenses along with links
cc0 = {
    "name": "Creative Commons Zero v1.0 Universal",
    "ident": "CC0",
    "link": "http://creativecommons.org/publicdomain/zero/1.0/"
}

# Collection of images
#
# images = [ [file_name, title, where, author, license], ... ]
images = [
    ["fsh.png", "Filesystem of Linux operating systems (Visualization)",
     "Chapter 1", author_01, cc0],
    ["pushd-vis.png", "GNU/Linux's pushd command (Visualization)", "Chapter 1",
     author_01, cc0],
    ["popd-vis.png", "GNU/Linux's popd command (Visualization)", "Chapter 1",
     author_01, cc0],
    ["symlink-vis.png", "Symbolic link - Visualization", "Chapter 2",
     author_01, cc0],
    ["broken_symlink-vis.png", "Broken Symbolic link - Visualization",
    "Chapter 2",  author_01, cc0],
    ["hard_link-vis.png", "Hard link - Visualization", "Chapter 2",
     author_01, cc0]
]

# **************************
# * START GENERATING TABLE *
# **************************

print("<!-- This table was generated using script/mkimgcreds.py -->\n")
print("|Image|Metadata|")
print("|:---:|---|")

# Template for each row of table in Markdown
template = "|![](%s) <br> %s [PNG](%s)|**Title**: %s <br> **Shown in**: %s " \
         + "<br> **Author**: %s <br> **License**: [%s][%s]|"

# Array containing the used licenses' links.
# This is used to create link shortcuts to the licenses.
templic = []

for img in images:
    # Get SVG source within the repository of image (i.e. stored in svg/)
    # Should be checked later if the source exists because some images might not
    # be SVG in the first place.
    # (img[0] -> Image title)
    svgsrc = "svg/" + img[0][0:len(img[0]) - img[0][::-1].index(".")] + "svg"

    # Get the link to the license which the image is licensed under,
    # and add that link to templic if it hasn't been added already.
    # (img[4] -> License (dictionary type))
    if img[4]["link"] in templic:
        md_imglic = "lic%d" % templic.index(img[4]["link"])
    else:
        templic.append(img[4]["link"])
        md_imglic = "lic%d" % (len(templic) - 1)

    # Process author's field
    # img[3] -> Image's author (dictionary type)
    md_author = img[3]["name"]

    if img[3]["profile"][:18] == "http://github.com/":
        # Add link to GitHub profile. The format is: "NAME (@GITHUB_USERNAME)"
        md_author += (" ([@%s](%s))" % (img[3]["profile"][18:], img[3]["profile"]))
    elif img[3]["profile"] != "":
        # Add link to any online profile if one is provided
        md_author = "[%s](%s)" % (md_author, img[3]["profile"])

    # *** PRINT MARKDOWN OUTPUT FOR TABLE ROW ***
    print(template % (
                      "img/thumb/" + img[0],
                      ("[SVG](%s) &mdash; " % svgsrc) if isfile("../" + svgsrc) else "",
                      "img/" + img[0],
                      img[1], img[2], md_author, img[4]["name"], md_imglic
                     )
            )

# Link shortcuts to licenses
print()
for lic_index in range(0, len(templic)):
    print("[lic%d]: %s" % (lic_index, templic[lic_index]))
