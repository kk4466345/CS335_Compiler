#!/usr/bin/python
import ply.lex as lex
import sys
from ply.lex import TOKEN
import csv


class kklex(object):
	keywords = {'ABSTRACT','ASSERT','BOOLEAN', 'BREAK',
	'BYTE', 'CASE', 'CATCH', 'CHAR', 'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO',
	'DOUBLE', 'ELSE', 'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'IF', 'GOTO',
	'IMPLEMENTS',
	'IMPORT', 
	'INSTANCEOF', 
	'INT', 'INTERFACE', 'LONG', 'NATIVE','STRING',
	'NEW','PACKAGE','PRIVATE','PROTECTED','PUBLIC',
	'RETURN','SHORT','STATIC','STRICTFP','SUPER','SWITCH',
	'SYNCHRONIZED','THIS','THROW',
	'THROWS','TRANSIENT','TRY','VOID'
	,'VOLATILE','WHILE'}

	# print(keywords)



	operators = {
				'PLUS','MINUS', 'STAR','DIVIDE', 'MOD', 'ASSIGN', 'AND','LOGICAL_AND', 'INCR', 'DECR', 'OR', 'XOR', 'LSHIFT', 'RSHIFT', 'PLUS_ASSIGN', 
				'MINUS_ASSIGN', 'STAR_ASSIGN', 'DIVIDE_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN', 'LOGICAL_OR', 
				'EQUALS', 'LESSER', 'GREATER', 'NOT', 'NOT_ASSIGN', 'LESS_EQUALS','MORE_EQUALS', 'QUICK_ASSIGN'}





