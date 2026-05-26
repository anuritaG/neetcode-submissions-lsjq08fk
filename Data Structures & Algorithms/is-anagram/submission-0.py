class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for char1 in s:
            if char1 in characters:
                characters[char1] += 1
            else:
                characters[char1] = 1
        for char2 in t:
            if char2 not in characters:
                return False
            characters[char2] -= 1
            if characters[char2] == 0:
                characters.pop(char2)
        print(characters)
        if len(characters) == 0:
            return True
        return False