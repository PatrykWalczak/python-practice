# pierwsza funkcja ktora sprawdza wporwadzone słowo i tworzy z niego słownik 
# ktory sprawdza ile razy wystepuje dana litera w podanym słowie

# word to argument funkcji, który w tym wypadku nie musi być przekazywany bezpośrednio w main ponieważ
# druga funkcja wywołuję pierwszą 
def letter_counts(word):
    #  pusty słownik
    counts = {}
    #  dla każdej literki w słowie
    for letter in word:
        #  sprawdzam czy litera jest już w słowniku
        if letter in counts:
            #  jesli jest - zwiększaj jej licznik występowania o 1
            counts[letter] += 1
        #  jeśli jej nie ma
        else:
            #  wpisuje ją pierwszy raz do słownika
            counts[letter] = 1
    #  funckja zwraca counts czyli utworzony słownik z wyrazu np. "dom" > zwraca {"d": 1, "o": 1, "m": 1}        
    return counts


#  druga funkcja, przyjmująca dwa paramtery i sprawdzająca czy dwa słowa to anagram czy też nie

def are_anagrams(word1, word2):
    #  sprawdzamy i tutaj wywołujemy 1 funkcję na zmiennej czyli w tym wypadku word1 gdzie 
    #  word 1 to wprowadzony w main() na sztywno wyraz
    #  porówujemy teraz ze sobą word1 i word2 i sprawdzamy, czy te słowniki są takie same

    #  i tutaj cała magia działania 
    if letter_counts(word1) == letter_counts(word2):
        print("Its anagram")
    else:
        print("Not anagram !")


def main():
    are_anagrams(input("Podaj pierwsze słowo: ").lower(), input("Podaj drugie słowo: ").lower())

main()