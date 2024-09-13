class Fotografo:
    
    fotografos = []
    
    def __init__(self, nome, categoria, agenda):
        self.nome = nome
        self.categoria = categoria
        self.agenda  = agenda
        self._ativo = False
        Fotografo.fotografos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.agenda} | {self.ativo}'

    def listar_fotografos():

        print('𝓕𝓸𝓽𝓸́𝓰𝓻𝓪𝓯𝓸𝓼')
        print('')
        print(f'{"Nome dos fotógrafos".ljust(20)} | {"Categoria".ljust(20)} | {"Agenda".ljust(20)} | {"Ativo"}')
        print('‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒')

        for fotografo in Fotografo.fotografos:
            print(f'{fotografo.nome.ljust(20)} | {fotografo.categoria.ljust(20)} | {fotografo.agenda.ljust(20)} | {fotografo.ativo}')
            print('‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒')


    @property
    def ativo(self):
        return '⋆ Ativo(a)' if self._ativo else '≛ Não ativo(a)'

fotografo_Igor = Fotografo('Igor', 'Retratista', 'Seg e Sextas')
fotografo_Sofia = Fotografo('Sofia', 'Fotografia Social', 'Ter e Sab')
fotografo_Natalia = Fotografo('Natalia', 'Street Style', 'Qua e Qui')

Fotografo.listar_fotografos()


