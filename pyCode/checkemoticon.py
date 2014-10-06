#!/usr/bin/python

import re
import codecs

processTweetSize=5000000
processTweetSizeSlide=processTweetSize/100

angerIcons=[ ':-7', ':-8(', ':-!', ':-[', ':-{~', ':-|', '?-(', ':-(*)', '(:-&', '(:-*', '>-r', '>:-<', '>>-(', '~~:-(', '@%&$%&', ':-/', ':-*']
depreIcons=[ ':-6', '(:<)', '(0--<', '*-(', '+-(', ':{', ':-"', '(-_-)', ':-\\', '-(', '(:^(', '..._...', ':-<', '(:-(', '(:-', '~~~~>_<~~~~', ':-{', '|-(', '}(:-(', '=:-(', ':-e', ':-\'|','[:|]', ':-(']
fatigIcons=[ '#-)', '|-)', ':-$', ':-1']
vigorIcons=[ ':-D', '8-)', ';-)', '(:-)', '|-D', '|-P', '^O^', '^-^', '^_<', '..~^.^~...', '...~*.*~...', '^_^', '=^-^=', '(:-D)', ':-9', ':->', ':~)', ':-]', '8:]', ':*)', ':%)%', ':-)8', ':-)-{8', ':-})', ':-<)', ':-=)', ':-{ )', '[:-)', '}:-)', '{(:-)', '0-)', 'B-)', '=:-)', '<<<<(:-)', 'i-)', ':>)', ':=)', ':-}', 'o-)', '@-)', '*:o)', '*<|:-)', ':-)', '+:-)', '0-)', '@:-)', '<:-)<<|', ':-)', ':-\')', '8:-)', '!-)', '#:-)', '%-)', '%-}', '\':-)', '&:-){:-)', '(:)-)', ':-P', ':-Q', ',-)', ',-}', '@>>--->---', ';-\\', ':-j', ':-*', '(:-*]']
frindIcons=[ 'x-<', ':-)', '(-:', ':)', '(:']
tensnIcons=[ ':-0', ':-o', ':-()',':-O', ':O','o_O', 'O_o','O_O','o_o']
confuIcons=[ '?_?', '@_@', '<@_@>']

angerEmo = {'filename': 'angerEmo.txt', 'Icons': angerIcons, 'cnt':0}
depreEmo = {'filename': 'depreEmo.txt', 'Icons': depreIcons, 'cnt':0}
fatigEmo = {'filename': 'fatigEmo.txt', 'Icons': fatigIcons, 'cnt':0}
vigorEmo = {'filename': 'vigorEmo.txt', 'Icons': vigorIcons, 'cnt':0}
frindEmo = {'filename': 'frindEmo.txt', 'Icons': frindIcons, 'cnt':0}
tensnEmo = {'filename': 'tensnEmo.txt', 'Icons': tensnIcons, 'cnt':0}
confuEmo = {'filename': 'confuEmo.txt', 'Icons': confuIcons, 'cnt':0}

Emotions = [angerEmo, depreEmo, fatigEmo, vigorEmo, frindEmo, tensnEmo, confuEmo];

tfile = open( '../data/tweets_small.txt', 'r' )

for x in range( processTweetSize + 1 ):
    line = tfile.readline()
    for emo in Emotions:
        flag = -2
        for eicon in emo['Icons']:
            flag = line.find( eicon )
            if flag != -1 :
                break
        if flag >= 0:
            emo['cnt'] = emo['cnt'] + 1
    if x % processTweetSizeSlide == 0:
        print str( x/processTweetSizeSlide ) + '%'

tfile.close()

print '===================='
print 'processed Tweets:' + str( processTweetSize )
for emo in Emotions:
    print emo['filename'] + ':' + str( emo['cnt'] )

