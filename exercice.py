#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	#aller chercher premier nom
	premier_nom = name.split("-")[0]
	#mettre la première lettre en majuscule et le reste en minuscules
	case = premier_nom[0].upper()+premier_nom[1:].lower()

	return "Bonjour "+case

def get_random_sentence(animals, adjectives, fruits):
	#choisir animal
	emplacement=random.randint(0, 2)
	animal=animals[emplacement]
	#choisir adjectif
	emplacement = random.randint(0, 2)
	adjectif=adjectives[emplacement]
	#choisir fruit
	emplacement = random.randint(0, 2)
	fruit=fruits[emplacement]
	return f"Aujourd’hui, j’ai vu un {animal} s’emparer d’un panier {adjectif} plein de {fruit}."

def encrypt(text, shift):
	code_secret=""
	for n in range (len(text)):
		if text[n].isalpha():
			lettre = (text[n]).upper()
			if (ord(lettre) + shift > 90):
				lettre_code = chr(ord(lettre)-(26-shift))
			else:
				lettre_code = chr(ord(lettre)+shift)
			code_secret += lettre_code
		else:
			code_secret += text[n]
	return code_secret

def decrypt(encrypted_text, shift):
	message_ini = ""
	for n in range(len(encrypted_text)):
		if encrypted_text[n].isalpha():
			lettre = (encrypted_text[n]).upper()
			if (ord(lettre) - shift < 65):
				lettre_code = chr(ord(lettre) + (26 - shift))
			else:
				lettre_code = chr(ord(lettre) - shift)
			message_ini += lettre_code
		else:
			message_ini += encrypted_text[n]

	return message_ini


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
