#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""


import dealTweets as dts
import json

def __io() :
    line = dts.readlineI()
    if not line:
        return
    obj = json.loads( line )
    text = obj['text']
    dts.writeO( text + '\n' )

dts.setSize( 300 )
dts.setFile( '../emojiOutput/afterPre.txt', '../emojiOutput/checkAfterPre.txt')
dts.openFiles()
dts.loop( __io, 'io' )
dts.closeFiles()
