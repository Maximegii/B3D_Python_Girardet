import re
import string
import unicodedata

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé.")
        return 0

def count_sentences(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            sentences = re.split(r'[.!?]', text)
            sentence_count = 0
            for sentence in sentences:
                if sentence.strip():
                    sentence_count += 1
            return sentence_count
    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé.")
        return 0
    
def count_vowels(filename):
    try:
        with open(filename , 'r', encoding='utf-8') as file:
            text = file.read()
            vowels = re.findall(r'[aeiouyAEIOUY]', text)
            return len(vowels)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé.")
        return 0

def count_five_words_most_used(filename):
    
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            word_count = {}
            for word in words:
                word = word.strip(string.punctuation).lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            return sorted_word_count[:5]
        
def count_five_word_most_used_with_more_than_7_letters(filename):
    
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        word_count = {}
        for word in words:
            word = word.strip(string.punctuation).lower()
            if len(word) > 7:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_word_count[:5]
    
def candideGen(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        
        
        letter_sequences = {}
        for char in text:
            if char.isalpha():
                char_normalized = unicodedata.normalize('NFD', char)
                
                char_base = char_normalized[0].lower()
                if char_base in letter_sequences:
                    letter_sequences[char_base] += char
                else:
                    letter_sequences[char_base] = char
        
        sorted_sequences = dict(sorted(letter_sequences.items()))
        
        with open('myCandideGen.txt', 'w', encoding='utf-8') as output_file:
            for sequence in sorted_sequences.values():
                output_file.write(sequence + '\n')
        
    

filename = 'candide.txt'
candideGen(filename)
most_used_words = count_five_words_most_used(filename)
most_used_words_with_more_than_7_letters = count_five_word_most_used_with_more_than_7_letters(filename)
word_count = count_words(filename)
sentence_count = count_sentences(filename)
vowels_count = count_vowels(filename)
print(f"Le fichier {filename} contient : {word_count} mots.")
print(f"Le fichier {filename} contient : {sentence_count} phrases.")
print(f"Le fichier {filename} contient : {vowels_count} voyelles.") 
print(f"Les 5 mots les plus utilisés sont : {most_used_words}")
print(f"Le mot le plus utilisé avec plus de 7 lettres est : {most_used_words_with_more_than_7_letters}")


    
        