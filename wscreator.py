#!/usr/bin/env python3

import os
import sys

def main():
	name = sys.argv[1]
	templatepath = sys.argv[2]
	contentpath = sys.argv[3]
	with open(templatepath, "r") as template:
		htmltemplate = template.readlines()
		with open(contentpath, "r") as content:
			htmlcontent = content.readlines()
			with open(name, "a") as final:
				final.write(htmltemplate)
				final.write(htmlcontent)



if __name__ == "__main__":
	if os.name == "posix":
		main()
	elif os.name == "nt":
		winmain()
	else:
		print("OS not recognized. Assume posix compliant OS.")
		main()