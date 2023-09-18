from googletrans import Translator
#a = input('Введите текст: ')
#translator = Translator()
#result = translator.translate('Привет!')
#print(result.text)


from textblob import TextBlob
#sentence = TextBlob("what is your name")
#a = sentence.translate(to= "es")
#print(a)

s1 = input('Введите текст: ')
sentences = s1.count('.') + s1.count('?') + s1.count('!') + s1.count('...')
print('Количество предложений:', sentences)

sentiment = TextBlob(s1).polarity
if sentiment == 0:
    sent = 'нейтральный'
elif sentiment >0:
    sent = 'положительный'
else:
    sent = 'отрицательный'
print('Тональность текста: ' + sent)

