#!/usr/bin/env python3

import os
import sys


def configurator(source, filename = "final.html"):
	author = input("Author? ")
	title = input("Title? ")
	description = input("Description? ")
	url = input("URL? ")
	with open(filename, "w") as f:
		f.write("<!doctype html>\n")
		f.write("<html>\n")
		f.write('\t<meta charset="utf-8">\n')
		f.write('\t<meta name="viewport" content="width=device-width">\n')
		f.write('\t<meta name="author" content="' + author + '">\n')
		f.write('\t<meta name="description" content="' + description + '">\n')
		f.write('\t<meta property="og:url" content="' + url + '">\n')
		f.write('\t<meta property="og:title" content="' + title + '">\n')
		f.write('\t<meta property="og:site_name" content="' + title + '">\n')
		f.write('\t<meta property="og:description" content="' + description + '">\n')
		f.write('\t<meta name="twitter:card" content="summary">\n')
		f.write('\t<meta name="twitter:title" content="' + title + '">\n')
		f.write('\t<meta name="twitter:description" content="' + description + '">\n')
		f.write('\t<meta name="twitter:creator" content="' + author + '">\n')
		f.write('\t<title>' + title + '</title>\n')
		f.write('\t<style type="text/css">body{margin:40px auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:010px}h1,h2,h3{line-height:1.2}</style>\n')
		f.write('</head>')
	with open(filename, "a") as final:
		with open(source, "r") as temp:
			lines = temp.readlines()
			final.writelines(lines)


def writetofile(name, templatepath, contentpath):
	with open(templatepath, "r") as template:
		htmltemplate = template.readlines()
		with open(contentpath, "r") as content:
			htmlcontent = content.readlines()
			with open(name, "a") as final:
				final.writelines(htmltemplate)
				final.writelines(htmlcontent)


def main():
	configurator(sys.argv[1], sys.argv[2])


def winmain():
	name = input("Please enter name of the final file: ")
	content = input("Enter contentpath")
	#writetofile(name, template, content)
	configurator(content, name)


if __name__ == "__main__":
	if os.name == "posix":
		main()
	elif os.name == "nt":
		winmain()
	else:
		print("OS not recognized. Assume posix compliant OS.")
		main()