#!/bin/bash
# Create thumbnails (stored in img/thumb) from PNGs found in img/

imgdir="../img"  # Path of img/ relative to where this Shell script is located
alias convert="/usr/bin/convert"  # Path to executable of ImageMagick's convert

# Create img/thumb if needed
! [ -d $imgdir/thumb ] && mkdir $imgdir/thumb

# Check if 'convert' command is found
[ -z $(command -v convert) ] && \
>&2 echo "ERROR: ImageMagick's convert utility not found" && exit 1

# Iterate over PNGs found in img/ (non-recursively)
# and use 'convert' to create thumbnails
for imgf in $(ls -Ap $imgdir | grep -v "/$"); do
    convert $imgdir/$imgf -resize 300 $imgdir/thumb/$imgf
done
