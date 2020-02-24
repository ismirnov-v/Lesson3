from collections import Counter 

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Тестовая запись в файл.')


with open('text.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

print(content)

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.upper()
        print(line)


with open('referat.txt', 'r', encoding='utf-8') as f:
    referat_content = f.read()
        
    
print(f'Длина строки файла "реферат" равна: {len(referat_content)}')
print(f'Количество слов в файле составляет: {len(referat_content.split())}')

referat_new = referat_content.replace(".", "!")
with open('referat_new.txt', 'w', encoding='utf-8') as f:
    f.write(referat_new)
