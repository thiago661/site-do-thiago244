from rich import print, inspect
from poligono import Quadrado

def main():
    q = Quadrado(20)
    inspect(q, methods=True)
    print(q.perimetro())
    print(q.area())


if __name__ == "__main__":
    main()