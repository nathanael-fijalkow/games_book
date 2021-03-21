import re

from macros_transformer import macros_transformer
from rewrite_macros import rewrite_macros

def match_next(s, open_parenthesis, closed_parenthesis, i=0, d=0):
	while (i < len(s)):
		if s[i:i + len(open_parenthesis)] == open_parenthesis:
		# if s.startswith(open_parenthesis, i):
			i += 1
			d += 1
		elif s[i:i + len(closed_parenthesis)] == closed_parenthesis:
		# elif s.startswith(closed_parenthesis, i):
			if d == 0:
				return i
			else:
				i += 1
				d -= 1
		else:
				i += 1
	return None

def section_transformer(nb_chap, file_name, path, title, label):
	f = open(path + file_name + ".tex", "r")
	content = f.read()
	f.close()

	print("> Reading %s" % file_name)

	#### Remove comments
	content = re.sub(r'(?!\\)%(.*?)(?=\n)', r'', content)

	#### Remove local macros for tex
	content = re.sub(r'\\input\{macros_local_tex\}', r'', content)

	#### Add macros
	f = open("macros_complexity.tex", "r")
	macros_complexity = f.read()
	content = macros_complexity + "```\n" + content
	f.close()

	f = open("macros.tex", "r")
	macros = f.read()
	macros = re.sub(r'%(.*?)\n', r'\n', macros)
	macros = re.sub(r'\n\n', r'\n', macros)
	content = macros + content
	f.close()

	f = open(path + "macros_local.tex", "r")
	macros_local = f.read()
	macros_local = re.sub(r'%(.*?)\n', r'\n', macros_local)
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

	#### Remove tilde
	# Question: what can go wrong with ~?
	# content = re.sub(r'~\$', r' $', content)
	content = re.sub(r'~', r' ', content)
	#### Remove hfill
	content = re.sub(r'\\hfill', r'', content)
	#### Rewrite textsuperscript
	content = re.sub(r'\\textsuperscript\{([\s\S]*?)\}', r'\1', content)
	#### Remove scriptsize
	content = re.sub(r'\\scriptsize\{([\s\S]*?)\}', r'\1', content)
	#### Make sure $$ can breath
	content = re.sub(r'\$\$', r'\n\n$$\n\n', content)
	#### Rewrite textsc
	content = re.sub(r'_\\textsc\{([\s\S]*?)\}', r'_{\1}', content)
	content = re.sub(r'\\textsc\{([\s\S]*?)\}', r'\1', content)
	#### Replace \[ \] by $$ $$
	content = re.sub(r'\\\[([\s\S]*?)\\\]', r'\n\n$$\1$$\n\n', content)
	#### Remove vskip1em
	content = re.sub(r'\\vskip1em', r'\n', content)
	#### Remove medskip
	content = re.sub(r'\\medskip', r'\n', content)
	#### Remove noindent
	content = re.sub(r'\\noindent', r'', content)
	#### Remove begingroup and endgroup
	content = re.sub(r'\\begingroup', r'', content)
	content = re.sub(r'\\endgroup', r'', content)
	#### Remove allowdisplaybreaks
	content = re.sub(r'\\allowdisplaybreaks', r'', content)
	#### Remove AP
	content = re.sub(r'\\AP', r'', content)
	#### Remove svgraybox
	## Obsolete: removed svgraybox
	# content = re.sub(r'\\begin\{svgraybox\}([\s\S]*?)\\end\{svgraybox\}', \
	# 	r'```{admonition} Problem\n\1\n```', content)
	#### Reshape quotes
	content = re.sub(r'\`(.*?)\'', r'\1', content)
	#### Remove ensuremath
	pattern = r'\\ensuremath\{([\s\S]*?)$'
	match = re.search(pattern, content)
	while match:
		(begin_eq,end_eq) = match.span()
		eq = match.group(1)
		end_eq = match_next(eq, '{', '}')
		new_eq = eq[:end_eq]
		# print("new_eq\n" + new_eq)
		content = content[:begin_eq] + new_eq + content[begin_eq + 13 + end_eq:]
		match = re.search(pattern, content)

	#### Rewrite \?, \+ 
	content = re.sub(r'\\[?](\w*?)(?=\W)', r'\\mathcal{\1}', content)
	content = re.sub(r'\\[+](\w*?)(?=\W)', r'\\mathbb{\1}', content)

	#### Remove textrm
	# pattern = r'\\textrm\{([\s\S]*?)$'
	# match = re.search(pattern, content)
	# while match:
	# 	(begin_eq,end_eq) = match.span()
	# 	eq = match.group(1)
	# 	end_eq = match_next(eq, '{', '}')
	# 	new_eq = eq[:end_eq]
	# 	# print("new_eq\n" + new_eq)
	# 	content = content[:begin_eq] + new_eq + content[begin_eq + 9 + end_eq:]
	# 	match = re.search(pattern, content)

	#### Deal with decpb
	# turns 
	# \decpb[title]{\label{label} input}{question}
	# into
	# ```{admonition} Problem title\n:name: label**INPUT**: input\n\n QUESTION**: question\n```

	# pattern = r'\\decpb\[([\s\S]*?)\]\s*\{(\\label\{.*?\})?([\s\S]*?)\}\s*\{([\s\S]*?)\}'
	pattern = r'\\decpb\[([\s\S]*?)\]\s*\{(\\label\{.*?\})?([\s\S]*?)$'
	match = re.search(pattern, content)
	while match:
		(start,end) = match.span()
		title = match.group(1)
		label = match.group(2)[7:-1] if match.group(2) else None
		rest = match.group(3)
		# locate end of input
		i = match_next(rest, '{', '}')	
		dec_input = rest[:i]
		# print("\nINPUT:\n" + dec_input)
		rest = rest[i+1:]
		# locate beginning of question
		match = re.search("{", rest)
		(start_question,end) = match.span()
		rest = rest[start_question + 1:]
		# locate end of question
		i = match_next(rest, '{', '}')	
		dec_question = rest[:i]
		# print("\nQUESTION:\n" + dec_question)
		rest = rest[i+1:]
		# print("\nREST:\n" + rest[:100])
		match = None
		if label:
			new_pb = r'```{admonition} Problem (' + title + ')\n:name: ' + label + '\n**INPUT**: ' + dec_input + '\n\n**QUESTION**: ' + dec_question + '\n```'
			content = content[:start] + new_pb + "\n" + rest
		else:
			new_pb = r'```{admonition} Problem (' + title + ')\n**INPUT**: ' + dec_input + '\n\n**QUESTION**: ' + dec_question + '\n```'
			content = content[:start] + new_pb + "\n" + rest
		match = re.search(pattern, content)

	#### Rewrite footnotes
	# We place the margin before the next stop
	def rewrite_footnote(s):
		st = s.group(1)
		i = match_next(st, '{', '}')
		# print(st[:i])
		end = re.match(r'[\s\S]*?[.\n]', st[i+1:]).end()
		# print(st[i+1:i+1+end])
		return st[i+1:i+1+end] + "\n\n```{margin}\n" + st[:i] + "\n```\n\n" + st[i+1+end:] 

	content = re.sub(r'~?\\footnote\{([\s\S]*)', rewrite_footnote, content)

	#### Deal with equations with labels using align or align* 

	# turn 

	# begin{align}
	# w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
	# \label{5-eq:disc-limit-transition}
	# \end{align}

	# into

	# $$
	# w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
	# $$ (5-eq:disc-limit-transition)

	pattern = r'\\begin\{equation\*?\}([\s\S]*?)\\end\{equation\*?\}'
	match = re.search(pattern, content)
	while match:
		(begin_eq,end_eq) = match.span()
		eq = match.group(1)
		# print(eq)
		pattern_label = r'([\s\S]*?)\\label\{([\d]*?)-eq:(.*?)\}([\s\S]*?)$'
		match_label = re.search(pattern_label, eq)
		if match_label:
			label = match_label.group(2) + '-eq:' + match_label.group(3)
			new_eq = '\n$$\n' + match_label.group(1) + '\n' + match_label.group(4) + '\n$$ (' + label + ')\n'
			# new_eq = '```{math}\n:label: ' + match_label.group(2) + '-eq:' + match_label.group(3) + '\n' + match_label.group(1) + '\n' + match_label.group(4) + '\n```'
		else:
			new_eq = '\n$$\n' + eq + '\n$$\n'
			# new_eq = '```{math}\\n' + eq + r'\\n```'
		content = content[:begin_eq] + new_eq + content[end_eq:]
		match = re.search(pattern, content)

	pattern = r'\\begin\{x?aligna?t?\*?\}([\s\S]*?)\\end\{x?aligna?t?\*?\}'
	match = re.search(pattern, content)
	while match:
		(begin_eq,end_eq) = match.span()
		eq = match.group(1)
		# print(eq)
		pattern_label = r'([\s\S]*?)\\label\{([\d]*?)-eq:(.*?)\}([\s\S]*?)$'
		match_label = re.search(pattern_label, eq)
		if match_label:
			new_eq = '\n$$\n' + match_label.group(1) + '\n' + match_label.group(4) + '\n$$ (' + label + ')\n'
			# new_eq = '```{math}\n:label: ' + match_label.group(2) + '-eq:' + match_label.group(3) + '\n' + match_label.group(1) + '\n' + match_label.group(4) + '\n```'
		else:
			new_eq = '\n$$\n' + eq + '\n$$\n'
			# new_eq = '```{math}\n' + eq + '\n```'
		content = content[:begin_eq] + new_eq + content[end_eq:]
		match = re.search(pattern, content)

	#### Deal with references to decision problems
	# [](link) DOES NOT WORK!
	# Here is [text](label)

	p1 = r"~\\[cC]ref\{(\d*?)-pb:(.*?)\}"
	s1 = r" [Problem](\1-pb:\2)"

	p2 = r"\\[cC]ref\{(\d*?)-pb:(.*?)\}"
	s2 = r"[Problem](\1-pb:\2)"

	content = re.sub(p1, s1, content)
	content = re.sub(p2, s2, content)

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

	#### Deal with references to equations

	p1 = r"~\\[cC]ref\{(\d*?)-eq:(.*?)\}"
	s1 = r" {eq}`\1-eq:\2`"
	p2 = r"\\[cC]ref\{(\d*?)-eq:(.*?)\}"
	s2 = r"{eq}`\1-eq:\2`"

	content = re.sub(p1, s1, content)
	content = re.sub(p2, s2, content)

	#### Deal with references to theorems and others: ["thm","def","prop","lem","ex","rmk"]

	def rewrite_ref(s):
		st = s.group(1)
		list_ref = re.split(r',', st)
		# print(list_ref)
		def ref_list(list_ref):
			if len(list_ref) == 1:
				return r'{prf:ref}`' + list_ref[0] + '`'
			elif len(list_ref) == 2:
				return r'{prf:ref}`' + list_ref[0] + r'` and {prf:ref}`' + list_ref[1] + '`'
			else:
				ref = ""
				for j in range(len(list_ref)-1):
					ref += r'{prf:ref}`' + list_ref[len(list_ref) - 1 - j] + '`, '
				ref += r'and {prf:ref}`' + list_ref[len(list_ref) - 1] + '`'
				return ref
		return ref_list(list_ref)

	p = r"\\[cC]ref\{(.*?)\}"
	content = re.sub(p, rewrite_ref, content)

	#### Deal with figures

	def rewrite_figs(s):
		st = s.group(2)
		# print(st)
		pattern = r'([\s\S]*?)\\caption\{([\s\S]*?)\}\s*\\label\{([\d]*?)-fig:(.*?)\}'
		match = re.search(pattern, st)
		label = match.group(3) + '-fig:' + match.group(4)

		h = open("FigAndAlgos/" + label + ".tex", 'w')
		macros_transformer(path,"macros_local.tex")
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\usepackage{amsfonts,amssymb,amsmath}\n\
\\usepackage{tikz}\n\\usetikzlibrary{automata,shapes,patterns,calc,arrows}\n\
\\input{../tikz-style.tex}\n\
\\input{../norenew_macros.tex}\n\
\\input{./../" + path + "norenew_macros_local.tex}\n\
\\begin{document}\n" + match.group(1) + "\n\\end{document}")
		h.close()

		new_fig = '\n```{figure} ./../FigAndAlgos/' + label 
		new_fig += '.png\n:name: ' + label  
		new_fig += '\n:align: center\n' + match.group(2) + '\n```'
		return new_fig

	pattern_figs = r'\\begin\{figure[*]?\}(\[\w*?\])?([\s\S]*?)\\end\{figure[*]?\}'
	content = re.sub(pattern_figs, rewrite_figs, content)

	#### Deal with algorithms

	# remove algorithms and creates files

	def rewrite_algos(s):
		st = s.group(2)
		# print(st)
		pattern = r'([\s\S]*?)\\caption\{([\s\S]*?)\}\s*\\label\{([\d]*?)-algo:(.*?)\}'
		match = re.search(pattern, st)
		label = match.group(3) + '-algo:' + match.group(4)

		h = open("FigAndAlgos/" + label + ".tex", 'w')
		macros_transformer(path,"macros_local.tex")
		h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
