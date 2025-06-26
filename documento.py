

class Documento:
    """ Modelo de uma classe Documento, que permite armazenar e modificar caracteres
        de texto. A classe poderá ser utilizada em aplicativos de edição de texto.

        Os caracteres são armazenados em lista, permitindo livre edição após serem
        armazenados. A classe Documento terá um cursor para navegar entre os 
        caracteres da lista, além de salvar o nome de arquivo para o documento
        instanciado. """
    def __init__(self):
        self.caracteres = []
        self.cursor = 0
        self.nome = ''

    def inserir(self, caractere):
        ''' Adiciona um novo caractere, fornecido pelo usuário, 
            à lista self.caracteres, movimentando o cursor. '''
        self.caracteres.insert(self.cursor, caractere)
        self.avancar()

    def deletar(self):
        ''' Remove o caractere na posição atual do cursor. '''
        del self.caracteres[self.cursor]

    def apagar(self):
        ''' Apaga o caraactere da posição anterior (backspace). '''
        self.voltar()
        self.deletar()
    
    def salvar(self):
        ''' Salva o arquivo no computador do usuário. '''
        with open(self.filename, 'w') as arquivo:
            arquivo.write(''.join(self.caracteres))

    def avancar(self):
        ''' Avança o cursor uma posição à frente. '''
        self.cursor += 1

    def voltar(self):
        ''' Retorna o cursor uma posição atrás. '''
        self.cursor -= 1
