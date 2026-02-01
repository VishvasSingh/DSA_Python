from typing import Dict

"""
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters


"""

def compare_dict(dict1: Dict, dict2: Dict) -> bool:
    if dict1.keys() != dict2.keys():
        return False

    for key, value in dict1.items():
        if key not in dict2:
            return False

        if value != dict2[key]:
            return False


    return True


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    char_count_map_source = {}
    char_count_map_target = {}
    for i in range(len(s1)):
        char_count_map_target[s1[i]] = char_count_map_target.get(s1[i], 0) + 1

    for i in range(len(s1)):
        char_count_map_source[s2[i]] = char_count_map_source.get(s2[i], 0) + 1

    if compare_dict(char_count_map_source,char_count_map_target):
        return True

    for i in range(len(s1), len(s2)):
        curr_char = s2[i-len(s1)]
        if char_count_map_source[curr_char] == 1:
            del char_count_map_source[curr_char]

        else:
            char_count_map_source[curr_char] = char_count_map_source[curr_char] - 1

        char_count_map_source[s2[i]] = char_count_map_source.get(s2[i], 0) + 1
        if compare_dict(char_count_map_source, char_count_map_target):
            return True

    return False


if __name__ == "__main__":
    s1, s2 = "abaa", "abababacaababbaa"
    print(check_inclusion(s1, s2))
