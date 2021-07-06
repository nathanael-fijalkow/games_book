import subprocess
import re 

from chapter_transformer import chapter_transformer
from macros_transformer import macros_transformer

f = open("book.tex", "r")
authors = f.read()
f.close()

# Find chapters

# \chapauthor{Nathana{\"e}l Fijalkow}
# \chapter{Introduction}
# \label{1-chap:introduction}

macros_transformer("","macros.tex")

s_in = r"\\chapauthor\{(.*?)\}\n\\chapter\{(.*?)\}\n\\label\{(\d*?)-chap:(.*?)\}\n\\chapterinput\{(.*?)\}\n"
list_chap = re.findall(s_in, authors)
# print(list_chap)

for (authors,title,nb_chap,label,path) in list_chap:
	authors = re.sub(r'\{\\"e}', r'&euml;', authors) 
	authors = re.sub(r'\{\\"i}', r'&iuml;', authors)
	authors = re.sub(r'\{\\\'e}', r'&eacute;', authors)
	authors = re.sub(r'\{\\\`e}', r'&egrave;', authors)
	authors = re.sub(r'\{\\\'n}', r'&#324;', authors)
	authors = re.sub(r'\{\\\'y}', r'&yacute;', authors)
	if int(nb_chap) == 1:
	# if int(nb_chap) <= 13:
		print("\nTransforming chapter {}".format(title))
		chapter_transformer(nb_chap, path + "/", title, label, authors)

