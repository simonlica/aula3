#criando uma classe usando decoreitor @property
class Restaurante:
    restaurantes=[]
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self._ativo=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'
    
    @classmethod
    def listar_restaurantres(cls):

        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}| {restaurante.categoria} | {restaurante.ativo}')


    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐' 
    
    def _alternar_estado(self):
        self._ativo =not self._ativo




restaurante_praca=Restaurante('Praça','Gourmet')
restaurante_pizza=Restaurante('Baeti','mexicana')
# restaurante_praca.nome='Bistro'
# restaurante_praca.categoria='Italiana'

# restaurante_pizza=Restaurante()

# restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))
Restaurante.listar_restaurantres()