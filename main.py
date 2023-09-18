'''

'''
from textblob import TextBlob
from googletrans import Translator

sentence = input('Введите текст: ')

translator = Translator()
translation = translator.translate(sentence)
trans = translation.text
print(trans)

sentences = trans.count('.') + trans.count('?') + trans.count('!') + trans.count('...')

word_count = sentence.count(" ") + 1

vowels_en = 'AEIOUYaeiouy'
tsll_en = 0
for i in range(len(trans)):
    if trans[i] in vowels_en:
        tsll_en = tsll_en + 1

sentiment = TextBlob(trans).polarity
if sentiment == 0:
    sent = 'нейтральный'
elif sentiment > 0:
    sent = 'положительный'
else:
    sent = 'отрицательный'

Sub_analysis = TextBlob(sentence).subjectivity

ASL = word_count / sentences
ASW = tsll_en / word_count

fre_en = 206.835 - 1.015 * ASL - 84.6 * ASW


if fre_en >= 0 and fre_en <= 30:
    print('Текст с очень низким уровнем удобочитаемости (уровень образования: выпускник колледжа.')
elif fre_en > 30 and fre_en <= 50:
    print('Текст с низким уровнем удобочитаемости (уровень образования: колледж).')
elif fre_en > 50 and fre_en <= 60:
    print ('Текст с уровнем удобочитаемости ниже среднего (уровень образования: 10-12 классов).')
elif fre_en > 60 and fre_en <= 70:
    print('Текст со средним уровнем удобочитаемости (уровень образования: 8-9 классов).')
elif fre_en > 70 and fre_en <= 80:
    print('Текст с уровнем удобочитаемости выше среднего (уровень образования: 7 классов).')
elif fre_en > 80 and fre_en <= 90:
    print('Текст с высоким уровнем удобочитаемости (уровень образования: 6 классов).')
elif fre_en > 90 and fre_en <= 100:
    print('Текст с очень высоким уровнем удобочитаемости (уровень образования: 5 классов).')

print('Предложений : ', sentences)
print('Слов: ', word_count)
print('Слогов: ', tsll_en)
print('Средняя длина предложения в словах: ', ASL)
print('Средняя длина слова в слогах: ', ASW)
print('Индекс удобочитаемости Флэша: ', fre_en)
print('Тональность текста: ' + sent)
print('Объективность: ', Sub_analysis)