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
    
def generate_password2(): 
    passw = []
    passw.append(random.choice(string.uppercase))
    for i in range (0,4):
        passw.append(random.choice(string.lowercase))

    passw.append(str(random.randrange(0, 9))) 
    passw.append(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ';', ':']))
    
    full_passw = ''
    for j in range (0,7):
        full_passw = full_passw + passw[j]
    print full_passw
    
def generate_password3(n): 
    if n < 4:
        print 'Please put bigger number in parameters'
        return  
    
    passw = []
    passw.append(random.choice(string.uppercase))
   
    for i in range (0,n-3):
        passw.append(random.choice(string.lowercase))
   
              
    passw.append(str(random.randrange(0, 9))) 
    passw.append(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ';', ':']))
    
      
    random.shuffle(passw)
    result = ''.join(passw)
    
    
    print result    

generate_password3(2)