#arquivo person.py  Learning Python 5th Edition pg 817 - 820

class Pessoa:                               # Inicia uma classe
      
    def __init__(self, nome, job=None, pay=0):     # Método construtor com trẽs argumentos
        self.nome = nome                    # Preencher os campos quando criados
        self.job = job                      # self é a nova instancia(objeto)
        self.pay = pay
    
bob = Pessoa('Bob Smith')
sue = Pessoa('Sue Jones', job='dev', pay=100000)
print(bob.nome, bob.pay)
print(sue.nome, sue.pay)