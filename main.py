from pessoa import Pessoa

pessoa = Pessoa('vitor', 20)
pessoa.guardar()
print(pessoa.buscar())
pessoa.idade = 21
pessoa.atualizar()
print(pessoa.buscar())
