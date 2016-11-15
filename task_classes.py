class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def square (self, radius):
        s = 3.14*(radius**2)
        print 'Square of your circle is: ' + str(s)
        return s

class Triangle:
    def __init__(self, height, side):
            self.height = height 
            self.side = side
            
    def square (self, height, side):
        s = 0.5*a*h
        print 'Square of your triangle is: ' + str(s)
        return s

class Rectangle:
    def __init__(self, side1, side2):
            self.side1 = side1 
            self.side2 = side2   
            
    def square (self, side1, side2):
        s = side1*side2
        print 'Square of your rectangle is: ' + str(s)
        return s

if __name__ == "__main__":
    figure = ''

    print 'Please input name of figure'

    figure = raw_input ('input \'c\' in the case of circle; input \'t\' in the sace of triangle; input \'r\' in the case of rectangle:')

    if figure == 'c':
        
        q = True
        while q == True:
            r = input ('Please input length of radius of your circle: ')
            if r <= 0:
                print 'Please put positive value'
            else:    
                q = False
        
        
       
        x = Circle(r)
        x.square(r)
        
    elif figure == 't':
        
        q = True
        while q == True:
            h = input ('Please input length of height of your triangle: ')
            if h <= 0:
                print 'Please put positive value'
            else:    
                q = False
                
        q = True
        while q == True:
            a = input ('PLease input length of base of your triangle: ') 
            if a <= 0:
                print 'Please put positive value'
            else:    
                q = False                
            
         
        x = Triangle(h, a)
        x.square(h, a)
    elif figure == 'r':
        q = True
        while q == True:
            a = input ('Please input length of first side of your rectangle: ')
            if a <= 0:
                print 'Please put positive value'
            else:    
                q = False
                
        q = True
        while q == True:
            b = input ('Please input length of second side of your rectangle: ') 
            if b <= 0:
                print 'Please put positive value'
            else:    
                q = False

                   
        x = Rectangle(a,b)
        x.square(a,b)
    else:
        print 'Define correct figure'




