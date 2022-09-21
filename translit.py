import json

fileName = "dictionary.json"

def read(fileName):
	with open(fileName, "r", encoding = "UTF-8") as file:
		return json.load(file)

def cyrillic_to_latin(text, replacement_sequence):
	for replacement_pairs in replacement_sequence:
		for cy, la in replacement_pairs.items():
			text = text.replace(cy, la)
			text = text.replace(cy.capitalize(), la.capitalize())
	return text

data = read(fileName)
replacement_sequence = (data["mixed combinations"], data["exception combinations"], data["paired combinations"], data["soft combinations"], data["hard combinations"], data["other edits"], data["letters"])

test_text = '''зелёная щётка\n обливаться\n широкий подъезд\n МФЮА\n УдГУ\n июнь\n пью йогурт\n лучший
съешь же ещё этих мягких французских булок, да выпей чаю\n'''

while True:
	text = input("Введите текст (Enter для быстрого тэста): ")
	if text == '':
		text = test_text
		print(text)
	print('\n', cyrillic_to_latin(text, replacement_sequence),'\n\n')