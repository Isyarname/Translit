# отдельные буквы
letters = {
	'а':'a', 'б':'b', 'в':'v', 'г':'g', 
	'д':'d', 'е':'e', 'ё':'jo', 'ж':'ž', 'з':'z',
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
	'йе':'e', 'йё':'jo', 'йя':'ja', 'йю':'ju',
	'ье':'e', 'ьё':'jo', 'ья':'ja', 'ью':'ju'
}

# прочие правки
other_edits = {'тс':'c'}

# буквосочетания с парными мягкими согласными
def paired_combinations():
	paired_consonants = {'б':'b', 'в':'v', 'г':'g', 'д':'d', 'з':'z', 'к':'k', 'л':'l', 'м':'m', 'н':'n', 'п':'p', 'р':'r', 'с':'s', 'т':'t', 'ф':'f', 'х':'h'}
	iotated_vowels = {"е":"e", "я":"'a", "ю":"'u", "ё":"'o"}
	return combine(paired_consonants, iotated_vowels)

# буквосочетания с мягкими и твёрдыми согласными
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

def cyrillic_to_latin(text, replace_queue):
	for d in replace_queue:
		for cy, la in d.items():
			text = text.replace(cy, la)
			text = text.replace(cy.capitalize(), la.capitalize())
	return text

p_comb = paired_combinations()
u_comb = unpaired_combinations()
replace_queue = (exception_combinations, u_comb, p_comb, other_edits, letters)

text = '''Че́шский алфави́т (чеш. Česká abeceda) — вариант латиницы, который используется при написании на чешском языке. Основные принципы этого алфавита: «один звук — одна буква» и добавление диакритических знаков над буквами для обозначения звуков, далёких от латинского языка.
Алфавиты некоторых других восточноевропейских языков (славянские, балтийские, эстонский) основаны на чешском алфавите, в котором убираются или добавляются символы в соответствии с потребностью в них в языке. Наиболее заметным отклонением от чешского является польский алфавит, который разрабатывался независимо.'''

print(cyrillic_to_latin(text, replace_queue))