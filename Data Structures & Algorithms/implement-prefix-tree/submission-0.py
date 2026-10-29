class PrefixTree:

    def __init__(self):
        self.tries = {}
        

    def insert(self, word: str) -> None:
        dictionary = self.tries
        for char in word:
            if char not in dictionary:
                dictionary[char] = {}
            dictionary = dictionary[char]
        dictionary['.'] = '.'


    def search(self, word: str) -> bool:
        dictionary = self.tries
        for char in word:
            if char not in dictionary:
                return False
            dictionary = dictionary[char]
        return '.' in dictionary
        

    def startsWith(self, prefix: str) -> bool:
        dictionary = self.tries
        for char in prefix:
            if char not in dictionary:
                return False
            dictionary = dictionary[char]
        return True
        