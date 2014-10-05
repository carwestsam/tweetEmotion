#ifndef UTIL_H
#define UTIL_H

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <ctype.h>
#include <cassert>
#include <cmath>

using namespace std;

typedef unsigned int uint;

const unsigned int MAX_LINEBUF = 1024;

#define foreach(container, it)\
	for(auto it=(container).begin();it!=(container).end();++it)
#define foreach_r(container, it)\
	for(auto it=(container).rbegin();it!=(container).rend();++it)

class Util
{
public:
	static vector<string>	ReadFromFile( string filename );
	static vector<string>	ReadTweetFile( string filename );
	static vector<string>	TweetTokenize( string initstr );
	static vector<string>	WordSplit( string initstr );
	static int		String2Int( string initstr );
};

#endif // UTIL_H
