import re

from macros_transformer import macros_transformer
# from rewrite_macros import rewrite_macros

def match_next(s, i=0, d=0):
	if s[i] == '{':
		# print("found {")
		return match_next(s, i+1, d+1)
	elif s[i] == '}':
		# print("found }")
		if d == 0:
			return i
		else:
			return match_next(s, i+1, d-1)
	else:
		return match_next(s, i+1, d)

def section_transformer(nb_chap, file_name, path, title, label):
	f = open(path + file_name + ".tex", "r")
	content = f.read()
	f.close()

	print("> Reading %s" % file_name)

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
		content = "```{image} ./../Illustrations/" + nb_chap + ".jpg\n:alt: illustration\n:class: bg-primary mb-1\n:width: 400px\n:align: center\n```\n" + content

	#### Add title and reference to it
	if file_name == "index":
		content = "(" + nb_chap + "-chap:" + label + ")=\n# " + title + "\n\n" + content
	else:
		content = "(" + nb_chap + "-sec:" + label + ")=\n# " + title + "\n\n" + content

	#### Remove comments
	content = re.sub(r'([^\\])%(.*?)\n', r'\1\n', content)
	#### Remove tilde
	content = re.sub(r'~\$', r' $', content)
	#### Remove hfill
	content = re.sub(r'\\hfill', r'', content)
	#### Rewrite textsuperscript
	content = re.sub(r'\\textsuperscript\{([\s\S]*?)\}', r'\1', content)
	#### Make sure $$ can breath
	content = re.sub(r'\$\$', r'\n$$\n', content)
	#### Replace \[ \] by $$ $$
	content = re.sub(r'\\\[([\s\S]*?)\\\]', r'\n\n$$\1$$\n\n', content)
	#### Remove vskip1em
	content = re.sub(r'\\vskip1em', r'\n', content)
	#### Remove noindent
	content = re.sub(r'\\noindent', r'\n', content)
	#### Remove svgraybox
	content = re.sub(r'\\begin\{svgraybox\}([\s\S]*?)\\end\{svgraybox\}', \
		r'```{admonition} Problem\n\1\n```', content)
	#### Reshape quotes
	content = re.sub(r'\`\`(.*?)\'\'', r'''\1''', content)
	#### Rewrite footnotes
	def rewrite_footnote(s):
		st = s.group(1)
		i = match_next(st)
		# print(st[:i])
		end = re.match(r'[\s\S]*?[:.]', st[i+1:]).end()
		# print(st[i+1:i+1+end])
		return st[i+1:i+1+end] + "\n\n```{margin}\n" + st[:i] + "\n```\n\n" + st[i+1+end:] 

	content = re.sub(r'~?\\footnote\{([\s\S]*)', rewrite_footnote, content)

	#### Deal with references to (sub)*sections

	p1 = r"~\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s1 = r" {} {{ref}}`\1-{}:\2`"

	p2 = r"\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s2 = r"{} {{ref}}`\1-{}:\2`"

	l = [\
	("chap","Chapter"), \
	("sec","Section"), \
	("subsec","Subsection") \
	]

	for (origin_name, destination_name) in l:
		content = re.sub(p1.format(origin_name), s1.format(destination_name, origin_name), content)
		content = re.sub(p2.format(origin_name), s2.format(destination_name, origin_name), content)

	#### Deal with references to parts

	content = re.sub(r'~\\[cC]ref\{part:(.*?)\}', r' Part {ref}`part:\1`', content)
	content = re.sub(r'\\[cC]ref\{part:(.*?)\}', r'Part {ref}`part:\1`', content)

	#### Deal with references to figures and algorithms

	p1 = r"~\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s1 = r" {{numref}}`\1-{}:\2`"
	p2 = r"\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s2 = r"{{numref}}`\1-{}:\2`"

	l = ["fig", "algo"]

	for origin_name in l:
		content = re.sub(p1.format(origin_name), s1.format(origin_name), content)
		content = re.sub(p2.format(origin_name), s2.format(origin_name), content)

	#### Deal with references to theorems and others

	p = r"~?\\[cC]ref\{{(\d*?)-{}:(.*?)\}}"
	s = r" {{prf:ref}}`\1-{}:\2`"

	l = ["thm","def","prop","lem", "ex"]

	for origin_name in l:
		content = re.sub(p.format(origin_name), s.format(origin_name), content)

	#### Deal with figures

	# remove figs and creates files

	list_fig = re.findall(r'\\begin\{figure\*?\}[\s\S]*?(\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\})[\s\S]*?\\caption\{[\s\S]*?\}\s*?\\label\{(.*?)\}\s*?\\end\{figure\*?\}', content)

	for x in list_fig:
		h = open("FigAndAlgos/" + x[1] + ".tex", 'w')
		macros_transformer(path,"macros_local.tex")
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\usepackage{amsfonts,amssymb,amsmath}\n\
\\usepackage{tikz}\n\\usetikzlibrary{automata,shapes,patterns,calc,arrows}\n\
\\input{../tikz-style.tex}\n\
\\input{../norenew_macros.tex}\n\
\\input{./../" + path + "norenew_macros_local.tex}\n\
\\begin{document}\n" + x[0] + "\n\\end{document}")

	pattern = r'\\begin\{figure\*?\}[\s\S]*?\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}[\s\S]*?\\caption\{([\s\S]*?)\}\s*?\\label\{(.*?)\}\s*?\\end\{figure\*?\}'
	content = re.sub(pattern, r'\n```{figure} ./../FigAndAlgos/\2.png\n:name: \2\n:align: center\n\1\n```', content)

	#### Deal with algorithms

	# remove algorithms and creates files

	list_algos = re.findall(r'\\begin\{algorithm\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{algorithm\}', content)

	# print(list_algos)

	for x in list_algos:
		h = open("FigAndAlgos/" + x[2] + ".tex", 'w')
		macros_transformer(path,"macros_local.tex")
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\usepackage{amsfonts,amssymb,amsmath}\n\
\\usepackage[norelsize,ruled,vlined,noend]{algorithm2e}\n\
\\input{../norenew_macros.tex}\n\
\\input{./../" + path + "norenew_macros_local.tex}\n\
\\begin{document}\n\\begin{algorithm}[H]\n" + re.sub(r'\\text\{', r'\\textrm{', x[0]) + "\n\\end{algorithm}\n\\end{document}")
		h.close()

	content = re.sub(r'\\begin\{algorithm\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{algorithm\}', \
		r'\n```{figure} ./../FigAndAlgos/\3.png\n:name: \3\n:align: center\n\2\n```', content)
	
	#### Deal with accents
	# Must be after extracting figs and algos: otherwise they would not have correct accents when compiled with LaTeX
	content = re.sub(r'\{\\"u}', r'&uuml;', content)
	content = re.sub(r'\{\\"e}', r'&euml;', content) 
	content = re.sub(r'\{\\"i}', r'&iuml;', content)
	content = re.sub(r'\{\\\'e}', r'&eacute;', content)
	content = re.sub(r'\{\\\'E}', r'&Eacute;', content)
	content = re.sub(r'\{\\\`e}', r'&egrave;', content)
	content = re.sub(r'\{\\\'n}', r'&#324;', content)
	content = re.sub(r'\{\\\'y}', r'&yacute;', content)

	#### Deal with decisionproblems and tasks
	def rewrite_decisionproblems(s):
		s = s.group(1)
		i = match_next(s)
		inp = s[:i]
		j = match_next(s[i+2:])
		out = s[i+2:i+2+j]
		return "**INPUT**: " + inp + "\n\n**QUESTION**: " + out + "\n" + s[i+2+j+1:]

	pattern = r'\\decisionproblem\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_decisionproblems, content)
		match = re.search(pattern, content)

	def rewrite_tasks(s):
		s = s.group(1)
		i = match_next(s)
		inp = s[:i]
		j = match_next(s[i+2:])
		out = s[i+2:i+2+j]
		return "**INPUT**: " + inp + "\n\n**COMPUTE**: " + out + "\n" + s[i+2+j+1:]

	pattern = r'\\task\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_tasks, content)
		match = re.search(pattern, content)

	# content = re.sub(r'\\task\{([\s\S]*?)\}\{([\s\S]*?)\}\n', r'**INPUT**: \1\n\n**COMPUTE**: \2\n', content)

	#### Deal with subsections and subsubsections

	# replace
	# \subsection*{Players}
	# \label(4-sec:label)
	# by
	# (4-sec:label)=
	# ## Players 

	def rewrite_subsections(s):
		s = s.group(1)
		i = match_next(s)
		title = s[:i]
		rest = s[i+1:]
		pattern = r'\s*?\\label\{.*?\}'
		if re.match(pattern, rest) != None:
			match = re.search(r'\{.*?\}', rest)
			return "\n(" + match.group()[1:match.end()-match.start()-1] + ")=\n## " + title + "\n" + rest[match.end()+1:]
		else:
			return "\n## " + title + "\n" + rest

	pattern = r'\\subsection\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_subsections, content)
		match = re.search(pattern, content)

	def rewrite_subsubsections(s):
		s = s.group(1)
		i = match_next(s)
		title = s[:i]
		rest = s[i+1:]
		pattern = r'\s*?\\label\{.*?\}'
		if re.match(pattern, rest) != None:
			match = re.search(r'\{.*?\}', rest)
			return "\n(" + match.group()[1:match.end()-match.start()-1] + ")=\n### " + title + "\n" + rest[match.end()+1:]
		else:
			return "\n### " + title + "\n" + rest

	pattern = r'\\subsubsection\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_subsubsections, content)
		match = re.search(pattern, content)

	# content = re.sub(r'\\subsection\*\{([\s\S]*?)\}\s*?\\label\{(.*?)\}', r'\n(\2)=\n## \1\n', content)
	# content = re.sub(r'\\subsection\*\{([\s\S]*?)\}\n', r'\n## \1\n', content)

	# content = re.sub(r'\\subsubsection\*\{([\s\S]*?)\}[\s]*?\\label\{(.*?)\}', r'\n(\2)=\n### \1\n', content)
	# content = re.sub(r'\\subsubsection\*\{([\s\S]*?)\}\n', r'\n### \1\n', content)
 
	#### Remove paragraphs

	def rewrite_paragraphs(s):
		s = s.group(1)
		i = match_next(s)
		title = s[:i]
		return "> **" + title + "**\n\n" + s[i+1:]

	pattern = r'\\paragraph\*?\{\\bf ([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_paragraphs, content)
		match = re.search(pattern, content)

	pattern = r'\\paragraph\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_paragraphs, content)
		match = re.search(pattern, content)

	#### Rewrite quotation

	# replace
	# \begin{quotation}
	# ``An extraordinary number of basic ideas in model theory can be expressed in terms of games.''
	# \end{quotation}
	# by
	# > An extraordinary number of basic ideas in model theory can be expressed in terms of games.

	content = re.sub(r'\\begin\{quotation\}\n``([\s\S]*?)\'\'\n\\end\{quotation\}', r'\n\n> \1\n\n', content)

	#### Rewrite highlighted text
	def rewrite_highlighted(s):
		s = s.group(1)
		i = match_next(s)
		high = s[:i]
		return "**" + high + "**" + s[i+1:]

	pattern = r'\\textit\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_highlighted, content)
		match = re.search(pattern, content)

	pattern = r'\\emph\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_highlighted, content)
		match = re.search(pattern, content)

	pattern = r'\\textbf\*?\{([\s\S]*)'
	match = re.search(pattern, content)
	while match:
		content = re.sub(pattern, rewrite_highlighted, content)
		match = re.search(pattern, content)

	#### Remove knowledge
	content = re.sub(r'""(.*?)""', r'\1', content)
	content = re.sub(r'"(.*?)"', r'\1', content)
	content = re.sub(r'\\knowledge.*?\n', r'', content)


	#### Deal with itemize

	def rewrite_itemize(s):
		return re.sub(r'\\item', r"* ", s.group(1))

	content = re.sub(r'\\begin\{itemize\}([\s\S]*?)\\end\{itemize\}', rewrite_itemize, content)

	#### Deal with enumerate

	class rewrite_numbered_items(object):
		def __init__(self, start = 1):
			self.count = start - 1
		def __call__(self, match):
			self.count += 1
			return "\n{}. ".format(self.count)

	def rewrite_enumerate(s):
		return re.sub(r'\\item', rewrite_numbered_items(), s.group(1))

	content = re.sub(r'\\begin\{enumerate\}([\s\S]*?)\\end\{enumerate\}', rewrite_enumerate, content)

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
	p1 = r'\\begin\{{{}\}}\[(.*?)\]\n*?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s1 = r'\n```{{prf:{}}} \1\n:label: \2\n:nonumber:\n\3\n```\n'
	s1 = r'\n````{{prf:{}}} \1\n:label: \2\n\3\n````\n'

	# just a label
	p2 = r'\\begin\{{{}\}}\n*?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s2 = r'\n```{{prf:{}}} NEEDS TITLE \1\n:label: \1\n:nonumber:\n\2\n```\n'
	s2 = r'\n````{{prf:{}}} NEEDS TITLE \1\n:label: \1\n\2\n````\n'

	# just a title
	p3 = r'\\begin\{{{}\}}\[(.*?)\]\n*?([\s\S]*?)\\end\{{{}\}}'
	# s3 = r'\n```{{prf:{}}} NEEDS LABEL \1\n:label: \1\n:nonumber:\n\2\n```\n'
	s3 = r'\n````{{prf:{}}} NEEDS LABEL \1\n\2\n````\n'

	# none
	p4 = r'\\begin\{{{}\}}([\s\S]*?)\\end\{{{}\}}'
	# s4 = r'\n```{{prf:{}}} NEEDS TITLE AND LABEL \1 \n:label: \1\n:nonumber:\n\1\n```\n'
	s4 = r'\n````{{prf:{}}} NEEDS TITLE AND LABEL \1 \n\1\n````\n'

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

	for (origin_name, destination_name) in l:
		content = re.sub(p1.format(origin_name,origin_name), s1.format(destination_name), content)
		content = re.sub(p2.format(origin_name,origin_name), s2.format(destination_name), content)
		content = re.sub(p3.format(origin_name,origin_name), s3.format(destination_name), content)
		content = re.sub(p4.format(origin_name,origin_name), s4.format(destination_name), content)

	#### Deal with examples
	# The issue is that examples may contain other environments, like figures

	# if it has a title and a label
	p1 = r'\\begin\{{{}\}}\[(.*?)\]\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s1 = r'\n```{{prf:{}}} \1\n:label: \2\n:nonumber:\n\3\n```\n'
	s1 = r'\n````{{prf:{}}} \1\n:label: \2\n\3\n````\n'

	# just a label
	p2 = r'\\begin\{{{}\}}\n?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s2 = r'\n```{{prf:{}}} NEEDS TITLE \1\n:label: \1\n:nonumber:\n\2\n```\n'
	s2 = r'\n````{{prf:{}}} NEEDS TITLE \1\n:label: \1\n\2\n````\n'

	# just a title
	p3 = r'\\begin\{{{}\}}\[(.*?)\]\n?([\s\S]*?)\\end\{{{}\}}'
	# s3 = r'\n```{{prf:{}}} NEEDS LABEL \1\n:label: \1\n:nonumber:\n\2\n```\n'
	s3 = r'\n````{{prf:{}}} NEEDS LABEL \1\n\2\n````\n'

	# none
	p4 = r'\\begin\{{{}\}}([\s\S]*?)\\end\{{{}\}}'
	# s4 = r'\n```{{prf:{}}} NEEDS TITLE AND LABEL \1 \n:label: \1\n:nonumber:\n\1\n```\n'
	s4 = r'\n````{{prf:{}}} NEEDS TITLE AND LABEL \1 \n\1\n````\n'

	origin_name = "example"
	destination_name = "example"
	content = re.sub(p1.format(origin_name,origin_name), s1.format(destination_name), content)
	content = re.sub(p2.format(origin_name,origin_name), s2.format(destination_name), content)
	content = re.sub(p3.format(origin_name,origin_name), s3.format(destination_name), content)
	content = re.sub(p4.format(origin_name,origin_name), s4.format(destination_name), content)

	#### Deal with remarks

	content = re.sub(r'\\begin\{remark\}([\s\S]*?)\\end\{remark\}', \
		r'\n````{admonition} Remark \1\n````\n', content)

	#### Deal with proof

	content = re.sub(r'\\begin\{proof\}([\s\S]*?)\\end\{proof\}', \
		r'\n````{admonition} Proof\n:class: dropdown tip\n\1\n````\n', content)

	#### Deal with citations
	content = re.sub(r'~\\cite\{(.*?)\}', r' {cite}`\1`', content)
	content = re.sub(r'\\cite\{(.*?)\}', r'{cite}`\1`', content)

	#### Remove indents
	content = re.sub(r'\t', r'', content)
	#### Remove double newlines
	content = re.sub(r'\n\n\n', r'\n\n', content)

	# print(content)

	g = open(path + file_name + ".md", "w")
	g.write(content)
	g.close()

	# rewrite_macros(path,file_name)

