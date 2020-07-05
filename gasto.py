import pymysql
import numpy as np
import matplotlib.pyplot as plt

#Conexão com o banco de dados
try:
    link = pymysql.connect(host="localhost", user="root", password="", db="")

except:
    print("Conexão com banco de dados não estabelecida.")


try:
    with link.cursor() as c:
        sql = "SELECT SUM(gastoR$) FROM servidores WHERE municipio = %s \
               AND unor = %s AND ano = %s GROUP BY mes"
	
        c.execute(sql, (1,'pm',2013))
        x = c.fetchall()
        mes = np.arange(len(x))

	#Montando um gráfico simples de linha
        plt.plot(mes,x, label = "Gasto com pessoal")
        plt.xlabel("Tempo(meses)")
        plt.ylabel("R$")
        plt.legend()
        plt.title("Gasto mensal com pessoal no ano de 2013 - P.M. Cruz do Espírito Santo-PB")
        plt.show()
except:
        print("Erro na execução da consulta")
	
finally:
    link.close() #Encerrando a conexão com o banco de dados
