# fre - Flesch reading ease scale
# ASL - average sentence length
# ASW - average number of syllables per word
# ASL = total words/total sentences
# ASW = total syllables/total words
tw =
tsn =

tsll = 0
vowels = set('aeiou')
for letter in s:
    if letter in vowels:
        tsll += 1
print (tsll)

asl = tw/tsn
asw = tsll/tw
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

if fre.ru >= 0 and fre.ru <= 30:
    print('Текст с очень низким уровнем удобочитаемости (уровень образования: выпускник колледжа.')
elif fre.ru > 30 and fre.ru <= 50:
    print('Текст с низким уровнем удобочитаемости (уровень образования: колледж).')
elif fre.ru > 50 and fre.ru <= 60:
    print ('Текст с уровнем удобочитаемости ниже среднего (уровень образования: 10-12 классов).')
elif fre.ru > 60 and fre.ru <= 70:
    print('Текст со средним уровнем удобочитаемости (уровень образования: 8-9 классов).')
elif fre.ru > 70 and fre.ru <= 80:
    print('Текст с уровнем удобочитаемости выше среднего (уровень образования: 7 классов).')
elif fre.ru > 80 and fre.ru <= 90:
    print('Текст с высоким уровнем удобочитаемости (уровень образования: 6 классов).')
elif fre.ru > 90 and fre.ru <= 100:
    print('Текст с очень высоким уровнем удобочитаемости (уровень образования: 5 классов).')