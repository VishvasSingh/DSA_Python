from typing import List, Dict

"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

"""


"""
Scratchpad:

s = "cbaebabacd", p = "abc"

char_count_map = {c: 1, b: 1, a:1}
p = abc


"""

"""
Brute force approach: 

def is_anagram(char_count_map: Dict, p: str) -> bool:
    for i in range(len(p)):
        if p[i] not in char_count_map:
            return False

        else:
            char_count_map[p[i]] = char_count_map[p[i]] - 1

    for count in char_count_map.values():
        if count != 0:
            return False

    return True

def find_anagrams(s: str, p:str) -> List[int]:
    if len(p) > len(s):
        return []

    char_count_map = {}
    anagrams = list()
    for i in range(len(p)):
        char_count_map[s[i]] = char_count_map.get(s[i], 0) + 1

    if is_anagram(char_count_map.copy(), p):
        anagrams.append(0)

    for i in range(len(p), len(s)):
        char_count_map[s[i-len(p)]] = char_count_map[s[i-len(p)]] - 1
        char_count_map[s[i]] = char_count_map.get(s[i], 0) + 1
        if is_anagram(char_count_map.copy(), p):
            anagrams.append(i-(len(p)-1))

    return anagrams

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


def find_anagrams(s: str, p:str) -> List[int]:
    if len(p) > len(s):
        return []

    char_count_map_source = {}
    char_count_map_target = {}
    anagrams = list()
    for i in range(len(p)):
        char_count_map_source[s[i]] = char_count_map_source.get(s[i], 0) + 1

    for i in range(len(p)):
        char_count_map_target[p[i]] = char_count_map_target.get(p[i], 0) + 1

    if compare_dict(char_count_map_source,char_count_map_target):
        anagrams.append(0)

    for i in range(len(p), len(s)):
        curr_char = s[i-len(p)]
        if char_count_map_source[curr_char] == 1:
            del char_count_map_source[curr_char]

        else:
            char_count_map_source[curr_char] = char_count_map_source[curr_char] - 1

        char_count_map_source[s[i]] = char_count_map_source.get(s[i], 0) + 1
        if compare_dict(char_count_map_source, char_count_map_target):
            anagrams.append(i-(len(p)-1))

    return anagrams




if __name__ == "__main__":
    s = "aa"
    p = "bb"
    print(find_anagrams(s,p))