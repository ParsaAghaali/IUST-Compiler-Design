grammar ArithmeticExpression;


//
//start: assigns  EOF;
//assigns: assign NEWLINE assigns | assign;
//assign: ID '=' expr;
//expr:  expr ADD term | expr SUB term | term | '-' term | '+' term |;
//term: term MUL factor | term DIV factor | factor;
//factor: NUMERICALVALUE | LPAREN expr RPAREN | STRING | ID;



start: assigns  EOF;
assigns: assign NEWLINE assigns | assign;
assign: ID '=' expr ;
expr:  expr ADD term | expr SUB term | term | '-' term | '+' term |;
term: term MUL factor | term DIV factor | factor;
factor: NUMERICALVALUE | '+' NUMERICALVALUE | '-' NUMERICALVALUE | LPAREN expr RPAREN | STRING | ID;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
NUMERICALVALUE: FLOAT | INTEGER;
fragment FLOAT:[0-9]*'.'[0-9]+;
fragment INTEGER:[0-9]+;
STRING: '"'.*?'"';
WS: [ \t\r]+ -> skip;
NEWLINE : '\n';
ID : [a-z,A-Z]([a-z,A-Z] | [0-9])*;