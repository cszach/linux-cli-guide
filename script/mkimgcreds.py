#!/usr/bin/env python3
# Script used to generate image credits table in CREDITS.md.

from os.path import isfile

# Authors
hduong = {
    "name": "Nguyen Hoang Duong",
    "profile": "http://github.com/NOVAglow",
}

katst = {
    "name": "Kat Stokes",
    "profile": "https://unsplash.com/@katstokes_/portfolio"
}

# Licenses along with links
cc0 = {
    "name": "Creative Commons Zero v1.0 Universal",
    "ident": "CC0",
    "link": "https://creativecommons.org/publicdomain/zero/1.0/"
}

unsplash = {
    "name": "The Unsplash License",
    "link": "https://unsplash.com/license"
}

# Collection of images
#
# images = [ [file_name, title, where, author, license], ... ]
images = [
    ["prem.jpg", "N/A", "Preamble", katst, unsplash],
    ["fsh.png", "Filesystem of Linux operating systems (Visualization)",
     "Chapter 1", hduong, cc0],
    ["pushd-vis.png", "GNU/Linux's pushd command (Visualization)", "Chapter 1",
     hduong, cc0],
    ["popd-vis.png", "GNU/Linux's popd command (Visualization)", "Chapter 1",
     hduong, cc0],
    ["symlink-vis.png", "Symbolic link - Visualization", "Chapter 3",
     hduong, cc0],
    ["broken_symlink-vis.png", "Broken Symbolic link - Visualization",
    "Chapter 3",  hduong, cc0],
    ["hard_link-vis.png", "Hard link - Visualization", "Chapter 3",
     hduong, cc0]
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

# Just like templic but for authors' profiles
tempau = []

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

    # Like above operation but for the author's profile link
    if img[3]["profile"] in tempau:
        auth_link_var = "aut%d" % tempau.index(img[3]["profile"])
    elif img[3]["profile"] != "":
        tempau.append(img[3]["profile"])
        auth_link_var = "aut%d" % (len(tempau) - 1)

    # Process author's field
    # img[3] -> Image's author (dictionary type)
    md_author = img[3]["name"]

    if img[3]["profile"][:18] == "http://github.com/":
        # Add link to GitHub profile. The format is: "NAME (@GITHUB_USERNAME)"
        md_author += (" ([@%s][%s])" % (img[3]["profile"][18:], auth_link_var))
    elif img[3]["profile"] != "":
        # Add link to any online profile if one is provided
        md_author = "[%s](%s)" % (md_author, auth_link_var)

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

# Link shortcuts to authors' profiles
print()
for aut_index in range(0, len(tempau)):
    print("[aut%d]: %s" % (aut_index, tempau[aut_index]))
