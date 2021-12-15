# main.py - Estrutura de funcionamento do programa Entrevistac.

class Entrevista(object):
    global respostas; respostas = []

    def salva_resposta(tuple):
        respostas.append((tuple))

    def perguntas():
        continuar = 's'

        print(f"{10*'#'} Questionário iniciado! {10* '#'}\n")
        while continuar == 's':
            
        #Questão gênero
            sexo = input("Informe o sexo/gênero: ").lower()
            if sexo not in ('m', 'f', 'o'):
                print("Resposta inválida. Tente Novamente.")
                Entrevista.perguntas()

        #Questão idade
            try:
                idade = int(input('Informe a idade: '))
                if idade not in range(16,100):
                    print('Idade fora do intervalo do público alvo. Dirija-se\
 para a próxima entrevista.')
                    break
            except:
                print('Resposta inválida.')

         #Questão interesse por política
            interesse = input("Se interessa por política?(0-não se interessa,\
1-pouco, 2-se interessa, 3-muito)")
            if interesse not in (0, 1, 2, 3):
                print('Resposta fora de intervalo.')

        #Questão comparecimento
            votou = input("Votou nas últimas eleições? ")
            if votou not in ('s', 'n', 'o'):
                print('Resposta inválida.')

            continuar = input("Continuar?(Digite 'S' para prosseguir ou \
qualquer tecla para sair.)").lower()



"""  try:
        salva_resposta((sexo, idade, interesse, votou))
        print("Repostas registradas com sucesso!")
    except:
        print("As respostas não foram registradas")

    continuar = input("Continuar? s-sim. ")
    

print(respostas)
print(f"Total de entrevistados: {len(respostas)}")"""
#Armazenar respostas em uma lista
#Armazer lista em arquivo
#Estatistica
if __name__=="__main__":
    Entrevista.perguntas()
