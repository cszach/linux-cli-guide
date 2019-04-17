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
to `stdout` (i.e. the console, if you don't reroute the output to anywhere
else).

A problem arose when it was necessary to replace full links in the table with
aliases (these can be possibly defined in Markdown). Formerly, you would have to
run this script and manually replace the links with their aliases,
correspondingly. In the present, you can just execute `alias-credits.sh`
instead (see section below).

### `alias-credits.sh`

This script invokes `mkimgcreds.py` and replace the links in the Python script's
output with the links' available aliases. Aliases are defined in
`/data/aliases`. The processed output is printed to `stdout`.

To execute the script:
```shell
bash alias-credits.sh
# or, if the file is executable
./alias-credits.sh
```

After that, replace the existing image credits table in `CREDITS.md` with the
output. Make sure that all of the aliases are defined in `CREDITS.md`. To
generate a chunk of Markdown code that define the aliases, run
`getaliases.sh` (see section below).

### `getaliases.sh`

Generate a piece of Markdown code that defines aliases for links that appear
multiple times in `CREDITS.md`.

To execute the script:
```shell
bash getaliases.sh
# or, if the file is executable
./getaliases.sh
```

After that, copy the output and paste it in CREDITS.md (under the line with the
comment `<!-- Link aliases -->`). Be sure to remove existing alias definitions
first.

### `mkthumb.sh`

Generate thumbnails of images found in `/img`. The thumbnails are stored in
`/img/thumb`. Should be executed after a new image is placed into `img/` or an
existing image is replaced. The script leverages ImageMagick's `convert` utility
to resize the images. Make sure the utility is available on your machine before
running the script.

To execute the script:
```shell
bash mkthumb.sh
# or, if the file is executable
./mkthumb.sh
```
