class Fotografo:
    def __init__(self, nome, categoria, agenda, ativo):
        self.nome = nome
        self.categoria = categoria
        self.agenda  = agenda
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.agenda} | {self.ativo}'

fotografo_Igor = Fotografo('Igor', 'Retratista', 'Seg e Sextas')
fotografo_Sofia = Fotografo('Sofia', 'Fotografia Social', 'Ter e Sab')
fotografo_Natalia = Fotografo('Natalia', 'Street Style', 'Qua e Qui')

fotografos = [fotografo_Igor, fotografo_Sofia, fotografo_Natalia]

print(fotografo_Natalia)

