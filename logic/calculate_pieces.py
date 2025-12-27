
def s20(width, height, quantity):
    width = int(width)
    height = int(height)
    quantity = int(quantity)
    
    pieces = {
        "horizontalFrame": {"lenght": width - 25, "quantity": quantity * 2},
        "verticalFrame": {"lenght": height, "quantity": quantity * 2},
        "lateralShash": {"lenght": height - 48, "quantity": quantity * 2},
        "centralShash": {"lenght": height - 48, "quantity": quantity * 2},
        "horizontalShash": {"lenght": width / 2 - 74, "quantity": quantity * 4},
        "glassWidth": {"lenght": width / 2 - 58, "quantity": quantity * 2},
        "glassHeight": {"lenght": height - 112, "quantity": quantity * 2},
        "screenWidth": {"lenght": width / 2 + 10, "quantity": quantity * 2},
        "screenHeight": {"lenght": height - 30, "quantity": quantity * 2},
        "screenGuideS20": {"lenght": width - 5, "quantity": quantity * 2}
    }
    return pieces

def s25(width, height, quantity):
    width = int(width)
    height = int(height)
    quantity = int(quantity)

    pieces = {
        "inferiorFrame": {"lenght": width - 51, "quantity": quantity},
        "superiorFrame": {"lenght": width - 51, "quantity": quantity},
        "verticalFrame": {"lenght": height, "quantity": quantity * 2},
        "lateralShash": {"lenght": height - 48, "quantity": quantity * 2},
        "centralShash": {"lenght": height - 48, "quantity": quantity * 2},
        "horizontalShashBig": {"lenght": width / 2 - 96, "quantity": quantity * 2},
        "horizontalShashSmall": {"lenght": width / 2 - 96, "quantity": quantity * 2},
        "glassWidth": {"lenght": width / 2 - 80, "quantity": quantity * 2},
        "glassHeight": {"lenght": height - 137, "quantity": quantity * 2},
        "glassDvhUHorizontal": {"lenght": width / 2 - 100, "quantity": quantity * 4},
        "glassDvhUVertical": {"lenght": height - 155, "quantity": quantity * 4},
        "glassDvhWidth": {"lenght": width / 2 - 111, "quantity": quantity * 2},
        "glassDvhHeight": {"lenght": height - 168, "quantity": quantity * 2},
        "screenWidth": {"lenght": width / 2 + 10, "quantity": quantity * 2},
        "screenHeight": {"lenght": height - 40, "quantity": quantity * 2},
        "screenGuideS25L": {"lenght": width - 5, "quantity": quantity},
        "screenGuideS25P": {"lenght": width - 5, "quantity": quantity}
    }
    return pieces

def s25TripleRiel(width, height, quantity):
    width = int(width)
    height = int(height)
    quantity = int(quantity)

    pieces = {
        "inferiorFrame": {"lenght": width - 51, "quantity": quantity},
        "superiorFrame": {"lenght": width - 51, "quantity": quantity},
        "verticalFrame": {"lenght": height, "quantity": quantity * 2},
        "lateralShash": {"lenght": height - 48, "quantity": quantity * 2},
        "centralShash": {"lenght": height - 48, "quantity": quantity * 4},
        "horizontalShashBig": {"lenght": width / 3 - 77, "quantity": quantity * 3},
        "horizontalShashSmall": {"lenght": width / 3 - 77, "quantity": quantity * 3},
        "glassWidth": {"lenght": width / 3 - 60, "quantity": quantity * 3},
        "glassHeight": {"lenght": height - 137, "quantity": quantity * 2}, # JS had quantity * 2, keep as is? Or 3? logic says 3 panes but 2 heights? keep JS logic. 
        "glassDvhUHorizontal": {"lenght": width / 3 - 81, "quantity": quantity * 6},
        "glassDvhUVertical": {"lenght": height - 155, "quantity": quantity * 6},
        "glassDvhWidth": {"lenght": width / 3 - 92, "quantity": quantity * 3},
        "glassDvhHeight": {"lenght": height - 168, "quantity": quantity * 3},
        "screenWidth": {"lenght": width / 3 - 9, "quantity": quantity * 2},
        "screenHeight": {"lenght": height - 40, "quantity": quantity * 2},
        "screenGuideS25L": {"lenght": width - 5, "quantity": quantity},
        "screenGuideS25P": {"lenght": width - 5, "quantity": quantity}
    }
    return pieces

def probbaCorrediza(width, height, quantity):
    width = int(width)
    height = int(height)
    quantity = int(quantity)

    pieces = {
        "horizontalFrame": {"lenght": width - 36, "quantity": quantity * 2},
        "verticalFrame": {"lenght": height, "quantity": quantity * 2},
        "lateralShash": {"lenght": height - 65, "quantity": quantity * 2},
        "centralShash": {"lenght": height - 65, "quantity": quantity * 2},
        "horizontalShash": {"lenght": width / 2 - 23, "quantity": quantity * 4},
        "glassWidth": {"lenght": width / 2 - 94, "quantity": quantity * 2},
        "glassHeight": {"lenght": height - 172, "quantity": quantity * 2},
        "screenWidth": {"lenght": width / 2 + 11, "quantity": quantity * 2},
        "screenHeight": {"lenght": height - 62, "quantity": quantity * 2},
        "screenGuideProbba": {"lenght": width - 5, "quantity": quantity * 2},
        "glassDvhWidth": {"lenght": width / 2 - 86, "quantity": quantity * 2},
        "glassDvhHeight": {"lenght": height - 165, "quantity": quantity * 2}
    }
    return pieces

def probbaCorredizaTripleRiel(width, height, quantity):
    width = int(width)
    height = int(height)
    quantity = int(quantity)

    pieces = {
        "horizontalFrame": {"lenght": width - 36, "quantity": quantity * 2},
        "verticalFrame": {"lenght": height, "quantity": quantity * 2},
        "lateralShash": {"lenght": height - 65, "quantity": quantity * 2},
        "centralShash": {"lenght": height - 65, "quantity": quantity * 4},
        "horizontalShashLateral": {"lenght": width / 3 - 7, "quantity": quantity * 4},
        "horizontalShashCentral": {"lenght": width / 3 + 12, "quantity": quantity * 2},
        "glassWidthCentral": {"lenght": width / 3 - 68, "quantity": quantity * 1},
        "glassWidthLateral": {"lenght": width / 3 - 77, "quantity": quantity * 2},
        "glassHeight": {"lenght": height - 173, "quantity": quantity * 3},
        "screenWidth": {"lenght": width / 3 + 11, "quantity": quantity * 2},
        "screenHeight": {"lenght": height - 62, "quantity": quantity * 2},
        "screenGuideProbba": {"lenght": width - 5, "quantity": quantity * 2},
        "glassDvhWidthCentral": {"lenght": width / 3 - 61, "quantity": quantity * 1},
        "glassDvhWidthLateral": {"lenght": width / 3 - 70, "quantity": quantity * 2},
        "glassDvhHeight": {"lenght": height - 165, "quantity": quantity * 3}
    }
    return pieces
