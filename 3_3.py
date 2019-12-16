filename = input('Введіть назву файлу у форматі filename.txt:  ') 
f = open(filename) 
lines = words = symbols = 0 
for line in f: 
    lines += 1 
    symbols += len(line)                     
    list_of_words = line.split() 
    words += len(list_of_words)  
print('Рядків -',lines) 
print('Слів -', words) 
print('Символів -', symbols) 
f.close()
    
