class Fotografo:
    
    fotografos = []
    
    def __init__(self, nome, categoria, agenda):
        self.nome = nome
        self.categoria = categoria
        self.agenda  = agenda
        self.ativo = False
        Fotografo.fotografos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.agenda} | {self.ativo}'

    def listar_fotografos():
        for fotografo in Fotografo.fotografos:
            print(f'{fotografo.nome} | {fotografo.categoria} | {fotografo.agenda} | {fotografo.ativo}')

fotografo_Igor = Fotografo('Igor', 'Retratista', 'Seg e Sextas')
fotografo_Sofia = Fotografo('Sofia', 'Fotografia Social', 'Ter e Sab')
fotografo_Natalia = Fotografo('Natalia', 'Street Style', 'Qua e Qui')

Fotografo.listar_fotografos()


