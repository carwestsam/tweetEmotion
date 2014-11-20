#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
get Unigram words from featvect from WangShuai
"""

import re
import json
import os
import codecs
import pickle

UnigramWords = []
UnigramWordsIdentify = False

def getUnigramWords():
    global UnigramWords,UnigramWordsIdentify
    if UnigramWordsIdentify:
        return UnigramWords
    ifile = codecs.open( '/home/server2103/tweetEmotion/data/featvect', 'r', 'utf-8' )
    line = ifile.readline()
    obj = eval( line )
    dict = obj[0]
    UnigramWords = dict.keys()
    UnigramWordsIdentify = True
    ifile.close()
    ofile = codecs.open( '../emojiOutput/UnigramWords', 'w', 'utf-8' )
    ofile.write( json.dumps( UnigramWords ) + u'\n' )
    ofile.close()

getUnigramWords()

if __name__ == "__main__":
    getUnigramWords()
    pass
