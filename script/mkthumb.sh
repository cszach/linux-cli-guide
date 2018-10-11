#!/bin/sh
# Create thumbnails (stored in img/thumb) from PNGs found in img/

imgdir="../img"  # Path of img/ relative to where this Shell script is located

! [ -d $imgdir/thumb ] && mkdir $imgdir/thumb  # Create img/thumb if needed

for imgf in $(ls -Ap $imgdir | grep -v "/$"); do
    convert $imgdir/$imgf -resize 300 $imgdir/thumb/$imgf
done
