from modelos.fotografos import Fotografo

fotografo_Igor = Fotografo('Igor', 'Retratista', 'Seg e Sextas')
fotografo_Sofia = Fotografo('Sofia', 'Fotografia Social', 'Ter e Sab')
fotografo_Natalia = Fotografo('Natália', 'Street Style', 'Qua e Qui')
fotografo_Caroline = Fotografo('Caroline', 'Publicidade', 'Seg a Sex' )

fotografo_Sofia.alterar_estado()
fotografo_Igor.receber_eventos('Exposições', 1, 'maio')
fotografo_Natalia.receber_eventos('Formaturas', 4, 'abril' )
fotografo_Caroline.receber_eventos('Books', 5, 'junho')


def main():
    Fotografo.listar_fotografos()
    
if __name__ == '__main__':
    main()