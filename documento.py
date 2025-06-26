

class Documento:
    """ Modelo de uma classe Documento, que permite armazenar e modificar caracteres
        de texto. A classe poderá ser utilizada em aplicativos de edição de texto.

        Os caracteres são armazenados em lista, permitindo livre edição após serem
        armazenados. A classe Documento terá um cursor para navegar entre os 
        caracteres da lista, além de salvar o nome de arquivo para o documento
        instanciado. """
    def __init__(self):
        self.caracteres = []
        self.cursor = Cursor(self)
        self.nome = ''

    def inserir(self, caractere):
        ''' Adiciona um novo caractere, fornecido pelo usuário, 
            à lista self.caracteres, movimentando o cursor. '''
        self.caracteres.insert(self.cursor.posicao, caractere)
        self.cursor.avancar()

    def deletar(self):
        ''' Remove o caractere na posição atual do cursor. '''
        del self.caracteres[self.cursor.posicao]

    def apagar(self):
        ''' Apaga o caractere da posição anterior (backspace). '''
        self.cursor.voltar()
        self.deletar()
    
    def salvar(self):
        ''' Salva o arquivo no computador do usuário. '''
        with open(self.filename, 'w') as arquivo:
            arquivo.write(''.join(self.caracteres))


class Cursor:
    ''' Modela o cursor do Documento, acrescentando métodos para avançar ou
        recuar, bem como permitindo retornar ao início do documento (Home) e
        avnçar ao final dele (End).'''
    def __init__(self, documento):
        self.documento = documento
        self.posicao = 0

    def avancar(self):
        ''' Move-se uma posição à frente. '''
        self.posicao += 1

    def voltar(self):
        ''' Recua uma posição. '''
        self.posicao -= 1

    def home(self):
        ''' Retorna diretamente ao início da linha. '''
        while self.documento.caracteres[self.posicao] != '\n':
            self.posicao -= 1
            if self.posicao == 0: # Chegou ao início do documento
                break

    def end(self):
        ''' Avança diretamente ao final da linha. '''
        while self.posicao < len(self.documento.caracteres) and self.documento.caracteres[
            self.posicao] != '\n':
            self.posicao += 1

