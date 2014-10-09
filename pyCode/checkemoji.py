#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import codecs
import dealTweets as dts


#ecstaIcons=[u'😀', u'😁', u'😂', u'😃', u'☺', u'😄', u'😅', u'😆', u'😇', u'😈', u'😉', u'😊', u'😋', u'😌', u'😎', u'😏', u'😛', u'😜', u'😝', u'😸', u'😹', u'😺', u'🙂', u'☺']

ecstaIcons=[u'😀', u'😁', u'😂', u'😃',  u'😄', u'😅', u'😆', u'😇', u'😈', u'😊', u'😋', u'😌', u'😎', u'😏', u'😛', u'😜', u'😝', u'😸', u'😹', u'😺', u'🙂' ]
loathIcons = [u'😑', u'😒', u'😕', u'😖', u'😨', u'😩', u'😪', u'😫', u'😬', u'😴', u'😵', u'😷', u'😼', u'🙀']
admirIcons=[u'🙇', u'🙍', u'🙎', u'🙏']
terroIcons = [u'😓', u'😰', u'😱']
amazeIcons=[u'😮', u'😲']
griefIcons=[u'😔', u'😞', u'☹', u'😟', u'😢', u'😣', u'😥', u'😦', u'😧', u'😭', u'😿', u'🙁', u'☹']
ragesIcons=[u'😠', u'😡', u'😤', u'😾']
vigilIcons=[u'😍', u'😗', u'😘', u'😙', u'😚', u'😻', u'😽', u'🙆', u'🙈', u'🙉', u'🙊', u'🙋', u'🙌']

ecstaEmo = {'filename': 'ecstaEmo.txt', 'Icons': ecstaIcons, 'cnt':0}
loathEmo = {'filename': 'loathEmo.txt', 'Icons': loathIcons, 'cnt':0}
admirEmo = {'filename': 'admirEmo.txt', 'Icons': admirIcons, 'cnt':0}
terroEmo = {'filename': 'terroEmo.txt', 'Icons': terroIcons, 'cnt':0}
amazeEmo = {'filename': 'amazeEmo.txt', 'Icons': amazeIcons, 'cnt':0}
griefEmo = {'filename': 'griefEmo.txt', 'Icons': griefIcons, 'cnt':0}
ragesEmo = {'filename': 'ragesEmo.txt', 'Icons': ragesIcons, 'cnt':0}
vigilEmo = {'filename': 'vigilEmo.txt', 'Icons': vigilIcons, 'cnt':0}

Emotions = [ecstaEmo, loathEmo, admirEmo, terroEmo, amazeEmo, griefEmo, ragesEmo, vigilEmo]
#Emotions = [ecstaEmo]

angerIcons=[ ':-7', ':-8(', ':-!', ':-[', ':-{~', ':-|', '?-(', ':-(*)', '(:-&', '(:-*', '>-r', '>:-<', '>>-(', '~~:-(', '@%&$%&', ':-/', ':-*']
depreIcons=[ ':-6', '(:<)', '(0--<', '*-(', '+-(', ':{', ':-"', '(-_-)', ':-\\', '-(', '(:^(', '..._...', ':-<', '(:-(', '(:-', '~~~~>_<~~~~', ':-{', '|-(', '}(:-(', '=:-(', ':-e', ':-\'|','[:|]', ':-(']
fatigIcons=[ '#-)', '|-)', ':-$', ':-1']
vigorIcons=[ ':-D', '8-)', ';-)', '(:-)', '|-D', '|-P', '^O^', '^-^', '^_<', '..~^.^~...', '...~*.*~...', '^_^', '=^-^=', '(:-D)', ':-9', ':->', ':~)', ':-]', '8:]', ':*)', ':%)%', ':-)8', ':-)-{8', ':-})', ':-<)', ':-=)', ':-{ )', '[:-)', '}:-)', '{(:-)', '0-)', 'B-)', '=:-)', '<<<<(:-)', 'i-)', ':>)', ':=)', ':-}', 'o-)', '@-)', '*:o)', '*<|:-)', ':-)', '+:-)', '0-)', '@:-)', '<:-)<<|', ':-)', ':-\')', '8:-)', '!-)', '#:-)', '%-)', '%-}', '\':-)', '&:-){:-)', '(:)-)', ':-P', ':-Q', ',-)', ',-}', '@>>--->---', ';-\\', ':-j', ':-*', '(:-*]']
frindIcons=[ 'x-<', ':-)', '(-:', ':)', '(:',u'☺️']
tensnIcons=[ ':-0', ':-o', ':-()',':-O', ':O','o_O', 'O_o','O_O','o_o']
confuIcons=[ '?_?', '@_@', '<@_@>']

angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0}
depreEmo = {'filename': 'depreEmo.txt', 'Icons': depreIcons, 'cnt':0}
fatigEmo = {'filename': 'fatigEmo.txt', 'Icons': fatigIcons, 'cnt':0}
vigorEmo = {'filename': 'vigorEmo.txt', 'Icons': vigorIcons, 'cnt':0}
frindEmo = {'filename': 'frindEmo.txt', 'Icons': frindIcons, 'cnt':0}
tensnEmo = {'filename': 'tensnEmo.txt', 'Icons': tensnIcons, 'cnt':0}
confuEmo = {'filename': 'confuEmo.txt', 'Icons': confuIcons, 'cnt':0}

#Emotions = [angerEmo, depreEmo, fatigEmo, vigorEmo, frindEmo, tensnEmo, confuEmo];

dts.setSize( 5000000 )
dts.setFile( '../data/tweet_noRT_noDup.txt' )
dts.openFiles()
def dealLine():
    line = dts.readlineI()
    for emo in Emotions:
        flag = -2
        for eicon in emo['Icons']:
            if eicon in line:
                print line
                #flag = line.find( eicon )
                flag = 0 
                break
        if flag >= 0:
            emo['cnt'] = emo['cnt'] + 1

dts.loop( dealLine, 'check Emoticons' )
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

print '============='
print 'processed Tweets:' + str( dts.processSize )
for emo in Emotions:
    print emo['filename'] + ':' + str( emo['cnt'] )

