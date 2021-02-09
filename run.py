import re
import sys

from script import translate

nb_chap = sys.argv[1]
title_chap = sys.argv[2]
path = sys.argv[3]

def extract_from_index():
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
		translate(nb_chap, file, path, title)
		
	# We finish with index
	translate(nb_chap, "index", path, title_chap)

	f = open(path + "index.md", "r")
	content = f.read()
	f.close()

	# Remove macros_local
	content = re.sub(r'\\input\{macros_local\}', r'\n', content)

	# Remove the inputs
	content = re.sub(s_in.format(nb_chap), '', content)

	# content = content + "\n ```{tableofcontents}```"

	g = open(path + "index.md", "w")
	g.write(content)
	g.close()

extract_from_index()
