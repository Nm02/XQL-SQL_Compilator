import ply.yacc as yacc
from lex import tokens, lexer

# Variables de salida (para traducción, etc.)
resultados = []

# Reglas de producción de la gramática (completaremos una por una después)
def p_S(p):
    'S : INICIO_PROGRAMA A FIN_PROGRAMA'
    p[0] = "\n".join(resultados)

#A
def p_A_seleccion(p):
    'A : SELECCION ID B ORIGEN ID C FIN_LINEA A'
    # p[2] = primer campo, p[3] = string con los campos restantes (ej: ', campo2, campo3')
    # p[5] = nombre de la tabla
    # p[6] = string con condiciones (ej: ' WHERE campo = valor AND ...') o ''
    campos = p[2] + (p[3] if p[3] else '')
    tabla = p[5]
    condiciones = p[6] if p[6] else ''
    resultados.append(f"SELECT {campos} FROM {tabla}{condiciones};")

def p_A_crear(p):
    'A : CREAR TABLA ID WITH ABRIR_PARENTESIS F CERRAR_PARENTESIS FIN_LINEA A'
    # p[3] = nombre de la tabla
    # p[6] = string con definición de campos (ej: 'campo1 tipo1, campo2 tipo2, ...')
    resultados.append(f"CREATE TABLE {p[3]} ({p[6]});")

def p_A_actualizar(p):
    'A : ACTUALIZAR ID CAMPOS ID Tk_TO E VERIFICACION ID OPERACION_LOGICA E H FIN_LINEA A'
    # p[2] = tabla
    # p[4] = primer campo a modificar, p[6] = nuevo valor, p[11] = otros campos a modificar (string tipo ', campo2 = valor2 ...')
    # p[8] = campo condición, p[9] = operador, p[10] = valor condición
    set_clause = f"{p[4]} = {p[6]}"
    if p[11]:
        set_clause += p[11]  # H devuelve string tipo ', campo2 = valor2 ...' o ''
    where_clause = f"{p[8]} {p[9]} {p[10]}"
    resultados.append(f"UPDATE {p[2]} SET {set_clause} WHERE {where_clause};")

def p_A_eliminar(p):
    'A : ELIMINAR TABLA ID FIN_LINEA A'
    # p[3] = nombre de la tabla
    resultados.append(f"DROP TABLE {p[3]};")

def p_A_comentario(p):
    'A : COMENTARIO A'
    pass

def p_A_vacio(p):
    'A : '
    pass

#B
def p_B_lista(p):
    'B : COMA ID B'
    # p[2] = nombre del campo, p[3] = resto de campos (string)
    if p[3]:
        p[0] = f", {p[2]}{p[3]}"
    else:
        p[0] = f", {p[2]}"

def p_B_vacio(p):
    'B : '
    # Caso base: no hay más campos
    p[0] = ''

# C
def p_C_filtrado(p):
    'C : INICIO_FILTRADO ID OPERACION_LOGICA E D FIN_FILTRADO'
    # p[2]: campo, p[3]: operador, p[4]: valor, p[5]: condiciones adicionales (string de D)
    condiciones = f" WHERE {p[2]} {p[3]} {p[4]}"
    if p[5]:
        condiciones += p[5]  # D devuelve el string para condiciones extra, tipo ' AND campo2 op valor2'
    p[0] = condiciones

def p_C_vacio(p):
    'C : '
    p[0] = ''

#D
def p_D_and(p):
    'D : COMA ID OPERACION_LOGICA E D'
    # p[2]: campo, p[3]: operador, p[4]: valor, p[5]: más condiciones (string)
    # Siempre anteponemos ' AND ' para las condiciones adicionales
    resto = p[5] if p[5] else ''
    p[0] = f" AND {p[2]} {p[3]} {p[4]}{resto}"

def p_D_vacio(p):
    'D : '
    # Caso base: no hay más condiciones
    p[0] = ''

#E
def p_E_numero(p):
    'E : NUMERO_ENTERO'
    p[0] = str(p[1])  # El valor del número

def p_E_cadena(p):
    'E : CADENA_TEXTO'
    # Si p[1] ya tiene las comillas, devolvé tal cual
    # Si lo limpiaste en el lexer (sin comillas), agregá aquí:
    p[0] = f"'{p[1]}'"

#F
def p_F(p):
    'F : ID SEPARADOR tipo_dato G'
    # p[1]: nombre del campo, p[3]: tipo de dato (ej: STRING, NUMBER...), p[4]: más campos (G)
    campos = f"{p[1]} {p[3]}"
    if p[4]:
        campos += p[4]  # G devuelve string tipo ', campo2 tipo2 ...'
    p[0] = campos

#G
def p_G_vacio(p):
    'G : '
    # Caso base: no hay más campos
    p[0] = ''

def p_G_campo(p):
    'G : COMA ID SEPARADOR tipo_dato G'
    # p[2]: nombre del campo, p[4]: tipo de dato, p[5]: resto de campos (G)
    resto = p[5] if p[5] else ''
    p[0] = f", {p[2]} {p[4]}{resto}"

#H
def p_H_mas(p):
    'H : ID Tk_TO E VERIFICACION ID OPERACION_LOGICA E H'
    # p[1]: campo a modificar, p[3]: nuevo valor, p[4]: VERIFICACION (siempre 'IF'), p[5]: campo condición, p[6]: operador, p[7]: valor condición, p[8]: más modificaciones
    # Pero según tu gramática, cada H solo agrega SET adicional
    resto = p[8] if p[8] else ''
    p[0] = f", {p[1]} = {p[3]}{resto}"

def p_H_vacio(p):
    'H : '
    p[0] = ''

#aux
def p_tipo_dato(p):
    '''tipo_dato : TEXTO
                 | NUMERO
                 | FECHA_HORA
    '''
    if p[1].upper() == 'STRING':
        p[0] = 'VARCHAR'
    elif p[1].upper() == 'NUMBER':
        p[0] = 'INT'
    elif p[1].upper() == 'TIMEDATE':
        p[0] = 'DATETIME'
    else:
        p[0] = p[1]



# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en la línea {p.lineno}: '{p.value}'")
    else:
        print("Error de sintaxis: fin inesperado del archivo")



# Construir el parser
parser = yacc.yacc()



# Ejemplo de uso
if __name__ == "__main__":
    # Test básico: podés leer de un archivo, de consola, etc.
    data = '''
    INICIO 
    /* Aca comienza el programa ejemplo 
    DESIGN TABLE catalogo WITH (producto-STRING, precio - NUMBER). 
    SELECT producto, codigo FROM catalogo WHERE precio > 50 APPLIES. 
    /* otro comentario 
    MODIFY catalogo FIELD precio TO 45 IF producto = 'Smartphone'. 
    DROP TABLE catalogo. 
    FIN 
    '''
    parser.parse(data)