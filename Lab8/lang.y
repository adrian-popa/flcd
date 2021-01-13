%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1

int yylex();
int yyerror(char *);
int strcmp(const char *, const char *);
%}

%token START
%token TASK
%token DEFINES
%token CONSTANT
%token INTEGER
%token BOOLEAN
%token STRING
%token FLOAT
%token DOUBLE
%token WHEN
%token OTHERWISE
%token RETURN
%token CONSOLE
%token READ
%token WRITE
%token TAKE
%token FROM
%token LIST
%token OF
%token FOR
%token WHILE
%token DO

%token COLON
%token SEMI_COLON
%token COMMA
%token DOT
%token OPENED_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPENED_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPENED_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET

%token ADD
%token SUB
%token MUL
%token DIV
%token MOD
%token LT
%token GT
%token LOET
%token GOET
%token EQUAL
%token NOT_EQUAL
%token ATTRIB
%token NOT
%token AND
%token OR

%token ID

%token CONST

%start program

%%

program : START cmpdstmt ;
task : type TASK ID OPENED_ROUND_BRACKET declarationList CLOSED_ROUND_BRACKET DEFINES COLON cmpdstmt ;
declarationList : declaration declarationTemp ;
declaration : type ID ;
declarationTemp : /*Empty*/ | COMMA declarationList ;
fnCall : ID OPENED_ROUND_BRACKET identifiersList CLOSED_ROUND_BRACKET SEMI_COLON ;
identifiersList : ID identifierTemp ;
identifierTemp : /*Empty*/ | COMMA identifiersList ;
type : type1 | arrayDecl ;
arrayDecl : LIST OF type1 EQUAL OPENED_SQUARE_BRACKET INTEGER CLOSED_SQUARE_BRACKET ;
type1 : INTEGER | BOOLEAN | STRING | FLOAT | DOUBLE ;
cmpdstmt : OPENED_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET ;
stmtlist :  stmt stmtTemp ;
stmtTemp : /*Empty*/ | stmtlist ;
stmt :  simplstmt SEMI_COLON | structstmt ;
simplstmt :  assignstmt | iostmt | declaration ;
structstmt :  cmpdstmt | ifstmt | whilestmt | forstmt | task | fnCall ;
ifstmt :  WHEN boolean_condition COLON cmpdstmt tempIf ;
tempIf : /*Empty*/ | OTHERWISE cmpdstmt ;
forstmt :  TAKE ID FROM ID COLON cmpdstmt ;
whilestmt :  WHILE boolean_condition DO cmpdstmt ;
assignstmt :  ID ATTRIB expression ;
expression : arithmetic2 arithmetic1 ;
arithmetic1 : ADD arithmetic2 arithmetic1 | SUB arithmetic2 arithmetic1 | /*Empty*/ ;
arithmetic2 : multiply2 multiply1 ;
multiply1 : MUL multiply2 multiply1 | DIV multiply2 multiply1 | /*Empty*/ ;
multiply2 : OPENED_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | CONST | ID | indexedIdentifier ;
indexedIdentifier :  ID OPENED_SQUARE_BRACKET CONST CLOSED_SQUARE_BRACKET ;
iostmt :  CONSOLE READ ID | CONSOLE WRITE ID | CONSOLE WRITE CONST ;
condition : expression GT expression | expression GOET expression | expression LT expression |
	expression LOET expression | expression EQUAL expression | expression NOT_EQUAL expression ;
boolean_condition : condition boolean_cond_temp ;
boolean_cond_temp : /*Empty*/ | AND boolean_condition | OR boolean_condition ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1)
    yyin = fopen(argv[1], "r");
  if ((argc > 2) && (!strcmp(argv[2], "-d")))
    yydebug = 1;
  if (!yyparse())
    fprintf(stderr,"All good!!\n");
}
