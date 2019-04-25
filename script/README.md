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

To execute the script:
```
python3 mkimgcreds.py
# or, if the file is executable
./mkimgcreds.py
```

After that, replace the existing image credits table in `CREDITS.md` with the
output. Make sure that all of the aliases are defined in `CREDITS.md`. To
generate a chunk of Markdown code that define the aliases, run
`getaliases.sh` (see section below).

Date files used by the script:
- `/data/img-credits.csv`: To fetch the images' information
- `/data/aliases`: To replace full links with existing aliases for them

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

> **Note**: The script does not generate thumbnails for GIF files, but you don't
have to worry about that.
