#precisamos criar um molde de uma pessoa. -> class
#caracteristicas -> atributos -> variaveis
# ações -> métodos -> funções

# metodo é uma função que esta dentro de uma classe

class Pessoa: 
    # construtor
    def __init__(self, nome, cpf, data_nascimento ):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento 

        #metodo de apresentação

        def apresentar(self) -> str:
            return f"Olá, meu nome é {self.nome}"
        
pessoa1 = Pessoa("Ana Lima", "123")
pessoa2 =  Pessoa("Bruno Costa", "987")

print(pessoa1.apresentar())
print(pessoa2.apresentar())