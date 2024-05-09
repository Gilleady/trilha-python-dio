# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "C:/Users/gille/Downloads/Bootcamp_Python/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt", "r"
)

# NOTE: Testar um por vez. Comentar os demais (inclusive o loop while) para testar.
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())

# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()

""" 
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line
        else:
            self.file.close()
            raise StopIteration

            
# Uso do FileIterator
for line in FileIterator('C:/Users/gille/Downloads/Bootcamp_Python/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt'):
    print(line)
"""