# Mathematical software

Course given in Spring 2021 at the University of Luxembourg.

If you just want to check out the notes for the course, see the `Lectures`
folder and the `Videos` section below. If you want to teach a similar course,
see the `Teaching` section below.

## Description

The goal of the course is to teach the basics of
[LaTeX](https://en.wikipedia.org/wiki/LaTeX) and
[SageMath](https://www.sagemath.org/), so that the students reach a broad
understanding of these tools and can use them whenever needed, such as if they
need to write a Thesis, prepare slides for a presentation or carry out
intense computations.

### LaTeX

LaTeX is a markup language to write and format documents of any type. It is
particularly well-suited for scientific documents, but it can be used for any
type of document, including books, CVs and even presentation slides.
It can be used together with a graphical front-end (such as TexMaker,
TexStudio, Overleaf...) to immediately see the pdf output. The main advantage
over a more classical word processor such as Microsoft Word, besides a much
better support for writing mathematical formulas and theorems, is that in
LaTeX [What you see is what you mean](https://en.wikipedia.org/wiki/WYSIWYM):
by typing commands instead of
visually changing the appearence of the text, the "compiler" will always try to
produce an output that is faithful to what the user indicated, so the user does
not have to manually adjust the result after every major modification.

### SageMath

SageMath is a free and open-source mathematical software system which builds
on top of many existing ones: NumPy, SciPy, matplotlib, Sympy, Pari/GP, GAP, R
and many more. Thanks to it, all the features all these languages can be
accessed from a common Python-based interface.
In practice, the SageMath "language" is almost identical to Python, but it
provides a complete set of libraries to deal with many mathematical objects and
computations.

## Videos

For the first few lectures I have filmed some videos which are a shorter
version of what explained in class. You can find all of them in [this YouTube
channel](https://www.youtube.com/channel/UCUPWzPfoW5UJInqZcqGCigg).

* [Getting started with LaTeX](https://www.youtube.com/watch?v=HVvQpZEeIDI)
* [LaTeX bibliography](https://www.youtube.com/watch?v=-KrNY7BXdPo)
* [Defining commands in LaTeX](https://www.youtube.com/watch?v=IFt259434Zg)
* [LaTeX theorem numbering](https://www.youtube.com/watch?v=pjm18Ceg6lg)
* [Graphics with TikZ](https://www.youtube.com/watch?v=mWqhB6qOIk0)
* [Introduction to Python](https://www.youtube.com/watch?v=b7k3hlW2DMs)

## Files

The files in this repository are organized as follows:

* `Lectures` contains the slides and notes I have made and used during the
  lectures. Some of them are classic (Beamer) slides, some other are
  [Jupyter Notebook](https://jupyter.org/) files.
* `Homework` contains the four homework assignment given during the course.
  They accounted for 100% of the final grade.
* `Resources` contains some random files (tutorials, reference manual) that I
  have found online. All credits go to the original authors.
* `src` contains the LaTeX and (and Sage) source code for the files in the
  `Lectures` and `Homework` folders, as well as some "scratchpad" LaTeX file
  written during the lectures as a live example.

## Teaching

INS guidelines for teachers who want to do something similar (including how long
each lecture was etc.)

INS also stuff about license (use my personal email address instead of unilu)

INS also list of topics for each lecture (take from moodle)
