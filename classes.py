import random

class JogoForca:
    def __init__(self):
        self.__letras_certas = []
        self.__letras_erradas = []
        self.__jogadas = 6
        self.__palavra_secreta = ["Computador", "Processador", "desempenho"]

    def escolherPalavra(self):
        palavra_secreta = random.choice(self.__palavra_secreta)
        return palavra_secreta

    def mostrarPalavra(self):
        palavra = self.escolherPalavra()
        palavra_mostrada = []

        for letra in palavra:
            if letra.lower() in self.__letras_certas:
                palavra_mostrada.append(letra)
            else:
                palavra_mostrada.append("_")
        
        return " ".join(palavra_mostrada)
    
    