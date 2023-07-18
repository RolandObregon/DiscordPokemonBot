activo = True
# variable para activar o desactivar el spawn de pokemon
import pymysql
host = ''  # Nombre de host de la base de datos
user = ''  # Nombre de usuario de la base de datos
password = ''  # Contraseña de la base de datos
database = ''  # Nombre de la base de datos

# Establecer conexión a la base de datos
connection = pymysql.connect(host=host, user=user, password=password, database=database)
def spawneo():
    if activo == True:
        try:
            with connection.cursor() as cursor:
                sql = "SELECT id, nombre, rareza FROM pokemon ORDER BY RAND() * rareza LIMIT 1"
                cursor.execute(sql)
                pokemon_spawned = cursor.fetchone()
                return pokemon_spawned
        except pymysql.Error as e:
            # Manejo de errores
            print(f'Ocurrió un error durante la consulta: {e}')


def pokdx(user_id):
    try:
        cursor = connection.cursor()
        sql_select = "select cantidades from inventario where user_id = "+ str(user_id)
        cursor.execute(sql_select)
        if cursor.fetchone():
            cursor.execute(sql_select)
            pkd = cursor.fetchone()[0]
            pkd = pkd.strip("[]")

            pkdf = []
            pkdlista = eval(pkd)
            for i, valor in enumerate(pkdlista):
                # Obtener el nombre del Pokémon según su ID de la base de datos de los Pokémon
                sql_pokemon = "SELECT nombre FROM pokemon WHERE id = %s"
                cursor.execute(sql_pokemon, (i + 1,))
                result = cursor.fetchone()
                pokemon_nombre = result[0]
                check = "❌"
                if valor > 0:
                    check = "✅"
                pkdf.append(check + pokemon_nombre)
            return pkdf
        else:
            return ""

    except pymysql.Error as e:
    # Manejo de errores
        print(f'Ocurrió un error durante la consulta: {e}')



nul = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# aqui una lista de 151 ceros, use un programa
# no la cree con un for porque me dolia la cabeza
nul = str(nul).strip("[]")
nul = nul.replace(" ", "")
def reset(user_id):
    try:
        with connection.cursor() as cursor:
            sqlupd = ("UPDATE inventario SET cantidades = %s WHERE user_id = " + str(user_id))
            cursor.execute(sqlupd, str(nul))
            connection.commit()
            # limpia la pokedex sin dejarla en nul, para luego poder escribir en ella con registercatch
    except pymysql.Error as e:
            print(f"Ocurrió un error durante la operación con la base de datos: {e}")





def registercatch(user_id, pokemon_id):
    try:
        cursor = connection.cursor()

        sql_select = "SELECT cantidades FROM inventario WHERE user_id = "+ str(user_id)
        cursor.execute(sql_select)
        if cursor.fetchone():
            cursor.execute(sql_select)
            inv = cursor.fetchone()[0]
            inv = inv.strip("[]")
            lis_cantidades = list(map(int, inv.split(',')))
            lis_cantidades[pokemon_id - 1] += 1

            cantidades_actualizadas = ','.join(map(str, lis_cantidades))
            consulta_update = "UPDATE inventario SET cantidades = %s WHERE user_id = " + str(user_id)
            cursor.execute(consulta_update, str(cantidades_actualizadas))
            connection.commit()
            return "Cantidad actualizada exitosamente."
        else:
            # aqui se crea un usuario si no existe uno ya
            sql_insert = "INSERT INTO inventario (user_id, cantidades) VALUES (%s, %s)"
            cursor.execute(sql_insert, (user_id, nul))
            connection.commit()
            registercatch(user_id, pokemon_id)
    except pymysql.Error as e:
        print(f"Ocurrió un error durante la operación con la base de datos: {e}")







