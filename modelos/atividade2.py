class Carro:
    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
    def __str__(self):
        return f'{self.modelo}|{self.cor}|{self.ano}'
    
carro1=Carro('Audi A3','Preto','2023')
print(carro1)

#atividade 2
class Restaurante:
    nome=''
    categoria=''
    chef=''
    avaliação=''
    ativo=False

restaurante_DOM=Restaurante()
restaurante_DOM.nome='D.O.M'
restaurante_DOM.categoria='Gourmet'
restaurante_DOM.chef='Cédric'
restaurante_DOM.avaliação='3 estrelas Michelin'
print(vars(restaurante_DOM))

#atividade 3
class Restaurante:
    def __init__(self,nome,categoria,chef,avaliação):
        self.nome=nome
        self.categoria=categoria
        self.chef=chef
        self.avaliação=avaliação
        self.ativo=False
#atividade 4
    def __str__(self):
        return f'{self.nome}|{self.categoria}|{self.chef}|{self.avaliação}|{self.ativo}'
#atividade 3
restaurante_DOM=Restaurante('D.O.M','Gourmet',' Cédric','3 estrelas Michelin')
#atividade 4
print(restaurante_DOM)

#atividade 5
class Cliente:
    def __init__(self,nome,idade,CPF):
        self.nome=nome
        self.idade=idade
        self.CPF=CPF
        self.estado='PR'
    
    def __str__(self):
        return f'{self.nome}|{self.idade}|{self.CPF}|{self.estado}'
cliente1=Cliente('Luiz',32, '129.697.625-47')

print(cliente1)