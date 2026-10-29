class WordDictionary:

    def __init__(self):
        self.tries = {}
        

    def addWord(self, word: str) -> None:
        curr = self.tries
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = "*"
        

    def search(self, word: str) -> bool:
        def dfs(curr, index):
            if index == len(word):
                return '*' in curr

            letter = word[index]
            if letter != '.':
                if letter not in curr:
                    return False
                return dfs(curr[letter], index + 1)

            for letter in curr:
                if letter != '*':
                    if dfs(curr[letter], index + 1):
                        return True
            return False
        return dfs(self.tries, 0)

        
