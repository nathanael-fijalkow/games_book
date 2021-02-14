import re

def section_transformer(nb_chap, file_name, path, title):
	f = open(path + file_name + ".tex", "r")
	content = f.read()
	f.close()

	print("reading %s" % file_name)

	#### Add macros

	f = open("macros_complexity.tex", "r")
	macros_complexity = f.read()
	content = macros_complexity + "```\n" + content
	f.close()

	f = open("macros.tex", "r")
	macros = f.read()
	macros = re.sub(r'%(.*?)\n', r'', macros)
	macros = re.sub(r'\n\n', r'\n', macros)
	content = macros + content
	f.close()

	f = open(path + "macros_local.tex", "r")
	macros_local = f.read()
	macros_local = re.sub(r'%(.*?)\n', r'', macros_local)
	macros_local = re.sub(r'\n\n', r'\n', macros_local)
	content = "```{math}\n" + macros_local + content
	f.close()

	#### Add illustration 
	if file_name == "index":
		content = "```{image} ./../" + nb_chap + ".jpg\n:alt: illustration\n:class: bg-primary mb-1\n:width: 400px\n:align: center\n```\n" + content

	#### Add title and reference to it
	content = "(" + nb_chap + "-sec:" + file_name + ")=\n# " + title + "\n\n" + content

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'', content)

	#### Remove tilde
	content = re.sub(r'~\$', r' $', content)

	#### Remove vfill
	content = re.sub(r'\\hfill', r'', content)

	#### Deal with figures

	# remove figs and creates files

	list_fig = re.findall(r'\\begin\{figure\*?\}[\s\S]*?(\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\})[\s\S]*?\\caption\{[\s\S]*?\}[\s\S]*?\\label\{(.*?)\}[\s\S]*?\\end\{figure\*?\}', content)

	for x in list_fig:
		h = open(x[1] + ".tex", 'w')
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\usepackage{tikz}\n\\usetikzlibrary{automata,shapes,patterns,calc,arrows}\n\
\\input{tikz-style.tex}\n\
\\input{norenew_macros.tex}\n\
\\input{" + path + "macros_local.tex}\n\
\\usepackage{amsfonts}\n\
\\begin{document}\n" + x[0] + "\n\\end{document}")

	pattern = r'\\begin\{figure\*?\}[\s\S]*?\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}[\s\S]*?\\caption\{([\s\S]*?)\}[\s\S]*?\\label\{(.*?)\}[\s\S]*?\\end\{figure\*?\}'
	content = re.sub(pattern, r'\n```{figure} ./../\2.png\n:name: \2\n:align: center\n\1\n```', content)

	#### Deal with algorithms

	# remove algorithms and creates files

	list_algos = re.findall(r'\\begin\{algorithm\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{algorithm\}', content)

	# print(list_algos)

	for x in list_algos:
		h = open(x[2] + ".tex", 'w')
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\input{norenew_macros.tex}\n\
\\input{" + path + "macros_local.tex}\n\
\\usepackage{amsfonts}\n\
\\usepackage[norelsize,ruled,vlined,noend]{algorithm2e}\n\
\\begin{document}\n\\begin{algorithm}[H]\n" + re.sub(r'\\text\{', r'\\textrm{', x[0]) + "\n\\end{algorithm}\n\\end{document}")
		h.close()

	content = re.sub(r'\\begin\{algorithm\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{algorithm\}', \
		r'\n```{figure} ./../\3.png\n:name: \3\n:align: center\n\2\n```', content)

	#### Deal with accents
	content = re.sub(r'\{\\"u}', r'&uuml;', content)
	content = re.sub(r'\{\\"e}', r'&euml;', content) 
	content = re.sub(r'\{\\"i}', r'&iuml;', content)
	content = re.sub(r'\{\\\'e}', r'&eacute;', content)
	content = re.sub(r'\{\\\'E}', r'&Eacute;', content)
	content = re.sub(r'\{\\\`e}', r'&egrave;', content)
	content = re.sub(r'\{\\\'n}', r'&#324;', content)

	#### Deal with decisionproblems and tasks

	content = re.sub(r'\\decisionproblem\{([\s\S]*?)\}\{([\s\S]*?)\}\n', r'**INPUT**: \1\n\n**QUESTION**: \2\n', content)
	content = re.sub(r'\\task\{([\s\S]*?)\}\{([\s\S]*?)\}\n', r'**INPUT**: \1\n\n**COMPUTE**: \2\n', content)

	#### Deal with subsections and subsubsections

	# replace
	# \subsection*{Players}
	# by
	# ## Players 

	content = re.sub(r'\\subsection\*\{([\s\S]*?)\}', r'\n## \1\n', content)
	content = re.sub(r'\\subsubsection\*\{([\s\S]*?)\}', r'\n### \1\n', content)

	#### Replace \[ \] by $$ $$
	content = re.sub(r'\\\[([\s\S]*?)\\\]', r'\n\n$$\1$$\n\n', content)

	#### Remove vskip1em
	content = re.sub(r'\\vskip1em', r'\n', content)
 
	#### Remove vskip1em
	content = re.sub(r'\\paragraph\*?\{\\bf (.*?)\}', r'> **\1**\n', content)

	#### Rewrite quotation

	# replace
	# \begin{quotation}
	# ``An extraordinary number of basic ideas in model theory can be expressed in terms of games.''
	# \end{quotation}
	# by
	# > An extraordinary number of basic ideas in model theory can be expressed in terms of games.

	content = re.sub(r'\\begin\{quotation\}\n``([\s\S]*?)\'\'\n\\end\{quotation\}', r'\n\n> \1\n\n', content)

	#### Rewrite textit and emph
	content = re.sub(r'\\textit\{([\s\S]*?)\}', r'**\1**', content)
	content = re.sub(r'\\emph\{([\s\S]*?)\}', r'**\1**', content)
	content = re.sub(r'\\textbf\{([\s\S]*?)\}', r'**\1**', content)

	#### Remove svgraybox
	content = re.sub(r'\\begin\{svgraybox\}([\s\S]*?)\\end\{svgraybox\}', \
		r'```{admonition} Problem\n\1\n```', content)

	#### Remove knowledge
	content = re.sub(r'""(.*?)""', r'\1', content)
	content = re.sub(r'"(.*?)"', r'\1', content)

	#### Reshape quotes
	content = re.sub(r'\`\`(.*?)\'\'', r'''\1''', content)

	#### Deal with itemize
	content = re.sub(r'\\begin\{itemize\}([\s\S]*?)\\end\{itemize\}', r'\1', content)
	content = re.sub(r'\\item([\s\S]*?)', r'* \1', content)

	#### Deal with theorem and many other environments

	# replace
	# \begin{theorem}[Banach fixed point theorem]
	# \label{1-thm:banach}
	# Content
	# \end{theorem}

	# by

	# ```{prf:theorem} Banach fixed point theorem
	# :label: 1-thm:banach
	# Content
	# ```

	# if it has a title and a label
	p1 = r'\\begin\{{{}\}}\[(.*?)\]\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	s1 = r'\n```{{prf:{}}} \1\n:label: \2\n:nonumber:\n\3\n```\n'

	# just a label
	p2 = r'\\begin\{{{}\}}\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	s2 = r'\n```{{prf:{}}} needs title \1\n:label: \1\n:nonumber:\n\2\n```\n'

	# just a title
	p3 = r'\\begin\{{{}\}}\[(.*?)\]\n?([\s\S]*?)\\end\{{{}\}}'
	s3 = r'\n```{{prf:{}}} needs label \1\n:label: \1\n:nonumber:\n\2\n```\n'

	# none
	p4 = r'\\begin\{{{}\}}([\s\S]*?)\\end\{{{}\}}'
	s4 = r'\n```{{prf:{}}} needs title and label \1 \n:label: \1\n:nonumber:\n\1\n```\n'

	l = [\
	("theorem","theorem"), \
	("lemma","lemma"), \
	("fact","observation"), \
	("corollary","corollary"), \
	("definition","definition"), \
	("convention","remark"), \
	("proposition","proposition"), \
	("property","property") \
	]

	for (short_name, long_name) in l:
		content = re.sub(p1.format(short_name,short_name), s1.format(long_name), content)
		content = re.sub(p2.format(short_name,short_name), s2.format(long_name), content)
		content = re.sub(p3.format(short_name,short_name), s3.format(long_name), content)
		content = re.sub(p4.format(short_name,short_name), s4.format(long_name), content)


	#### Deal with remarks

	p = r'\\begin\{{remark\}}([\s\S]*?)\\end\{{remark\}}'
	s = r'\n```{{admonition}} Remark\1\n```\n'
	content = re.sub(p.format(short_name,short_name), s.format(long_name), content)

	#### Deal with proof

	content = re.sub(r'\\begin\{proof\}([\s\S]*?)\\end\{proof\}', \
		r'\n```{admonition} Proof\n:class: dropdown tip\n\1\n```\n', content)

	#### Deal with references to (sub)*sections

	p = r"~?\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s = r" {} {{ref}}`\1-{}:\2`"

	l = [\
	("chap","Chapter"), \
	("sec","Section"), \
	("subsec","Subsection") \
	]

	for (short_name, long_name) in l:
		content = re.sub(p.format(short_name), s.format(long_name, short_name), content)

	#### Deal with references to parts

	content = re.sub(r'~?\\[cC]ref\{part:(.*?)\}', r' Part {ref}`part:\1`', content)

	#### Deal with references to figures and algorithms

	p = r"~?\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s = r" {{numref}}`\1-{}:\2`"

	l = ["fig", "algo"]

	for short_name in l:
		content = re.sub(p.format(short_name), s.format(short_name), content)


	#### Deal with references to theorems and others

	p = r"~?\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s = r" {{prf:ref}}`\1-{}:\2`"

	l = ["thm","def","prop","lem"]

	for short_name in l:
		content = re.sub(p.format(short_name), s.format(short_name), content)

	#### Deal with citations
	content = re.sub(r'~\\cite\{(.*?)\}', r' {cite}`\1`', content)
	#### Remove indents
	content = re.sub(r'\t', r'', content)
	#### Remove double newlines
	content = re.sub(r'\n\n\n', r'\n\n', content)
	#### Rewrite footnotes
	content = re.sub(r'\\footnote\{(.*?).\}', r' (\1)', content)

	# print(content)

	g = open(path + file_name + ".md", "w")
	g.write(content)
	g.close()
