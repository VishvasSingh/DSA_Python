"""
https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


"""

"""
Optimized approach -> O(T)
"""

# def is_subsequence(s: str, t: str) -> bool:
#     i, j = 0, 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#
#         j += 1
#
#     if i == len(s):
#         return True
#
#     return False


"""
Optimized for billion of strings
"""
def is_subsequence(s: str, t: str) -> bool:
    char_index_mapping = {}
    for index, char in enumerate(t):
        if char_index_mapping.get(char):
            char_index_mapping[char].append(index)
        else:
            char_index_mapping[char] = [index]

    prev_index = -1
    for index, char in enumerate(s):
        char_indexes = char_index_mapping.get(char)
        if char_indexes:
            for each_index in char_indexes:
                if each_index > prev_index:
                    prev_index = each_index
                    break

            else:
                return False

        else:
            return False

    return True


"""


import bisect
from collections import defaultdict

def is_subsequence_optimized(s: str, t: str) -> bool:
    # Preprocessing (done once)
    char_map = defaultdict(list)
    for i, char in enumerate(t):
        char_map[char].append(i)

    # Query Processing
    prev_index = -1
    for char in s:
        # If char not in t, return False immediately
        if char not in char_map:
            return False
            
        indices_list = char_map[char]
        
        # Binary Search: Find the first index in indices_list that is > prev_index
        # bisect_right returns the insertion point to maintain order
        i = bisect.bisect_right(indices_list, prev_index)
        
        # If the insertion point is at the end, it means all indices are <= prev_index
        if i == len(indices_list):
            return False
            
        # Update prev_index to the actual index found
        prev_index = indices_list[i]
        
    return True
"""



if __name__ == "__main__":
    s = "abc"
    t = "acb"
    print(is_subsequence(s, t))