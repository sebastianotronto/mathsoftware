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

SageMath is a free and open-source mathematical software system which builds
on top of many existing ones: NumPy, SciPy, matplotlib, Sympy, Pari/GP, GAP, R
and many more. Thanks to it, all the features all these languages can be
accessed from a common Python-based interface.
In practice, the SageMath "language" is almost identical to Python, but it
provides a complete set of libraries to deal with many mathematical objects and
computations.

## Videos

For the first few lectures I have filmed some videos which are a shorter
version of what explained in class. You can find all of them in
[this YouTube channel]
(https://www.youtube.com/channel/UCUPWzPfoW5UJInqZcqGCigg).

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
	[Jupyter Notebook](https://jupyter.org/) files. Each notebook file has
	also been converted to pdf.
* `Homework` contains the four homework assignment given during the course.
	They accounted for 100% of the final grade.
* `Resources` contains some random links and files (tutorials, reference
	manual) that I have found online. All credits go to the original authors.
* `src` contains the LaTeX and (and Sage) source code for the files in the
	`Lectures` and `Homework` folders, as well as some "scratchpad" LaTeX file
	written during the lectures as a live example.

## Teaching

If you want to teach a course on the same or similar topic, feel free to use,
modify, adapt and share, as a whole or in part, the material you find in this
repository.
Technically the license is Creative Commons Attribution (see `LICENSE`), so
you should mention where you got this from: a link to this git repository at
the beginning of the course is enough.

Moreover, you should remove or replace the university logo and my email
address, which you can replace with your own or with my personal address
`sebastiano [dot] tronto [at] gmail [dot] com`.

Below you can find some details on how the course was taught.

### Lecture mode, duration and frequency

The lectures were given in remote format, except for the last one which was
given in a classroom with some of the students following it remotely.

For lectures with slides I would switch to a LaTeX editor or Python console
every time I introduced a new feature, so that I could immediately show
it in practice.
For lectures with Jupyter notes I would simply follow them on a Jupyter
notebook, modifying the example and solving the exercises as I went through
them.

The lectures were 3 hours and 30 minutes long (four 45 minute units + 30
minutes for breaks) and they were given roughly once every two weeks, with
some exceptions. This heavily influenced the distribution of the topics in
some cases: for example, the first and second lectures were 3 weeks apart,
so I decided to give a very broad overview of the main features of LaTeX on
the first lecture, saving the technical details for lecture 2, so that the
students could start using it immediately. With a different schedule I would
have probably taken a different approach.

### Content

The content of each lecture was as follows:

* **Lecture 1 (slides 1 and 2):** introduction to the course,
	LaTeX fundamentals.
* **Lecture 2 (slides 3):** more technical details on LaTeX; defining commands,
	using counters (e.g. for theorem numbering) and basic bibliography with
	Bibtex.
* **Lecture 3 (slides 4 and 5):** graphics with TikZ and presentations with
	Beamer.
* **Lecture 4 (slides 6):** a "practical" introduction to Python; in this
	lecture I assumed that the students did not know even the basics of
	programming and I introduced Python mainly as an interactive language, 
	explaining the most common programming structures (conditional statements,
	loops, functions) only towards the end.
* **Lecture 5 (notebook 7):** introduction to SageMath, algebra and some
	cryptography.
* **Lecture 5 (notebooks 8 and 9):** calculus and some basic data analysis
	and plotting with SageMath; interactions between SageMath and LaTeX.
	This lecture was 4 hours and 15 minutes long.
* **Lecture 6 (slides X1 and X2 and respective notebooks):** extra topics;
	the first part is an introduction to the topic of computational complexity,
	the second part covers two topics requested by the students via an
	anonymous questionaire (more cryptography, numerical methods for PDEs).

*Note: Symbolic expressions, a very basic feature of Sage, was introduced at
the beginning of Lecture 5 but used extensively only in the following lecture.
In hindsight it would have been better to swap the contents of the two
lectures and do Symbolic expressions and calculus before algebra. This is
because the Algebra part requires more specific constructions (polynomials,
rings), while one can do most calculus operations simply working with
Symbolic expressions.*

### Homework

There were 4 homework assignments, 2 for LaTeX and 2 for SageMath,
accounting for 100% of the students' final grade.

For the LaTeX assignments some of the exercises are of the type "copy this
thing that you see here" and others were of type "write some stuff in LaTeX,
it does not matter what". The rationale behind the latter type is that I wanted
the students to use LaTeX for whatever they were going to use in their daily
life, inlcuding (if they wanted) homework for other courses.

Most of the SageMath exercises simply required the students to compute some
things, without much "real" programming involved, with the exception of
the second exercise of homework 2. For that one I tried to do something
"fun", but I am not very satisfied with the result: in the end it was harder
to understand the problem than how to solve it.

### Final comments

(I will elaborate my comments on the course overall once I receive the
course evaluation from the students)
