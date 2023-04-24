import math

class Circulo():
    
    def __init__(self,raio,diametro):
        self.raio = raio;
        self.diametro = diametro;

    def perimetro(self):
        perimetro = 2*math.pi*self.raio;
        
        return perimetro;

    def area(self):
        area = math.pi*self.raio**2;

        return area;

    def __str__(self):
        return str(f'\n__Dados_do_Círculo__\n\nRaio:{self.raio} Diâmetro:{self.diametro} \nPerímetro: {self.perimetro():.3f}\nÁrea: {self.area():.3f}')
