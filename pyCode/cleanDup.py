#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 server2103 <server2103@2103>
#
# Distributed under terms of the MIT license.

"""
clean duplicate Tweet from noRT file
"""

import re
import codecs
import hashlib

ifileName = '../data/tweet_noRT.txt'
ofileName = '../data/tweet_noRT_noDup.txt'
lfileName = '../log/tweet_noRT_noDup.log' 
ifile = codecs.open(ifileName, 'r', 'utf-8')
ofile = codecs.open(ofileName, 'w', 'utf-8')
lfile = codecs.open(lfileName, 'w', 'utf-8')

processSize = 31105948
#processSize = 5000000
processSlide = processSize / 100 

md5set = set()


print 'Start to Calc md5 ...'

for i in range(processSize):
    line = ifile.readline()
    md5 = hashlib.md5(line.encode('utf-8')).hexdigest()
    md5set.add(md5)
    #print md5
    if i % processSlide == 0:
        print str(i/processSlide) + '% added'

print 'Calc md5 finished'

ifile.close()
ifile = codecs.open(ifileName, 'r', 'utf-8')

cnt = 0

print 'remove duplicate start..'

for i in range(processSize):
    line = ifile.readline()
    md5 = hashlib.md5(line.encode('utf-8')).hexdigest()
    if md5 in md5set:
        md5set.remove(md5)
        ofile.write(line)
        cnt += 1
    if i%processSlide == 0:
        print str(i/processSlide) + '% done'

print 'Calc md5 finished'
print str( cnt ) + '\t tweets remain'
lfile.write( str(cnt)+'\t tweets remain\n' )


ifile.close()
ofile.close()
lfile.close()

