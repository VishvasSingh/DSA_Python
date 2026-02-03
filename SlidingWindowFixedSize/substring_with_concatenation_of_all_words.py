from typing import List
from utils import time_it
from itertools import permutations

"""
DIFFICULTY: HARD

https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/


You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].



Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.


"""

@time_it
def find_substring(s: str, words: List[str]) -> List[int]:
    permutations_map = dict()
    permutations_list = ["".join(p) for p in permutations(words)]
    matched_indexes = []
    for word in permutations_list:
        permutations_map[word] = permutations_map.get(word, 0) + 1

    permutation_size = len(list(permutations_map.keys())[0])
    if len(s) < permutation_size:
        return []

    current_window = s[:permutation_size]
    if current_window in permutations_map:
        matched_indexes.append(0)

    for i in range(permutation_size, len(s)):
        current_window = current_window[1:]
        current_window += s[i]
        if current_window in permutations_map:
            matched_indexes.append(i-permutation_size+1)


    return matched_indexes




if __name__ == "__main__":
    s = "fffffffffffffffffffffffffffffffff"
    words = ["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
    print(find_substring(s, words))