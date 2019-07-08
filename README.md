<h1 align="center">42tm's Linux Command Line Guide</h1>

<p align="center">
    <img src="icon.png" width="200" height="200">
</p>

Description
-----------

This repository contains a beginner-friendly Linux command line guide and all
the resources used by the guide. The guide is intended for beginners, including
those who have never touched a command line interface before. It will guide you
from the most fundamental concepts and commands to more advanced ones, with
their practical applications alongside.

:heavy_check_mark: Learn to use Bash's built-ins, GNU utilities and their
helpful options  
:heavy_check_mark: Learn concepts with illustrations  
:heavy_check_mark: Practical use cases of commands  
:heavy_check_mark: Learn Bash scripting to automate tasks  
:heavy_check_mark: Learn how to use common CLI programs (e.g. `nano`, `rsync`, `ssh`, etc.)  
:heavy_check_mark: Revise by taking a quiz at the end of every chapter  
:heavy_check_mark: Written in simple English, suitable for English learners  
:heavy_check_mark: Contents are in the Public Domain, contributions are welcomed

<p align="center">
    <a href="guide/\_preamble.md"><img src="img/readme/read-btn.png" width="24%" /></a>
    <a href="guide/GLOSSARY.md"><img src="img/readme/glossary-btn.png" width="24%" /></a>
    <a href="CREDITS.md"><img src="img/readme/credits-btn.png" width="24%" /></a>
    <a href="LICENSE"><img src="img/readme/license-btn.png" width="24%" /></a>
</p>

> **Note**: Different documents and different parts of any document might refer
to the guide as "tutorial" or "book".

Prerequisites
-------------

- **Understanding of basic computer concepts** (e.g. file, folder, program,
mouse pointer, keyboard): These won't be explained.
- **Moderate experience in using a graphical operating system** (e.g. Ubuntu,
Linux Mint, Fedora, macOS): This includes capability of searching for
applications, downloading software, and navigating around using a graphical
interface.
- **Access to a command line environment running Bash** (e.g. terminal emulator
in a GNU/Linux distribution or macOS, online terminal emulator): So that you can
learn by doing. If you only read the text, you will forget quickly. The best
option is having a GNU/Linux distribution or macOS running.

### Bonuses

In addition, these are not prerequisites, but are great bonuses.

- **Solid experience in computer programming** (e.g. in C, Java, Python): Bash
scripting and computer programming share many technical terms and both boil down
to how computer works. The guide also contains analogies to various aspects of
computer programming.
- **Multiple working computers**: They'll better help you learn about computer
networking and network-related tasks (e.g. remote login using `ssh`, remote
backup using `rsync`, sharing a NFS file system).
- **Previous experience using the Linux command line**: If you've learned Bash
and/or the Linux command line and are here for a refresher, that's a good start.

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

Goals for Linux Command Line Guide
----------------------------------

- Become an easily-understood and extended Linux command line learning resource
- Establish a friendly community and be a community-contributed guide
- Available in the Public Domain with no licensing conflict

Repository structure
--------------------

- `README.md`: This document
- `TAGS.md`: Glossary for the tags used in the guide
- `guide/`: Contains the guide's chapters written in Markdown
- `img/`: Images used in the guide in the form of raster graphics
- `img/thumb/`: Thumbnails of images
- `svg/`: Original SVG images of some of the exported PNG images that appear in
the guide
- `script/`: Some helpful scripts for repository development
- `data/`: Contains data files that serve the scripts
- `icon.png`: The icon for the repository, seen above
- `42tm.png`: 42tm Team's logo
- `42tm-circular.png`: 42tm Team's logo rounded with a grey border
- `LICENSE`: A copy of the Creative Commons Zero v1.0 Universal, which is the
license that most of the materials contained within this repository are licensed
under

Other Linux Command Line guides/references on GitHub
----------------------------------------------------

- [**The Art of Command Line**][rr1] by [**jlevy**][rra1]: A guide that covers
both Bash commands and Bash programming. However it assumes that you already
knew the basic stuff.
- [**Pure Bash Bible**][rr2] by [**dylanaraps**][rra2]: A document focused on
Bash programming "using only built-in `bash` features".
- [**42tm's Linux CLI Reference**][rr3] by [**42tm**][rra3]: A reference for
Linux command line that gets upstreamed with 42tm's Linux Command Line Guide.
- [**`bash-guide`**][rr4] by [**Idnan**][rra4]: A supposedly guide for Bash,
however it is more of a reference because the explanations are short and some
(if not all) technical terms are not explained.

[rr1]: https://github.com/jlevy/the-art-of-command-line
[rra1]: https://github.com/jlevy
[rr2]: https://github.com/dylanaraps/pure-bash-bible
[rra2]: https://github.com/dylanaraps
[rr3]: https://github.com/42tm/linux-cli-ref
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
