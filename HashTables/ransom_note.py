"""
DIFFICULTY: EASY

https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

"""

def can_construct(ransom_note: str, magazine: str) -> bool:
    char_count_map = dict()
    for char in magazine:
        char_count_map[char] = char_count_map.get(char, 0) + 1

    for char in ransom_note:
        if char_count_map.get(char, 0) <= 0:
            return False

        else:
            char_count_map[char] = char_count_map[char] - 1

    return True



if __name__ == "__main__":
    ransom_note = 'ab'
    magazine = 'aab'
    print(can_construct(ransom_note, magazine))
