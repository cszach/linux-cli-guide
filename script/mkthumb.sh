#!/bin/bash
# Create thumbnails (stored in img/thumb) from PNGs found in img/

imgdir="../img"  # Path of img/ relative to where this Shell script is located

# Create img/thumb if needed
! [ -d $imgdir/thumb ] && /usr/bin/mkdir $imgdir/thumb

# Check if 'convert' command is found
[ -z $(command -v convert) ] && \
>&2 echo "ERROR: ImageMagick's convert utility not found" && exit 1

# Find all images and write their paths in .thumbs.query
/usr/bin/find $PWD/$imgdir \
    -not -path "$PWD/$imgdir/thumb*" \
    -not -path "$PWD/$imgdir/.ignore*" \
    -not -path $PWD/$imgdir \
    > .thumbs.query

# Generate thumbnails
for imgpath in $(cat ./.thumbs.query)
do
    /usr/bin/convert $imgpath -resize 300 $imgdir/thumb/$(/usr/bin/basename $imgpath)
done

/usr/bin/rm -f .thumbs.query
