# main.py - Estrutura de funcionamento do programa Entrevistac.
# autor:    Edson Sales<sales_eds@hotmail.com>
#-----------------------------------------------------------------------------
class Entrevista():
    def __init__(self):
        self.data = []

    def perguntas(self):
        continuar = "s"
        while continuar == "s":
            sexo = input("Sexo/gênero? ").lower()
            idade = input("Qual sua idade? ")

            flag = input("Salvar resposta? [s/n]").lower()
            if flag == 's':
                self.data.append((sexo, idade))
                print("Respostas salvas com sucesso!")
            elif flag == 'n':
                print("As respostas não foram salvas.")
            else:
                print("Respostas não registradas.")

            continuar = input('Ir para a próxima entrevista?[s/n]')
            if continuar != "s":
                print("Encerrando entrevista.")

    def respostas(self):
        print(self.data)

    def arquivar(self):
        pass

    def estatistica(self):
        pass
        
if __name__=='__main__':
    exec = Entrevista()
    exec.perguntas()