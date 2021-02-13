import re
import sys

from section_transformer import section_transformer
from bib_transformer import bib_transformer

nb_chap = sys.argv[1]
title_chap = sys.argv[2]
path = sys.argv[3]

def chapter_transformer():
	f = open(path + "index.tex", "r")
	content = f.read()

	# Match:
	# \section{What is this book about?}
	# \label{1-sec:intro}
	# \input{intro}

	s_in = r"\\section\*?\{{(.*?)\}}\n\\label\{{{}-sec:.*?\}}\n\\input\{{(.*?)\}}"
	list_section = re.findall(s_in.format(nb_chap), content)
	f.close()

	for (title,file) in list_section:
		section_transformer(nb_chap, file, path, title)


	## Special case: references
	f = open(path + "references.md", "a")
	f.write('\n\n```{bibliography}\n:style: unsrtalpha\n:filter: cited and chap == \"' + nb_chap + '\"\n```')
	f.close()

	# Transforms the bibliography
	new_bib = bib_transformer(nb_chap)
	g = open(nb_chap + "_bib.bib", "w")
	f = open("acronyms.bib", "r")
	h = open("people.bib", "r")

	new_bib = f.read() + h.read() + new_bib
	# print(new_bib)
	g.write(new_bib)
	g.close()

	## Special case: index
	section_transformer(nb_chap, "index", path, title_chap)

	f = open(path + "index.md", "r")
	content = f.read()
	f.close()

	# Remove macros_local
	content = re.sub(r'\\input\{macros_local\}', r'\n', content)

	# Remove the inputs
	content = re.sub(s_in.format(nb_chap), '', content)

	g = open(path + "index.md", "w")
	g.write(content)
	g.close()

chapter_transformer()
