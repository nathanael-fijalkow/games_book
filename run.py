import re
import sys

from script import translate

#### Usage:
## python run.py 1 Introduction

nb_chap = sys.argv[1]
title_chap = sys.argv[2]

def extract_from_main():
	f = open(nb_chap + "_" + title_chap + "/main.tex", "r")
	content = f.read()

	# Match:
	# \section{What is this book about?}
	# \label{1-sec:intro}
	# \input{intro}

	s_in = r"\\section\*?\{{(.*?)\}}\n\\label\{{{}-sec:.*?\}}\n\\input\{{(.*?)\}}"

	list_section = re.findall(s_in.format(nb_chap), content)

	f.close()

	for (title,file) in list_section:
		translate(nb_chap, title_chap, file, title)

	# We finish with main
	translate(nb_chap, title_chap, "main", title_chap)

	f = open(nb_chap + "_" + title_chap + "/main.md", "r")
	content = f.read()
	f.close()

	# Remove macros_local
	content = re.sub(r'\\input\{macros_local\}', r'\n', content)

	# Remove the inputs
	content = re.sub(s_in.format(nb_chap), '', content)

	g = open(nb_chap + "_" + title_chap + "/main.md", "w")
	g.write(content)
	g.close()


extract_from_main()
