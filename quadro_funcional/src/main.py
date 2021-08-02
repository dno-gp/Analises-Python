'''Este programa retorna relatórios com a quantidade de funcionários 
do município de Sapé/PB no ano de 2021.

Data criação: 19/07/2021
Versão 0.0.0

Autor: Edson Sales <sales_eds@hotmail.com
'''

#  vscode://vscode.github-authentication/did-authenticate?windowid=1&
# code=95d3002bb2010ab78402&state=3ef527cb-07a1-4032-8c36-07c2e795cf95 

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
            efetivo.append(i[0])
            
        resultset = cur.execute("select sum(quantidade) from agentes \
                                 where vinculo='comissionado' group by mes order by mes")
        for i in resultset:
            comissionado.append(i[0])

        resultset = cur.execute("select sum(quantidade) from agentes \
                                 where vinculo='contrato' group by mes order by mes")
        for i in resultset:
            contratado.append(i[0])

        # Exibindo os resultados:
        print(65*"-")
        print(f"{'Quantidade de servidores-Sapé/PB/2021':^65}")
        print(65*"-")
        print(f"{'Jan':>19}{'Fev':>9}{'Mar':>8}{'Abr':>8}{'Mai':>8}")
        print(f"{'Efetivos:':>15}", str(efetivo[0]) + '\t', str(efetivo[1]) + '\t', str(efetivo[2]) + '\t', str(efetivo[3]) + '\t', 
                                    str(efetivo[4]) + '\t')

        print(f"{'Comissionados:':>15}", str(comissionado[0]) + '\t', str(comissionado[1]) + '\t', str(comissionado[2]) + '\t', 
                                         str(comissionado[3]) + '\t', str(comissionado[4]) + '\t',)

        print(f"{'Contratados:':>15}", str(contratado[0]) + '\t', str(contratado[1]) + '\t', str(contratado[2]) + '\t', str(contratado[3]) + '\t', 
                                       str(contratado[4]) + '\t',)
        print(65*"-")

if __name__=='__main__':
    a = Relatorio()
    a.geral()

