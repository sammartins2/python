
class Data:

    def __init__(self, dia, mes, ano) -> None:
         print ("Construindo objeto ...{}".format(self))
         self.dia = dia
         self.mes = mes
         self.ano = ano

    def formato(self):
        print(f'{self.dia}/{self.mes:}/{self.ano}')