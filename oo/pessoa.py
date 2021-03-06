class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade = 42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    benjamin = Pessoa(nome='Benjamin')
    luciano = Pessoa(benjamin, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Neute'
    del luciano.idade
    print(luciano.sobrenome)
    print(luciano.__dict__)
    benjamin.sobrenome = 'Neute'
    print(benjamin.sobrenome)
    print(benjamin.__dict__)
    print(luciano.olhos)
    print(benjamin.olhos)
    print(id(luciano.olhos), id(benjamin.olhos))

