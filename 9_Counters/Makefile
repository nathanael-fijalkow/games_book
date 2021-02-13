all:
	@grep 'newlabel' ../book.aux | grep -v '11-' > book.aux || /bin/true
	@latexmk -cd -pdf ../11_standalone.tex
	@if [ ! -r main.pdf ] || [ main.pdf -ot 11_standalone.pdf ]; then cp -f 11_standalone.pdf main.pdf; fi

.PHONY: clean
clean:
	rm -f *.aux *.log *~ *.idx *.ilg *.ind *.fdb_latexmk *.fls *.blg *.bbl *.diagnose *.kaux *.out
