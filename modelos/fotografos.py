from modelos.eventos import Eventos

class Fotografo:
    
    fotografos = []
    
    def __init__(self, nome, categoria, agenda):
        self._nome = nome.upper()
        self._categoria = categoria
        self.agenda  = agenda 
        self._ativo = False
        self._eventos = []
        Fotografo.fotografos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.agenda} | {self.ativo}'
    
    @classmethod
    def listar_fotografos(cls):

        print('𝓕𝓸𝓽𝓸́𝓰𝓻𝓪𝓯𝓸𝓼')
        print('')
        print(f'{"Nome dos fotógrafos".ljust(20)} | {"Categoria".ljust(20)} | {"Agenda".ljust(20)} | {"Ativo"} | {"Eventos em %"}')
        print('‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒')

        for fotografo in cls.fotografos:
            print(f'{fotografo._nome.ljust(20)} | {fotografo._categoria.ljust(20)} | {fotografo.agenda.ljust(20)} | {fotografo.ativo} | {fotografo.media_precos}')
            print('‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒')


    @property
    def ativo(self):
        return '⋆ Ativo(a)' if self._ativo else '≛ Não ativo(a)'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_eventos(self, comemoracoes, precos, entrega):
        eventos = Eventos(comemoracoes, precos, entrega)
        self._eventos.append(eventos)

    @property
    def media_precos(self):
        if not self._eventos:
            return 0
        soma_dos_precos = sum(eventos._precos for eventos in self._eventos)
        quantidade_comemoracoes = len(self._eventos)
        media = round(soma_dos_precos/quantidade_comemoracoes, 1)
        return media
        



