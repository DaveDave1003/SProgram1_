class Barva:
    def __init__(self, r, g, b):
        if (r >= 0 and r <= 255) and (g >= 0 and g <= 255) and (b >= 0 and b <= 255):
            self.r = max(0, min(255, r))
            self.g = max(0, min(255, g))
            self.b = max(0, min(255, b))
        
        else:
            pass
            
        
    
    def __str__(self):
        return f"RGB({self.r}, {self.g}, {self.b})" 
    


    def __add__(self, jina):
        return Barva((self.r + jina.r) // 2 , (self.g + jina.g) // 2 , (self.b + jina.b) // 2)
    


    def __mul__(self, nasobek):
        nova_r = max(0, min(255, int(self.r * nasobek)))
        nova_g = max(0, min(255, int(self.g * nasobek)))
        nova_b = max(0, min(255, int(self.b * nasobek)))

        return Barva(nova_r, nova_g, nova_b)


    def invertuj(self):
        return Barva(255 - self.r, 255 - self.g, 255 - self.b)
    
    def to_hex(self):
        # TODO: Převeď r, g, b na hex formát       
        hex_r = hex(self.r)[2:]
        hex_g = hex(self.g)[2:]
        hex_b = hex(self.b)[2:]

        if len(hex_r) == 1:
            hex_r = "0" + hex_r
        if len(hex_g) == 1:
            hex_g = "0" + hex_g
        if len(hex_b) == 1:
            hex_b = "0" + hex_b
        # TODO: Vrať string ve formátu "#RRGGBB"
        return f"HEX(#{hex_r}{hex_g}{hex_b})"

oranzova = Barva(255, 100, 0)
print(f"{oranzova} = {oranzova.to_hex()}")  
# RGB(255, 100, 0) = #FF6400
bila = Barva(255, 255, 255)
print(f"{bila} = {bila.to_hex()}")  
# RGB(255, 255, 255) = #FFFFFF