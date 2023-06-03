from collections import Counter

# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
res = Counter(word.lower())
print(res['а'])


# Вывести количество гласных букв в слове
word = 'Архангельск'
res = Counter(word.lower())
i = 0
for letter in 'аеёиоуыэюя':
    letter_count = res.get(letter)
    if letter_count is not None:
        i = i + letter_count
print(f'Количество гласных букв в слове "{word}": {i}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении: {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for w in sentence.split():
    print(w[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
total_len = sum([len(w) for w in words])
print(f'Усреднённая длина слова в предложении: {total_len / len(words)}')