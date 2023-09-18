'''

'''
from textblob import TextBlob
sentence = input('Введите текст: ')


word_count = sentence.count(" ") + 1

sentences = sentence.count('.') + sentence.count('?') + sentence.count('!') + sentence.count('...')

tsll = 0
vowels = set('aeiou')
for letter in s:
    if letter in vowels:
        tsll += 1

sentiment = TextBlob(sentence).polarity
if sentiment == 0:
    sent = 'нейтральный'
elif sentiment >0:
    sent = 'положительный'
else:
    sent = 'отрицательный'


Sub_analysis = TextBlob(sentence).subjectivity

ASL = word_count / sentences
ASW = tsll / word_count

fre.en = 206.835 - 1.015 * ASL - 84.6 * ASW

fre.ru = 206.835 - 1.52 * ASL - 65.14 * ASW

if fre.en >= 0 and fre.en <= 30:
    print('Текст с очень низким уровнем удобочитаемости (уровень образования: выпускник колледжа.')
elif fre.en > 30 and fre.en <= 50:
    print('Текст с низким уровнем удобочитаемости (уровень образования: колледж).')
elif fre.en > 50 and fre.en <= 60:
    print ('Текст с уровнем удобочитаемости ниже среднего (уровень образования: 10-12 классов).')
elif fre.en > 60 and fre.en <= 70:
    print('Текст со средним уровнем удобочитаемости (уровень образования: 8-9 классов).')
elif fre.en > 70 and fre.en <= 80:
    print('Текст с уровнем удобочитаемости выше среднего (уровень образования: 7 классов).')
elif fre.en > 80 and fre.en <= 90:
    print('Текст с высоким уровнем удобочитаемости (уровень образования: 6 классов).')
elif fre.en > 90 and fre.en <= 100:
    print('Текст с очень высоким уровнем удобочитаемости (уровень образования: 5 классов).')

print('Предложений : ', sentences)
print('Слов: ', word_count)
print('Слогов: ', tsll)
print('Средняя длина предложения в словах: ', ASL)
print('Средняя длина слова в слогах: ', ASW)
print('Индекс удобочитаемости Флэша: ', fre.en)
print('Тональность текста: ' + sent)
print('Объективность: ', Sub_analysis)