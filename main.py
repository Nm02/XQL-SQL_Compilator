from yacc import parser

def main():
    # Solicitar el archivo de entrada
    input_file = input("Ingrese el nombre del archivo XQL a traducir: ")
    try:
        with open(rf"test_files\{input_file}", "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"ERROR: No se pudo encontrar el archivo '{input_file}'.")
        return

    # Traducir el código XQL a SQL
    print("Traduciendo...")
    codigo_sql = parser.parse(data)

    # Crear el nombre del archivo de salida
    if "." in input_file:
        output_file = input_file.rsplit(".", 1)[0] + ".sql"
    else:
        output_file = input_file + ".sql"

    # Guardar el resultado en el archivo de salida
    with open(rf"output_files\{output_file}", "w", encoding="utf-8") as f:
        f.write(codigo_sql)
        
    print(f"¡Traducción completa! El archivo SQL se guardó como '{output_file}'.")

if __name__ == "__main__":
    main()
