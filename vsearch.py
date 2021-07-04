def search4vowels(phrase:str):
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou'):
    return set(letters).intersection(set(phrase))

    