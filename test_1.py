import random 
import string 

    
def generate_password(): 
    passw = []
    passw.append(random.choice(string.uppercase))
    for i in range (0,5):
        passw.append(random.choice(string.lowercase))

    passw.append(str(random.randrange(0, 9))) 
    passw.append(random.choice(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', ';', ':']))
    
    full_passw = ''
    for j in range (0,8):
        full_passw = full_passw + passw[j]
    print full_passw
    return full_passw


def test_check1():
    assert len(generate_password()) == 8
    
    
def test_check2(): 
    a = '#'
    assert a.find(generate_password()) != -1
    

#generate_password()