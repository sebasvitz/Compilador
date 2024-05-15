#
#
# COMPILADOR
#
#


P_reservada = {

    'numero' : 'NUMERO' ,
    'imprimir' : 'IMPRIMIR',
    'mientras' : 'MIENTRAS',
    'if' : 'IF',
    'else' : 'ELSE' }


tokens = (
    'REVALUAR',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'ENTERO',
    'PTCOMA'
    
)

#TOKENS
t_REVALUAR = r'Evaluar'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIR = r'/'
t_PTCOMA = r';'

def t_DECIMAL(t):
    r'\d+\. \d+'
    try:
        t.value = float(r.value)
    except ValueError:
        print('Float Value Too large %d', t.value) 
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Integer vaie too large %d', t.value)
        t.value = 0
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1: -1] # remuevo las con
    return t

# Caracteres ignorados
t_ignore = "\t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Iligal charater '%d'" % t.value[]) #2
    t.lexer.skip(1)

# Construimos el analisador lexico
import ply.lex as lex   
lexer = lex.lex()


#Asociacion de operadores
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS',),
    )

# definicion de la gramatica 

def p_instrucciones_lista(t):  #3
    '''instrucciones    : instruccion instruc... 
                          instruccion'''

def p_instrucciones_evaluar(t):
    'instruccion : REVALUAR CORIZQ expresion'
    print('El valor de la expresion es ' + s) #4

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                    | expresion menos expresion
                    | expresion POR expresion
                    | expresion DIVIDIDO expresion'''
if t[2] == '+' : t[0] = t[1] + t[3]
elif t[2] == '-' : t[0] = t[1] - t[3]
elif t[2] == '*' : t[0] = t[1] * t[3]
elif t[2] == '/' : t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER '
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | DECIMAL'''
    t[0] = t[1]

def p_error(t):
    print("error sintactico en '%s'" % t.value)





import piy.yacc as yacc
parser = yacc.yacc()\


f = open(" ./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)

