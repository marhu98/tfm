compile:
	pdflatex tfm.tex
	bibtex tfm
	pdflatex tfm.tex
	pdflatex tfm.tex
watch:
	ls chapters/*.tex | entr -c make compile
