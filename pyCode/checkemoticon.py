#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
python checkemoticon.py 500000 10000 ../output1/
"""


import sys
import re
import codecs
import dealTweets as dts


angerIcons=[ ':-7', ':-8(', ':-!', ':-[', ':-{~', ':-|', '?-(', ':-(*)', '(:-&', '(:-*', '>-r', '>:-<', '>>-(', '~~:-(', '@%&$%&', ':-/', ':-*']
depreIcons=[ ':-6', '(:<)', '(0--<', '*-(', '+-(', ':{', ':-"', '(-_-)', ':-\\', '-(', '(:^(', '..._...', ':-<', '(:-(', '(:-', '~~~~>_<~~~~', ':-{', '|-(', '}(:-(', '=:-(', ':-e', ':-\'|','[:|]', ':-(', u'☹']
fatigIcons=[ '#-)', '|-)', ':-$', ':-1']
vigorIcons=[ ':-D', '8-)', ';-)', '(:-)', '|-D', '|-P', '^O^', '^-^', '^_<', '..~^.^~...', '...~*.*~...', '^_^', '=^-^=', '(:-D)', ':-9', ':->', ':~)', ':-]', '8:]', ':*)', ':%)%', ':-)8', ':-)-{8', ':-})', ':-<)', ':-=)', ':-{ )', '[:-)', '}:-)', '{(:-)', '0-)', 'B-)', '=:-)', '<<<<(:-)', 'i-)', ':>)', ':=)', ':-}', 'o-)', '@-)', '*:o)', '*<|:-)', ':-)', '+:-)', '0-)', '@:-)', '<:-)<<|', ':-)', ':-\')', '8:-)', '!-)', '#:-)', '%-)', '%-}', '\':-)', '&:-){:-)', '(:)-)', ':-P', ':-Q', ',-)', ',-}', '@>>--->---', ';-\\', ':-j', ':-*', '(:-*]']
frindIcons=[ 'x-<', ':-)', '(-:', ':)', '(:',u'☺️']
tensnIcons=[ ':-0', ':-o', ':-()',':-O', ':O','o_O', 'O_o','O_O','o_o']
confuIcons=[ '?_?', '@_@', '<@_@>']

angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0, 'fileptr':0, 'label':'1'}
depreEmo = {'filename': 'depreEmo.txt', 'Icons': depreIcons, 'cnt':0, 'fileptr':0, 'label':'2'}
fatigEmo = {'filename': 'fatigEmo.txt', 'Icons': fatigIcons, 'cnt':0, 'fileptr':0, 'label':'3'}
vigorEmo = {'filename': 'vigorEmo.txt', 'Icons': vigorIcons, 'cnt':0, 'fileptr':0, 'label':'4'}
frindEmo = {'filename': 'frindEmo.txt', 'Icons': frindIcons, 'cnt':0, 'fileptr':0, 'label':'5'}
tensnEmo = {'filename': 'tensnEmo.txt', 'Icons': tensnIcons, 'cnt':0, 'fileptr':0, 'label':'6'}
confuEmo = {'filename': 'confuEmo.txt', 'Icons': confuIcons, 'cnt':0, 'fileptr':0, 'label':'7'}

Emotions = [angerEmo, depreEmo, fatigEmo, vigorEmo, frindEmo, tensnEmo, confuEmo];

outputDir='../output/'


if __name__ == '__main__':
    print '%d of argv has been set ' % (len(sys.argv));
    ProcessSize = 500000
    MaxEmotionSize = 20000
    print sys.argv
    print len(sys.argv)
    if len( sys.argv ) == 0:
        print 'no argv given'
        pass
    elif len(sys.argv) != 4:
        print 'error argvs'
    else:
        ProcessSize = int(sys.argv[1])
        MaxEmotionSize = int(sys.argv[2])
        outputDir=sys.argv[3]


    print 'ProcessSize set to %d, MaxEmotionSize set to %d' % ( ProcessSize, MaxEmotionSize )
    print 'outputDir = %s' % outputDir

    dts.setSize( ProcessSize )
    dts.setFile( '../data/tweet_noRT_noDup.txt', '', '../log/dividedByEmoticons_'+str(ProcessSize) + '.log' )
    dts.openFiles()

    for emo in Emotions:
        emo['fileptr'] = codecs.open( outputDir + emo['filename'], 'w', 'utf-8' )

    def dealLine():
        line = dts.readlineI()
        for emo in Emotions:
            if emo['cnt'] > MaxEmotionSize:
                continue
            flag = -2
            for eicon in emo['Icons']:
                flag = line.find( eicon )
                if flag != -1 :
                    emo['fileptr'].write( line )
                    break
            if flag >= 0:
                emo['cnt'] = emo['cnt'] + 1

    dts.loop( dealLine, 'check Emoticons' )

    for emo in Emotions:
        emo['fileptr'].close()

    print '============='
    print 'processed Tweets:' + str( dts.processSize )
    for emo in Emotions:
        print emo['filename'] + ':' + str( emo['cnt'] )
        dts.writeL( emo['filename'] + ':' + str( emo['cnt'] ) + '\n' )

    dts.closeFiles()

#tfile = open( '../data/tweets_small.txt', 'r' )
#
#for x in range( processTweetSize + 1 ):
#    line = tfile.readline()
#    for emo in Emotions:
#        flag = -2
#        for eicon in emo['Icons']:
#            flag = line.find( eicon )
#            if flag != -1 :
#                break
#        if flag >= 0:
#            emo['cnt'] = emo['cnt'] + 1
#    if x % processTweetSizeSlide == 0:
#        print str( x/processTweetSizeSlide ) + '%'
#
#tfile.close()
#
#print '===================='
#print 'processed Tweets:' + str( processTweetSize )
#for emo in Emotions:
#    print emo['filename'] + ':' + str( emo['cnt'] )
#


