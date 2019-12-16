'''Описуємо функцію, яка приймає рядок s і
повертатиме кількість унікальних символів у ньому'''
def unique(s):
    d = {}
    for symbol in s:    
        if symbol not in d:
            d[symbol] = 1   
        else:               
            d[symbol] += 1
    return len(d)           

s = input('Введіть рядок: ') 
unique_symbols = unique(s)   
print('Унікальних символів у рядку:', unique_symbols) 
