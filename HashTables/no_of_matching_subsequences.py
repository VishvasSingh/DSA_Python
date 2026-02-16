from typing import List
from collections import defaultdict

"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/number-of-matching-subsequences/description/

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.

"""

"""
BRUTE FORCE APPROACH: O(S. Words) worst case.
Space complexity: O(1)

def num_matching_subseq(s: str, words: List[str]) -> int:
    s_char_index_map = {}
    matching_subseq_count = 0

    for i in range(len(s)):
        if s[i] in s_char_index_map:
            s_char_index_map[s[i]].append(i)

        else:
            s_char_index_map[s[i]] = [i]

    for word in words:
        prev_matched_index = float('-inf')
        for char in word:

            if char not in s_char_index_map:
                break

            for index in s_char_index_map.get(char, []):
                if index > prev_matched_index:
                    prev_matched_index = index
                    break

            else:
                break

        else:
            matching_subseq_count += 1

    return matching_subseq_count
    
"""

def num_matching_subseq(s: str, words: List[str]) -> int:
    # 1. Create buckets for words waiting for specific characters
    # Key: character, Value: list of word iterators waiting for this char
    waiting_list = defaultdict(list)

    # 2. Initialize: Put every word in the bucket of its first character
    for word in words:
        it = iter(word)
        try:
            char = next(it)
            waiting_list[char].append(it)

        except StopIteration:
            continue # Skip empty words if any

    count = 0

    # 3. Process the string s once
    for char in s:
        # Get the list of words waiting for this specific character 'char'
        # We must reassign to [] because we are about to process them all
        curr_char_words_iterators = waiting_list[char]
        waiting_list[char] = []

        for word_it in curr_char_words_iterators:
            try:
                # Advance the iterator to the next character
                next_char = next(word_it)
                # Move this word to the bucket of the next character it needs
                waiting_list[next_char].append(word_it)

            except StopIteration:
                # If StopIteration is raised, the word is fully consumed!
                count += 1

    return count





if __name__ == "__main__":
    # s = "dsahjpjauf"
    # words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    words = ["a","bb","acd","ace"]
    s = "abcde"
    print(num_matching_subseq(s, words))