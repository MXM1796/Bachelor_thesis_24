# University of Bonn thesis style

Thesis style that can be used for bachelor, master and PhD theses
in physics and astronomy (and other subjects) at the University of Bonn.
See `CHANGELOG.md` or Git log for history of changes.

*Responsible:* Ian Brock (i.brock@uni-bonn.de)

Copyright (C) 2011-2023 Ian Brock

------

## Version 10.0 03/03/2023

The original idea with this package was that you also look at the LaTeX that
is used to create it, in order to find out how things are done.
As time goes by I am including more examples as listings directly inside the thesis guide.

The files that make up this package are available in a Git
repository and as a tar file. To get the latest version
give the command:

```bash
git clone https://bitbucket.team.uni-bonn.de/scm/uni/ubonn-thesis.git
```

If you want a particular release use the command:

```bash
git clone --branch 8.0 https://bitbucket.team.uni-bonn.de/scm/uni/ubonn-thesis.git
```

Note that the Git repository is only accessible from inside the University of Bonn network.

The tar file includes the guide as a PDF file: `guide/thesis_guide.pdf`.
It can also be obtained from:
<https://www.pi.uni-bonn.de/brock/en/thesis-guide>

## New thesis

You can give the command:

```bash
make new [THESIS=dirname]
```

to create a new directory with a few files to help you get
started. By default the directory name will be mythesis.
To compile your thesis try:

```bash
cd mythesis [or dirname]
make thesis|thesislua|thesisxe
```

All packages that are needed should be part of your TeX installation.
If not you may have to install them or ask your system administrator to do so.

## Style file

My original idea was that the style file should work for all recent
TeX installations.  However, some of the packages I recommend have
been changing quite a lot over the past years, particularly
`biblatex` and `siunitx`.  It may therefore be necessary to make a few
changes in order to get the thesis to compile on your machine.
The default version assumes that you have TeX Live 2020 or later.

If you just want to make the cover pages, use the file `cover_only.tex`.
Be sure to adapt the font selected in `ubonn-thesis.sty` to the font
you actually used in your thesis. Be aware that not all font sizes are
available in all font collections. If you used the default LaTeX font
in your thesis, then choose `lmodern` in the style file.

## Compiling the guide

The main file for this guide is `guide/thesis_guide.tex` and it
includes the LaTeX files in the directory `./guide` and the
Feynman graphs in the directories `./feynmf`, `./tikz`, `./pyfeyn` and `./pyfeynhand`.

You can create your own copy of the guide using the commands:

```bash
cd guide|guidelua|guidexe
make guide
```

If you do not have the `newtx` fonts, either install them 
or do not pass an option such as `txfonts` to ubonn-thesis.
If you want to include a glossary and use `latexmk`, you should copy the `latexmk`
directory to your `~/.config/` directory.
Support for TeX Live versions older than 2015 has been removed in version 9.1.

As of version 7.0 I have started testing the thesis skeleton and the guide using
LuaLaTeX and XeLaTeX, as well as the usual pdfLaTeX.
As indicated above, you can use `make thesislua` or `make thesisxe`
to compile with LuaLaTeX or XeLaTeX, respectively.

The guide also includes a description of how to use the package under Windows.
