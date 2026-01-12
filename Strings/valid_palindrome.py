"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


"""

"""
This is the correct approach, however we are storing the cleaned string, which means it has O(S) 
space complexity, Time complexity is still O(S)
"""

# def valid_palindrome(s: str) -> bool:
#     cleaned = ''.join(char.lower() for char in s if char.isalnum())
#     i = 0
#     j = len(cleaned)-1
#
#     while i < j:
#         if cleaned[i] == cleaned[j]:
#             i += 1
#             j -= 1
#
#         else:
#             return False
#
#     return True

"""
Optimized approach, with O(1) space and O(S) time
"""

# def valid_palindrome(s: str) -> bool:
#     i = 0
#     j = len(s)-1
#
#     while i < j:
#         if s[i].isalnum() and s[j].isalnum():
#             if s[i].lower() == s[j].lower():
#                 i += 1
#                 j -= 1
#
#             else:
#                 return False
#
#         elif s[i].isalnum() and not s[j].isalnum():
#             j -= 1
#             # when j is not alphanumeric,
#             # just decrease j to reach a valid character
#
#         elif not s[i].isalnum() and s[j].isalnum():
#             i += 1
#             # when i is not alphanumeric,
#             # just increase i to reach a valid character
#
#         else:
#             # when both are invalid characters move onto next from each side
#             i += 1
#             j -= 1
#
#     return True


"""
Optimized approach with cleaner code, with O(1) space and O(S) time
"""


def valid_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        # Fast-forward i until it hits a valid char
        while i < j and not s[i].isalnum():
            i += 1

        # Rewind j until it hits a valid char
        while i < j and not s[j].isalnum():
            j -= 1

        # Compare
        if s[i].lower() != s[j].lower():
            return False

        # Move pointers inward after a successful match
        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    print(valid_palindrome(string))