The `script` directory
======================

This directory contains executable scripts that you may use while working on
this project.

What's in this directory
------------------------

### `mkimgcreds.py`

`mkimgcreds.py` is a script that is used to generate a 2-column Markdown table
that shows images found in `img/` on the left and their respective information
on the right. The script is written in Python 3. The generated table is printed
to stdout (i.e. the console, if you don't reroute the output to anywhere else)
and should be copied to replace the existing table in `/CREDITS.md`.

The typical workflow is this:
1. You have just edited the data stored in `img-credits.csv`
2. Run `mkimgcreds.py` to generate a new table i.e. by running
```shell
./mkimgcreds.py
```
or
```shell
python3 mkimgcreds.py
```
3. Copy the output and use it to replace the existing table in `/CREDITS.md`
(in particular, the table that displays the information of the images)

### `mkthumb.sh`

This script generates thumbnails of images found in `/img`. The thumbnails are
stored in `/img/thumb`. Should be executed after a new image is placed into
`img/` or an existing image is replaced. The script leverages ImageMagick's
`convert` utility to resize the images. Make sure the utility is available on
your machine before running the script.

The script is written in Bash. There are 2 ways to execute it:

1.
```shell
./mkthumb.sh
```
2.
```shell
bash mkthumb.sh
```
