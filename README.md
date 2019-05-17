<h1 align="center">42tm's Bash Guide</h1>

<p align="center">
    <img src="icon.png" width="200" height="200">
</p>

Description
-----------

This repository contains a beginner-friendly Bash guide and all the resources
used by the guide. The guide is intended for beginners, even those who have
never touched a command line interface before. It will guide you from the most
fundamental concepts and commands to more advanced ones, with their practical
applications alongside.

:heavy_check_mark: Learn to use Bash's built-ins, GNU utilities and their
helpful options  
:heavy_check_mark: Learn concepts with illustrations  
:heavy_check_mark: Practical use cases of commands  
:heavy_check_mark: Learn Bash scripting to automate tasks  
:heavy_check_mark: Learn how to use common compiled programs and commonly installed packages (such as `nano` for text editing, `rsync` for backing up data, `ssh` for remote login, etc.)  
:heavy_check_mark: Revise by taking a quiz at the end of every chapter  
:heavy_check_mark: Written in simple English, suitable for English learners  
:heavy_check_mark: Contents are in the Public Domain, contributions are welcomed

<p align="center">
    <a href="book/\_preamble.md"><img src="img/readme/read-btn.png" width="24%" /></a>
    <a href="book/GLOSSARY.md"><img src="img/readme/glossary-btn.png" width="24%" /></a>
    <a href="CREDITS.md"><img src="img/readme/credits-btn.png" width="24%" /></a>
    <a href="LICENSE"><img src="img/readme/license-btn.png" width="24%" /></a>
</p>

> **Note**: Different documents and different parts of any document might refer
to the guide as "tutorial" or "book".

Prerequisites
-------------

- Understanding of the most basic computer concepts (e.g. file, folder, program)
- Access to a command line environment running Bash (e.g. terminal emulator in
a GNU/Linux distribution like Ubuntu or Fedora, terminal emulator provided as a
web service, Windows Subsystem for Linux, recent macOS system)

### I use macOS, can I take the guide?

Mostly yes.

Mac OS X Jaguar (released in 2002) and its successors come with Bash. However,
the guide does not just stop at teaching Bash. It also contains guides on how to
use some common compiled command line programs. This is where GNU/Linux and
macOS differ (e.g. macOS has `pbcopy`, GNU/Linux does not). The guide was
originally intended for GNU/Linux users, thus it is GNU/Linux-oriented and most
of it contains instructions for procedures that will definitely be possible on
GNU/Linux, but _maybe_ not on macOS. We rather see this whole situation as an
existing downside of the guide and will endeavor to fix it. We welcome and much
appreciate contributions from dedicated macOS users to make the guide more
complete.

Sections that are only for GNU/Linux users are labeled **`#linux-only`**.
Sections that are only for macOS users are labeled **`#macos-only`**.

### I use Microsoft Windows, can I take the guide?

If you can access Bash on it, yes. Consider [Windows Subsystem for
Linux](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) if you want to
use Bash on Windows 10.

Please note that we do **not** guarantee that every procedure introduced in the
guide will work in Windows Subsystem for Linux or a similar technology. The best
option is still getting yourself a GNU/Linux system running. Please consult the
Web for detailed instructions.

Goals for Bash Tutorial
-----------------------

- Become an easily-understood and extended Bash learning resource
- Establish a friendly community and be a community-contributed guide
- Available in the Public Domain with no licensing conflict

Repository structure
--------------------

- `README.md`: This document
- `TAGS.md`: Glossary for the tags used in the guide
- `TODO.md`: Development to-dos
- `book/`: Contains the guide's chapters written in Markdown
- `img/`: Images used in the guide in the form of raster graphics
- `img/thumb/`: Thumbnails of images
- `svg/`: Original SVG images of some of the exported PNG images that appear in
the guide
- `script/`: Some helpful scripts for repository development
- `data/`: Contains data files that serve the scripts
- `icon.png`: The icon for the repository, seen above
- `LICENSE`: A copy of the Creative Commons Zero v1.0 Universal, which is the
license that most of the materials contained within this repository are licensed
under

Other Bash guides/references on GitHub
--------------------------------------

- [**The Art of Command Line**][rr1] by [**jlevy**][rra1]: A guide that covers
both Bash commands and Bash programming. However it assumes that you already
knew the basic stuff.
- [**Pure Bash Bible**][rr2] by [**dylanaraps**][rra2]: A document focused on
Bash programming "using only built-in `bash` features".
- [**42tm's Bash Reference**][rr3] by [**42tm**][rra3]: A reference for Bash
from 42tm that gets upstreamed with 42tm's Bash Guide.
- [**`bash-guide`**][rr4] by [**Idnan**][rra4]: A supposedly guide for Bash,
however it is more of a reference because the explanations are short and some
(if not all) technical terms are not explained.

[rr1]: https://github.com/jlevy/the-art-of-command-line
[rra1]: https://github.com/jlevy
[rr2]: https://github.com/dylanaraps/pure-bash-bible
[rra2]: https://github.com/dylanaraps
[rr3]: https://github.com/42tm/bash-ref
[rra3]: https://github.com/42tm
[rr4]: https://github.com/Idnan/bash-guide
[rra4]: https://github.com/Idnan

License
-------

![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)

By licensing this work under the [Creative Commons Zero](LICENSE) (CC0) license,
we dedicate it to the Public Domain. We do this for the benefit of the public at
large. Being in the Public Domain means this work can be freely used by anyone
and by any means, even for commercial purposes, without attribution (although it
is super appreciated).

All text contents and the scripts found in `script/` are all CC0-licensed.
Licenses of images are listed in details in [CREDITS.md](CREDITS.md).
