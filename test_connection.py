import mysql.connector
from time import sleep


def testar_bd(*args):
    index = 0
    try:
        # sleep(2)
        connection = mysql.connector.connect(host=args[0], database=args[1], user=args[2],
                                             password=args[3], port=args[4])

    except mysql.connector.Error as error:
        if error.errno == 1049:
            index = 1
        elif error.errno == 1045:
            index = 2
        elif error.errno == 2013:
            print(error)
    else:
        connection.close()
    resultados = [True, 'Banco de dados inexistente.', 'Nome do usuário ou password incorreto.']
    return resultados[index]


# retorno = testar_bd('localhost', 'bd_contratos', 'root', '1234', 3306)
# print(retorno)
