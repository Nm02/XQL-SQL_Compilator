import ply.lex as lex

errores_lexicos = []

# Diccionario de palabras reservadas
reserved = {
    'inicio': 'INICIO_PROGRAMA',
    'fin': 'FIN_PROGRAMA',
    'number': 'NUMERO',
    'string': 'TEXTO',
    'timedate': 'FECHA_HORA',
    'select': 'SELECCION',
    'from': 'ORIGEN',
    'where': 'INICIO_FILTRADO',
    'applies': 'FIN_FILTRADO',
    'design': 'CREAR',
    'drop': 'ELIMINAR',
    'table': 'TABLA',
    'with': 'WITH',
    'modify': 'ACTUALIZAR',
    'field': 'CAMPOS',
    'to': 'Tk_TO',
    'if': 'VERIFICACION',
}

# Lista de tokens
tokens = [
    'FIN_LINEA',
    'COMENTARIO',
    'ABRIR_PARENTESIS',
    'CERRAR_PARENTESIS',
    'COMA',
    'OPERACION_LOGICA',
    'ID',
    'NUMERO_ENTERO',
    'CADENA_TEXTO',
    'PUNTO_COMA',
    'SEPARADOR',
] + list(reserved.values())

# Tokens simples (variables)
t_FIN_LINEA        = r'\.'
t_ABRIR_PARENTESIS = r'\('
t_CERRAR_PARENTESIS = r'\)'
t_COMA             = r','
t_OPERACION_LOGICA = r'(>=|<=|=|<|>)'
t_PUNTO_COMA       = r';'
t_SEPARADOR        = r'-'


# Comentario (ignora)
def t_COMENTARIO(t):
    r'/\*([A-Za-z0-9!\"#\$%&\'\(\)\*\+\,\-\./:;<=>\?@\[\]\\\^_`\{\|\}~ ]*)'
    pass

# Números enteros
def t_NUMERO_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Cadenas de texto (comillas simples o dobles)
def t_CADENA_TEXTO(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

# Identificadores y palabras reservadas
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t\r'


# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico en la línea {t.lineno}: caracter inesperado '{t.value[0]}'")
    errores_lexicos.append(f"Error léxico en la línea {t.lineno}: caracter inesperado '{t.value[0]}'")
    t.lexer.skip(1)




# Construir el lexer
lexer = lex.lex()

# Prueba básica
if __name__ == "__main__":
    data = '''
    INICIO
    /* Create a table for orders
    DESIGN TABLE orders WITH (order_id-NUMBER, customer-STRING, total-NUMBER, created_at-TIMEDATE).
    /* Select high value orders
    SELECT order_id, customer FROM orders WHERE created_at > '2024-01-01' APPLIES.
    /* Set all orders before 2023 as archived
    MODIFY orders FIELD customer TO 'archived' IF created_at < '2023-01-01'.
    /* Remove old table
    DROP TABLE old_orders.
    FIN
    '''

    lexer.input(data)
    for token in lexer:
        print(token)




