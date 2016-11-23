#!/usr/bin/env python3

import os
import sys


def configurator():
	csspart = """<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width">
	<meta name="author" content="Paul Kramme">
	<meta name="description" content="My new cool website">
	<meta property="og:url" content="http://txti.es/dmnc0">
	<meta property="og:title" content="TheGreatTitle">
	<meta property="og:site_name" content="txti">
	<meta property="og:description" content="My new cool website">
	<meta name="twitter:card" content="summary">
	<meta name="twitter:title" content="TheGreatTitle">
	<meta name="twitter:description" content="My new cool website">
	<meta name="twitter:creator" content="Paul Kramme">
	<title>TheGreatTitle</title>
	<style type="text/css">body {font-size: 1.1em; line-height: 1.5em; max-width: 45em; margin: auto; padding: 0 2%;} img {max-width: 100%; display: block; margin: .75em auto;}</style>
"""


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