'''Este programa retorna relatório com a quantidade de funcionários 
do município de Sapé/PB no ano de 2021.

Data criação: 19/07/2021
Versão 1.0.0

Autor: Edson Sales <sales_eds@hotmail.com
'''
import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/data.db')
cur = conn.cursor()


class Relatorio:    
    def geral(self):
        efetivo = []
        comissionado = []
        contratado = []

        resultset = cur.execute("select sum(quantidade) from agentes \
                                 where vinculo='efetivo' group by mes order by mes")
        for i in resultset:
            efetivo.append(i)
            
        resultset = cur.execute("select sum(quantidade) from agentes \
                                 where vinculo='comissionado' group by mes order by mes")
        for i in resultset:
            comissionado.append(i)

        resultset = cur.execute("select sum(quantidade) from agentes \
                                 where vinculo='contrato' group by mes order by mes")
        for i in resultset:
            contratado.append(i)

        print("Quantidade de servidores/2021")
        print("\tJan\tFev\tMar\tAbr\tMai")
        print("Efetivos: ", str(efetivo[0])+'\t'+str(efetivo[1])+'\t'+str(efetivo[2])+'\t'+str(efetivo[3])+'\t'+str(efetivo[4]))
        print('Comissionados: ', comissionado)
        print('Contratados: ', contratado)

