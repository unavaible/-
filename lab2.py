from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():
    print(Rectangle(2, 2, 'blue').repr(), '\n')
    print(Circle(2, 'green').repr(), '\n')
    print(Square(2, 'red').repr(), '\n')


if __name__ == "__main__":
    main()
