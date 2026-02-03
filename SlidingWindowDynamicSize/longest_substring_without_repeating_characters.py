
"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

"""
SCRATCHPAD:

S = ()

s = "abcabcbb"

i == 0:
curr_window = (a)
curr_window_len = 1
max_window_len = 1

i == 1:
curr_window = (a, b)
curr_window_len = 2
max_window_len = 2

i == 2:
curr_window = (a, b, c)
curr_window_len = 3
max_window_len = 3

i == 3:
curr_window = (a, b, c)
curr_window_len = 3
max_window_len = 3

remove i-curr_window_len from the curr_window_set = (b, c)
curr_window_len = 2
max_window_len = 3


"""


"""
Time Complexity O(N * K) (due to dict copy/loop)
Space Complexity: O(K)

def length_of_longest_substring(s: str) -> int:
    current_window_elements_index_mapping = dict()
    max_window_len = 0
    for i in range(len(s)):
        if s[i] in current_window_elements_index_mapping:
            prev_same_char_index = current_window_elements_index_mapping[s[i]]
            for key, val in current_window_elements_index_mapping.copy().items():
                if val <= prev_same_char_index:
                    del current_window_elements_index_mapping[key]

        current_window_elements_index_mapping[s[i]] = i



        max_window_len = max(max_window_len, len(current_window_elements_index_mapping))


    return max_window_len
    
"""

"""
Optimized approach: Pure O(N)

"""


def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If we have seen the char before, AND it's inside the current window
        if char in char_index_map and char_index_map[char] >= left:
            # Move the left pointer to the right of the previous occurrence
            left = char_index_map[char] + 1

        # Update the character's latest index
        char_index_map[char] = right

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len


"""
Alternate optimized approach using Set:

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If s[right] is already in the set, we have a duplicate.
        # Shrink the window from the left until s[right] is removed from the set.
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Add the current character
        char_set.add(s[right])
        
        # Update max length
        max_len = max(max_len, right - left + 1)
        
    return max_len

"""





if __name__ == "__main__":
    s = "pwwkew"
    print(length_of_longest_substring(s))