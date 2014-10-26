#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 carwest <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
import codecs
import io
import time
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, AdaptiveETA, AdaptiveTransferSpeed

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
        #ifile = io.open( ifileName, 'r', encoding='utf-8-mb4' )
        print 'ifile open :\t' + ifileName
    else:
        print 'ifileName no set!!'
    if ofileName != '':
        ofile = codecs.open( ofileName, 'w', 'utf-8' )
        #ofile = io.open( ofileName, 'w', encoding='utf8mb4' )
        print 'ofile open :\t' + ofileName
    else:
        print 'ofileName no set!!'
    if lfileName != '':
        lfile = codecs.open( lfileName, 'w', 'utf-8' )
        #lfile = io.open( lfileName, 'w', encoding='utf-8' )
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
    #print info
    #widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    widgets = [Percentage(), Bar('>') , info, ReverseBar('<'), ETA()]
    widgets = [Percentage(), Bar('>') , info, ReverseBar('<'), Timer()]
    pbar = ProgressBar(widgets=widgets, maxval=processSize)
    for x in pbar(i for i in range(processSize)):
        func()
        #if x % processSlide == 0:
        #    print str(x/processSlide) + '% processed'

def loop_with_param(func, params={}, info=''):
    #print info
    #widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    widgets = [Percentage(), Bar('>') , info, ReverseBar('<'), Timer()]
    pbar = ProgressBar(widgets=widgets, maxval=processSize)
    for x in pbar ( i for i in range (processSize) ):
        #for x in range(processSize):
        func(params)
        #if x % processSlide == 0:
        #    print str(x/processSlide) + '% processed'

def loop_with_param_clean(func, clean, params={}, info=''):
    widgets = [Percentage(), Bar('>') , info, ReverseBar('<'), Timer()]
    pbar = ProgressBar(widgets=widgets, maxval=processSize)
    for x in pbar ( i for i in range (processSize) ):
        func(params)
        if x % processSlide == 0:
            clean( params )

