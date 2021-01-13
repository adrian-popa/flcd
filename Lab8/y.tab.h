/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     START = 258,
     TASK = 259,
     DEFINES = 260,
     CONSTANT = 261,
     INTEGER = 262,
     BOOLEAN = 263,
     STRING = 264,
     FLOAT = 265,
     DOUBLE = 266,
     WHEN = 267,
     OTHERWISE = 268,
     RETURN = 269,
     CONSOLE = 270,
     READ = 271,
     WRITE = 272,
     TAKE = 273,
     FROM = 274,
     LIST = 275,
     OF = 276,
     FOR = 277,
     WHILE = 278,
     DO = 279,
     COLON = 280,
     SEMI_COLON = 281,
     COMMA = 282,
     DOT = 283,
     OPENED_CURLY_BRACKET = 284,
     CLOSED_CURLY_BRACKET = 285,
     OPENED_ROUND_BRACKET = 286,
     CLOSED_ROUND_BRACKET = 287,
     OPENED_SQUARE_BRACKET = 288,
     CLOSED_SQUARE_BRACKET = 289,
     ADD = 290,
     SUB = 291,
     MUL = 292,
     DIV = 293,
     MOD = 294,
     LT = 295,
     GT = 296,
     LOET = 297,
     GOET = 298,
     EQUAL = 299,
     NOT_EQUAL = 300,
     ATTRIB = 301,
     NOT = 302,
     AND = 303,
     OR = 304,
     ID = 305,
     CONST = 306
   };
#endif
/* Tokens.  */
#define START 258
#define TASK 259
#define DEFINES 260
#define CONSTANT 261
#define INTEGER 262
#define BOOLEAN 263
#define STRING 264
#define FLOAT 265
#define DOUBLE 266
#define WHEN 267
#define OTHERWISE 268
#define RETURN 269
#define CONSOLE 270
#define READ 271
#define WRITE 272
#define TAKE 273
#define FROM 274
#define LIST 275
#define OF 276
#define FOR 277
#define WHILE 278
#define DO 279
#define COLON 280
#define SEMI_COLON 281
#define COMMA 282
#define DOT 283
#define OPENED_CURLY_BRACKET 284
#define CLOSED_CURLY_BRACKET 285
#define OPENED_ROUND_BRACKET 286
#define CLOSED_ROUND_BRACKET 287
#define OPENED_SQUARE_BRACKET 288
#define CLOSED_SQUARE_BRACKET 289
#define ADD 290
#define SUB 291
#define MUL 292
#define DIV 293
#define MOD 294
#define LT 295
#define GT 296
#define LOET 297
#define GOET 298
#define EQUAL 299
#define NOT_EQUAL 300
#define ATTRIB 301
#define NOT 302
#define AND 303
#define OR 304
#define ID 305
#define CONST 306




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