\\usepackage{amsfonts,amssymb,amsmath}\n\
\\usepackage[norelsize,ruled,vlined,noend]{algorithm2e}\n\
\\input{../norenew_macros.tex}\n\
\\input{./../" + path + "norenew_macros_local.tex}\n\
\\begin{document}\n\\begin{algorithm}[H]\n" + re.sub(r'\\text\{', r'\\textrm{', match.group(1)) + "\n\\end{algorithm}\n\\end{document}")
		h.close()

		new_algo = '\n```{figure} ./../FigAndAlgos/' + label 
		new_algo += '.png\n:name: ' + label  
		new_algo += '\n:align: center\n' + match.group(2) + '\n```'
		return new_algo

	pattern_algos = r'\\begin\{algorithm[*]?\}(\[\w*?\])?([\s\S]*?)\\end\{algorithm[*]?\}'
	content = re.sub(pattern_algos, rewrite_algos, content)
	
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

	#### Deal with subsections and subsubsections

	# replace
	# \subsection*{Players}
	# \label(4-sec:label)
	# by
	# (4-sec:label)=
	# ## Players 

	def rewrite_subsections(s):
		s = s.group(1)
		i = match_next(s, '{', '}')
		title = s[:i]
		rest = s[i+1:]
		pattern = r'\s*?\\label\{.*?\}'
		if re.match(pattern, rest):
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
		i = match_next(s, '{', '}')
		title = s[:i]
		rest = s[i+1:]
		pattern = r'\s*?\\label\{.*?\}'
		if re.match(pattern, rest):
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
		i = match_next(s, '{', '}')
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
	# An extraordinary number of basic ideas in model theory can be expressed in terms of games.
	# \end{quotation}
	# by
	# > An extraordinary number of basic ideas in model theory can be expressed in terms of games.

	content = re.sub(r'\\begin\{quotation\}\n([\s\S]*?)\n\\end\{quotation\}', r'\n\n> `\1\'\n\n', content)

	#### Remove knowledge
	content = re.sub(r'""([^"]*?)@[^"]*?""', r'\1', content)
	content = re.sub(r'""([^"]*?)""', r'\1', content)
	content = re.sub(r'"([^"]*?)@[^"]*?"', r'\1', content)
	content = re.sub(r'"([^"]*?)"', r'\1', content)
	content = re.sub(r'\\knowledge[\s\S]*?\n', r'', content)
	content = re.sub(r'\\index\{(\w*?)![\s\S]*?mymoot\}', r'\1', content)

	#### Rewrite highlighted text
	def rewrite_highlighted(s):
		s = s.group(1)
		i = match_next(s, '{', '}')
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

	#### Deal with itemize and enumerate

	class rewrite_numbered_items(object):
		def __init__(self, start = 1):
			self.count = start - 1
		def __call__(self, match):
			self.count += 1
			return "{}. ".format(self.count)

	def rewrite_itemize_enumerate(s, depth = 0):
		pattern_it = r'\\begin\{itemize\}([\s\S]*?)'
		match_it = re.search(pattern_it, s)
		if match_it:
			(begin,end) = match_it.span()
			end = match_next(s[begin+15:], r'\begin{itemize}', r'\end{itemize}')
			s_it = s[begin+15:begin+15+end]
			s_it = rewrite_itemize_enumerate(s_it, depth + 1)
			space = ""
			for i in range(4 * depth): 
				space += " "
			s_it = re.sub(r'\\item', space + "* ", s_it)
			new_s = s[:begin] + s_it + s[begin+28+end:]
			return rewrite_itemize_enumerate(new_s, depth)

		pattern_enum = r'\\begin\{enumerate\}([\s\S]*?)'
		match_enum = re.search(pattern_enum, s)
		if match_enum:
			(begin,end) = match_enum.span()
			end = match_next(s[begin+17:], r'\begin{enumerate}', r'\end{enumerate}')
			s_enum = s[begin+17:begin+17+end]
			s_enum = rewrite_itemize_enumerate(s_enum, depth + 1)
			space = ""
			for i in range(4 * depth): 
				space += " "
			s_enum = re.sub(r'\\item', space + r'\\item', s_enum)
			s_enum = re.sub(r'\\item', rewrite_numbered_items(), s_enum)
			new_s = s[:begin] + s_enum + s[begin+32+end:]
			return rewrite_itemize_enumerate(new_s, depth)			

		return s

	content = rewrite_itemize_enumerate(content)

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
	p1 = r'\\begin\{{{}\}}\[(.*?)\]\s*?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s1 = r'\n```{{prf:{}}} \1\n:label: \2\n:nonumber:\n\3\n```\n'
	s1 = r'\n````{{prf:{}}} \1\n:label: \2\n\3\n````\n'

	# just a label
	p2 = r'\\begin\{{{}\}}\s*?\\label\{{(.*?)\}}([\s\S]*?)\\end\{{{}\}}'
	# s2 = r'\n```{{prf:{}}} NEEDS TITLE \1\n:label: \1\n:nonumber:\n\2\n```\n'
	s2 = r'\n````{{prf:{}}} NEEDS TITLE \1\n:label: \1\n\2\n````\n'

	# just a title
	p3 = r'\\begin\{{{}\}}\[(.*?)\]\s*?([\s\S]*?)\\end\{{{}\}}'
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
	("remark","remark"), \
	("definition","definition"), \
	("convention","remark"), \
	("proposition","proposition"), \
	("property","property"), \
	("example","example") \
	]

	for (origin_name, destination_name) in l:
		content = re.sub(p1.format(origin_name,origin_name), s1.format(destination_name), content)
		content = re.sub(p2.format(origin_name,origin_name), s2.format(destination_name), content)
		content = re.sub(p3.format(origin_name,origin_name), s3.format(destination_name), content)
		content = re.sub(p4.format(origin_name,origin_name), s4.format(destination_name), content)

	#### Deal with proof

	content = re.sub(r'\\begin\{proof\}(\[Sketch\])?([\s\S]*?)\\end\{proof\}', \
		r'\n````{admonition} Proof\n:class: dropdown tip\n\2\n````\n', content)

	#### Deal with citations
	content = re.sub(r'~\\cite[ptm]?\{(.*?)\}', r' {cite}`\1`', content)
	content = re.sub(r'\\cite[ptm]?\{(.*?)\}', r'{cite}`\1`', content)
	content = re.sub(r'~\\cite[ptm]?\[(.*?)\]\{(.*?)\}', r' (\1 in {cite}`\2`)', content)
	content = re.sub(r'\\cite[ptm]?\[(.*?)\]\{(.*?)\}', r'(\1 in {cite}`\2`)', content)

	#### Remove indents
	content = re.sub(r'\t', r'', content)

	# print(content)

	g = open(path + file_name + ".md", "w")
	g.write(content)
	g.close()

	rewrite_macros(path,file_name)

# section_transformer("5", "notations", "5_MDP/", "Index", 'index')