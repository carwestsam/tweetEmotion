#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
form divideByEmoji.py{'../emojiOutput/labeled_by_emoji_[EMO].txt' }
generating features by Unigram Words, given by entity/getUnigramWords.py

Dict write to  '../emojiOutput/UnigramDict'

"""

import re
import json
import os
import codecs
import utilities
import dealTweets as dts
import divideByEmoji
import preprocess_func

UnigramDict = {}
UnigramDict_Cnt = 0
tokenizer = utilities.Tokenizer()

PC = 0

DictDir = '../emojiOutput/UnigramDict'

def get_Index( word, edit=0 ):
    global UnigramDict, UnigramDict_Cnt
    if edit == 1:
        UnigramDict_Cnt += 1
        UnigramDict.update( { word: UnigramDict_Cnt  } )
        return UnigramDict_Cnt

    return UnigramDict.get( word, 0 )

def init_Index():
    ifile = codecs.open( '../emojiOutput/UnigramWords', 'r', 'utf-8' )
    line = ifile.readline()
    ifile.close()

    list = json.loads( line )
    for word in list:
        index = get_Index( word, 1 )
        print '%s:%d' % ( word, index )

    ofile = codecs.open( DictDir, 'w', 'utf-8' )
    ofile.write( json.dumps( UnigramDict ) + u'\n' )
    ofile.close()

def init_Index_UnigramHashtag():
    global DictDir
    DictDir = '../emojiOutput/UnigramHashtagDict'

    ufile = codecs.open( '../emojiOutput/UnigramWords', 'r', 'utf-8' )
    hfile = codecs.open( '../emojiOutput/hashtagList_emoji', 'r', 'utf-8' )
    uni = ufile.readline()
    has = hfile.readline()
    ufile.close()
    hfile.close()

    ulist = json.loads( uni )
    hlist = json.loads( has )

    for u in ulist:
        index = get_Index( u, 1 )
        print '%s:%d' % ( u, index )

    for h in hlist:
        index = get_Index( h, 1 )
        print '%s:%d' % ( h, index )

    ofile = codecs.open( DictDir, 'w', 'utf-8' )
    ofile.write( json.dumps( UnigramDict ) + u'\n' )
    ofile.close()

def init_Index_UnigramEmoticon():
    global DictDir
    DictDir = '../emojiOutput/UnigramEmoticonDict'

    ufile = codecs.open( '../emojiOutput/UnigramWords', 'r', 'utf-8' )
    efile = codecs.open( '../emojiOutput/emoticonList.txt', 'r', 'utf-8' )
    uni = ufile.readline()
    emo = efile.readline()
    ufile.close()
    efile.close()

    ulist = json.loads( uni )
    elist = json.loads( emo )

    for u in ulist:
        index = get_Index( u, 1 )
        print '%s:%d' % ( u, index )

    for e in elist:
        index = get_Index( e, 1 )
        print '%s:%d' % ( e, index )

    ofile = codecs.open( DictDir, 'w', 'utf-8' )
    ofile.write( json.dumps( UnigramDict ) + u'\n' )
    ofile.close()

def load_Index():
    ifile = codecs.open( DictDir, 'r', 'utf-8' )
    line = ifile.readline()
    ifile.close()

    global UnigramDict
    UnigramDict = json.loads( line )

    for k,v in UnigramDict.iteritems():
        print '-%s:%d' % ( k, v )

def gen_Feature ( text ):
    uni_dict = {}
    wordlist = tokenizer.tokenize( text.lower())
    if len( wordlist ) < 3:
        return
    output = ''
    for word in wordlist:
        index = get_Index ( word )
        #if index > 0:
        uni_dict.update( {index : uni_dict.get( word, 0 ) + 1 } )
    
    for key, value in [(k,uni_dict[k]) for k in sorted(uni_dict.keys())]:
        output+= str( key ) + ':' + str( value ) + ' '

    return output

def parse_line() :
    line = dts.readlineI()
    if not line:
        return
    try:
        obj = json.loads( line )
    except:
        return

    label = obj[u'label']
    text = obj[u'text']

    global PC
    if int( label ) == 1:
        PC += 1
    output = '%d %s\n' % ( label, gen_Feature( text ) )
    dts.writeO( output )
    dts.writeL( str( label ) + '\n')

if __name__ == "__main__":

    __type = 'UnigramEmoticon_run'
    
    if __type == 'unigramhash_init':
        init_Index_UnigramHashtag()
    if __type == 'unigramemoticon_init':
        init_Index_UnigramEmoticon()
    if __type == 'unigram_init':
        init_Index()

    if 'run' in __type:
        global DictDir
        loop_ofilename = ''
        loop_lfilename = ''
        all_ofilename = ''
        all_lfilename = ''

        if __type == 'Unigram_run':
            DictDir = '../emojiOutput/UnigramDict'
            loop_ofilename = '../emojiOutput/feautre_emoji_'
            loop_lfilename = '../Compare_Output/ans_emoji_'
            all_ofilename = '../emojiOutput/feautre_emoji_all'
            all_lfilename = '../Compare_Output/ans_emoji_all'
        elif __type == 'UnigramHash_run':
            DictDir = '../emojiOutput/UnigramHashtagDict'
            loop_ofilename = '../emojiOutput/feautre_unihash_'
            loop_lfilename = '../Compare_Output/ans_unihash_'
            all_ofilename = '../emojiOutput/feautre_unihash_all'
            all_lfilename = '../Compare_Output/ans_unihash_all'
        elif __type == 'UnigramEmoticon_run':
            DictDir = '../emojiOutput/UnigramEmoticonDict'
            loop_ofilename = '../emojiOutput/feautre_uniemo_'
            loop_lfilename = '../Compare_Output/ans_uniemo_'
            all_ofilename = '../emojiOutput/feautre_uniemo_all'
            all_lfilename = '../Compare_Output/ans_uniemo_all'
        load_Index()


        for Emo in divideByEmoji.Emotions:
            ifilename = divideByEmoji.OutputDir + Emo['name']
            ofilename = loop_ofilename + Emo['name']
            lfilename = loop_lfilename + Emo['name'] 
            dts.setSize( 100000 )
            dts.setFile( ifilename, ofilename, lfilename )
            dts.openFiles()
            PC = 0
            dts.loop( parse_line, 'generating ' + Emo['name'] )
            dts.closeFiles()


        ifilename = '../emojiOutput/featre_all'
        dts.setSize( 100000 )
        dts.setFile( ifilename, all_ofilename, all_lfilename )
        dts.openFiles()
        dts.loop( parse_line, 'generating all' )
        dts.closeFiles()

    pass


