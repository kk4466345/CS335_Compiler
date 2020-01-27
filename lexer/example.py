 # ------------------------------------------------------------
 # calclex.py
 #
 # tokenizer for a simple expression evaluator for
 # numbers and +,-,*,/
 # ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

# List of token names.   This is always required
keywords = {
    'ABSTRACT'  , 'CONTINUE'  , 'FOR'         , 'NEW' ,        'SWITCH',
'ASSERT' ,    'DEFAULT',    'IF',           'PACKAGE',     'SYNCHRONIZED',
'BOOLEAN',    'DO',         'GOTO',         'PRIVATE',     'THIS',
'BREAK',      'DOUBLE',     'IMPLEMENTS',   'PROTECTED',   'THROW',
'BYTE',       'ELSE',       'IMPORT',       'PUBLIC' ,     'THROWS',
'CASE'  ,     'ENUM'  ,     'INSTANCEOF',   'RETURN',      'TRANSIENT',
'CATCH',      'EXTENDS',    'INT',          'SHORT',       'TRY',
'CHAR'       ,'FINAL'      ,'INTERFACE' ,   'STATIC',      'VOID',
'CLASS',      'FINALLY'  ,  'LONG',         'STRICTFP',    'VOLATILE',
'CONST',      'FLOAT',      'NATIVE',       'SUPER',       'WHILE',
'NUMBER',      'STRING',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN'
}
ops = {'SEMICOLON'}
reserved = {}
for key in keywords:
    reserved[key.lower()] = key
identity = {'IDENTIFIER'}

tokens = list(ops) + list(identity) + list(reserved.values())
# print(tokens)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'

t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'  
string_lit = """("[^"]*")"""
rune_lit = "\'(.|(\\[abfnrtv]))\'"

identifier_lit = "[_a-zA-Z]+[a-zA-Z0-9_]*"
@TOKEN(identifier_lit)
def t_IDENTIFIER(t):
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value) 
    return t



def t_STRING(t):
    r'\"( ([ -~]|(\\\"))+ )\"'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# Test it out
data = '''
string a = ' kamlesh '
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
 tok = lexer.token()
 if not tok: 
     break      # No more input
 print(tok)