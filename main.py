'''

'''
from textblob import TextBlob
from googletrans import Translator
import ru_local as ru

sentence = input(ru.start)

translator = Translator()
translation = translator.translate(sentence)
trans = translation.text

sentences_count = sentence.count('.') + sentence.count('?') + sentence.count('!') + sentence.count('...')
if sentences_count == 0:
    sentences_count = 1

words_count = sentence.count(" ") + 1

vowels_count = 'AEIOUYaeiouyауоыиэяюёеАУОЫИЭЯЮЕЁ'
tsll_count = 0
for i in range(len(sentence)):
    if sentence[i] in vowels_count:
        tsll_count = tsll_count + 1

sentiment = TextBlob(trans).polarity
if sentiment == 0:
    sent = ru.neutral
elif sentiment > 0:
    sent = ru.positive
else:
    sent = ru.negative

subjectivity = TextBlob(trans).subjectivity
percentage = str(round(subjectivity * 100))

ASL = words_count / sentences_count
ASW = tsll_count / words_count

fre_en = 206.835 - 1.015 * ASL - 84.6 * ASW


if fre_en >= 0 and fre_en <= 30:
    print(ru.fre_en1)
elif fre_en > 30 and fre_en <= 50:
    print(ru.fre_en2)
elif fre_en > 50 and fre_en <= 60:
    print(ru.fre_en3)
elif fre_en > 60 and fre_en <= 70:
    print(ru.fre_en4)
elif fre_en > 70 and fre_en <= 80:
    print(ru.fre_en5)
elif fre_en > 80 and fre_en <= 90:
    print(ru.fre_en6)
elif fre_en > 90 and fre_en <= 100:
    print(ru.fre_en7)

print('Предложений : ', sentences_count)
print('Слов: ', words_count)
print('Слогов: ', tsll_count)
print('Средняя длина предложения в словах: ', ASL)
print('Средняя длина слова в слогах: ', ASW)
print('Индекс удобочитаемости Флэша: ', fre_en)
print('Тональность текста: ' + sent)
print('Объективность: ' + percentage + '%')
