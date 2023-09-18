'''

'''
from textblob import TextBlob
sentence = input('Введите текст: ')


word_count = sentence.count(" ") + 1

sentences = sentence.count('.') + sentence.count('?') + sentence.count('!') + sentence.count('...')

sentiment = TextBlob(sentence).polarity
if sentiment == 0:
    sent = 'нейтральный'
elif sentiment >0:
    sent = 'положительный'
else:
    sent = 'отрицательный'

Sub_analysis = TextBlob(sentence).subjectivity


print('Предложений : ', sentences)
print('Слов: ', word_count)
print('Слогов: ')
print('Средняя длина предложения в словах: ')
print('Средняя длина слова в слогах: ')
print('Индекс удобочитаемости Флэша: ')
print('Тональность текста: ' + sent)
print('Объективность: ', Sub_analysis)