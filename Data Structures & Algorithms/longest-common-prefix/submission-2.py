class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for ptr in range(len(strs[0])):
            cur_char = strs[0][ptr]
            for num_str in range(1, len(strs)):
                if ptr >= len(strs[num_str]) or strs[num_str][ptr] != cur_char:
                    return prefix
            prefix += cur_char

        return prefix
