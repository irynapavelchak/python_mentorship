import random 
import string 

def generate_password(): 
    a = random.choice(string.letters).upper() 
    b = random.choice(string.letters).lower() 
    c = random.choice(string.letters).lower() 
    d = random.choice(string.letters).lower() 
    e = random.choice(string.letters).lower() 
    f = random.choice(string.letters).lower() 
    g = random.randrange(0, 9) 
    h = random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ';', ':']) 
    passw = a + b + c + d + e + f + str(g) + h 

    print passw 

generate_password()