
from .calculate_pieces import s20, s25, s25TripleRiel, probbaCorrediza, probbaCorredizaTripleRiel
from .models import Frame

class Opening:
    def __init__(self, width, height, serie, color, dvh, preframe, quantity):
        self.width = float(width)
        self.height = float(height)
        self.serie = serie
        self.color = color
        # handle JS boolean or string "true"/"false" if passed from UI
        self.dvh = dvh if isinstance(dvh, bool) else (str(dvh).lower() == 'true')
        self.preframe = preframe
        self.quantity = int(quantity)
        self.pieces = {}
        self.frames = {}
        self.glass = {}
        self.stringFrames = []

    def calculate_pieces(self):
        if self.serie == "s20":
            self.pieces = s20(self.width, self.height, self.quantity)
        elif self.serie == "s25":
            self.pieces = s25(self.width, self.height, self.quantity)
        elif self.serie == "s25TripleRiel":
            self.pieces = s25TripleRiel(self.width, self.height, self.quantity)
        elif self.serie == "probbaCorrediza":
            self.pieces = probbaCorrediza(self.width, self.height, self.quantity)
        elif self.serie == "probbaCorredizaTripleRiel":
            self.pieces = probbaCorredizaTripleRiel(self.width, self.height, self.quantity)

    def framing(self):
        self.calculate_pieces()
        
        if self.serie == "s20":
            self.frames = {
                "horizontalFrame": Frame(self.serie, {"abasur": "N1749", "urualum": "190", "juan": "204 o 190", "aluminiosDelUruguay": "PN 0190"}, self.pieces["horizontalFrame"]["lenght"], "Horizontal Frame", "Horizontal de Marco", self.color, self.pieces["horizontalFrame"]["quantity"]),
                "verticalFrame": Frame(self.serie, {"abasur": "N1753", "urualum": "191", "juan": "205 o 191", "aluminiosDelUruguay": "PN 0191"}, self.pieces["verticalFrame"]["lenght"], "Vertical Frame", "Lateral de Marco", self.color, self.pieces["verticalFrame"]["quantity"]),
                "lateralShash": Frame(self.serie, {"abasur": "N1751", "urualum": "193", "juan": "202 o 193", "aluminiosDelUruguay": "PN 0193"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash", "Lateral de Hoja", self.color, self.pieces["lateralShash"]["quantity"]),
                "centralShash": Frame(self.serie, {"abasur": "E2864", "urualum": "189", "juan": "216 o 189", "aluminiosDelUruguay": "PN 0189"}, self.pieces["centralShash"]["lenght"], "Central Shash", "Enganche", self.color, self.pieces["centralShash"]["quantity"]),
                "horizontalShash": Frame(self.serie, {"abasur": "N1752", "urualum": "192", "juan": "192", "aluminiosDelUruguay": "PN 0192"}, self.pieces["horizontalShash"]["lenght"], "Horizontal Shash", "Horizontal de Hoja", self.color, self.pieces["horizontalShash"]["quantity"]),
                "screenShash": Frame(self.serie, {"abasur": "E4436", "urualum": "2314", "juan": "214", "aluminiosDelUruguay": "PN 2314"}, {"width": self.pieces["screenWidth"]["lenght"], "height": self.pieces["screenHeight"]["lenght"]}, "Screen Shash", "Hoja de Mosquitero", self.color, quantity=0, width_quantity=self.pieces["screenWidth"]["quantity"], height_quantity=self.pieces["screenHeight"]["quantity"]),
                "screenGuide": Frame(self.serie, {"abasur": "E4821", "urualum": "213", "juan": "213", "aluminiosDelUruguay": "PN 0213"}, self.pieces["screenGuideS20"]["lenght"], "Screen Guide S20", "Guía de Mosquitero", self.color, self.pieces["screenGuideS20"]["quantity"])
            }
            self.glass = {"glassWidth": self.pieces["glassWidth"], "glassHeight": self.pieces["glassHeight"]}

        elif self.serie == "s25":
            self.frames = {
                "inferiorFrame": Frame(self.serie, {"abasur": "E2857", "urualum": "2500", "juan": "150 o 2500", "aluminiosDelUruguay": "Not available"}, self.pieces["inferiorFrame"]["lenght"], "Inferior Frame", "Inferior de Marco", self.color, self.pieces["inferiorFrame"]["quantity"]),
                "superiorFrame": Frame(self.serie, {"abasur": "E2858", "urualum": "2528", "juan": "151 o 2528", "aluminiosDelUruguay": "Not available"}, self.pieces["superiorFrame"]["lenght"], "Superior Frame", "Superior de Marco", self.color, self.pieces["superiorFrame"]["quantity"]),
                "verticalFrame": Frame(self.serie, {"abasur": "E3513", "urualum": "2501", "juan": "2501", "aluminiosDelUruguay": "Not available"}, self.pieces["verticalFrame"]["lenght"], "Vertical Frame", "Lateral de Marco", self.color, self.pieces["verticalFrame"]["quantity"]),
                "lateralShash": Frame(self.serie, {"abasur": "E2862", "urualum": "4505", "juan": "4505", "aluminiosDelUruguay": "Not available"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash", "Lateral de Hoja", self.color, self.pieces["lateralShash"]["quantity"]),
                "centralShash": Frame(self.serie, {"abasur": "E2861", "urualum": "4507", "juan": "155 o 4507", "aluminiosDelUruguay": "Not available"}, self.pieces["centralShash"]["lenght"], "Central Shash", "Enganche", self.color, self.pieces["centralShash"]["quantity"]),
                "horizontalShashBig": Frame(self.serie, {"abasur": "E2859", "urualum": "4503", "juan": "4503", "aluminiosDelUruguay": "Not available"}, self.pieces["horizontalShashBig"]["lenght"], "Horizontal Shash Big", "Horizontal de Hoja Grueso", self.color, self.pieces["horizontalShashBig"]["quantity"]),
                "horizontalShashSmall": Frame(self.serie, {"abasur": "E2863", "urualum": "4504", "juan": "4504", "aluminiosDelUruguay": "Not available"}, self.pieces["horizontalShashSmall"]["lenght"], "Horizontal Shash Small", "Horizontal de Hoja Fino", self.color, self.pieces["horizontalShashSmall"]["quantity"]),
                "screenShash": Frame(self.serie, {"abasur": "E3514", "urualum": "2343", "juan": "2343", "aluminiosDelUruguay": "PN 2343"}, {"width": self.pieces["screenWidth"]["lenght"], "height": self.pieces["screenHeight"]["lenght"]}, "Screen Shash", "Hoja de Mosquitero", self.color, quantity=0, width_quantity=self.pieces["screenWidth"]["quantity"], height_quantity=self.pieces["screenHeight"]["quantity"]),
                "screenGuideS25L": Frame(self.serie, {"abasur": "E4678", "urualum": "213", "juan": "213", "aluminiosDelUruguay": "PN 0213"}, self.pieces["screenGuideS25L"]["lenght"], "Screen Guide S25 L", "Guía de Mosquitero S25 L", self.color, self.pieces["screenGuideS25L"]["quantity"]),
                "screenGuideS25P": Frame(self.serie, {"abasur": "E4677", "urualum": "2344", "juan": "2344", "aluminiosDelUruguay": "PN 0213"}, self.pieces["screenGuideS25P"]["lenght"], "Screen Guide S25 P", "Guía de Mosquitero S25 P", self.color, self.pieces["screenGuideS25P"]["quantity"])
            }

            if not self.dvh:
                self.glass = {
                    "glassWidth": self.pieces["glassWidth"],
                    "glassHeight": self.pieces["glassHeight"]
                }
                self.frames["glassDvhU"] = None
            else:
                self.glass = {
                    "glassWidth": self.pieces["glassDvhWidth"],
                    "glassHeight": self.pieces["glassDvhHeight"]
                }
                self.frames["glassDvhU"] = Frame(self.serie, {"abasur": "E4886", "urualum": "Not available", "juan": "4590", "aluminiosDelUruguay": "Not available"}, {"width": self.pieces["glassDvhUHorizontal"]["lenght"], "height": self.pieces["glassDvhUVertical"]["lenght"]}, "U Dvh", "U Dvh", self.color, quantity=0, width_quantity=self.pieces["glassDvhUHorizontal"]["quantity"], height_quantity=self.pieces["glassDvhUVertical"]["quantity"])

        elif self.serie == "s25TripleRiel":
            self.frames = {
                "inferiorFrameTripleRiel": Frame(self.serie, {"abasur": "E4940", "urualum": "Not available", "juan": "2538", "aluminiosDelUruguay": "Not available"}, self.pieces["inferiorFrame"]["lenght"], "Inferior Frame Triple Riel", "Inferior de Marco Triple Riel", self.color, self.pieces["inferiorFrame"]["quantity"]),
                "superiorFrameTripleRiel": Frame(self.serie, {"abasur": "E4674", "urualum": "Not Available", "juan": "2532", "aluminiosDelUruguay": "Not available"}, self.pieces["superiorFrame"]["lenght"], "Superior Frame Triple Riel", "Superior de Marco Triple Riel", self.color, self.pieces["superiorFrame"]["quantity"]),
                "verticalFrameTripleRiel": Frame(self.serie, {"abasur": "E4676", "urualum": "Not available", "juan": "2534", "aluminiosDelUruguay": "Not available"}, self.pieces["verticalFrame"]["lenght"], "Vertical Frame", "Lateral de Marco Triple Riel", self.color, self.pieces["verticalFrame"]["quantity"]),
                "lateralShash": Frame(self.serie, {"abasur": "E2862", "urualum": "4505", "juan": "4505", "aluminiosDelUruguay": "Not available"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash", "Lateral de Hoja", self.color, self.pieces["lateralShash"]["quantity"]),
                "centralShash": Frame(self.serie, {"abasur": "E2861", "urualum": "4507", "juan": "155 o 4507", "aluminiosDelUruguay": "Not available"}, self.pieces["centralShash"]["lenght"], "Central Shash", "Enganche", self.color, self.pieces["centralShash"]["quantity"]),
                "horizontalShashBig": Frame(self.serie, {"abasur": "E2859", "urualum": "4503", "juan": "4503", "aluminiosDelUruguay": "Not available"}, self.pieces["horizontalShashBig"]["lenght"], "Horizontal Shash Big", "Horizontal de Hoja Grueso", self.color, self.pieces["horizontalShashBig"]["quantity"]),
                "horizontalShashSmall": Frame(self.serie, {"abasur": "E2863", "urualum": "4504", "juan": "4504", "aluminiosDelUruguay": "Not available"}, self.pieces["horizontalShashSmall"]["lenght"], "Horizontal Shash Small", "Horizontal de Hoja Fino", self.color, self.pieces["horizontalShashSmall"]["quantity"]),
                "screenShash": Frame(self.serie, {"abasur": "E2860", "urualum": "4506", "juan": "4506", "aluminiosDelUruguay": "Not available"}, {"width": self.pieces["screenWidth"]["lenght"], "height": self.pieces["screenHeight"]["lenght"]}, "Screen Shash", "Hoja de Mosquitero", self.color, quantity=0, width_quantity=self.pieces["screenWidth"]["quantity"], height_quantity=self.pieces["screenHeight"]["quantity"]),
                "screenGuideS25L": Frame(self.serie, {"abasur": "E4678", "urualum": "213", "juan": "213", "aluminiosDelUruguay": "PN 0213"}, self.pieces["screenGuideS25L"]["lenght"], "Screen Guide S25 L", "Guía de Mosquitero S25 L", self.color, self.pieces["screenGuideS25L"]["quantity"]),
                "screenGuideS25P": Frame(self.serie, {"abasur": "E4677", "urualum": "2344", "juan": "2344", "aluminiosDelUruguay": "PN 0213"}, self.pieces["screenGuideS25P"]["lenght"], "Screen Guide S25 P", "Guia de Mosquitero S25 P", self.color, self.pieces["screenGuideS25P"]["quantity"])
            }
            if not self.dvh:
                self.glass = {"glassWidth": self.pieces["glassWidth"], "glassHeight": self.pieces["glassHeight"]}
                self.frames["glassDvhU"] = None
            else:
                self.glass = {"glassWidth": self.pieces["glassDvhWidth"], "glassHeight": self.pieces["glassDvhHeight"]}
                self.frames["glassDvhU"] = Frame(self.serie, {"abasur": "E4886", "urualum": "Not available", "juan": "4590", "aluminiosDelUruguay": "Not available"}, {"width": self.pieces["glassDvhUHorizontal"]["lenght"], "height": self.pieces["glassDvhUVertical"]["lenght"]}, "U Dvh", "U Dvh", self.color, quantity=0, width_quantity=self.pieces["glassDvhUHorizontal"]["quantity"], height_quantity=self.pieces["glassDvhUVertical"]["quantity"])

        elif self.serie == "probbaCorrediza":
            # Logic similar to JS
            self.frames["horizontalFrame"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 93150"}, self.pieces["horizontalFrame"]["lenght"], "Horizontal Frame", "Horizontal de Marco", self.color, self.pieces["horizontalFrame"]["quantity"])
            self.frames["verticalFrame"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90021"}, self.pieces["verticalFrame"]["lenght"], "Vertical Frame", "Lateral de Marco", self.color, self.pieces["verticalFrame"]["quantity"])
            
            if self.dvh:
                self.frames["lateralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90031"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash for DVH", "Lateral de Hoja para DVH", self.color, self.pieces["lateralShash"]["quantity"])
                self.frames["centralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90030"}, self.pieces["centralShash"]["lenght"], "Central Shash for DVH", "Enganche para DVH", self.color, self.pieces["centralShash"]["quantity"])
                self.frames["horizontalShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90026"}, self.pieces["horizontalShash"]["lenght"], "Horizontal Shash for DVH", "Horizontal de Hoja para DVH", self.color, self.pieces["horizontalShash"]["quantity"])
                self.glass = {"glassWidth": self.pieces["glassDvhWidth"], "glassHeight": self.pieces["glassDvhHeight"]}
            else:
                self.frames["lateralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90027"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash for Single Glass", "Lateral de Hoja para Vidrio Simple", self.color, self.pieces["lateralShash"]["quantity"])
                self.frames["centralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90028"}, self.pieces["centralShash"]["lenght"], "Central Shash for Single Glass", "Enganche para Vidrio Simple", self.color, self.pieces["centralShash"]["quantity"])
                self.frames["horizontalShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90025"}, self.pieces["horizontalShash"]["lenght"], "Horizontal Shash for Single Glass", "Horizontal de Hoja para Vidrio Simple", self.color, self.pieces["horizontalShash"]["quantity"])
                self.glass = {"glassWidth": self.pieces["glassWidth"], "glassHeight": self.pieces["glassHeight"]}

            self.frames["screenShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 41043"}, {"width": self.pieces["screenWidth"]["lenght"], "height": self.pieces["screenHeight"]["lenght"]}, "Screen Shash", "Hoja de Mosquitero", self.color, quantity=0, width_quantity=self.pieces["screenWidth"]["quantity"], height_quantity=self.pieces["screenHeight"]["quantity"])
            self.frames["screenGuideProbba"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 93074"}, self.pieces["screenGuideProbba"]["lenght"], "Screen Guide", "Guía de Mosquitero", self.color, self.pieces["screenGuideProbba"]["quantity"])

        elif self.serie == "probbaCorredizaTripleRiel":
            self.frames["horizontalFrame"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 93054"}, self.pieces["horizontalFrame"]["lenght"], "Horizontal Frame Triple Riel", "Horizontal de Marco triple Riel", self.color, self.pieces["horizontalFrame"]["quantity"])
            self.frames["verticalFrame"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 93073"}, self.pieces["verticalFrame"]["lenght"], "Vertical Frame Triple Riel", "Lateral de Marco Triple Riel", self.color, self.pieces["verticalFrame"]["quantity"])
            
            if self.dvh:
                self.frames["lateralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90031"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash for DVH", "Lateral de Hoja para DVH", self.color, self.pieces["lateralShash"]["quantity"])
                self.frames["centralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90030"}, self.pieces["centralShash"]["lenght"], "Central Shash for DVH", "Enganche para DVH", self.color, self.pieces["centralShash"]["quantity"])
                self.frames["horizontalShashLateral"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90026"}, self.pieces["horizontalShashLateral"]["lenght"], "Horizontal Shash for DVH (Lateral Shashes)", "Horizontal de Hoja para DVH (Hojas Laterales)", self.color, self.pieces["horizontalShashLateral"]["quantity"])
                self.frames["horizontalShashCentral"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90026"}, self.pieces["horizontalShashCentral"]["lenght"], "Horizontal Shash for DVH (Central Shash)", "Horizontal de Hoja para DVH (Hoja Central)", self.color, self.pieces["horizontalShashCentral"]["quantity"])
                self.glass = {"glassWidthLateral": self.pieces["glassDvhWidthLateral"], "glassWidthCentral": self.pieces["glassDvhWidthCentral"], "glassHeight": self.pieces["glassDvhHeight"]}
            else:
                self.frames["lateralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90027"}, self.pieces["lateralShash"]["lenght"], "Lateral Shash for Single Glass", "Lateral de Hoja para Vidrio Simple", self.color, self.pieces["lateralShash"]["quantity"])
                self.frames["centralShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90028"}, self.pieces["centralShash"]["lenght"], "Central Shash for Single Glass", "Enganche para Vidrio Simple", self.color, self.pieces["centralShash"]["quantity"])
                self.frames["horizontalShashLateral"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90025"}, self.pieces["horizontalShashLateral"]["lenght"], "Horizontal Shash for Single Glass (Lateral Shashes)", "Horizontal de Hoja para Vidrio Simple (Hojas Laterales)", self.color, self.pieces["horizontalShashLateral"]["quantity"])
                self.frames["horizontalShashCentral"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 90025"}, self.pieces["horizontalShashCentral"]["lenght"], "Horizontal Shash for Single Glass (Central Shash)", "Horizontal de Hoja para Vidrio Simple (Hoja Central)", self.color, self.pieces["horizontalShashCentral"]["quantity"])
                self.glass = {"glassWidthLateral": self.pieces["glassWidthLateral"], "glassWidthCentral": self.pieces["glassWidthCentral"], "glassHeight": self.pieces["glassHeight"]}

            self.frames["screenShash"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 41043"}, {"width": self.pieces["screenWidth"]["lenght"], "height": self.pieces["screenHeight"]["lenght"]}, "Screen Shash", "Hoja de Mosquitero", self.color, quantity=0, width_quantity=self.pieces["screenWidth"]["quantity"], height_quantity=self.pieces["screenHeight"]["quantity"])
            self.frames["screenGuideProbba"] = Frame(self.serie, {"abasur": "Not Available", "urualum": "Not Available", "juan": "Not Available", "aluminiosDelUruguay": "PN 93074"}, self.pieces["screenGuideProbba"]["lenght"], "Screen Guide", "Guía de Mosquitero", self.color, self.pieces["screenGuideProbba"]["quantity"])

    def init(self):
        self.framing()
        self.to_string()

    def to_string(self):
        # Format logic...
        dvh_str = "true" if self.dvh else "false"
        returned = f"--------------------------------------------------\n"
        returned += f"{self.quantity} Aberturas de {self.width} Ancho x {self.height} Alto {self.serie} {self.color} DVH? = {dvh_str}\n"

        def fmt(v):
            if v is None: return 'N/A'
            if isinstance(v, (int, float)):
                # Return int if integer, else 1 float decimal
                return str(int(v)) if v == int(v) else f"{v:.1f}"
            return str(v)

        for key, frame in self.frames.items():
            if frame is None: continue
            if frame.name == "Screen Shash" or frame.name == "U Dvh":
                 returned += f"{frame.spanish_name} Anchos = {fmt(frame.width_quantity)} de {fmt(frame.lenght['width'])} \nAltos = {fmt(frame.height_quantity)} de {fmt(frame.lenght['height'])}\n"
            elif frame.name in ["Horizontal Frame", "Inferior Frame", "Superior Frame", "Lateral Shash", "Central Shash", "Lateral Shash for DVH", "Central Shash for DVH", "Lateral Shash for Single Glass", "Central Shash for Single Glass"]:
                returned += f"{fmt(frame.quantity)} {frame.spanish_name} {fmt(frame.lenght)} Mitad = {fmt(frame.half)}\n"
            else:
                 returned += f"{fmt(frame.quantity)} {frame.spanish_name} {fmt(frame.lenght)}\n"
        
        # Glass
        if "glassWidthLateral" in self.glass:
             gwL = self.glass.get("glassWidthLateral")
             gwC = self.glass.get("glassWidthCentral")
             gh = self.glass.get("glassHeight")
             returned += f"Ancho de Vidrio Hoja Central = {fmt(gwC['lenght'])} \n Ancho de Vidrios Hojas Laterales = {fmt(gwL['lenght'])}\n Alto de Vidrios = {fmt(gh['lenght'])} \n Cantidad de Vidrios Laterales = {fmt(gwL['quantity'])} \n Cantidad de vidrios centrales = {fmt(gwC['quantity'])}\n"
        elif "glassWidth" in self.glass:
             gw = self.glass.get("glassWidth")
             gh = self.glass.get("glassHeight")
             returned += f"Ancho de Vidrio = {fmt(gw['lenght'])}\n Alto de Vidrio = {fmt(gh['lenght'])}\n Cantidad de Vidrios = {fmt(gw['quantity'])}\n"
        else:
             returned += "Ancho de Vidrio = N/A Alto de Vidrio = N/A Cantidad de Vidrios = 0\n"

        return returned
