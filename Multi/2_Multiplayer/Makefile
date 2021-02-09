compile: main.tex
	cd .. && pdflatex 14_standalone.tex

multiplayer.pdf: multiplayer.md
	pandoc multiplayer.md -o multiplayer.pdf

main.tex: multiplayer.md
	pandoc multiplayer.md -o main.tex
