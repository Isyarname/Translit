import json

fileName = "dictionary.json"

def read(fileName):
	with open(fileName, "r", encoding = "UTF-8") as file:
		return json.load(file)

def write(fileName, data):
	with open(fileName, "w", encoding = "UTF-8") as file:
		json.dump(data, file)

def display_dictionary(data):
	for k, v in data.items():
		print(k, v, "\n")






def combine(consonants, vowels):
	combinations = {}
	for cy_con, la_con in consonants:
		for cy_vow, la_vow in vowels:
			combinations[cy_con+cy_vow] = la_con+la_vow
	return combinations

# буквосочетания с парными мягкими согласными
def paired_combinations():
	paired_consonants = (('б', 'b'), ('в', 'v'), ('г', 'g'), ('д', 'd'), ('з', 'z'), ('к', 'k'), ('л', 'l'), ('м', 'm'), ('н', 'n'), ('п', 'p'), ('р', 'r'), ('с', 's'), ('т', 't'), ('ф', 'f'), ('х', 'h'))
	iotated_vowels = (('е', 'e'), ('я', "'a"), ('ю', "'u"), ('ё', "'o"))
	return combine(paired_consonants, iotated_vowels)

# буквосочетания с непарными мягкими согласными
def soft_combinations():
	soft_consonants = (('ч', 'č'), ('щ', 'ŝ'))
	vowels = (('е', 'e'), ('я', 'a'), ('ю', 'u'), ('ё', 'o'), ('и','i'))
	return combine(soft_consonants, vowels)

# буквосочетания с непарными твёрдыми согласными
def hard_combinations():
	hard_consonants = (('ж', 'ž'), ('ш', 'š'), ('ц', 'c'))
	vowels = (('е', 'e'), ('я', 'a'), ('ю', 'u'), ('ё', 'o'), ('и','y'))
	return combine(hard_consonants, vowels)






data = read(fileName)

letters = data["letters"]
ec = data["exception combinations"]
oe = data["other edits"]
pc = data["paired combinations"]
sc = data["soft combinations"]
hc = data["hard combinations"]


d = [ec, oe, pc, sc, hc]
for i in d:
	for cy1, la1 in i.items():
		for j in d:
			if i == j:
				continue
			for cy2, la2 in j.items():
				if cy1[-1] == cy2[0]:
					cy = cy1+cy2[1:]
					if not cy in data["exception combinations"].keys():
						data["mixed combinations"][cy] = la1+la2[1:]

#write(fileName, data)
display_dictionary(data)