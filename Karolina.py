from textblob import TextBlob

sentence = str(input())
word_count = sentence.count(" ") + 1
print("Количество слов в строке:", word_count)