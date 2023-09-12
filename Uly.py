# fre - Flesch reading ease scale
# ASL - average sentence length
# ASW - average number of syllables per word
# ASL = total words/total sentences
# ASW = total syllables/total words
tw =
tsn =
tsll =
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
    print('')
elif fre.en > 80 and fre.en <= 90:
    print('')
elif fre.en > 90 and fre.en <= 100:
    print('')