#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
find emoji in tweets
"""
import io
import os
import re
import codecs
import dealTweets as dts

dts.setSize( 5000000 )
dts.setFile("../data/tweet_noRT_noDup.txt","../tmp/b.out", "../tmp/c.out")
dts.openFiles()

def findemoji(str):
    line = dts.readlineI()
    if str in line:
        print (line)
        dts.writeO(line)

dts.loop_with_param( findemoji, b'\xf0\x9f\x98\x80'.decode('utf-8'), 'try to find Emoji :😀' )
#dts.writeL( u'\xe2\x98\xba\xef\xb8\x8f with hay!' )
#smile = '\xe2\x98\xba\xef\xb8\x8f'.decode('utf-8')

#dts.loop_with_param( findemoji, smile, u'try to find Emoji :' + smile)
#print '\xe2\x98\xba\xef\xb8\x8f'.decode('utf-8').encode('utf-8')

dts.closeFiles()
