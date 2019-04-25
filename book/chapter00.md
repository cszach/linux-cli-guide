<p align="center">
    <img src="../img/ch00/header.part1.png" width="28%" />
    <img src="../img/ch00/header.part2.png" width="70.5%" />
</p>

<p align="center">
    <b><a style="text-decoration: none"
          href="#chapter-summary">Chapter Summary</a></b>
    &mdash;
    <b><a style="text-decoration: none"
          href="#chapter-quiz">Chapter Quiz</a></b>
</p>

**New concepts**:  

<!-- Define link aliases (if any) here -->

- - -

<!-- This is where you introduce what the chapter is about. -->
If you're new to Bash in specific and the command line in general, **welcome!**
In this very first chapter of the Bash Tutorial, you'll get to know about the
command line environment, Shell, differences between Shell interpreters,
terminal emulator's shortcuts, and more. Let's begin!

Table of Content
----------------

1. [Command line user interface](#command-line-user-interface)

Command line user interface
---------------------------

The majority of computer users make use of **graphical user interfaces**
(abbreviated **_GUI_** or **_GUIs_** for plural) to control their machines. That
is, they navigate and control their computers by clicking/sliding icons,
buttons, sliders, etc. with a mouse pointer. Of course, they do use the
keyboard, but not all of the time. The screenshot below shows a graphical user
interface that came with Fedora Core 2 - an old release of the Fedora operating
system that was first released in 2004.

![Screenshot of Fedora Core 2
with a graphical user interface](../img/ch00/fedo_core_2-screenshot.png)  
**Figure 0.1** A screenshot of Fedora Core 2. The presence of graphical icons
and a mouse pointer tells us that this is indeed a GUI.

In a graphical user interface, the visual design (i.e. UI/UX design) takes a
very important role in the user's interpretation and experience. One example of
the effect that the design has on the user's interpretation is, if a button on a
web page that links to the site's Search page contains an icon that illustrates
a house, the user will think that the button will lead to the site's homepage.
Visual design is the key in GUIs.

The graphical user interface is sufficient for average computer users. However,
those who seek for more productivity and efficiency on the computer should know
how to use a **command line interface** (abbreviated **_CLI_**).

A command line interface is where the user controls a computer primarily by
typing commands. Typically, in a command line session, the user types a command
to specify an action, then waits for the action to be done, and then types the
next command. In general, a command line session has 3 distinctive components:
the **prompt**, the **user input**, and the **console output**. They are shown
in **Figure 0.2**.

![Components of a command line session](../img/ch00/cli_components.png)  
**Figure 0.2** 3 distinct types of components in a command line session.

- The **prompt** is a string of text that appears when the computer is ready for
the next command. It basically indicates that the user can now type the next
command.
- The **user input** is a command in the form of text typed in by the user to
specify what the user wants to do.
- The **console output** is a visible chunk of text produced during the
execution of the user's command. The text can be log messages (such as warning
messages or error messages) or the result the user expected to see. For an
example, take a look at **Figure 0.2** again. The first command typed by the
user is `cal`. It is a command used to see a calendar printed in the format
typically used in ordinary calendars. Indeed, the console output produced by
`cal` showed a calendar with the current date highlighted.

As stated earlier, commands are successively executed in a command line
interface. That means, after typing a command, the user will have to wait for
the execution of that command to finish before he/she can issue the next
command<sup><a href="#footnote-1">[1]</a></sup>. To better understand what that
means, see **Figure 0.3**.

![A command line session (shown in an animated GIF)](../img/ch00/cli_session.gif)  
**Figure 0.3** A command line session. Here, it can be clearly seen that
command inputs are successive.

<a name="footnote-1"></a>
> **[1]**: Strictly speaking, this is not true for most CLIs that go with macOS
or GNU/Linux machines, because these are operating systems that can multi-task.
You can technically start a process, let it run in the background, and continue
executing other commands without waiting for the process started earlier to
finish. There are also "terminal multiplexers" which can give you a better image
of different running processes. But for now, let's not worry about those at the
moment, and assume that CLIs don't offer the ability to multitask like they
traditionally did.

Why is it more efficient to use the command line and who use it?
----------------------------------------------------------------

Chapter Summary
---------------

Chapter Quiz
------------
