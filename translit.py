# отдельные буквы
letters = {
	'а':'a', 'б':'b', 'в':'v', 'г':'g', 
	'д':'d', 'е':'je', 'ё':'jo', 'ж':'ž', 'з':'z',
	'и':'i', 'й':'j', 'к':'k', 'л':'l', 'м':'m',
	'н':'n', 'о':'o', 'п':'p', 'р':'r',
	'с':'s', 'т':'t', 'у':'u', 'ф':'f',
	'х':'h', 'ц':'c', 'ч':'č', 'ш':'š',
	'щ':'ŝ', 'ъ':'', 'ы':'y', "ь":"'", 'э':'ě',
	'ю':'ju', 'я':'ja'
}

# буквосочетания-исключения
exception_combinations = {
	'ци':'cy', 'жи':'žy', 'ши':'šy',
	'ться':'ca', 'тся':'ca',
	'йе':'je', 'йё':'jo', 'йя':'ja', 'йю':'ju',
	'ье':'je', 'ьё':'jo', 'ья':'ja', 'ью':'ju',
	'ъе':'je', 'ъё':'jo', 'ъя':'ja', 'ъю':'ju'
}

# прочие правки
other_edits = {'тс':'c'}

# буквосочетания с парными мягкими согласными
def paired_combinations():
	paired_consonants = {'б':'b', 'в':'v', 'г':'g', 'д':'d', 'з':'z', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'ф':'f', 'х':'h'}
	iotated_vowels = {"е":"e", "я":"'a", "ю":"'u", "ё":"'o"}
	return combine(paired_consonants, iotated_vowels)

# буквосочетания с непарными мягкими и твёрдыми согласными
def unpaired_combinations():
	unpaired_consonants = {'ч':'č', 'щ':'ŝ', 'ж':'ž', 'ш':'š', 'ц':'c'}
	vowels = {"е":"e", "я":"a", "ю":"u", "ё":"o", "и":"и"}
	return combine(unpaired_consonants, vowels)

def combine(consonants, vowels):
	combinations = {}
	for cy_con, la_con in consonants.items():
		for cy_vow, la_vow in vowels.items():
			combinations.update({cy_con+cy_vow:la_con+la_vow})
	return combinations

def cyrillic_to_latin(text, replacement_sequence):
	for d in replacement_sequence:
		for cy, la in d.items():
			text = text.replace(cy, la)
			text = text.replace(cy.capitalize(), la.capitalize())
	return text

replacement_sequence = (exception_combinations, unpaired_combinations(), paired_combinations(), other_edits, letters)
text = input("Введите текст: ")
print(cyrillic_to_latin(text, replacement_sequence))