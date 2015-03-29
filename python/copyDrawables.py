#!/usr/bin/python

import os
import glob
import shutil
import sys, getopt

drawableDirs = ['drawable-mdpi', 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi', 'drawable-xxxhdpi']


def main(argv):
	cpCount = 0;
	if len(argv) != 2:
		print """
		usage
		pattern targetDir
		ex)
		*white_18dp.png selectedDir
		"""
	else:
		cpCount = 0;
		for file in glob.glob('*/*/'+argv[0]+'.png'):
			tokens = file.split('/')
			target = argv[1] + '/' + '/'.join(tokens[-2:-1])+'/'
			try:
				if not os.path.exists(target):
					os.makedirs(target)
				shutil.copy(file, target)
				cpCount+=1
			except IOError:
				print >> sys.stderr, 'error!'
		print cpCount, 'files copied'

if __name__ == "__main__":
   main(sys.argv[1:])
