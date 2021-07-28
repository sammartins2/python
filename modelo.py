class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'nome: {self.nome} - {self.ano} - {self.likes} likes'

class Filme (programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - ano {self.ano} - {self.duracao} minutos - {self._likes} likes'
        
class Serie (programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        pass

    def __str__(self):
        return f'{self._nome} - ano {self.ano} - {self.temporadas} temporadas - {self._likes} likes'
        
class Playlist: 
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme ('vingadores guerra infinita', 2018, 160)
atlanta = Serie ('atlanta', 2018, 2)
todo_mundo_odeia_o_chris = Serie('todo mundo odeia o chris', 2000, 10)
lucas = Filme ('lucas', 2021, 100)

todo_mundo_odeia_o_chris.dar_like()
todo_mundo_odeia_o_chris.dar_like()
lucas.dar_like()
lucas.dar_like()
lucas.dar_like()
vingadores.dar_like()
atlanta.dar_like() 
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, todo_mundo_odeia_o_chris, lucas]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)


print (f'tamanho: {len(playlist_fim_de_semana)}')

print (playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana:
    print(programa)
