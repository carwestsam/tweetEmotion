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

dts.setSize( 50000 )
dts.setFile("../data/tweet_noRT_noDup.txt","../tmp/b.out", "../tmp/c.out")
dts.openFiles()

def findemoji(str):
    line = dts.readlineI()
    if str in line:
        print line
        dts.writeO(line)

#dts.loop_with_param( findemoji, u'☺️', u'try to find Emoji :☺️' )
#dts.writeL( '0001F612'.decode('hex').encode('utf-8') )
dts.writeL( u'\xe2\x98\xba\xef\xb8\x8f with hay!' )
smile = '\xe2\x98\xba\xef\xb8\x8f'.decode('utf-8')

dts.loop_with_param( findemoji, smile, u'try to find Emoji :' + smile)
print '\xe2\x98\xba\xef\xb8\x8f'.decode('utf-8').encode('utf-8')

dts.closeFiles()
