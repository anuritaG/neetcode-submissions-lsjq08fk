class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        firstWrd, secondWrd = 0, 0
        while firstWrd < len(word1) and secondWrd < len(word2):
            result += word1[firstWrd]
            result += word2[secondWrd]
            firstWrd += 1
            secondWrd += 1
        if firstWrd < len(word1):
            result += word1[firstWrd:]
        if secondWrd < len(word2):
            result += word2[secondWrd:]
        return result