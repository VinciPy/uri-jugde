from decimal import Decimal
class Circle:
    n = 3.14159
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        area = self.n * (self.raio * self.raio)
        return area
        
raio = float(input())
circulo = Circle(raio)
area = circulo.area()
print(f"A={area:.4f}")

