import ply.lex as lex

# class Lexer(object):


operators={'MULTIPLICATION','DIVISION','MODULO','ADDITION','SUBTRACTION', 
'UNARY_MINUS', 'UNARY_PLUS' , 'INCREMENT', 'DECREMENT' , 'LOGICAL_NOT',
'PLUS_EQUAL' , 'MINUS_EQUAL' , 'START_EQUAL', 'DIVIDE_EQUAL' , 'MODULO_EQUAL' , 
'EQUAL_EQUAL','NOT_EQUAL' , 'LESSTHEN' , 'LESS_EQUAL', 'GREATERTHEN' , 'GREATER_EQUAL',
'LOGICAL_AND' , 'LOGICAL_OR' ,
#TERNARY OPERATOR
'BIT_AND' , 'BIT_OR', 'BIT_XOR', 'BIT_COMPLEMENT',
'SHIFTLL', 'SHIFTSIGNRR', 'SHIFTUNSIGNRR'
}

saperators = {
	'leftsmallbr' , 'rsmallbr','lmiddlebr','rmiddlebr','lbigbr','rbigbr', 'Semicolon' , 'koma' , 'dot','colon',
	#   (   )   {   }   [   ]   ;   ,   .   :   ::

	}




reserved = {}

for r in keywords:
	reserved[r.lower()]=r

tokens=list(reserved.values())

print(tokens)



t_ignore  = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

 
 # Define a rule so we can track line numbers
 # Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'   
    t.lexer.lineno += len(t.value)


 
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer=lex.lex()


f=open("/home/kkmeena/CS335_Compiler/lexer/data.java","r");
contents = f.read();
 
 # Give the lexer some input
lexer.input(contents)
print("wjebfewkj\n")
 
 # Tokenize
while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 print(tok)
 # Tokenize


f.close();