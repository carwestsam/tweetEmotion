#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Parse featureVector
"""

import dealTweets as dts


name_dict = {}
index_dict = 1


def __getIndex( index_name ):
    global name_dict, index_dict
    if -1 == name_dict.get( index_name, -1 ):
        name_dict.update( {index_name : index_dict })
        index_dict += 1
    return name_dict.get( index_name, -1 ) 

def __lineParse():
    line = dts.readlineI()
    if not line:
        return
    obj = eval(line)
    output = str ( obj[1] ) + ' '
    wordlist = {}
    for word,value in obj[0].iteritems():
        if value > 0 :
            wordlist.update( {__getIndex(word) : value} )
            #output += str(__getIndex(word))  + ':'+ str(value) +' '
    
    for key, value in [(k,wordlist[k]) for k in sorted(wordlist.keys())]:
        output+= str( key ) + ':' + str( value ) + ' '

    if obj[1] > 1:
        dts.writeO( output + '\n' )
    #dts.writeO( output + '\n' )
    
    

def featureVectorParse():
    dts.setSize( 10000 )
    dts.setFile( '../data/featvect', '../emojiOutput/featureWang10000_no01', '../log/featureWang' )
    dts.openFiles()
    dts.loop( __lineParse, 'parse featvect' )
    
    dts.writeL( str(name_dict ))

    dts.closeFiles()

if __name__ == "__main__":
    featureVectorParse()
    pass

