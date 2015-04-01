#!/usr/bin/python

import os
import glob
import shutil
import sys, getopt

drawableDirs = ['drawable-mdpi', 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi', 'drawable-xxxhdpi']


def main(argv):
	cpCount = 0;
	targetDir = 'result'

	if len(argv) > 2 or len(argv) < 1:
		print """
		usage
		pattern targetDir
		ex)
		'*white_18dp' ['targetDir']
		"""
	else:
		cpCount = 0;

		if(len(argv) == 2):
			targetDir = argv[1];
		
		for file in glob.glob('*/*/'+argv[0]+'.png'):
			tokens = file.split('/')
			target = targetDir + '/' + '/'.join(tokens[-2:-1])+'/'
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
