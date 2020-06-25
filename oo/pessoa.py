class Pessoa:
    #declarar metodo com atributos
    def __init__(self, nome=None, idade = 42):
        #atributo self.nome
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    #mostrar mensagem e id
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    #imprime valor do atributo
    print(p.nome)
    #alterar valor do atributo
    p.nome = 'LucianoNeute'
    print(p.nome)
    print(p.idade)