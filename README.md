# Summer 2025 Crash Course for Katelyn.

# Task 0: Git git.

Git is a version control system that can keep track of a project's changes over time,
especially as multiple people start working on it.
Think about how a team of programmers and artists might use something like Google Drive.
They'd upload their code and stuff using a shared drive,
but this would be annoying to manage
when the only thing you could do to tell about the state
of the project is whether or not someone uploaded something and when they did it.

For instance, what happens if some idiot accidentally wipes an entire folder from existence?
or if you see a file was "Last Changed by Ralph Yesterday";
did Ralph do a major change that he hasn't gotten around to telling you yet,
or was it because he just overwrote the file with the
same content when he was drag-and-dropping into the drive?
Git, while quite obtuse and annoying, is designed for this purpose:
to keep a history of who did what
and provide ways to undo or merge people's changes together.

For you though, we can keep the git usage simple
where you'll pretty much use it to download this repository,
keep it up-to-date whenever I make changes,
and upload code as a way to keep track of your progress so far.
Because of this, you don't need to learn git within the console (the traditional way);
you can take the more user-friendly approach with the [GitHub Desktop GUI](https://git-scm.com/downloads/guis).

![](./data/GitDesktopDownload.png)

# Task 1: Using brain more.

REPL stands for Read-Evalulate-Print-Loop.
The idea is that you have a command-line program that prompts the user for some sort of expression.
The REPL program would take this input, interpret it, evaluate it, print the result, and then prompt the user for the next input.
For instance, a simple example of a REPL program could do some basic math operations:
```
> 2 + 2
4

> 3 * 4
12
```

... be able to handle operator precedence (think PEMDAS) and have subexpressions:
```
> (5 - 2 * 10) / 4
-3.25

> 2 - 2^2 * 2
-6
```

... even have some built-in functions:
```
> abs((5 - 2 * 10) / 4)
3.25

> sqrt(4)
2
```

... and even variables defined by the user:
```
> a = 3
a = 3

> b = 5
b = 5

> c = -2
c = -2

> a + b + c
6

> (-b + sqrt(b^2 - 4 * a * c)) / (2 * a)
1.434258545910665
```

Python has a REPL program too; you simply run the `python` (or `python3`) command in
the shell/terminal/console and then you can type some Python code line-by-line and have it
be evaluated each time you press enter.
I highly suggest you play with that a bit to be more famailar with the idea of REPL.

Your goal then would be to make a REPL program as described above using Python.
It should be able to prompt the user for input, be able to print out the correct calculation,
maybe give an error message if the input is malformed, etc.
The exact requirements are all up to you, but if you need help getting started, check out
the hints described in the other files.
