import csv
import os
from os import path
import re

fieldnames = ['tasks', 'start', 'end', 'span']

row_pattern = r'(\w+):\s(\d\d/\d\d/\d\d\s\d\d:\d\d)\s~\s(\d\d/\d\d/\d\d\s\d\d:\d\d)\s\s(\d\d:\d\d:\d\d)'

def initlogs(fname):
	if not os.path.exists(fname):
		with open(fname, mode = 'w', newline = '') as f:
			writer = csv.DictWriter(f, fieldnames = fieldnames)
			writer.writeheader()

def savelogs(fname, text):
	with open(fname, mode = 'a', newline='') as f:
		writer = csv.DictWriter(f, fieldnames = fieldnames)
		pattern = re.compile(row_pattern)
		matches = pattern.finditer(text)
		for match in matches:
			task = match.group(1)
			start = match.group(2)
			end = match.group(3)
			span = match.group(4)
			writer.writerow({'Tasks': task, 'Start': start, 'End':end, 'Span':span})

if __name__ == '__main__':
	fname = 'logs.csv'
	initlogs(fname)
	text = 'work: 01/21/21 21:03 ~ 01/21/21 21:03  00:00\nstudy: 01/21/21 21:03 ~ 01/21/21 21:03  00:00\nreading: 01/21/21 21:03 ~ 01/21/21 21:03  00:00\ncustom1: 01/21/21 21:03 ~ 01/21/21 21:03  00:00\n\n'
	savelogs(fname, text)