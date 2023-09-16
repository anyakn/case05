'''

'''
from textblob import TextBlob
sentence = str(input())


word_count = sentence.count(" ") + 1



Sub_analysis = TextBlob(sentence).subjectivity

text = input('Введите текст: ')
print('Предложений : ')
print('Слов: ', word_count)
print('Слогов: ')
print('Средняя длина предложения в словах: ')
print('Средняя длина слова в слогах: ')
print('Индекс удобочитаемости Флэша: ')
print('Тональность текста: ')
print('Объективность: ', Sub_analysis)