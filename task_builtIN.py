def divisors(n):
    l = []
    for i in range (1, n+1):
        res = divmod(n, i)
        if res[1] == 0:
            l.append(i)
    print l
        




if __name__ == '__main__':
    q = True
    while q == True:
        n1 = input('Please input positive number: ')
        if n1 <= 0:
            print 'Please put positive value'
        else:
            q = False
    divisors(n1)
              
              