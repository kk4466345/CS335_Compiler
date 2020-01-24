import ply.lex as lex



class lexer(object):
	keywords = {'abstract' , 'assert' , 'boolean' , 'break' , 'byte' , 'case' ,
	'catch' , 'char' , 'class' , 'const' , 'continue' , 'default' , 'do' , 'double' , 'else' ,
	'enum' , 'exports' , 'extends' , 'final' , 'finally' , 'float' , 'for' , 'goto' , 'if' , 'implements' ,
	'import' , 'instanceof' , 'int' , 'interface' , 'long' , 'module' , 'native' . 'new' , 'open' , 
	'package' , 'private' , 'protected' , 'provides' , 'public' , 'requires' , 'return' , 'short' ,
	'static' , 'strictfp' , 'super' , 'switch' , 'synchronized' , 'this' , 'throw' , 'throws' , 'to' ,
	'transient' , 'transitive' , 'try' , 'uses' , 'void' , 'volatile' , 'while' , 'with' }

	# operator_arthmatic={ 'multiplication' , 'division' , 'modulo' , 'addition' , 'subtraction'}
	# operator_unary = { 'u_minus' , 'u_plus' , 'preincrement' , 'postincrement' , 'postdecrement' , 'logicalnot'}
	# operator_relational = {'equal' , 'equala_equal' ,'notequal','lessthen','graterthen','lessthenorequal' ,'graterthenorequal' }
	# operator_logical = {'logicaland' , 'logicalor'}
	# operator_bitwise = {'bitwiseand','bitwieor' , 'bitwiseor' , 'bitwisexor' , 'bitwisecomplement'}
	# operator_shift = {'leftshift' , 'rightshiftsigned' , 'rightshiftunsign'}

	operator = {'addition','subtraction', 'division','multiplication','modulo', 
	'plusplus', 'minusminus','not' ,
	'equal' , 'plusequal','minusequal', 'multequal' , 'divequal' ,'divequal' ,'modequal' ,  'powequal'
	'equalequal' , 'notequal' , 'less' , 'greater' , 'lessequal' , 'greaterequal' ,
	'andand','oror',
	'and' , 'or' , 'xor' , 'bitwisenot' ,
	'leftshift' , 'rightshiftsigned' , 'rightshiftunsigned' ,
	'Lbrack' , 'Rbrack' , 'Lpara' , 'Rpara' , 'Lbrace' , 'Rbrace' ,'comma' ,'semi-colon' , 'asterisk' }

	literals={'integer' , 'float' , 'charactor' , 'string' , 'boolean','short' , 'long' , 'double' ,'byte'}

	identity = {'IDENTIFIER'}

	tokens=list(operator) + list(literals) + list(identity) + list(keywords)



	# token assignment




	t_ignore_COMMENT = r'(/\*([^*]|\n|(\*+([^*/]|\n])))*\*+/)|(//.*)'
	t_ignore = ' \t'

	t_addition =r'\+'
	t_subtraction=r'-'
	t_division=r'/'
	t_multiplication=r'\*'
	t_modulo=r'%'
#uniry
	t_plusplus=r'\+\+'
	t_minusminus=r'--'
	t_not=r'!'




	#assignment
	t_equal=r'='
	t_plusequal=r'\+='
	t_minusequal=r'-='
	t_multequal=r'\*='
	t_divequal=r'/='
	t_divequal=r'%='

	# assignm me a value
	t_powequal=r'^='



	# next
	t_equalequal=r'=='
	t_notequal=r'!='
	t_less=r'<'
	t_greater=r'>'
	t_greaterequal=r'>='
	t_lessequal=r'<='


	#logical
	t_andand=r'&&'
	t_oror=r'\|\|'

	# bitwise

	t_and=r'&'
	t_or=r'\|'
	t_xor=r'^'
	t_bitwisenot=r'~'

	# shift

	t_leftshift=r'<<'
	t_rightshiftsigned=r'>>'
	t_rightshiftunsigned=r'>>>'

	# brackets

	t_Lbras=r'\{'
	t_Rbrac=r'\}'
	t_Lpara=r'\('
	t_Rpara=r'\)'
	t_Lbrack=r'\['
	t_Rbrack=r'\]'

	t_comma=r','
	t_semi-colon=r';'
	# t_dot=r'\.'



	# Operator	Examples
	# Arithmetic	+ , – , / , * , %
	# Unary	++ , – – , !
	# Assignment	= , += , -= , *= , /= , %= , ^=
	# Relational	==, != , < , >, <= , >=
	# Logical	&& , || 
	# Ternary	(Condition) ? (Statement1) : (Statement2);
	# Bitwise	& , | , ^ , ~
	# Shift	<< , >> , >>>
		
