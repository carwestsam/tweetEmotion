#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 carwest <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import codecs

processSize = 50000
processSlide = processSize / 100

ifileName=''
ofileName=''
lfileName=''

ifile=''
ofile=''
lfile=''

def setSize( ps=50000 ):
    global processSize, processSlide
    processSize = ps
    processSlide = ps / 100

def setFile( ifname='', ofname='', lfname='' ):
    global ifileName, ofileName, lfileName
    print 'set File'
    ifileName=ifname
    ofileName=ofname
    lfileName=lfname

def openFiles():
    global ifile, ofile, lfile
    if ifileName != '':
        ifile = codecs.open( ifileName, 'r', 'utf-8' )
        print 'ifile open :\t' + ifileName
    else:
        print 'ifileName no set!!'
    if ofileName != '':
        ofile = codecs.open( ofileName, 'w', 'utf-8' )
        print 'ofile open :\t' + ofileName
    else:
        print 'ofileName no set!!'
    if lfileName != '':
        lfile = codecs.open( lfileName, 'w', 'utf-8' )
        print 'lfile open :\t' + lfileName
    else :
        print 'lfileName no set!!'

def closeFiles():
    if ifileName != '':
        ifile.close()
    if ofileName != '':
        ofile.close()
    if lfileName != '':
        lfile.close()

def readlineI(  ):
    if ifileName != '':
        return ifile.readline()

def writeO( str ):
    if ofileName != '':
        ofile.write( str )

def writeL( str ):
    if lfileName != '':
        lfile.write( str )

def loop(func, info=''):
    print info
    for x in range(processSize):
        func()
        if x % processSlide == 0:
            print str(x/processSlide) + '% processed'

