'''Este programa retorna relatórios com a quantidade de funcionários do
município de Sapé/PB no ano de 2021.

Data criação: 19/07/2021
Versão 0.0.0

Autor: Edson Sales <sales_eds@hotmail.com
'''

##############################################################################

import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/data.db')
cur = conn.cursor()


class Relatorio:    
    def geral(self):
        efetivo = []
        comissionado = []
        contratado = []

        ############################# COLETAR DADOS ##########################
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

        ########################### EXIBIR RESULTADOS ########################
        e1, e2, e3, e4, e5 = efetivo        # Os itens das listas são salvos
        c1, c2, c3, c4, c5 = comissionado   # em variáveis como solução para
        t1, t2, t3, t4, t5 = contratado     # eliminar os colchetes das listas 
                                            # e a quantidade de código na 
                                            # construção dessa exibição

        print(65*"-")
        print(f"{'Quantidade de servidores-Sapé/PB/2021':^65}")
        print(f"{'GERAL':^65}")
        print(65*"-")
        print(f"{'Jan':>19}{'Fev':>9}{'Mar':>8}{'Abr':>8}{'Mai':>8}")
        print(f"{'Efetivos:':>15}", str(e1) + '\t', str(e2) + '\t',
                                    str(e3) + '\t', str(e4) + '\t', 
                                    str(e5) + '\t')

        print(f"{'Comissionados:':>15}", str(c1) + '\t', str(c2) + '\t',
                                         str(c3) + '\t', str(c4) + '\t',
                                         str(c5) + '\t',)

        print(f"{'Contratados:':>15}", str(t1) + '\t', str(t2) + '\t', 
                                        str(t3) + '\t', str(t4) + '\t', 
                                        str(t5) + '\t',)
        print(65*"-")

if __name__=='__main__':
    a = Relatorio()
    a.geral()
