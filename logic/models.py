
class Frame:
    def __init__(self, serie, code, lenght, name, spanish_name, color, quantity, width_quantity=0, height_quantity=0):
        self.serie = serie
        self.code = code
        self.lenght = lenght
        self.name = name
        self.spanish_name = spanish_name
        self.color = color
        self.quantity = quantity
        
        # Handle complex quantity objects (like for Screen Shash) from JS
        # In JS: {widthQuantity: ..., heightQuantity: ...}
        # We will store them as attributes if passed
        self.width_quantity = width_quantity
        self.height_quantity = height_quantity

        # Calculate half if length is a number
        self.half = 0
        if isinstance(self.lenght, (int, float)):
            self.half = self.lenght / 2

class Bar:
    def __init__(self, quantity, name, serie, color, code):
        self.quantity = quantity
        self.name = name
        self.serie = serie
        self.color = color
        self.code = code
