grammar VM;

/**
 * Parser rules
 */
program:
    statements
    EOF
    ;

statements:
    statement*
    ;

statement:
    push
    | pop
    | arithmetic
    | logical
    ;

push:
    PUSH segment INT ;

pop:
    POP segment INT ;

arithmetic:
    ADD
    | SUB
    | NEG
    ;

logical:
    LT
    | EQ
    | GT
    | AND
    | OR
    | NOT
    ;

// Target segment
segment:
    LOCAL
    | ARGUMENT
    | THIS
    | THAT
    | CONSTANT
    | STATIC
    | POINTER
    | TEMP
    ;

/**
 * Lexer rules
 */
INT: [0-9]+ ;

// Keywords
PUSH: P U S H ;
POP: P O P ;

// Arithmetic
ADD: A D D ;
SUB: S U B ;
NEG: N E G ;

// Logical
LT: L T ;
EQ: E Q ;
GT: G T ;
AND: A N D ;
OR: O R ;
NOT: N O T ;

// Stacks
LOCAL: L O C A L ;
ARGUMENT: A R G U M E N T ;
THIS: T H I S ;
THAT: T H A T ;
CONSTANT: C O N S T A N T ;
STATIC: S T A T I C ;
POINTER: P O I N T E R ;
TEMP: T E M P ;

// Skip whitespaces and comments by default
COMMENT: '//' ~( '\r' | '\n' )* -> channel(HIDDEN) ;
WS: [ \t\r\n] -> channel(HIDDEN);

fragment A : [aA]; // match either an 'a' or 'A'
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];