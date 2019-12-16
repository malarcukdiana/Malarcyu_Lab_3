'''Рекурсивна формула для обчислення факторіалу:
n! = (n-1)! * n, якщо n > 0,
0! = 1'''
def fact(n):        
    if n == 0:      
        return 1     
    return fact(n-1)*n 
 
n = int(input('n = ')) 
result = '{0}! = {1}'.format(n, fact(n))
print(result) 
