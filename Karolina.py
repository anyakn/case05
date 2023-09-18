from textblob import TextBlob

sentence = str(input())
words_count = sentence.count(" ") + 1
print("Количество слов в строке:", words_count)

subject = TextBlob(sentence).subjectivity

print('Объективность: ', subject)