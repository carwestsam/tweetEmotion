#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 Carwest Sung <carwestsam@gmail.com>
#
# Distributed under terms of the MIT license.

"""
select Topics form tweets
"""

import dealTweets as dts
import re
import json
import os


topicList = [ur"#emabiggestfans1d", ur"#emabiggestfansjustinbieber", ur"#porn", ur"#ipad", ur"#halloween", ur"#emabiggestfans5sos", ur"#stealmygirl", ur"#thewalkingdead", ur"#ebola", ur"#emabiggestfansarianagrande", ur"#lol"]

def filterHashtags():
    line = dts.readlineI()
    if not line:
        return
    try:
        obj = json.loads(line)
    except:
        return

    text = obj["text"]
    pt = "space"
    for topic in topicList:
        matchs = re.search( topic, text )
        if not matchs:
            continue
        else:
            pt = topic
            break

    if not matchs:
        return
    else:
        nobj = {"text":text, "hashtag":pt }
        dts.writeO( json.dumps( nobj ) + '\n' )
    
    pass

def topicFilter():
    dts.setSize( 14000000 )
    dts.setFile( "/home/server2103/dump/twitter.tweet.json", "../entityOutput/topictwitter", "../log/matchtwitter" )
    dts.openFiles()
    dts.loop( filterHashtags, 'filterHashtags' )
    dts.closeFiles()
    

if __name__ == "__main__":
    topicFilter()
    pass


