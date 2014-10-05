#include "databaseCutter.h"

const int MAX_BUF = 10240;

void DatabaseCutter::dealHeader( FILE* fin )
{
	char tmpc = 0;
	for ( int i=0; i<=42; i++ ){
		do {
			tmpc = fgetc( fin );
		}while ( tmpc != '\n' );
	}
}

void DatabaseCutter::dealLine( FILE* fin )
{
}

void DatabaseCutter::dealSQuote( FILE* fin, FILE* fout, bool outflag )
{
	char tmpc = 0;
	while ( true ){
		tmpc = fgetc( fin );
		if ( tmpc == '\\' ){
			if ( outflag ) fputc( tmpc, fout );
			tmpc = fgetc(fin);
		}else if ( tmpc == '\'' ){
			break;
		}
		if ( outflag ) fputc( tmpc, fout );
	}
}

void DatabaseCutter::ReadTillCom( FILE* fin, FILE* fout, bool outflag )
{
	while ( true ) {
		char tmpc = fgetc( fin );
		if ( tmpc == ',' ){
			//if ( outflag ) putc( tmpc, fout );
			break;
		}else if ( tmpc == '\''){
			dealSQuote( fin, fout, outflag );
			continue;
		}
		if ( outflag ) fputc( tmpc, fout );
	}
}

void DatabaseCutter::ReadParaPair( FILE* fin, FILE* fout, bool outflag )
{
	ReadTillCom ( fin, fout, 0 ); // id
	ReadTillCom ( fin, fout, 0 ); // user id
	ReadTillCom ( fin, fout, 1 ); // tweet_text
	fputc('\n',fout);
	ReadTillCom ( fin, fout, 0 ); // tweet_link
	ReadTillCom ( fin, fout, 0 ); // tweet_time
	ReadTillCom ( fin, fout, 0 ); // num 1
	while ( true ){
		char tmpc = fgetc( fin );
		if ( tmpc == ')' ) break;
	}
}
void DatabaseCutter::ReadLines( FILE* fin, FILE* fout, bool outflag )
{
	int Cnt = 0;
	const int Max_Cnt = 40000000;
	const int Max_Cnt_Piece = Max_Cnt / 100;
	while ( Cnt < Max_Cnt )
	{
		int tmpc = fgetc( fin );
		if ( tmpc == EOF ) break;
		else if ( tmpc == '(' ){
			ReadParaPair( fin, fout, outflag );
			Cnt ++;
			if ( Cnt % Max_Cnt_Piece == 0 ) {
				printf("%lf\t%d/%d lines had done\n",(Cnt*100.0)/(1.0*Max_Cnt), Cnt, Max_Cnt);
			}
		}
	}
	FILE* fx = fopen( "output/DocCnt.txt" , "w" );
	fprintf( fx, "%d\n", Cnt );
	fclose(fx);
	printf("%d Tweets added to tweets_small.txt\n", Cnt);
}

#ifdef DATABASECUTTER
/* 
 *	Use To Parse Tweets Dump File to Tweets only file
 *	convert '\n' -> ' '
 */
int main ()
{
	FILE* fin = fopen("data/big/tweets_0826.sql","r");
	FILE* fout = fopen ("data/tweets_small.txt","w");
	DatabaseCutter::dealHeader(fin);
	DatabaseCutter::ReadLines(fin,fout,0);
	fclose(fin);
	fclose(fout);
	return 0;
}
#endif

