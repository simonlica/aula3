# questão 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e trabalha como {self.profissao}."

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
            return f'A profissão de: {self.nome} é {self.profissao}'

pessoa1=Pessoa('Fábio',42,'vendedor')
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)

#questão2 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Titular: {self._titular}, Saldo: {self._saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True
        return conta.ativo

    @property
    def titular(self):
        return self._titular

#questão3
class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, cpf, endereco):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

    @classmethod
    def conta(cls):
        return "Método de classe para a conta do ClienteBanco"


# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("João", 30, "Engenheiro")
print(pessoa1)
pessoa1.aniversario()
print(pessoa1.saudacao)

# Criando instâncias da classe ContaBancaria
conta1 = ContaBancaria("Fulano", 1000)
conta2 = ContaBancaria("Ciclano", 2000)
print(conta1)
print(conta2)
ContaBancaria.ativar_conta(conta1)
print(conta1.ativo)

# Acessando a propriedade titular
print(conta1.titular)

# Criando instâncias da classe ClienteBanco
cliente1 = ClienteBanco("Maria", "Silva", 25, "123.456.789-00", "Rua A")
cliente2 = ClienteBanco("Pedro", "Santos", 35, "987.654.321-00", "Rua B")
cliente3 = ClienteBanco("Ana", "Souza", 40, "111.222.333-44", "Rua C")

# Chamando o método de classe para a conta ClienteBanco
print(ClienteBanco.conta())
