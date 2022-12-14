def combine(consonants, vowels, n):
	combinations = {}
	for ru_con, be_con in consonants:
		for ru_vow, be_vow in vowels:
			if n == 1:
				combinations[ru_con+ru_vow] = "9"+be_con+"9"+be_vow+"9"
			else:
				combinations[be_con+be_vow] = "9"+ru_con+"9"+ru_vow+"9"
	return combinations

def paired_combinations(n=1):
	paired_consonants = (('б', 'б'), ('в', 'в'), ('г', 'г'), ('д', 'д'), ('з', 'з'), ('к', 'к'), ('л', 'л'), ('м', 'м'), ('н', 'н'), ('п', 'п'), ('р', 'р'), ('с', 'с'), ('т', 'т'), ('ф', 'ф'), ('х', 'х'))
	iotated_vowels = (('ё','ь9о'), ('ю','ь9у'), ('я','ь9а'), ('е','ь9э'))
	return combine(paired_consonants, iotated_vowels, n)

# буквосочетания с непарными мягкими согласными
def soft_combinations(n):
	soft_consonants = (('ч', 'ч'), ('щ', 'щ'))
	vowels = (('а', 'я'), ('у', 'ю'), ('о', 'ё'), ('и','и'))
	return combine(soft_consonants, vowels, n)

# буквосочетания с непарными твёрдыми согласными
def hard_combinations(n):
	hard_consonants = (('ж', 'ж'), ('ш', 'ш'), ('ц', 'ц'))
	vowels = (('е', 'э'), ('я', 'a'), ('ю', 'у'), ('ё', 'o'), ('и','ы'))
	return combine(hard_consonants, vowels, n)

def re(rules):
	nr = {}
	for ru, be in rules.items():
		nr[be] = ru
	return nr

rules = {'ться': 'ца', 'тся': 'цa', 
'шь ': 'ш ', 'щь ': 'щ ', 'чь ': 'ч ', 'жь ': 'ж ', 'ць ': 'ц ',  
'ъе': 'йэ', 'ъё': 'йо', 'ъя': 'йа', 'ъю': 'йу',
'тс': 'ц', 'зс': 'с', 'чш': 'тш', '':'9'}

rules9 = {'ться': 'ц9а', 'тся': 'ц9a', 
'шь ': 'ш ', 'щь ': 'щ ', 'чь ': 'ч ', 'жь ': 'ж ', 'ць ': 'ц ', 
'йе': 'й9э', 'йё': 'й9о', 'йя': 'й9а', 'йю': 'й9у', 
'ье': 'й9э', 'ьё': 'й9о', 'ья': 'й9а', 'ью': 'й9у', 
'ъе': 'й9э', 'ъё': 'й9о', 'ъя': 'й9а', 'ъю': 'й9у',
'тс': 'ц', 'зс': 'с', 'чш': 'т9ш'}

def irules():
	vowels = ('а', 'у', 'е', 'ы', 'о', 'э', 'я', 'и', 'ю', 'ё')
	iotated_vowels = (('ё','й9о'), ('е','й9э'), ('я','й9а'), ('ю', 'й9у'), ('и','й9и'))
	d = {}
	for v in vowels:
		for i in iotated_vowels:
			d[v+i[0]] = v+i[1]
	return d

def tr(text, replacement_sequence):
	for replacement_pairs in replacement_sequence:
		for ru, be in replacement_pairs.items():
			text = text.replace(ru, be)
			text = text.replace(ru.capitalize(), be.capitalize())
	return text

replacement_sequence = (irules(), rules9, soft_combinations(1), hard_combinations(1), soft_combinations(2), hard_combinations(2), paired_combinations(), re(rules))
test_text = '''зелёная щётка\n обливаться\n широкий подъезд\n МФЮА\n УдГУ\n июнь\n пью йогурт\n лучший
съешь же ещё этих мягких французских булок, да выпей чаю\n'''

while True:
	text = input("Введите текст (Enter для быстрого тэста): ")
	if text == '':
		text = test_text
		print(text)
	print('\n', tr(text, replacement_sequence),'\n\n')