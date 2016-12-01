#!/usr/bin/env python3

import random

size = int(input('Article Size in MB: '))
total = int(input('The Number of Article: '))

print ('Article Size:', size, 'MB')
print ('Total Number:', total, 'Article(s)')

sizeInByte = size * 1024 * 1024

alpha = 'abcdefghijklmnopqrstuvwxyz          '
alphaLen = len(alpha)-1

p = ' '
c = ' '

for i in range(total):
	p = ' '
	c = ' '
	
	name = str.format('article{}', i)
	f = open(name, 'w')
	print ('Generating file', name)
	
	for j in range(sizeInByte):
		c = alpha[random.randint(0, alphaLen)]
		while p == ' ' and p == c:
			c = alpha[random.randint(0, alphaLen)]
		f.write(c)
		p = c
	
	f.close()
	print ('Generating file', name, '- done')