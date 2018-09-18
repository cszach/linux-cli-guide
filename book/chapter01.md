<h3 align="center">Chapter 1</h3>
<h1 align="center">Basic operations with directories</h1>

**New commands**: [`pwd`](#pwd), [`cd`](#moving-between-directories-using-cd),
[`pushd`](#pushd), [`dirs`](#dirs), [`popd`](#popd), [`ls`](#ls),
[`tree`](#tree), [`mkdir`](#creating-a-new-directory),
[`rm`](#removing-a-directory)  
**New concepts**: [Linux file system hierarchy][al1], [Root folder (`/`)][al1],
[Absolute path][al1], [Relative path][al1], [Current working directory](#pwd),
[Stack][al2], [Directory stack][al2]

[al1]: #brief-description-of-the-Linux-file-system-hierarchy
[al2]: #the-notion-of-stack-and-directory-stack

This section introduces the basic commands that get you moving between different
locations in the file system and viewing the items in a folder or many folders.
If you are relatively new to the GNU/Linux system, you might want to read the
brief description of the Linux file system first, before diving into the
commands.

### Brief description of the Linux file system hierarchy
###### Tags: `#new-concept`, `#directory`, `#folder`, `#file`, `#hierarchy`, `#path`

The files & folders system in GNU/Linux (so-called "Linux") is hierarchical,
like Windows. This means that a folder can contain files, as well as other
folders, and those folders can contain more files and folders. All accessible
files and folders in a GNU/Linux system is stored in a folder, and this folder
is called the root folder, denoted "/". The below graph illustrates a small part
of a file system on a typical GNU/Linux machine, according to the hierarchy.

![File system hierarchy illustration](../img/fsh.png)

In a hierarchical file system like this, each file and folder has its own
address (commonly called **paths**). There are 2 types of paths:

1. **Absolute path**: An absolute path goes from the root folder (`/`) and
traces down to the destination folder/file. For example, in the system in the
above illustration, the absolute path of the file `bashrc` is `/etc/bashrc`.
2. **Relative path**: The relative path of a file or folder is the path relative
to a folder. For example, in the system illustrated above, the relative path of
the `boot.log` file relative to the `var` directory is `log/boot.log`. Unlike
absolute paths, relative paths don't begin with `/`.

As you might have noticed, GNU/Linux systems (and Unix-like systems in general)
use the forward slash character ("/") to separate folders at different
hierarchical level (unlike Windows, which uses the backward slash character "\\").

There are three symbols, usually appear in paths, that are reserved for special
purposes:
1. **The dot symbol** ("`.`"): The dot symbol refers to the current working
directory.
2. **The double dots symbol** ("`..`"): The double dots symbol refers to the
parent directory (i.e. the directory that is one level above in terms of
hierarchy). For example, in the system illustrated above, the relative path of
the `README` file to the `/usr/include` folder has to contain the double dots
symbol: `../../var/log/README`.
3. **The tilde symbol** ("`~`"): The tilde symbol refers to the home directory
of the current logged-in user. If you have logged in as a normal user, your home
directory should be `/home/USERNAME`, replacing "USERNAME" with your username
(e.g. if your username is "john", your home directory should be `/home/john/`).
If you have logged in as root (equivalence of admin in Windows), the home
directory should be `/root`.

Just one final note before we proceed: "folder" and "directory" are the same
concepts; the difference is, the term "folder" is used more in graphical
interface, while the term "directory" is used more when talking about the
command line interface. Hence, in this document, you will see the term
"directory" appears more.

### `pwd`
###### Tags: `#new-command`, `#new-concept`, `#directory`

At any time in the command line, you are in a directory, and it's called the
"current working directory". To see the _absolute path_ of that directory, enter
`pwd` (<b>p</b>rint <b>w</b>orking <b>d</b>irectory). Usually, when you just
jumped into the command line, the working directory is the home directory
(either `/root` or `/home/USERNAME`, replacing "USERNAME" with the logged in
user's name).

### Moving between directories using `cd`
###### Tags: `#new-command`, `#directory`, `#navigating`

`cd` (<b>c</b>hange <b>d</b>irectory) moves you to another directory on the
system. It is commonly invoked with just one argument: the directory the user
wants to go to.

|Example input|Description|
|:--:|---|
|`cd /home/john/Pictures`|Move to directory `/home/john/Pictures` (absolute path).|
|`cd ../Code/Project1`|Move to directory `../Code/Project1` (relative path). Remember that the `..` symbol is<br>used to refer to the parent directory, as discussed in the introduction above.|
|`cd ~`|Move to the home directory. The `~` symbol refers to the home directory.|
|`cd -`|Move to the previous directory that you were in. For example, if you were in `/home/john`,<br>and then you moved to `/home/john/Pictures/Family`, doing `cd -` will move you back<br>to `/home/john`.|
|`cd ..`|Move to the parent directory.|
|`cd`|`cd` with no option and argument, which is the same as `cd ~`, because by default, `cd` moves you to your home directory.|

### Moving between directories, advanced: `pushd`, `popd`, and `dirs`
###### Tags: `#new-command`, `#new-concept`, `#directory`, `#navigating`


#### The notion of stack and directory stack
###### Tags: `#new-concept`, `#directory`

Stacks to computer science is like telescopes to astronomy. In computing, you
can think of a stack as a collection of items. There are two basic operations
with stacks, they are **push** and **pop**. The push operation adds an item to
the _end_ of the stack, and the pop operation removes the most recently added
item.

Let's say we have a stack of fruit over here. They are numbered in order from
the least recently added item (number 1) to the most recently added item (number
5).

|     1      |   2    |     3      |  4   |     5     |
|   :---:    | :---:  |   :---:    |:---: |   :---:   |
|:strawberry:|:banana:|:watermelon:|:pear:|:pineapple:|

If we perform a push operation to our fruit stack to add a, say, melon :melon:
to our collection, the stack will look like this:

|     1      |   2    |     3      |  4   |     5     |   6   |
|   :---:    | :---:  |   :---:    |:---: |   :---:   | :---: |
|:strawberry:|:banana:|:watermelon:|:pear:|:pineapple:|:melon:|

If we perform a single pop operation to the new stack (the one with 6 items
above, not the original one with 5 items), the stack will look like this:

|     1      |   2    |     3      |  4   |     5     |
|   :---:    | :---:  |   :---:    |:---: |   :---:   |
|:strawberry:|:banana:|:watermelon:|:pear:|:pineapple:|

Note that after the pop, the most recently added item - the melon :melon: - is
now removed from the stack. Pop one more time:

|     1      |   2    |     3      |  4   |
|   :---:    | :---:  |   :---:    |:---: |
|:strawberry:|:banana:|:watermelon:|:pear:|

Now that you know what a stack is, you might have guessed what a directory
stack is. A directory stack is a stack containing absolute paths that we've
pushed into it. You will see it in action by learning the `pushd`, `popd`, and
`dirs` command below.

#### `pushd`
###### Tags: `#new-command`, `#directory`, `#navigating`

Just like `cd`, `pushd` (**push** <b>d</b>irectory) moves you to a new
directory. However, `pushd` does one more thing: adding the new directory to the
directory stack.

> **Note**: `cd .` is useless, but `pushd .` can be useful.

#### `dirs`
###### Tags: `#new-command`, `#directory`

`dirs` (<b>dir</b>ectory <b>s</b>tack) displays the directory stack.

Let's say you started at your home directory. Then you do
`pushd Pictures/Miscellaneous/`, and then `pushd ~/Videos/`, and then stop at
` pushd ../Templates/`. The output of `dirs` should be like this:

```
~/Templates ~/Videos ~/Pictures/Miscellaneous ~
```

The default display is, however, hard to interpret. If you want `dirs` to print
each path on its own line instead, feed `dirs` the `-p` option. So that is
`dirs -p`. The output should be like this:

```
~/Templates
~/Videos
~/Pictures/Miscellaneous
~
```

You can see that the most recently added element (`~/Templates`) is in the first
line of the output, and the least recently added element
(`~/Pictures/Miscellaneous`) is in the second last line of the output. The last
line of the output is the directory that you were in _before_ you did your first
`pushd` command.

The `~` symbol, as mentioned, refers to the home directory. If you don't want
`dirs` to use this symbol, but use the actual path instead, throw the `-l`
option at it. `dirs -l -p` should be like this (still in the context of our
example, assuming the username is "john"):

```
/home/john/Templates
/home/john/Videos
/home/john/Pictures/Miscellaneous
/home/john
```

To remove all the elements in the directory stack, type `dirs -c`.

Useful options for `dirs`, summarized in a table:

| Option |    Hint    |                                    Description                                    |
| :---:  |    ---     |                                        ---                                        |
|  `-l`  |  **l**ong  |Instead of writing the `~` symbol, write the actual path that the symbol refers to.|
|  `-p`  |**p**er line|Print each element on its own line.                                                |
|  `-c`  | **c**lear  |Clear the stack: Remove all the items in the directory stack.                      |

#### `popd`
###### Tags: `#new-command`, `#directory`

`popd` (**pop** <b>d</b>irectory) pops the most recently `pushd`ed path, and
moves you to the directory that is now the last element in our directory stack
(after the pop operation).

Example: Let's say your directory stack currently looks like this (this is from
a previous example):

```
~/Templates
~/Videos
~/Pictures/Miscellaneous
~
```

...in which `~/Templates` is the most recently added path. If you do a `popd`,
you will be moved to `~/Videos`, and `~/Templates` will be gone from the stack:

```
~/Videos
~/Pictures/Miscellaneous
~
```

`popd` won't do anything (but warns you) if the directory stack is empty.

### Viewing items in a directory: `ls` and `tree`
###### Tags: `#new-command`, `#view`, `#directory`

#### `ls`
###### Tags: `#new-command`, `#view`, `#directory`

`ls` (<b>l</b>i<b>s</b>t) is used to list files. If you only enter `ls` (with
no option), it will list all files and folders (excluding hidden ones) in the
current working directory. You can specify a directory's path to `ls` as an
argument, and `ls` will list the files and folders in that directory (e.g.
`ls /etc` will list all the files and folders in `/etc`).

It has several helpful options:

| Option |  Hint   |                                       Description                                       |
| :---:  |   ---   |                                           ---                                           |
|  `-A`  | **a**ll |List all files and folders, including the hidden ones.                                   |
|  `-l`  |**l**ong |Display list in long format (see below for more information).                            |
|  `-s`  |**s**ize |Display size of each file, should be used with the -h option.                            |
|  `-h`  |**h**uman|Display size in a human readable form (e.g. "5.5M" for 5.5 megabytes instead of "5500"). |

Note that you must put the options before the directory you wish to look inside
(e.g. `ls -l -A /proc` will list all the files and folders (including hidden
ones) in the `/proc` directory with long listing format). The overall usage of
the `ls` command is:

```
ls [options] [directories]
```

...replacing `[options]` with actual options there (each option should be
separated by a space character), and `[directories]` with path(s) of folder(s).

If you use the long listing format, you will see something like this:

```
drwxrwxr-x.  3 john john 4096 Jul 13 21:40 basecalc
drwxrwxr-x.  9 john john 4096 Jul 19 18:39 firefox-dev
drwxrwxr-x. 16 john john 4096 Jul 17 14:16 inkscape
-rw-rw-r--.  1 john john  578 Jul 19 11:04 Inkscape-Dependencies.txt
drwxrwxr-x.  2 john john 4096 Jun 21 21:17 iso
drwxrwxr-x.  4 john john 4096 Jul  8 13:38 TerminalImageViewer
drwx------.  3 john john 4096 Jul 12 22:57 tor-browser
```

...which is to say, there are 7 columns. The meaning of each column is as
follows:

1. File/Folder permission
2. Number of links
3. File/Folder's owner
4. File/Folder's owner group
5. File size (in bytes, but can be made easier to interpret with -h option)
6. When was the file/folder last modified? (this one actually spans to multiple
columns)
7. The file/folder's name

Those may be hard for you to understand, especially if you're relatively new to
computers. We will see what most of them are in later sections, so you can
safely ignore the above list for now, and come back later.

`ls` also takes multiple directories' paths. Below is an example of using `ls`
to list files and folders in two directories, `Documents` and `F-IT1`:

```
> ls Documents/ F-IT1/
Documents/:
firefox-bookmarks.html  fp_addrs.txt  mail-addrs.txt

F-IT1/:
Word
```

#### `tree`
###### Tags: `#new-command`, `#view`, `#directory`, `#hierarchy`

`ls dir` lists the files and folders inside the `dir` directory, but if `dir`
actually has sub-directories in it, `ls` won't list the items inside those
sub-directories. There's actually an option for `ls` to do that, but why would
you use it when you have `tree`?

The `tree` command lists file and folders, recursively, in a hierarchical tree
format. This means that `tree` displays the hierarchical relationship between
files and folders (e.g. which folder does this file reside in). An example of
an output of `tree` is as follow:

```
wfind
├── example
│   ├── file1
│   ├── file2
│   └── file3
├── lib
│   ├── wfind.cpp
│   └── wfind.hpp
├── main.cpp
├── Makefile
├── README.md
├── UNLICENSE
└── wfind

2 directories, 10 files
```

By looking at the output above, you can interpret that `file1`, `file2`, `file3`
are inside the `example` folder, `wfind.cpp` is in `lib` folder, and, of course,
`lib` and `example` folders are inside the `wfind` folder.

Just like `ls`, `tree` does not list hidden files by default. Instead, you have
to throw the `-a` option in. Here are some useful `tree` options:

| Option |    Hint     |                             Description                              |
| :---:  |     ---     |                                 ---                                  |
|  `-a`  |   **a**ll   |List all files and folders, including the hidden ones.                |
|  `-d`  |**d**irectory|List folders only, don't list files.                                  |
|  `-f`  |  **f**ull   |Print the absolute path, not just the name of the files/folders found.|

### Creating a new directory
###### Tags: `#new-command`, `#new`, `#directory`

To create a new directory, use the `mkdir` (<b>m</b>a<b>k</b>e <b>dir</b>ectory)
command:

```
mkdir newdir
```

...replacing "newdir" with the name of the new directory at your choice. This
will create a new directory in the current working directory. If you want to
create a new directory in somewhere else that is not the current working
directory, say, `/home/john/Programs`, you can do:

```
mkdir /home/john/Programs/newdir
```

Note that in the above command, if the parent directory `/home/john/Programs`
does not exist, an error will be thrown. If you want `mkdir` to create those
parent directories for you (in case they don't exist), simply feed it with the
`-p` option.

```
mkdir -p /home/john/Programs/newdir
```

### Removing a directory
###### Tags: `#new-command`, `#remove`, `#directory`

`rm -r dir`, replacing "dir" with the name of the directory you want to remove.
The `rm` command (<b>r</b>e<b>m</b>ove) can also be used to delete files, which
we will discuss later. The `-r` option must be specified so that `rm` can remove
the directory <b>r</b>ecursively (meaning all files and folders inside that
directory will also be deleted).

Chapter Summary
---------------

Congratulations! You've finished chapter 1. :tada: :tada: :tada:

Let's recover what we've covered in this chapter.

1. The Linux file system is hierarchical. The folder at the top of this
hierarchical model is called "root" in Linux, denoted "/".
2. Every file and every folder has its own address, commonly called "path".
There are two types of paths:
    - **Absolute path** which starts from the root folder and traces down the
    hierarchical system to the destination file/folder.
    - **Relative path** which shows the relative position of a file/folder with
    another file/folder on the system.
3. Files and folders at different hierarchical levels are separated using the
forward slash symbol ("/").
4. There are 3 symbols reserved for specific purposes in a path:

|Symbol|                                   Description                                   |
|:---: |                                       ---                                       |
| `.`  |Current working directory                                                        |
| `..` |Parent directory (i.e. directory that is one level above in the hierarchy model) |
| `~`  |User's home directory                                                            |

5. The current working directory is the address (i.e. path) of where you are in
the file system. The `pwd` command is used to see the current working directory
while you are in the command line environment.
6. `cd` can be used to go to another location (i.e. path) in the file system.
7. A stack is a collection of items that can be manipulated with 2 common
operations:
    - **Push** which adds a new item to the end of the collection, and
    - **Pop** which removes the most recently added item (i.e. the item at the
    end of the collection)
8. A directory stack is a stack of directory paths. It can be viewed using the
`dirs` command.
9. `pushd` moves you to another directory and pushes that directory's path to
the directory stack.
10. `popd` pops the directory stack once and moves you back to the last pushed
directory.
11. `ls` is usually used to list files and folders in a directory. `tree` is
greater at doing this recursively.
12. `mkdir` is used to create new directories, while `rm` with the `-r` option
is used to remove directories.

Chapter Quiz
------------

1. What symbol does Linux systems use as a separator between directories at
different hierarchical level in paths?
2. Fire up a terminal and use `pwd` to see the current working directory. What
directory is it? What type of directory is it?
3. Use `pwd` to see the current working directory, and then run `cd .`, and then
`pwd` again. Does the current working directory change after running the `cd`
command? What does this remind you of the dot ("`.`") symbol in paths?
4. What is the relative path of the `Pictures` folder in your home directory,
relative to your home directory?
5. What is a stack? What is a directory stack?
6. How does `pushd` differ from `cd`?

Chapter Quiz's Answers
----------------------

<details>
    <summary>What symbol does Linux systems use as a separator between
    directories at different hierarchical level in paths?</summary>

Linux systems use the forward slash symbol ("/") to separate directories at
different hierarchical level in paths. Considering the following path:

```
/home/john/Templates/
```

We can interpret that, the directory `Templates` is one level under the
`john` directory, and the `john` directory is one level under the `home`
directory. For greater precision, we can add the forward slash symbol after
the names of the directories. So, the directories we just mentioned can be
re-written as `Templates/`, `john/`, and `home/`. Thus that leaves us with
one unmentioned directory: `/` - the root directory.
</details>
