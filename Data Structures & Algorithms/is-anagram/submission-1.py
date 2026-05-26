class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        characters = [0] * 26
        for char1 in s:
            characters[ord(char1) - ord('a')] += 1
        for char2 in t:
            characters[ord(char2) - ord('a')] -= 1
        for chars in characters:
            if chars != 0:
                return False
        return True