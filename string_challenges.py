# Вывести последнюю букву в слове
word = 'Архангельск'
    # №1:
print(f'1) В слове "{word}" последняя буква = "{word[-1]}"')
    # №2:
word_list = []
for literal in word:
    word_list.append(literal)
print(f'2) В слове "{word}" последняя буква = "{word_list[-1]}"')

# Вывести количество букв "а" в слове
word = 'Архангельск'
# Если только маленькую букву то:
print(f'3) Количество маленьких букв "а" в слове {word} равно: {word.count("а")}')
# Подсчитать все буквы "а"
print(f'4) Количество букв "а" или "А" в слове {word} равно: {word.lower().count("а")}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = list('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
consonats = list('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
#print(vowels)
#print(consonats)
count_vowels = sum(x in vowels for x in word)
count_consonats = sum(x in consonats for x in word)
print(f'5) Количество гласных букв в слове "{word}" равно: {count_vowels}.')
print(f'6) Количество согласных букв в слове "{word}" равно: {count_consonats}.')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_list = sentence.split(" ")
print(f'7) Количество слов в предложении: {len(sentence_list)}')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print('8) Первые буквы в предложении, каждая с новой строки:')
for word in sentence_list:
    print('\t',word[0][0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words_len = sum(len(x) for x in sentence_list)
avg_word_len = words_len / len(sentence_list)
print(f'9) Средняя длинна слова в преложении равна: {avg_word_len}')