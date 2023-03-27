'''Code: #01'''
'''Description: Criação de classe com método de inicialização e chamando outro método da classe para exibir um dado que 
foi instanciado na classe.'''

'''bash
Comando para Executar
$ python content/learning_functions/learning_functions.py
'''
'''
Welcome to  Turing
'''
'''
Higor Souza - souzarogih
'''

class Welcome:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Welcome to ', self.name)

cw = Welcome('Turing')
cw.say_hello()




