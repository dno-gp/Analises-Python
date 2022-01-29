# main.py - Estrutura de funcionamento do programa Entrevistac.

class Entrevista():
    def __init__(self):
        self.data = []

    def respostas(self):
        print(self.data)

    def perguntas(self):
        sexo = input("Sexo/gênero? ").lower() # Esse bloco deve ser inserido
        idade = input("Qual sua idade? ")     # em um loop.

        flag = input("Salvar resposta? [s/n]").lower()
        if flag == 's':
            self.data.append((sexo, idade))
            print("Respostas salvas com sucesso!")
        elif flag == 'n':
            print("As respostas não foram salvas.")
        else:
            print("Respostas não registradas.")

        


exec = Entrevista()
exec.perguntas()