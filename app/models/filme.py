class Filme:
    def __init__(self, nome, genero, lancamento):
        self.nome=nome
        self.genero=genero
        self.lancamento=lancamento

filme1 = Filme('Harry Pottere a Ordem da Fenix', 'Fantasia', '2010')
filme2 = Filme('Piratas do Caribe no Fim do Mundo', 'Aventura', '2014')
filme3 = Filme('Os Vingadores Ultimato', 'Luta', '2016')
filme4 = Filme('Batman o cavaleiro das trevas', 'Aventura', '2011')
filme5 = Filme('Jogos Mortais 7', 'Terror', '2009')
lista = [filme1, filme2, filme3, filme4, filme5]