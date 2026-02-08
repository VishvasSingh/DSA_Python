
"""
DIFFICULTY: EASY

https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true



Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


"""

def is_isomorphic(s: str, t: str) -> bool:
    s_t_map = {}
    t_s_map = {}
    for char_s, char_t in zip(s ,t):
        if char_s in s_t_map and s_t_map.get(char_s) != char_t:
            return False

        elif char_t in t_s_map and t_s_map.get(char_t) != char_s:
            return False

        else:
            s_t_map[char_s] = char_t
            t_s_map[char_t] = char_s
    return True


if __name__ == "__main__":
    s = 'badc'
    t = 'baba'
    print(is_isomorphic(s, t))
