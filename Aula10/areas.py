import math

def SquareArea(x):
    """Calculates the square's area
    
    Parameters:
    - The square side
    """

    return math.pow(x, 2)

def RectangleArea(b, h):
    """Calculates the rectangle's area
    
    Parameters:
    - The rectangle's base 
    - The rectangle's height 
    """
    
    return b * h

def CircleArea(r):
    """Calculates the circle's area
    
    Parameter:
    - The circle radius
    """

    return round(math.pi * math.pow(r, 2), 2)

def TriangleArea(b, h):
    """Calculates the triangle's area
    
    Parameters:

    - The triangle's base
    - The triangle's height

    """

    return b * h / 2

def CylinderVolume(r, h):
    """Calculates the cylinder's area
    
    Parameters:
    - The cylinder's radius
    - The cylinder's height
    """
    return round(math.pi * math.pow(r, 2) * h, 2)

def CubeVolume(x):
    """Calculates the cube's volume
    
    Parameter:
    - The cube's side
    """
    return math.pow(x, 3)

def TerrainArea():
    """"""
    base = int(input("Digite o valor da base do terreno: "))
    height = int(input("Digite o valor da altura do terreno: "))

    area = base * height

    return(area)

print(f"A área do quadrado é: {SquareArea(3)}")
print(f"A área do retângulo é: {RectangleArea(3, 4)}")
print(f"A área do círculo é: {CircleArea(3)}")
print(f"A área do triângulo é: {TriangleArea(3, 4)}")
print(f"O volume do cilindro é: {CylinderVolume(3, 4)}")
print(f"O volume do cubo é: {CubeVolume(3)}")
print(f"A área do terreno é de {TerrainArea()}m²")
