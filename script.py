import re

def translate(nb_chap, title_chap, file, title):
	f = open(nb_chap + "_" + title_chap + "/" + file + ".tex", "r")
	content = f.read()
	f.close()

	print("reading %s" % file)

	#### Add title and reference to it
	content = "(" + nb_chap + "-sec:" + file + ")=\n# " + title + "\n\n" + content

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'', content)

	#### Remove tilde
	content = re.sub(r'~\$', r' $', content)

	# #### Remove line breaks
	# content = re.sub(r'\\\\', r'', content)
	### DOES NOT WORK, WE WOULD REMOVE IN TABLES AND ARRAYS

	#### Deal with accents
	content = re.sub(r'\{\\"u}', r'&uuml;', content)
	content = re.sub(r'\{\\"e}', r'&euml;', content) 
	content = re.sub(r'\{\\"i}', r'&iuml;', content)
	content = re.sub(r'\{\\\'e}', r'&eacute;', content)
	content = re.sub(r'\{\\\`e}', r'&egrave;', content)

	#### Deal with figures

	# remove figs and creates files

	list_fig = re.findall(r'\\begin\{figure\}([\s\S]*?)(\\begin\{tikzpicture\}[\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{figure\}', content)

	for x in list_fig:
		h = open(nb_chap + "_" + title_chap + "/Fig/" + x[3] + ".tex", 'w')
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
			\\usepackage{tikz}\n\\usetikzlibrary{automata,shapes,patterns,calc,arrows}\n\
			\\input{tikz-style.tex}\n\\begin{document}\n" + x[1] + "\n\\end{document}")

	content = re.sub(r'\\begin\{figure\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(\d*?)-fig:(.*?)\}\n\\end\{figure\}', \
		r'\n```{figure} Fig/\3-fig:\4.png\n:name: \3-\4\n:align: center\n\2\n```', content)

	#### Deal with subsections and subsubsections

	# replace
	# \subsection*{Players}
	# by
	# ## Players 

	content = re.sub(r'\\subsection\*\{([\s\S]*?)\}', r'\n## \1\n', content)
	content = re.sub(r'\\subsubsection\*\{([\s\S]*?)\}', r'\n### \1\n', content)

	#### Replace \[ \] by $$ $$
	content = re.sub(r'\\\[([\s\S]*?)\\\]', r'\n\n$$\n\1\n$$\n\n', content)

	#### Remove vskip1em
	content = re.sub(r'\\vskip1em', r'\n', content)

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
	# \begin{theorem}[Banach's fixed point theorem]
	# \label{1-thm:banach}
	# Content
	# \end{theorem}

	# by

	# ```{admonition} Theorem
	# :class: result
	# :name: 1-thm:banach
	# Content
	# ```


	# if it has a title and a label
	p1 = r'\\begin\{{{}\}}\[(.*?)\]\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	s1 = r'\n```{{admonition}} {} (\1)\n:class: {}\n:name: \2\n\3\n```\n'

	# just a label
	p2 = r'\\begin\{{{}\}}\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	s2 = r'\n```{{admonition}} {}\n:class: {}\n:name: \1\n\2\n```\n'

	# just a title
	p3 = r'\\begin\{{{}\}}\[(.*?)\]\n?([\s\S]*?)\\end\{{{}\}}'
	s3 = r'\n```{{admonition}} {} (\1)\n:class: {}\n\2\n```\n'

	# none
	p4 = r'\\begin\{{{}\}}([\s\S]*?)\\end\{{{}\}}'
	s4 = r'\n```{{admonition}} {}\n:class: {}\n\1\n```\n'

	l = [\
	("theorem","Theorem"), \
	("lemma","Lemma"), \
	("fact","Fact"), \
	("corollary","Corollary"), \
	("remark","Remark"), \
	("definition","Definition"), \
	("convention","Convention"), \
	("proposition","Proposition"), \
	("principle","Principle") \
	]

	for (short_name, long_name) in l:
		content = re.sub(p1.format(short_name,short_name), s1.format(long_name,short_name), content)
		content = re.sub(p2.format(short_name,short_name), s2.format(long_name,short_name), content)
		content = re.sub(p3.format(short_name,short_name), s3.format(long_name,short_name), content)
		content = re.sub(p4.format(short_name,short_name), s4.format(long_name,short_name), content)


	#### Deal with proof

	content = re.sub(r'\\begin\{proof\}([\s\S]*?)\\end\{proof\}', \
		r'\n```{admonition} Proof\n:class: dropdown tip\n\1\n```\n', content)

	#### Deal with references

	p1 = r"~\\cref\{{(\d*?)-{}:(.*?)\}}"
	s1 = r" {{ref}}`{} <\1-{}:\2>`"

	p2 = r"\\cref\{{(\d*?)-{}:(.*?)\}}"
	s2 = r" {{ref}}`{} <\1-{}:\2>`"

	p3 = r"\\Cref\{{(\d*?)-{}:(.*?)\}}"
	s3 = r"{{ref}}`{} <\1-{}:\2>`"

	l = [\
	("sec","Section"), \
	("chap","Chapter"), \
	("thm","Theorem"), \
	("def","Definition"), \
	("lem","Lemma"), \
	("fig","Figure"), \
	("algo","Algorithm"), \
	]

	for (short_name, long_name) in l:
		content = re.sub(p1.format(short_name), s1.format(long_name, short_name), content)
		content = re.sub(p2.format(short_name), s2.format(long_name, short_name), content)
		content = re.sub(p3.format(short_name), s3.format(long_name, short_name), content)

	content = re.sub(r'~\\cref\{part:(.*?)\}', r' Part {ref}`part:\1`', content)
	content = re.sub(r'\\Cref\{part:(.*?)\}', r'Part {ref}`part:\1`', content)
	content = re.sub(r'\\cref\{part:(.*?)\}', r'Part {ref}`part:\1`', content)


	#### Deal with citations
	content = re.sub(r'~\\cite\{(.*?)\}', r' {cite}`\1`', content)

	#### Remove indents
	content = re.sub(r'\t', r'', content)
	#### Remove double newlines
	content = re.sub(r'\n\n\n', r'\n\n', content)

	### If references, add bibliography
	if file == "references":
		content = content + '\n\n```{bibliography}\n:style: unsrtalpha\n```'

	print(content)

	g = open(nb_chap + "_" + title_chap + "/" + file + ".md", "w")
	g.write(content)
	g.close()
