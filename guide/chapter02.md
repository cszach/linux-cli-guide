<p align="center">
    <img src="../img/ch02/header.part1.png" width="28%" />
    <img src="../img/ch02/header.part2.png" width="70.5%" />
</p>

<p align="center">
    <b><a style="text-decoration: none"
          href="#chapter-summary">Chapter Summary</a></b>
    &mdash;    
    <b><a style="text-decoration: none"
          href="#chapter-summary-commands">Commands Summary</a></b>
    &mdash;
    <b><a style="text-decoration: none"
          href="#chapter-quiz">Chapter Quiz</a></b>
</p>

**New commands**: [`cat`](#cat-and-tac), [`tac`](#cat-and-tac), [`less`](#less),
[`head`](#head-and-tail), [`tail`](#head-and-tail), [`stat`](#stat),
[`file`](#file), [`touch`](#using-touch)  
**Commands extended**: [`ls`](#viewing-a-files-timestamp-using-ls)  
**New concepts**: [File handles](#file-handles), [File timestamps][la1]

[la1]: #notion-of-file-timestamp--types-of-file-timestamps-in-gnulinux

- - -

Dealing with files is one of the most important tasks to do on a computer. In
this chapter, you will be greeted with some commands that are used to perform
very basic file operations, such as creating, editing, and deleting files. In
the next chapter, more advanced commands will be introduced.

Table of Content
----------------

1. [Viewing text files](#viewing-text-files)
2. [Input/Output](#inputoutput)
3. [File timestamps](#file-timestamps)
4. [Viewing file's details](#viewing-files-details)
5. [Using `touch`](#using-touch)
6. [Adding and editing file's content](#adding-and-editing-a-files-content)
7. [Deleting a file](#deleting-a-file)

Viewing text files
------------------
###### Tags: `#view`, `#file`, `#text-file`, `#new-command`

### `cat` and `tac`

The `cat` command (con**cat**enate) is usually used to display the content of a
text file to the screen.

Examples:

- `cat myfile`: Print the content of the file `myfile` in the current working
directory to the terminal screen
- `cat /home/john/.bashrc`: Print the content of the file `.bashrc` in
`/home/john` directory

You can also print multiple files out. Example:

```
$ cat file1 file2 file3
This is content inside file1.
This is content inside file2.
This is content inside file3.
```

`cat` can also number the lines if you want to with the `-n` option:

```
$ cat -n doc.txt
     1	The cat command has only one option
     2	that is both helpful and commonly used.
     3	And that is the -n option.
```

The `tac` command is similar to `cat`, but it prints the file in the reversed
order (last line in the file is printed first, then go up until the first line).

> **Note**: `tac`'s options are different from those of `cat`, and those options
aren't used much, so you can safely ignore `tac`'s options.

### `less`

The problem with `cat` is, it prints the content of the file and then return you
to the command prompt. Which means if you `cat` a long text file, the content of
the file will not be fully displayed inside your screen, and you will have to
use shortcuts like `Shift` + `Fn` + `Up arrow key` and `Shift` + `Fn` + `Down
arrow key` to scroll. But things got worse. If the text file is thousands of
lines long, the first lines will be gone.

To solve this problem, you need a program that provides you an interface to view
text file with up and down arrow keys for scrolling. And that program is `less`.
Doing `less large_file.txt` allows you to view the file `large_file.txt`, and
you can use the up and down arrow keys for scrolling. To return to the command
prompt, hit the Q key.

Some useful `less`'s options are:

|Option|         Hint          |                 Description                 |
|:---: |         :---:         |                     ---                     |
| `-I` |Case-<b>i</b>nsensitive|Search results are case-insensitive.         |
| `-M` |                       |Show current position within the file.       |
| `-N` |     <b>N</b>umber     |Number the lines (like `cat`'s `-n` option). |

Once you've entered `less`'s interface, there are several commands you can use
to perform operations, such as navigating and finding text.

|   Command   |   Hint    |             Description             |
|    :---:    |   :---:   |                 ---                 |
|   (Space)   |           |Next page.                           |
| (Up arrow)  | Go **up** |Go up 1 line.                        |
|(Down arrow) |Go **down**|Go down 1 line.                      |
|     `/`     |           |Search for text.                     |
|     `?`     |           |Just like `/` but searches backward. |
|     `n`     |<b>n</b>ext|Go to next search result.            |
|     `N`     |           |Opposite of `n`.                     |
|     `q`     |<b>q</b>uit|Exit `less`.                         |

### `head` and `tail`

`head` prints the first few lines of a text file only. By default, it prints
the first 10 lines. You can customize the number using the `-n` option.

Examples:
- `head script.sh`: Print the first 10 lines in the file `script.sh`
- `head -n 25 script.sh`: Print the first 25 lines in the file `script.sh`
- `head -25 script.sh`: Shorthand for `head -n 25 script.sh`

In contrast, the `tail` command prints the last few lines in a text file. Other
than that, `tail` is the same as `head` at the basic level:

- Just like `head`, `tail` prints out 10 lines by default
- `tail` also has the `-n` option which lets the user changes the number of
lines printed to the console
- `tail` also has a shorthand for `-n`

Just like `cat`, `head` and `tail` can take multiple files as input. However,
when taking multiple files as input, `head` and `tail` do explicitly write the
name of each of the file before printing the first lines of that file. This
behavior isn't presented in `cat`. See example below. The command is
`head -5 COPYING COPYING.LESSER`.

```
==> COPYING <==
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies

==> COPYING.LESSER <==
                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
```

Input/Output
------------
###### Tags: `#new-concept`, `#file`, `#io`

### File handles
###### Tags: `#new-concept`, `#file`, `#io`

When a program (e.g. a Bash command) is ran, three file handles can be used
by the program. They are **stdin** (<b>st</b>an<b>d</b>ard <b>in</b>put),
**stdout** (<b>st</b>an<b>d</b>ard <b>out</b>put), and **stderr**
(<b>st</b>an<b>d</b>ard <b>err</b>or).

| Handle's name |Handle's symbolic name|                       Description                       |      Example      |
|     :---:     |        :---:         |                           ---                           |        ---        |
|Standard input |        stdin         |Where the program reads to get information from the user.|Keyboard           |
|Standard output|        stdout        |Where the program writes output to.                      |The terminal screen|
|Standard error |        stderr        |Where the program writes error information to.           |Log file           |

### I/O Redirection
###### Tags: `#file`, `#io`

Now that we've learned about file handles, let's talk about I/O redirection
("I/O" is short for "Input/Output"). I/O redirection refers to the redirection
of the three file handles so that we can get the input from somewhere else
and/or print the output to somewhere else.

Take the `cat` command that we talked about earlier, for example. If you tried
running `cat`, you know that `cat` writes the content of a file (or many files)
to the terminal screen. But what if you want it to write to a file instead? This
can simply done by I/O redirection. In particular, you use the greater than sign
(">") after the `cat` command, followed by the name of the file that you want
`cat` to write its output to. Here's an example:

```
cat file1 file2 file3 > myfile
```

In the above example, instead of writing the contents of the files `file1`,
`file2` and `file3` to the terminal screen, `cat` writes to `myfile` instead.
`myfile` should now contain the content of `file1`, `file2` and `file3`
concatenated together.

We just redirected the stdout. What about stdin? You can feed a command with
input from a file, by using the less than sign ("<"). Here's an example:

```
cat < myfile
```

Again, we use `cat` as example, because `cat` can take stdin from a file. In the
above example, `cat` takes `myfile` to consume for input data. It should print
out the content of `myfile` (which is the same as doing `cat myfile`).

What about stderr? Usually, stderr is written to the terminal screen and a log
file, but you can also redirect stderr. Redirecting `stderr` is the same as
redirecting `stdout`, but the only difference is, you type "2>" instead of ">".

```
rm myfile 2> error_file.txt
```

In the above example, `rm myfile2` is executed and any error message produced
by the `rm` command should not be written out to the terminal screen but to the
text file `error_file.txt` instead.

Finally, if you want to redirect both stdout and stderr to a text file, use the
">&" symbol.

```
tree . >& output.txt
```

In the example above, all normal output and error information coming from `tree`
should be written to the text file `output.txt` instead of the terminal screen.

File timestamps
---------------
###### Tags: `#file`, `#new-concept`, `#extend`, `#timestamp`

### Notion of file timestamp & Types of file timestamps in GNU/Linux
###### Tags: `#file`, `#new-concept`, `#timestamp`

A file's timestamp is the time when something happened to the file (e.g. when
the file's content was last changed). In GNU/Linux (as well as other Unix &
Unix-like operating systems), each file has 3 timestamps: access time,
modification time, and change time. The following table gives you more
information about these timestamps:

|    Timestamp    |Abbreviation|                                         Description                                         |
|      :--:       |    :--:    |                                             ---                                             |
|   Access time   |   atime    |The time when the file was last read (e.g. by a program like `cat`).                         |
|Modification time|   mtime    |The time when the file's content was last changed.                                           |
|   Change time   |   ctime    |The time when anything of the file was last changed (e.g. content, permission, owner, etc.). |

Knowing about file timestamps is very useful, especially when you are a Linux
system administrator. For example, you might want to delete files that haven't
been accessed (read) for more than 90 days. We'll learn how to do that later,
but first, you need to know how to view the timestamps, and that is shown in
this section below.

### Viewing a file's timestamp using `ls`
###### Tags: `#file`, `#extend`, `#timestamp`, `#view`

The `ls` lists files in a directory by specifying the path of the directory to
it, but you can also specify file names to it. For example:

```
$ ls myfile1.txt
myfile1.txt
$ ls myfile1.txt myfile2.txt myfile3.txt
myfile1.txt myfile2.txt myfile3.txt
```

Specifying files' paths without an option to `ls` seems useless, so we'll use
the `-l` option instead. The `-l` option tells `ls` to list files in long
format that includes some information associating with the each of the file,
including the modification time (mtime), as [previously mentioned](chapter01.md#ls)
(see that section again if you want to refresh your memory on these). Example
output of `ls -l report.txt`:

```
-rwxrwxr-x. 1 john john 7170 May 20 13:45 report.txt
```

In the above example output, the mtime is written ("May 20 13:45"), indicating
that the file `report.txt` was last modified on 20 of May at 13:45. With
additional option, you can get `ls` to print out the atime or ctime instead of
the mtime. The options for those are `-u` and `-c`, respectively.

```
$ ls -l -u README.md
-rwxrwxr-x. 1 jane jane 7170 Jul 25 14:30 README.md
```

The above example output shows that the last time the file `README.md` was read
(the atime) is 25 of July, at 14:30.

```
$ ls -l -c punchcard
-rwxrwxr-x. 1 you_create you_create 7170 May 20 13:45 punchcard
```

The above example output shows that the last time the file `punchcard` was
changed (the ctime) is 20 of May, at 13:45.

Viewing file's details
----------------------
###### Tags: `#view`, `#file`, `#new-command`

### `stat`

`stat` (<b>stat</b>us) is a command line utility that is used to print various
information of a file. Simply give it a file's path or directory's path. Below
is an example.

```
$ stat git-punchcard
File: git-punchcard
Size: 7170      	Blocks: 24         IO Block: 4096   regular file
Device: fd02h/64770d	Inode: 7215076     Links: 1
Access: (0775/-rwxrwxr-x)  Uid: ( 1000/john)   Gid: ( 1001/john)
Context: unconfined_u:object_r:user_home_t:s0
Access: 2018-07-30 22:33:35.718549094 +0700
Modify: 2018-05-20 13:44:09.077679229 +0700
Change: 2018-05-20 13:44:16.043662333 +0700
Birth: -
```

In the example above, the input command `stat git-punchcard` and its output are
shown. Several information about the file can be gathered from the output:
- The file's size is 7170 bytes (or 7.1 kilobytes).
- It is a regular file (can also be "directory" or "symbolic link").
- Its inode number is 7215076 (a file's inode number is like its index number
within the file system).
- Its access permission ("`Access: (0775/-rwxrwxr-x`"), we'll cover this later,
but this is a pretty important information, so keep in mind).
- The user who owns this file is "john" ("`Uid: ( 1000/john)`") and the group
that owns the file is "john" ("`Gid: ( 1001/john)`"). Again, we'll learn about
users and groups later.
- It's access time (atime), modification time (mtime), and change time (ctime).

As mentioned, you can also give `stat` a directory's path.

### `file`

Unlike `stat`, `file` is an utility that focuses on displaying information that
is specific to a certain file type.

Most files have an extension each. For example, the file `report.txt`'s
extension is "txt", which indicates that it is a text file. That is not the case
100% of the time, however. For instance, you can change the `report.txt` file's
extension to "pdf", which is a PDF file's extension. Now we end up with
`report.pdf`, but `report.pdf` is still a text file: Changing a file's extension
in its name doesn't change the file's actual type. Hence you cannot rely on the
file's extension to determine a file's type. The Windows operating system relies
on the file's extension to determine the file type and the default application
to open files with that type, but that's not a good approach.

This is where the `file` command comes into play. The `file` command determines
a file's type by analyzing that file's content instead of the file's extension.
After knowing the file's actual type, `file` might also display more information
that is specific to that file's type. Let's look at some examples.

```
$ file git-punchcard
git-punchcard: Python script, ASCII text executable
```

In the above example, it appears that the file `git-punchcard` is an ASCII text
file. Furthermore, it's a Python script (code and script are text, basically).
`file` also tells us that `git-punchcard` is executable.

```
$ file image.png
image.png: PNG image data, 1100 x 400, 8-bit/color RGB, non-interlaced
```

In the above example, the file `image.png` appears to be a PNG image that is
1100 pixels in width and 400 pixels in height. The image uses 8-bit RGB color
profile.

```
$ file venture.mp3
venture.mp3: Audio file with ID3 version 2.3.0, contains:MPEG ADTS, layer III, v1, 320 kbps, 44.1 kHz, JntStereo
```

In the above example, we can interpret that the file `venture.mp3` is an audio
file using ID3 metadata scheme version 2.3.0 with a bit-rate of 320kbps.

Using `touch`
-------------
###### Tags: `#new`, `#timestamp`, `#file`, `#new-command`

`touch` has two functions: Creating new file and updating a file's timestamp

### Creating a new file
###### Tags: `#new`, `#file`

Simply throw a name as an argument to `touch`:

```
$ touch newfile
```

That's it. In the example above, an empty file called `newfile` will be created.
You can also create multiple new empty files.

```
$ touch newfile1 newfile2 newfile3
```

### Changing a file's timestamps
###### Tags: `#file`, `#timestamp`

If you give `touch` a file that is already presented on the system, however,
`touch` will set the file's timestamps (all of the timestamps) to the current
time (meaning the time when you ran the `touch` command). Let's have an example.
Here we have a file called `image.png`:

```
$ stat image.png
  File: image.png
  Size: 21292     	Blocks: 48         IO Block: 4096   regular file
Device: fd02h/64770d	Inode: 7215568     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/you_create)   Gid: ( 1001/you_create)
Context: unconfined_u:object_r:user_home_t:s0
Access: 2018-07-31 12:30:52.089412120 +0700
Modify: 2018-07-28 11:19:05.686188118 +0700
Change: 2018-07-28 11:19:05.686188118 +0700
 Birth: -
```

As you can see, the file's timestamps vary. Now if we do `touch image.png`...

```
$ touch image.png
$ stat image.png
  File: image.png
  Size: 21292     	Blocks: 48         IO Block: 4096   regular file
Device: fd02h/64770d	Inode: 7215568     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/you_create)   Gid: ( 1001/you_create)
Context: unconfined_u:object_r:user_home_t:s0
Access: 2018-07-31 20:45:30.299611928 +0700
Modify: 2018-07-31 20:45:30.299611928 +0700
Change: 2018-07-31 20:45:30.299611928 +0700
 Birth: -
```

...all three timestamps are updated to the current time.

You might be wondering, "what's the point of updating a file's timestamps?".
One example of real usage of that is this: A lot of GNU/Linux users (mostly
those that are system administrators) have scripts to clean old files that are
ran between intervals. For example, one might want to delete old log files that
haven't been accessed for at least 10 months. If one of those log files still
needs to be kept, however, one can use `touch` to update that file's
timestamps so that the automated file deleting task won't delete that particular
log file.

If you don't want `touch` to update all of the file timestamps but a particular
timestamp only, there are `touch`'s options for that. Below is a table of useful
`touch` options. The option(s) must be specified before the file name(s).

|  Option   |          Hint          |                                   Description                                   |
|   :---:   |         :---:          |                                       ---                                       |
|   `-a`    |   <b>a</b>ccess time   |Change the access time (atime) only.                                             |
|   `-m`    |<b>m</b>odification time|Change the modification time (mtime) only.                                       |
| `-r` FILE |    <b>r</b>eference    |Make a file's atime and mtime the same as _FILE_'s atime and mtime.              |
| `-t` TIME |      <b>t</b>ime       |Update to _TIME_ instead of current time (_TIME_ format: [[CC]YY]MMDDhhmm[.ss]). |

For `-r` option, you must also specify a reference file as an argument. This
option updates the targeted file's atime and mtime to match the reference file's
atime and mtime. The ctime is updated to the current time as usual. For instace,
running the command below will match `crash-report.txt`'s atime and mtime to
`reffile`'s atime and mtime, respectively.

```
$ touch -r var/reffile crash-report.txt
```

For `-t` option, you must specify a particular time as an argument. This time is
in the format CCYYMMDDhhmm.ss, in which:
- CC is for first two digits of a year, YY is for the last two digits of a year,
M is for month, D is for day of the month, h is for hour, m is for minute, s is
for second
- CC, YY, and .ss are optional parts, but if you do specify the CC part, you
must also specify the YY part

Example arguments for the `-t` option:

|   Argument   |                   Meaning                   |
|    :---:     |                     ---                     |
|   08202200   |20 of August this year, at 22:00 (10PM)      |
| 201612300830 |30 of December, 2016, at 8:30 (8:30 AM)      |
|1701121620.50 |12 of January, 2017, at 16:20:50 (4:20:50 PM)|

> **Note**: You can also use `touch` to change a directory's timestamps :+1:.

Adding and editing a file's content
-----------------------------------
###### Tags: `#file`, `#editing`, `#io`, `#extend`, `#text-file`

### Adding content to a text file
###### Tags: `#file`, `#text-file`, `#io`, `#extend`

There are 2 simple commands that we've covered that can be used to add text
content to a text file: `echo` and `cat`, plus the use of I/O redirection.

> **Note**: See the section on [I/O redirection](#io-redirection) again if you
need to refresh your memory on this topic.

In addition to the greater than sign (">") and the less than sign ("<") that
we've learned in the section about I/O redirection, there is also the double
greater than sign (">>"). The double greater than sign is used to append
standard output. For instance, if you have a non-empty file `demo.txt`, doing
`echo "This is some text" > demo.txt` will overwrite `demo.txt`'s existing
content, meaning `demo.txt` will only have the line "This is some text". But if
you use the double greater than sign operator ("`echo "This is some text" >>
demo.txt`"), the line "This is some text" will be added at the end of the file,
and the file's existing content will still be there.

As for `cat`, this command will write whatever you've entered in to stdout if
you give it no argument. You can try that out, just type `cat`, that's it, and
hit Enter.

```
$ cat
Line 1
Line 1
Line 2
Line 2
Line 3
Line 3
```

You can quit by hitting Ctrl + D (or Ctrl + C). The main point here is, we can
actually use this feature, redirect the stdout to a file, thus populating that
file with text. The file does not necessary have to be presented before you do
this.

```
$ cat > somefile
Line 1  
Line 2
Line 3
$ cat somefile
Line 1
Line 2
Line 3
```

### Editing a text file's content
###### Tags: `#file`, `#text-file`, `#editing`, `#new-command`, `#new-program`

As for editing a text file, you can use a text editor. There are text editors
that are made to operate in the command line environment, but there are, of
course, graphical text editors. There should be at least one graphical text
editor that comes pre-installed on your system (ummm...assuming you've installed
a GNU/Linux distribution that comes with a graphical interface and not something
like Arch Linux). If you are using the GNOME desktop environment, there should
be GEdit. If you are using KDE desktop environment, there can be KWrite, KEdit,
or Kate. Graphical editors should be easy for you to use, if you've had some
experience with computers before.

> **Note**: A desktop environment is a little bit out of scope to explain in
details in this tutorial, but basically it provides your computer a graphical
interface, usually along with graphical programs that share the same look.

> **Note**: You can invoke a graphical text editor from your terminal emulator
window. For example, to start GEdit - the default text editor in GNOME, type
"`gedit`". Of course, this assumes that you are in a graphical environment.

- **Graphical text editors**: GEdit, KEdit, Atom, Geany, GVim, ...
- **CLI text editors**: Nano, Vim, Emacs, ...

Deleting a file
---------------
###### Tags: `#file`, `#extend`, `#remove`

[As mentioned in chapter 1](#removing-a-directory), the `rm` command can be used
to delete files. Simply give `rm` the name(s) of the file(s) you want to delete.

This command removes `file1`:
```
rm file1
```

This command removes `file1`, `file2`, `file3`:
```
rm file1 file2 file3
```

Note that the `-r` option, which is necessary to remove directories, isn't
necessary when you delete files only. But there's no harm doing it.

This command removes `file1` and `file2`, which are 2 example files used here,
and `dir1` and `dir2`, which are directories.
```
rm -r file1 file2 dir1 dir2
```

`rm` has several other useful options, which are `-i` and `-I`. If you use `-i`,
`rm` will prompt you before every removal. Enter "y" to remove, "n" to keep.

```
$ rm -r -i file1 file2 file3 dir1 dir2
rm: remove regular empty file 'file1'? y
rm: remove regular empty file 'file2'? y
rm: remove regular empty file 'file3'? n
rm: remove directory 'dir1'? y
rm: descend into directory 'dir2'? y
rm: remove regular empty file 'dir2/file2'? n
rm: remove regular empty file 'dir2/file1'? y
rm: remove directory 'dir2'? n
```

In the example above:
- The files `./file1`, `./file2` are deleted.
- Empty directory `./dir1` is deleted.
- File `./file3` is **not** removed.
- Directory `./dir2` is _not_ empty, so `rm` has to prompt the user before
deleting _every_ file and _every_ folder before removing. If a directory inside
`./dir2` is also not empty, `rm` will do the same as it does with `./dir2`.
- `./dir2/file1` is removed, `./dir2/file2` is **not**.
- `./dir2` is **not** removed. Even if the user typed "y", it still wouldn't be
removed, because if it is removed, `./dir2/file2` must also be removed, but
earlier the user confirmed that `./dir2/file2` shall not be removed.

> **Note**: In case you are wondering what the "./" thing shown above is: The
dot symbol (".") refers to the current working directory, and the "/" is the
directory delimiter as usual. So `./file1` is `file1` in the current working
directory. The dot symbol was first mentioned and explained in
[early chapter 1][edc1].

[edc1]: chapter01.md#brief-description-of-the-linux-file-system-hierarchy

> **Note**: The Bash input used to generate the example files and folders in
the above example is `mkdir dir1 dir2; touch file1 file2 file3 dir2/file1
dir2/file2`.

The `-I` option makes `rm` prompts if you are trying to remove more than 3
files, or removing recursively (with the `-r` option). `rm` with `-I` prompts
_only once_.

```
$ rm -I report.txt git-c.txt log-0245.txt log-0362.txt
rm: remove 4 arguments? y
```

`-i` and `-I` are options that make you think twice before removing files or
directories, avoiding mistakes. Note that **`rm` deletes stuff permanently**
(i.e. it does not move the specified files/folders into Trash or Recycle Bin or
anything like that).

This table summarizes `rm`'s useful options:

|Option|Hint|Description|
|:---:|:---:|---|
|`-r` (or `--recursive`)|<b>r</b>ecursively|Remove directories recursively. This option must be invoked when removing a directory.|
|`-i`||Prompt before _every_ removal.|
|`-I`||Prompt once before removing recursively or removing more than 3 files.|
|`-f` (or `--force`)|<b>f</b>orce|If a specified file or directory does not exist, ignore and move on. Also, never prompt the user to confirm.|

Chapter Summary
---------------

Well done! You've finished chapter 2! :tada: :tada: :tada:

Let's review what we've learned in this chapter.

1. `cat`, `tac`, and `less` can be used to view a file's content. `head` and
`tail` are used to view first or last few lines only.
2. Each file has 3 file handles open for use:
    - stdin: Where the program reads input
    - stdout: Where the program writes output
    - stderr: Where the program reports errors occurred while running
3. I/O redirection: "`>`" redirects stdout, "`<`" redirects stdin, "`2>`"
redirects stderr, "`>&`" redirects both stdout and stderr, and "`>>`" appends
stdout.
4. A file's timestamp is the time when an event happened to a file (e.g. read
from, written to, permission changed, ...). In GNU/Linux, every file has 3 file
timestamps:
    - atime (<b>a</b>ccess **time**): When the file was last read
    - mtime (<b>m</b>odification **time**): When the file's content was last modified
    - ctime (<b>c</b>hange **time**): When anything of the file was last changed, which includes atime,
    mtime, permissions, owner, mode, ...
5. `ls -l` shows a file's mtime. `ls -lc` shows a file's ctime, `ls -lu` shows
a file's atime
6. The `stat` utility shows information for a file in great details, while the
`file` utility shows information specific to a file's type.
7. `touch` has two functions: Creating a new file and changing a file's
timestamp(s).
8. Text file editing is usually done using a text editor, like Vim (for command
line environment) or Atom (for graphical user interface).
9. `rm` can be used to delete files. `rm` can delete both files and directories.

Take a break, because there's more to operations with files. :cake:

Chapter Summary: Commands
-------------------------

### `cat`

Display a file's content or multiple files' content concatenated together.

```
$ cat file1.txt
Go not unto the Usenet for advice, for you will be told both yea and nay (and
quite a few things that just have nothing at all to do with the question).
	-- seen in a .sig somewhere
$ cat file1.txt file2.txt
Go not unto the Usenet for advice, for you will be told both yea and nay (and
quite a few things that just have nothing at all to do with the question).
	-- seen in a .sig somewhere
Zero Defects, n.:
	The result of shutting down a production line.
```

Usage:

```
cat [option(s)] [file(s)]
```

Probably the only commonly used helpful option is `-n` (n for "number"), which
index the lines.

```
$ cat -n fav-fortune.txt
     1	Topologists are just plane folks.
     2		Pilots are just plane folks.
     3			Carpenters are just plane folks.
     4				Midwest farmers are just plain folks.
     5			Musicians are just playin' folks.
     6		Whodunit readers are just Spillane folks.
     7	Some Londoners are just P. Lane folks.
```

### `tac`

Just like `cat` but the order of lines is reversed.

```
$ cat justafile.txt
This is line 1.
This is line 2.
This is line 3.
$ tac justafile.txt
This is line 3.
This is line 2.
This is line 1.
```

<a name="tacre">

> **Note**: If given multiple files, `tac` prints each file in reverse direction
of lines instead of concatenating all the files and reverse the concatenated
content. Compare the output of `tac file1.txt file2.txt` below and
`cat file1.txt file2.txt` (in `cat`'s summary above) and you'll see.

</a>

```
$ tac file1.txt file2.txt
	-- seen in a .sig somewhere
quite a few things that just have nothing at all to do with the question).
Go not unto the Usenet for advice, for you will be told both yea and nay (and
	The result of shutting down a production line.
Zero Defects, n.:
```

### `less`

View a file with scrolling for navigation. Useful for viewing large text files.

```
less [option(s)] [file(s)]
```

`[option(s)]` may include:

|Option|         Hint          |                 Description                 |
|:---: |         :---:         |                     ---                     |
| `-I` |Case-<b>i</b>nsensitive|Search results are case-insensitive.         |
| `-M` |                       |Show current position within the file.       |
| `-N` |     <b>N</b>umber     |Number the lines (like `cat`'s `-n` option). |

`less` also has several commands that you can use while viewing the text file.

|   Command   |   Hint    |             Description             |
|    :---:    |   :---:   |                 ---                 |
|   (Space)   |           |Next page.                           |
| (Up arrow)  | Go **up** |Go up 1 line.                        |
|(Down arrow) |Go **down**|Go down 1 line.                      |
|     `/`     |           |Search for text.                     |
|     `?`     |           |Just like `/` but searches backward. |
|     `n`     |<b>n</b>ext|Go to next search result.            |
|     `N`     |           |Opposite of `n`.                     |
|     `q`     |<b>q</b>uit|Exit `less`.                         |

### `head`

`head` prints the first _N_ line(s) (10 by default) of one or more text files.

```
head [option(s)] [file(s)]
```

Some `head`'s useful options are:

|Option|    Hint     |                           Description                           |
|:---: |    :---:    |                               ---                               |
|`-n` N|<b>n</b>umber|Print the first _N_ lines.                                       |
| `-N` |             |Print the first _N_ lines (e.g. `-15` -> Print first 15 lines).  |
| `-q` |<b>q</b>uiet |If given multiple files, don't print headers giving files' names.|

Example:

```
$ head -5 -q mac1.txt mac2.txt
E2:40:76:20:27:2D
D2:3B:24:22:74:6E
AA:34:83:DA:2B:10
0A:69:73:AC:55:9E
72:DA:68:C6:3F:97
EE:05:70:87:24:F0
2E:FE:90:BC:41:2D
56:3C:A9:76:E6:3D
66:9E:27:79:38:70
6E:2C:D1:58:F8:C0
```

### `tail`

Similar to `head` (see above), but instead of printing the first lines, print
the last lines. Useful options listed for `head` also work the same way with
`tail`.

### `ls` (extended)

`ls` (<b>l</b>i<b>s</b>t) lists all files and folders (non-recursively) in the
current working directory (if no argument is given) or in a given directory.

```
ls [option(s)] [directories]
```

`[options]` may include:

| Option |   Hint   |                                       Description                                       |
| :---:  |   ---    |                                           ---                                           |
|  `-A`  | **a**ll  |List all files and folders, including the hidden ones.                                   |
|  `-l`  | **l**ong |Display list in long format (see below for more information).                            |
|  `-s`  | **s**ize |Display size of each file, should be used with the -h option.                            |
|  `-h`  |**h**uman |Display size in a human readable form (e.g. "5.5M" for 5.5 megabytes instead of "5500"). |
|  `-u`  |          |Along with `-l`: Show access time (instead of modification time) in long format display. |
|  `-c`  |**c**hange|Along with `-l`: Show change time (instead of modification time) in long format display. |

`[directories]` include one or more target directories.

Both `[option(s)]` and [`directories`] are option parts: `ls` can be used
without them.

### `stat`

Display various general information of one or more files. Information includes
file size (in bytes by default), inode number, file type, permissions, owner,
and the 3 file timestamps.

```
$ stat EXITCODE.md
  File: EXITCODE.md
  Size: 1073      	Blocks: 8          IO Block: 4096   regular file
Device: fd05h/64773d	Inode: 16646628    Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/john)   Gid: ( 1000/john)
Context: unconfined_u:object_r:user_home_t:s0
Access: 2018-10-15 18:41:18.141332645 +0700
Modify: 2018-07-03 00:02:55.608352000 +0700
Change: 2018-09-01 17:56:58.011309168 +0700
 Birth: -
```

Usage:

```
stat [option(s)] [file(s)]
```

> **Note**: `stat` can also be used to display information of directories
(e.g. /home) and other stuff (e.g. /dev/sda1).

### `file`

Display information of a file specific to that file's type.

```
file [option(s)] [file(s)]
```

Example:

```
$ file Documents/todo.txt Pictures/desktop_preview.png Music/russia_anthem.ogg
Documents/todo.txt:           ASCII text
Pictures/desktop_preview.png: PNG image data, 1366 x 768, 8-bit/color RGBA, non-interlaced
Music/russia_anthem.ogg:      Ogg data, Vorbis audio, stereo, 44100 Hz, ~499821 bps, created by: Xiph.Org libVorbis I (1.2.0)
```

### `touch`

`touch` can be used to create new files or update timestamps of existing files.

```
touch [option(s)] [file(s)]
```

Any existing file specified in `[file(s)]` will get its timestamps updated,
otherwise it will be created.

`[option(s)]` may include:

|  Option   |          Hint          |                                   Description                                   |
|   :---:   |         :---:          |                                       ---                                       |
|   `-a`    |   <b>a</b>ccess time   |Change the access time (atime) only.                                             |
|   `-m`    |<b>m</b>odification time|Change the modification time (mtime) only.                                       |
| `-r` FILE |    <b>r</b>eference    |Make a file's atime and mtime the same as _FILE_'s atime and mtime.              |
| `-t` TIME |      <b>t</b>ime       |Update to _TIME_ instead of current time (_TIME_ format: [[CC]YY]MMDDhhmm[.ss]). |

### `rm` (extended)

`rm` (<b>r</b>e<b>m</b>ove) removes directories and files.

```
rm [options] [directories|file(s)]
```

`[directories|file(s)]` is where you specify all the files and directories you
wish to delete.

`[options]` may include the following useful options:

|Option|Hint|Description|
|:---:|:---:|---|
|`-r` (or `--recursive`)|<b>r</b>ecursively|Remove directories recursively. This option must be invoked when removing a directory.|
|`-i`||Prompt before _every_ removal.|
|`-I`||Prompt once before removing recursively or removing more than 3 files.|
|`-f` (or `--force`)|<b>f</b>orce|If a specified file or directory does not exist, ignore and move on. Also, never prompt the user to confirm.|

Chapter Quiz
------------

<details>
    <summary><b>
        If given multiple files, <code>tac</code> prints each file in reverse
        <a href="#tacre">as explained</a>. What if you want to concatenate the
        files first then reverse the whole thing?
    </b></summary>

Using what we've learned so far:

```
$ cat lorem1.txt lorem2.txt lorem3.txt > result.txt
$ tac result.txt
```

:warning: **Fowarding alert!** There's actually a better way to do this, which
is using a pipe ("|"):

```
$ cat lorem1.txt lorem2.txt lorem3.txt | tac
```

A pipe is another way to redirect I/O. It takes the output (in the above case,
both stdout and stderr) of the command ran on the left side of it as the input
(stdin) for the command on the right side of it. So the output of
`cat lorem1.txt lorem2.txt lorem3.txt` is taken as the input of `tac`. Doing
this way, we do not need a medium file (like `result.txt`). We'll go over pipes
in the next chapter.
</details>

<details>
    <summary><b>
        Get <code>LICENSE-1</code> and <code>LICENSE-2</code>. Can you tell
        which one is (a copy of) the GNU General Public License and which one is
        (a copy of) the GNU Lesser General Public License? (hint: each file has
        the license's name written in the first line!)
    </b></summary>

You could have `cat`ed them, but a better way to do this is just to see the
first line, because that's where the name of each license is written.

```
$ head -1 LICENSE-1 LICENSE-2
==> LICENSE-1 <==
                   GNU LESSER GENERAL PUBLIC LICENSE

==> LICENSE-2 <==
                    GNU GENERAL PUBLIC LICENSE
```

So, `LICENSE-1` contains a text copy of the GNU Lesser General Public License,
and `LICENSE-2` contains a text copy of the GNU General Public License.
</details>

<details>
    <summary><b>
        Think of more examples of stdout.
    </b></summary>

The standard output (stdout) is where a program writes its output to. Programs
like `cat`, `tree`, `ls`, `pwd` print output to the terminal, and a lot of
commands and terminal programs you are going to use will do that too.
</details>
