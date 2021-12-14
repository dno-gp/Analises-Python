# main.py - Estrutura de funcionamento do programa.

class Entrevista:
    respostas = []
    continuar = "s"

    def salva_resposta(*args):
        respostas.append((*args))


    def perguntas():
        while continuar == "s":
            
            #sexo
            sexo = input("Informe o sexo/gênero: ").lower()
            if sexo != "m":
                print("Resposta inválida.")
                #idade
            idade = input("Informe a idade: ")

                #se interessa por política?
            interesse = input("Se interessa por política?(0-não se interessa,\
                                        1-pouco, 2-se interessa, 3-muito)")

                #votou nas últimas eleições?
            votou = input("Votou nas últimas eleições? ")

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
