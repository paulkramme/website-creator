#!/usr/bin/env python3

import os
import sys


def configurator():
	author = input("Author? ")
	title = input("Title? ")
	description = input("Description? ")
	url = input("URL? ")
	


def writetofile(name, templatepath, contentpath):
	with open(templatepath, "r") as template:
		htmltemplate = template.readlines()
		with open(contentpath, "r") as content:
			htmlcontent = content.readlines()
			with open(name, "a") as final:
				final.writelines(htmltemplate)
				final.writelines(htmlcontent)


def main():
	name = sys.argv[1]
	template = sys.argv[2]
	content = sys.argv[3]
	writetofile(name, template, content)


def winmain():
	name = input("Please enter name of the final file: ")
	template = input("Enter templatepath: ")
	content = input("Enter contentpath")
	writetofile(name, template, content)


if __name__ == "__main__":
	if os.name == "posix":
		main()
	elif os.name == "nt":
		winmain()
	else:
		print("OS not recognized. Assume posix compliant OS.")
		main()