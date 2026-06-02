class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphaToPosMap = dict()
        i = 0
        for alpha in order:
            alphaToPosMap[alpha] = i
            i += 1
        i = 0
        def lexCheck(word1, word2):
            j = 0
            for j in range(len(word1)):
                # if len(word2) > len(word1) given the prefix matches,
                if j == len(word2):
                    return False
                # if the letters are same, comparison do not matter
                if word1[j] != word2[j]:
                    if alphaToPosMap[word1[j]] > alphaToPosMap[word2[j]]:
                        return False
                    break
            return True
        # lexicographically compare 2 strings
        while i < len(words)-1:
            if not lexCheck(words[i], words[i+1]):
                return False
            i += 1
        return True