#     keywords = {'ABSTRACT', 'ASSERT' , ' BOOLEAN' , 'BREAK', 'BYTE', 'CASE' , 'CATCH', 'CHAR', 'CLASS', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE', 'ELSE' , 'ENUM', 'EXTENDS', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'IF', 'GOTO', 'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT','INTERFACE', 'LONG', 'NATIVE' , 'NEW', 'PACKAGE', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'RETURN' , 'SHORT' , 'STATIC' , 'STRICTFP', 'SUPER' ,'SWITCH', 'SYNCHRONIZED', 'THIS','THROW', 'THROWS' , 'TRANSIENT', 'TRY' ,'VOID' , 'VOLATILE','WHILE'
# }


	seperators={'LSQUARE', 'RSQUARE', 'LCURL', 'LPAREN', 'RPAREN',
             'RCURL', 'COMMA', 'DOT', 'SEMICOLON', 'COLON'}



	reserved = {}
	for r in keywords:
		reserved[r.lower()] = r

	

	types = {'INTEGER', 'OCTAL', 'HEX', 'IMAGINARY','FLOATLIT','STRINGLIT','DECIMALLIT','BOOLEANLIT','NULLLIT','RUNE'}

	identity = {'IDENTIFIER'}

	tokens = list(reserved.values()) + list(operators)+list(seperators) + list(types) + \
	              list(identity) 

	

	# Token definitions

	t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
	t_ignore = ' \t'
	t_error=
	t_PLUS = r'\+'
	#t_UPLUS = r'\+'
	t_MINUS = r'-'
	#t_UMINUS = r'-'
	t_STAR = r'\*'
	#t_USTAR = r'\*'
	t_DIVIDE = r'/'
	t_MOD = r'%'
	t_ASSIGN = r'='
	t_AND = r'&'
	#t_UAND = r'&'
	t_LOGICAL_AND = r'&&'
	t_INCR = r'\+\+'
	t_DECR = r'--'
	t_LPAREN = r'\('
	t_RPAREN = r'\)'
	t_OR = r'\|'
	t_XOR = r'\^'
	t_LSHIFT = r'<<'
	t_RSHIFT = r'>>'
	t_PLUS_ASSIGN = r'\+='
	t_MINUS_ASSIGN = r'-='
	t_STAR_ASSIGN = r'\*='
	t_DIVIDE_ASSIGN = r'/='
	t_MOD_ASSIGN = r'%='
	t_AND_ASSIGN = r'&='
	t_OR_ASSIGN = r'\|='
	t_XOR_ASSIGN = r'\^='
	t_LSHIFT_ASSIGN = r'<<='
	t_RSHIFT_ASSIGN = r'>>='
	t_LOGICAL_OR = r'\|\|'
	t_EQUALS = r'=='
	t_LESSER = r'<'
	t_GREATER = r'>'
	t_NOT = r'!'
	#t_UNOT = r'!'
	t_NOT_ASSIGN = r'!='
	t_LESS_EQUALS = r'<='
	t_MORE_EQUALS = r'>='
	t_QUICK_ASSIGN = r':='
	t_LSQUARE = r'\['
	t_RSQUARE = r'\]'
	t_LCURL = r'\{'
	t_RCURL = r'\}'
	t_COMMA = r','
	t_DOT = r'\.'
	t_SEMICOLON = r';'
	t_COLON = r':'

	# Integer based reg variables
	newline = "\\n"
	# wspace = "\s"

	decimal_lit = "(0|([1-9][0-9]*))"
	octal_lit = "(0[0-7]*)"	
	hex_lit = "(0x|0X)[0-9a-fA-F]+"

	# Float based reg variables
	float_lit = "[0-9]*\.[0-9]+([eE][-+]?[0-9]+)?"

	# string_lit = """("[^"]*")|(\'[^\']*\')"""
	string_lit = """("[^"]*")"""
	boolean_lit="[true | false]"


	imaginary_lit = "(" + decimal_lit + "|" + float_lit + ")i"

	rune_lit = "\'(.|(\\[abfnrtv]))\'"

	identifier_lit = "[_a-zA-Z]+[a-zA-Z0-9_]*"



	@TOKEN(identifier_lit)
	def t_IDENTIFIER(self,t):
		if t.value == 'true':
			t.type="BOOLEANLIT"
			return t;
		if t.value=='false':
			t.type="BOOLEANLIT"
			return t;
		if t.value == 'null':
			t.type="NULLLIT"
			return t;

		t.type = self.reserved.get(t.value, 'IDENTIFIER')
		return t


	@TOKEN(rune_lit)
	def t_RUNE(self,t):
	    t.value = ord(t.value[1:-1])
	    return t


	@TOKEN(string_lit)
	def t_STRING(self,t):
	    t.value = t.value[1:-1]
	    t.type = "STRINGLIT"
	    return t


	# @TOKEN(boolean_lit)
	# def t_BOOLEAN(self,t):
	#     t.value = t.value[1:-1]
	#     t.type = "LITERAL"
	#     print("kwnelafhkjqbwkb")
	#     return t

	

	@TOKEN(imaginary_lit)
	def t_IMAGINARY(self,t):
	    t.value = complex(t.value.replace('i', 'j'))
	    return t


	@TOKEN(float_lit)
	def t_FLOAT(self,t):
	    t.value = float(t.value)
	    t.type='FLOATLIT'
	    return t


	@TOKEN(hex_lit)
	def t_HEX(self,t):
	    t.value = int(t.value, 16)
	    return t


	@TOKEN(octal_lit)
	def t_OCTAL(self,t):
	    t.value = int(t.value, 8)
	    return t


	@TOKEN(decimal_lit)
	def t_INTEGER(self,t):
	    # re.escape(decimal_lit)
	    t.value = int(t.value)
	    return t




	# def t_ignore(self,t):
	# 	r' \t'
	# 	self.f.write("</br>")

    # track line numbers
	@TOKEN(newline)
	def t_NEWLINE(self, t):
		r'\n+'
	
		t.lexer.lineno += len(t.value)

    # handle Error
	# def t_error(self, t):
	# 	# self.f.write("<br>Line :: %d  Illegal entry '%s'<br>" %(t.lexer.lineno, t.value))
	# 	t.lexer.skip(1)



	def t_error(selt, t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

    # Build the lexer
	def build(self, **kwargs):
		self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
	def test(self, data):
		self.lexer.input(data)
		

		line_num = 1;
		dict={}
		kk=kklex()

		while True:
			tok = self.lexer.token()
			# print(tok)
			if tok != None:
				# print(tok)
				
				# print (key,tok.value,tok.type)
				for abc in kk.reserved.values():
					if abc==tok.type:
						if abc==tok.value.upper():
							# print(abc , tok.type ,tok.value,' is a keywords##################')
							tok.type='keywords'
						else:
							tok.type='literal'

						
						break;
				for abc in kk.operators:
					if abc == tok.type:
						tok.type='operator';
						break;

				for abc in kk.seperators:
					if abc==tok.type:
						tok.type='seperators'
						break;


				for abc in kk.types:
					if abc==tok.type:
						tok.type='literal'
						break;






				output={};

				print(tok)

			

				if not tok.value in dict:
					dict[tok.value]=[1,tok.type]
					# print("adding",tok.value,"=", dict[tok.value])
				else:

					dict[tok.value][0] +=1
					# print("increasing",tok.value,dict[tok.value])

		
				k = int(str(tok).split(',')[-1].split(')')[0])
				v = int(str(tok).split(',')[-2])
				self.tokenList[k] = v	
			if not tok:
				# self.f.write("</p>\r\n</body>\r\n</html>\r\n")
				break

		# pprint(dict)

		with open('output.csv', 'w',newline='') as file:
			writer=csv.writer(file)
			for a in dict:
				# print(a,dict[a][1],dict[a][0]);
				writer.writerow([a,dict[a][1],dict[a][0]])


	

	def __init__(self):
		self.Num_Keyword=0
		# outfile = sys.argv[3].split("=")[1]
		# self.f=open(outfile,"w+")
		self.dict = {}
		self.row=0;
		self.col=0;
		self.tokenList={}


kklexer = kklex()
kklexer.build()           # Build the lexer



try:
	# configfile = sys.argv[1].split("=")[1]
	filename = sys.argv[1]
	# outfile = sys.argv[2].split("=")[1]

	f = open(filename, 'r')
	data = f.read()
	
	kklexer.test(data)     # Test it
except IndexError:
	print("Usages:python lexer.py tests/input1/some-input")

token_t = kklexer.tokenList



