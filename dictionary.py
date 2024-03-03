#extracting meaning using python lib PyDictionary 
#simple 

from PyDictionary import PyDictionary

dictionary = PyDictionary()
word = input('asd')
meaning = dictionary.meaning(word)

print(f"the meaning of '{word}' is")
for part_of_speech, definitions in meaning.items():
    print(f"{part_of_speech.capitalize()}:")
    for definition in definitions:
        print(f"- {definition}")
