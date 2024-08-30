class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Nome: {self.nome} | Idade: {self.idade}"
    
    @property
    def printer(self):
       print( f"Nome: {self.nome} | Idade: {self.idade}")

    