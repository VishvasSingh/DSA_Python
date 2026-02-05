"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/longest-repeating-character-replacement/description/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


"""

"""
SCRATCHPAD

s = "AABABABBBA"
k = 2
left = 0, right = 0
window is valid until we have (window_size - most_freq_char_curr_window <=k)


"""



def character_replacement(s: str, k: int) -> int:
    max_window_size = 0
    char_count_map = {}
    left = 0

    for right in range(len(s)):
        char_count_map[s[right]] = char_count_map.get(s[right], 0) + 1

        while left < right and (right-left + 1 - max(char_count_map.values())) > k:
            char_count_map[s[left]] = char_count_map.get(s[left], 0) - 1
            left += 1

        max_window_size = max(max_window_size, right - left + 1)


    return max_window_size



if __name__ == "__main__":
    s = 'AAAABABBB'
    k = 1
    print(character_replacement(s, k))