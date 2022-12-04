class punto:
    def _init_(self,cordenada_x,cordenada_y):
        self.cordenada_x=cordenada_x
        self.cordenada_y=cordenada_y
def cuadrante(self):
        if(self.x>=0 and self.y>=0):
            print("Cuadrante 1")
        elif (self.x<0 and self.y>=0):
            print("Cuadrante 2")
        elif self.x<0 and self.y<0:
            print("Cuadrante 3")
        else:
            print("Cuadrante 4")
cordenada = punto (3)
print("la cordenada x es",cordenada.cordenada_x)
print("la cordenada y es ",cordenada.cordenada_y)
