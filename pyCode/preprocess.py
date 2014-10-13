#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Preprocess for tweet file

take out RT, url addresses, punctuations, ans paramiters
"""

import re
import sys
import codecs
import HTMLParser
import preprocess_func
import dealTweets as dts
import utilities
#from nltk.stem.wordnet import WordNetLemmatizer


dts.setSize( 25770000 )
dts.setFile( '../data/tweet_noRT_noDup.txt', '../output/afterPre.txt', '../log/pre.log' )
dts.openFiles()

tokenizer = utilities.Tokenizer()

def __preprocess():
    line = preprocess_func.preprocess( dts.readlineI() )
    dts.writeO( line )
#    terms = [term for term in tokenizer.tokenize(line)]
#    print terms


dts.loop( __preprocess, 'preprocess symbols' )



dts.closeFiles()

