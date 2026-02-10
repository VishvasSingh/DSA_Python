from typing import List

"""
DIFFICULTY: MEDIUM 

https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_str_mapping = {}
    for str in strs:
        char_map = {}
        for char in str:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        anagram_key = ''

        for key in sorted(list(char_map.keys())):
            anagram_key += f"{key}:{char_map[key]}"
            """
            Instead of manually building the string "a:1e:1t:1", you could do this:
            Sort the string: key = tuple(sorted(s)) -> ('a', 'e', 't'). 
            Trade-off: This changes complexity to O(N.K log K) because of sorting the whole string.
            
            Count Tuple: Create a tuple of 26 zeros, update counts, and use that as the key.
            key becomes (1, 0, 0, 1, ..., 1, ...) (counts for a, b, c... z).
            This preserves your O(N.K) efficiency with less code.
            """

        if anagram_key in anagram_str_mapping:
            anagram_str_mapping[anagram_key].append(str)

        else:
            anagram_str_mapping[anagram_key] = [str]

    return list(anagram_str_mapping.values())


if __name__ == "__main__":
    # strs = ["eat","tea","tan","ate","nat","bat"]
    strs = ["ddddddddddg","dgggggggggg"]
    print(group_anagrams(strs))