import glob
import subprocess
import os

# latexmk XXXX.tex -shell-escape

list_fig = glob.glob('*.tex')
stripped_list = [x for x in list_fig if x != "tikz-style.tex"]

print(stripped_list)

command = "latexmk {} -c -shell-escape"

for fig in stripped_list:
	subprocess.call(command.format(fig), shell=True)

