#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Label Counter
"""

import dealTweets as dts
import re
import json
import os

counter = [0,0,0,0,0,0,0,0,0,0]

def __line():
    line = dts.readlineI()
    if not line:
        return
    obj = eval(line)
    counter[ obj[1] ] += 1

def labelCounter():
    dts.setSize( 100000 )
    dts.setFile( '../data/featvect', '', '../log/featvectLabelCount' )
    dts.openFiles()
    global counter
    for x in range( 9 ):
        counter[x] = 0
    dts.loop( __line, 'parse featvect' )
    
    sum = 0
    for x in range( 9 ):
        sum += counter[x]

    for x in range( 9 ):
        print 'Label\t%d\t:%d (%.2f%%)'  % (x, counter[x], float( counter[x] * 100.0) / float(sum))
        dts.writeL( 'Label\t%d\t:%d (%.2f%%)\n'  % (x, counter[x], float( counter[x] * 100.0) / float(sum)) )

    print 'Sum\t\t:%d'    % sum

    dts.closeFiles()

if __name__ == "__main__":
    labelCounter()
    pass
