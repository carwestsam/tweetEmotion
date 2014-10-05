#ifndef DATABASECUTTER_H
#define DATABASECUTTER_H

/*
 *	Use To Parse Tweets Dump File to Tweets only file
 *	
 */
#include "util.h"

class DatabaseCutter
{
public:
	//  there are some head file (15 lines) in the mysql dump file, innocent to delete
	static void dealHeader( FILE* fin );
	//  Many line in the dump file (multi record in each line), deal one line
	static void dealLine( FILE* fin ) ;
	static void dealSQuote( FILE* fin, FILE* fout, bool outflag);
	static void ReadTillCom ( FILE* fin, FILE* fout, bool outflag );
	static void ReadParaPair ( FILE* fin, FILE* fout, bool outflag );
	static void ReadLines    ( FILE* fin, FILE* fout, bool outflag );
};

#endif 
