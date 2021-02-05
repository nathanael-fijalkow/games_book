import re
import sys

chap = sys.argv[1]
file = sys.argv[2]
name = sys.argv[3]
title = sys.argv[4]

f = open(chap + "/" + file + ".tex", "r")

content = f.read()

#### Add title and reference to it
content = "(" + name + ")=\n# " + title + "\n\n" + content

#### Deal with accents
content = re.sub(r'\{\\"u}', r'&uuml;', content)
content = re.sub(r'\{\\"i}', r'&iuml;', content)
content = re.sub(r'\{\\\'e}', r'&eacute;', content)
content = re.sub(r'\{\\\`e}', r'&egrave;', content)

#### Deal with figures

# remove figs and creates files

list_fig = re.findall(r'\\begin\{figure\}([\s\S]*?)(\\begin\{tikzpicture\}[\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(.*?)\}\n\\end\{figure\}', content)

for x in list_fig:
	h = open(chap + "/Fig/" + x[3] + ".tex", 'w')
	h.write("\\documentclass[preview,border=0mm,convert={density=600,outext=.png}]{standalone}\n\
		\\usepackage{tikz}\n\\usetikzlibrary{automata,shapes,patterns,calc,arrows}\n\
		\\input{tikz-style.tex}\n\\begin{document}\n" + x[1] + "\n\\end{document}")

content = re.sub(r'\\begin\{figure\}([\s\S]*?)\\caption\{([\s\S]*?)\}\n\\label\{(\d*?)-fig:(.*?)\}\n\\end\{figure\}', \
	r'\n```{figure} Fig/\3-fig:\4.png\n:name: \3-\4\n:align: center\n\2\n```', content)

#### Deal with subsections

# replace
# \subsection*{Players}
# by
# ## Players 

content = re.sub(r'\\subsection\*\{(.*?)\}', r'## \1', content)

#### Replace \[ \] by $$ $$
content = re.sub(r'\\\[', r'\n$$', content)
content = re.sub(r'\\\]', r'$$\n', content)

#### Remove vskip1em
content = re.sub(r'\\vskip1em', r'\n', content)

#### Rewrite textit
content = re.sub(r'\\textit\{(.*?)\}', r'\1', content)

#### Remove knowledge
content = re.sub(r'""(.*?)""', r'\1', content)

#### Reshape quotes
content = re.sub(r'\`\`(.*?)\'\'', r'''\1''', content)

#### Deal with itemize
content = re.sub(r'\\begin\{itemize\}', r'', content)
content = re.sub(r'\\end\{itemize\}', r'', content)
content = re.sub(r'\\item(.*?)', r'* \1', content)

#### Deal with theorem

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

content = re.sub(r'\\begin\{theorem\}[(.*?)]\n\\label\{(\d*?)-thm:(.*?)\}', \
	r'```{admonition} Theorem \1\n:class: result\n:name: \2-thm:\3\n', content)

# case no []
content = re.sub(r'\\begin\{theorem\}\n\\label\{(\d*?)-thm:(.*?)\}', \
	r'```{admonition} Theorem\n:class: result\n:name: \2-thm:\3\n', content)

# case no label
content = re.sub(r'\\begin\{theorem\}[(.*?)]', \
	r'```{admonition} Theorem \1\n:class: result\n', content)

# case no [] no label
content = re.sub(r'\\begin\{theorem\}\n', \
	r'```{admonition} Theorem\n:class: result\n', content)

content = re.sub(r'\\end\{theorem\}', r'```', content)

#### Deal with references
content = re.sub(r'~\\cref\{(\d*?)-sec:(.*?)\}', r' Section {ref}`\1-sec:\2`', content)
content = re.sub(r'~\\cref\{(\d*?)-thm:(.*?)\}', r' Theorem {ref}`\1-thm:\2`', content)
content = re.sub(r'~\\cref\{(\d*?)-lem:(.*?)\}', r' Lemma {ref}`\1-lem:\2`', content)
content = re.sub(r'~\\cref\{(\d*?)-fig:(.*?)\}', r' Figure {ref}`\1-fig:\2`', content)
content = re.sub(r'~\\cref\{(\d*?)-chap:(.*?)\}', r' Chapter {ref}`\1-chap:\2`', content)
content = re.sub(r'~\\cref\{part:(.*?)\}', r' Part {ref}`part:\1`', content)

content = re.sub(r'\\Cref\{(\d*?)-sec:(.*?)\}', r'Section {ref}`\1-sec:\2`', content)
content = re.sub(r'\\Cref\{(\d*?)-thm:(.*?)\}', r'Theorem {ref}`\1-thm:\2`', content)
content = re.sub(r'\\Cref\{(\d*?)-lem:(.*?)\}', r'Lemma {ref}`\1-lem:\2`', content)
content = re.sub(r'\\Cref\{(\d*?)-fig:(.*?)\}', r'Figure {ref}`\1-fig:\2`', content)
content = re.sub(r'\\cref\{(\d*?)-chap:(.*?)\}', r'Chapter {ref}`\1-chap:\2`', content)
content = re.sub(r'\\Cref\{part:(.*?)\}', r'Part {ref}`part:\1`', content)

content = re.sub(r'\\cref\{(\d*?)-sec:(.*?)\}', r'Section {ref}`\1-sec:\2`', content)
content = re.sub(r'\\cref\{(\d*?)-thm:(.*?)\}', r'Theorem {ref}`\1-thm:\2`', content)
content = re.sub(r'\\cref\{(\d*?)-lem:(.*?)\}', r'Lemma {ref}`\1-lem:\2`', content)
content = re.sub(r'\\cref\{(\d*?)-fig:(.*?)\}', r'Figure {ref}`\1-fig:\2`', content)
content = re.sub(r'\\cref\{(\d*?)-chap:(.*?)\}', r'Chapter {ref}`\1-chap:\2`', content)
content = re.sub(r'\\cref\{part:(.*?)\}', r'Part {ref}`part:\1`', content)


#### Deal with citations
content = re.sub(r'~\\cite\{(.*?)\}', r' {cite}`\1`', content)

#### Remove indents
content = re.sub(r'\t', r'', content)

print(content)
f.close()

g = open(chap + "/" + file + ".md", "w")
g.write(content)


