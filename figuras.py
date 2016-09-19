class Figuras:
    def cuadrado(self, lado):
        try:
            lado = float(lado)
            return lado * lado
        except Exception as e:
            return 'dato incorrecto'


    def rectangulo(self,base,altura):
        try:
            base=float(base)
            altura=float(altura)
            return base * altura
        except Exception as e:
            return 'dato incorrecto'

    def triangulo(self,base, altura):
        try:
            base=float(base)
            altura=float(altura)
            resultado = base *altura
            return resultado/2
        except Exception as e:
            return 'dato incorrecto'


    def circulo(self,radio):
        try:
            radio=float(radio)
            pi = 3.1416
            radio = radio * radio

            resultado = pi * radio
            return resultado
        except Exception as e:
            return 'dato incorrecto'
