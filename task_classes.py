class Circle:
    def square (self):
        r = input ('Please input length of radius of your circle: ')
        s = 3.14*(r**2)
        print 'Square of your circle is: ' + str(s)
        return s

class Triangle:
    def square (self):
        h = input ('Please input length of height of your triangle: ')
        a = input ('PLease input length of base of your triangle: ')
        s = 0.5*a*h
        print 'Square of your triangle is: ' + str(s)
        return s

class Rectangle:
    def square (self):
        a = input ('Please input length of first side of your rectangle: ')
        b = input ('Please input length of second side of your rectangle: ')
        s = a*b
        print 'Square of your rectangle is: ' + str(s)
        return s

if __name__ == "__main__":
    figure = ''

    print 'Please input name of figure'

    figure = input ('input \'c\' in the case of circle; input \'t\' in the sace of triangle; input \'r\' in the case of rectangle:')

    if figure == 'c':
        x = Circle()
        x.square()
    elif figure == 't':
        x = Triangle()
        x.square()
    else:
        x = Rectangle()
        x.square()




