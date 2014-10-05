
#include "util.h"


int charlistcmp( const char *a, const char * b, int len )
{
	for ( int i=0; i<len; i++ ){
		if ( a[i] < b[i] ) return -1;
		else if ( a[i] > b[i] ) return 1;
	}
	return 0;
}

vector<string> Util::ReadTweetFile( string filename )
{
	printf("reading from %s\n", filename.c_str());
	FILE* fin = fopen( filename.c_str() , "r" );


	vector<string> vec;
	vec.clear();

	char last[5] = {0};
	const char linebreak[5] = "$#@#";

	while ( true ){
		//puts("line");
		char tmpline [MAX_LINEBUF] = {0};
		int tmplineCnt=0;
		char tmpc = EOF;
		while ( true ){
			tmpc = fgetc(fin);
			if ( tmpc == '\n' && charlistcmp( linebreak, last, 4 )!= 0) tmpc = ' ';
			else if ( tmpc == '\t' ) tmpc = ' ';
			if ( tmpc == EOF || tmpc == '\n' ) {
				tmpline[tmplineCnt] = 0;
				break;
			}else {
				tmpline[tmplineCnt++ ] = tmpc;
				for ( uint i=4; i>0; i-- ) last[i] = last[i-1];
				last[0] = tmpc;
			}
		}
		string tmpstr(tmpline);
		if ( tmpc==EOF || tmpstr.size() < 3 ) break;
		vec.push_back( tmpstr );
	}

	fclose(fin);

	printf("read %u line from tweet file %s\n", vec.size(), filename.c_str());
	return vec;
}

vector<string> Util::TweetTokenize( string initstr )
{

	bool flag[MAX_LINEBUF]={0};
	char TOK_SIGN[4]="#@#";

	for ( uint i=0; i<initstr.size()-3; i++ ){
		bool tmp = true;
		for ( uint j=0; j<3; j++ ){
			if ( initstr[j+i] != TOK_SIGN[j] ){
				tmp = false;
				break;
			}
		}
		if ( tmp ) flag[i] = true;
	}

	vector<string> vec;
	vec.clear();
	int lpos=0, rpos=-3;
	for ( uint i=0; i<initstr.size(); i++ ){
		if ( flag[i] ) {
			rpos = i;
			char tmpcharlist[MAX_LINEBUF]={0};
			for ( uint j=lpos; j<rpos; j++ ){
				tmpcharlist[j-lpos] = initstr[j];
			}tmpcharlist[rpos]=0;
			string tmpstr (tmpcharlist);
			vec.push_back( tmpstr );
			lpos = rpos + 3;
		}
	}
	return vec;
}

vector<string> Util::WordSplit( string initstr )
{
	const char whitecase[128] = "#@-.,:;'\\()[]{}";
	uint whitelen = strlen( whitecase );

	for ( uint i=0; i<initstr.size(); i++ ){
		for ( uint j=0; j<whitelen; j++ ){
			if ( initstr[i] == whitecase[j] )
				initstr[i] = ' ';
		}
	}

	vector<string> vec;
	vec.clear();

	char tmpword[MAX_LINEBUF] = {0};
	int pos=0;
	for ( uint i=0; i<initstr.size(); i++ ){
		if ( isalnum( initstr[i] )){
			tmpword[pos++] = tolower(initstr[i]);
		}else {
			if ( pos > 0 ){
				tmpword[pos] = 0;
				string tmpstr ( tmpword );
				vec.push_back( tmpstr );
				tmpstr[0]=0;
				pos = 0;
			}else {
				pos = 0;
			}
		}
	}

	return vec;
}

int Util::String2Int ( string initstr )
{
	if ( initstr.empty() ) return 0;
	for ( uint i=0; i<initstr.size(); i++ ){
		if ( !isdigit(initstr[i]) )
			return 0;
	}
	char tmp[128];
	sprintf(tmp, "%s", initstr.c_str() );
	int tn = 0;
	sscanf(tmp, "%d", &tn );
	return tn;

}
















