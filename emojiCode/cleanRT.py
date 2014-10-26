#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 server2103 <server2103@2103>
#
# Distributed under terms of the MIT license.

"""
clean RT from tweet_small file
save file to /data/tweet_noRT
"""

import re
import codecs
import dealTweets as dts

ifileName = '../data/twitter.tweets.json'
ofileName = '../data/tweet_noRT.txt'
lfileName = '../log/tweet_noRT.log' 
ifile = codecs.open(ifileName, 'r', 'utf-8')
ofile = codecs.open(ofileName, 'w', 'utf-8')
lfile = codecs.open(lfileName, 'w', 'utf-8')

processSize = 50000000


#ilines = ifile.readlines()
#length = len(ilines)
length = processSize
length_1 = length / 100
i=0
cnt =0

#for line in ilines:
for i in range(length):
    line = ifile.readline()
    if 'RT ' not in line:
#        print ( line )
        ofile.write( line )
        cnt +=1
    i += 1
    if i % length_1 == 0:
        print ('process {0}% of data'.format( i/length_1 )) 

ifile.close()
ofile.close()

print "================="
print 'Before:\t' , length
print 'After:\t', cnt 

lfile.write( 'Before:\t' + str(length ) + '\n')
lfile.write( 'After:\t' + str( cnt ) + '\n' )


lfile.close()
