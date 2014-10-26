#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Some common use of functions
"""


def __calcDistribution_list( list ):
    sum = 0
    for x in list:
        sum += x
    sum += 0.0
    nlist = []
    for x in list:
        if sum == 0 :
            nlist.append( 0 )
        else :
            nlist.append( x / sum )
    return nlist



def __calcDistribution_dict( dict ):
    sum = 0.0
    for x in dict.itervalues():
        sum += x
    newdict = {}
    for key,value in dict.iteritems() :
        if sum == 0:
            newdict.update ( {key: 0} )
        else :
            newdict.update( { key : value / sum } )
    return newdict 
