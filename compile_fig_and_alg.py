import glob
import subprocess
import os

# latexmk XXXX.tex -shell-escape

list_fig = glob.glob('*-fig:*.tex')
# print(list_fig)
list_alg = glob.glob('*-algo:*.tex')
# print(list_alg)

command = "latexmk {} -shell-escape"

for fig in list_fig:
	if not os.path.isfile(fig[:-3] + "png"):
		print("Compile %s" % fig)
		subprocess.call(command.format(fig), shell=True)

for alg in list_alg:
	if not os.path.isfile(alg[:-3] + "png"):
		print("Compile %s" % alg)
		subprocess.call(command.format(alg), shell=True)

subprocess.call("rm *.fls", shell=True)
subprocess.call("rm *.aux", shell=True)
subprocess.call("rm *.fdb_latexmk", shell=True)
subprocess.call("rm *.log", shell=True)
subprocess.call("rm *.ps", shell=True)
subprocess.call("rm *.dvi", shell=True)
