def max_v(a,b,c): 
    if (a>b) and (a>c): 
        max_value = a 
    elif (b>a) and (b>c): 
        max_value = b 
    else: 
        max_value = c 

        print max_value 

if __name__ == '__main__': 
    max_v(2,5,8)