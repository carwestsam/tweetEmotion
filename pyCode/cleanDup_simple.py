#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
clean duplicate tweet , with simple set method
"""


import dealTweets as dts

dts.setSize( 5000000 )
dts.setFile( '../data/tweet_noRT.txt', '../tmp/noDup.txt', '../log/checkNoDup.log')


def __cleanDup():
    dts.openFiles()
    tw = set()
    def __push():
        text = dts.readlineI()
        tw.add( text )
    dts.loop( __push, 'push into set' )
    print 'start write to file %s' % dts.ofileName
    cnt = 0
    for text in tw:
        dts.writeO( text )
        cnt += 1
    print 'write finished, tot tweet left: %d' % cnt


    dts.closeFiles()

if __name__ == '__main__':
    __cleanDup()
