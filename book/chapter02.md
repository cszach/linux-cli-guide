<h3 align="center">Chapter 2</h3>
<h1 align="center">Basic operations with files</h1>

### Viewing text files
###### Tags: `#view`, `#file`, `#text-file`, `#new-command`

#### `cat` and `tac`

The `cat` command (con**cat**enate) is usually used to display the content of a
text file to the screen.

Examples:

- `cat myfile`: Print the content of the file `myfile` in the current working
directory to the terminal screen
- `cat /home/john/.bashrc`: Print the content of the file `.bashrc` in
`/home/john` directory

You can also print multiple files out. Example:

```
> cat file1 file2 file3
This is content inside file1.
This is content inside file2.
This is content inside file3.
```

The `tac` command is similar to `cat`, but it prints the file in the reversed
order (last line in the file is printed first, then go up until the first line).

#### `less`

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

#### `head` and `tail`

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

### Input/Output
###### Tags: `#new-concept`, `#file`, `#io`

#### File handles
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

#### I/O Redirection
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

### File timestamps
###### Tags: `#file`, `#new-concept`, `#extend`, `#timestamp`

#### Notion of file timestamp & Types of file timestamps in GNU/Linux
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

#### Viewing a file's timestamp using `ls`
###### Tags: `#file`, `#extend`, `#timestamp`, `#view`

The `ls` lists files in a directory by specifying the path of the directory to
it, but you can also specify file names to it. For example:

```
> ls myfile1.txt
myfile1.txt
> ls myfile1.txt myfile2.txt myfile3.txt
myfile1.txt myfile2.txt myfile3.txt
```

Specifying files' paths without an option to `ls` seems useless, so we'll use
the `-l` option instead. The `-l` option tells `ls` to list files in long
format that includes some information associating with the each of the file,
including the modification time (mtime), as [previously mentioned](#ls) (see
that section again if you want to refresh your memory on these). Example output
of `ls -l report.txt`:

```
-rwxrwxr-x. 1 john john 7170 May 20 13:45 report.txt
```

In the above example output, the mtime is written ("May 20 13:45"), indicating
that the file `report.txt` was last modified on 20 of May at 13:45. With
additional option, you can get `ls` to print out the atime or ctime instead of
the mtime. The options for those are `-u` and `-c`, respectively.

```
> ls -l -u README.md
-rwxrwxr-x. 1 jane jane 7170 Jul 25 14:30 README.md
```

The above example output shows that the last time the file `README.md` was read
(the atime) is 25 of July, at 14:30.

```
> ls -l -c punchcard
-rwxrwxr-x. 1 you_create you_create 7170 May 20 13:45 punchcard
```

The above example output shows that the last time the file `punchcard` was
changed (the ctime) is 20 of May, at 13:45.

### Viewing file's details

#### `stat`

`stat` (<b>stat</b>us) is a command line utility that is used to print various
information of a file.

### Using `touch`

#### Creating a new file

#### Changing a file's timestamps
