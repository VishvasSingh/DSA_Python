
"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""

"""
Time Optimized approach: O(S) time and O(s) space 
"""

# def reverse_words(s: str) -> str:
#     word_container = list()
#     output = ""
#     i = len(s)-1
#     while i >= 0:
#         if s[i].isalnum():
#             word_container.append(s[i])
#
#         if (s[i] == " " or i == 0) and word_container:
#             output += f"{''.join(reversed(word_container))}" \
#                 if len(output) == 0 else f" {''.join(reversed(word_container))}"
#             word_container.clear()
#
#
#
#         i -= 1
#
#     return output


def reverse_words(s: str) -> str:
    word_container = []
    final_words = []

    # Iterate backwards
    i = len(s) - 1
    while i >= 0:
        # Collect non-space characters
        if s[i] != ' ':
            word_container.append(s[i])

        # If we hit a space (or end of string) AND we have a word pending
        if (s[i] == ' ' or i == 0) and word_container:
            # Since we collected backwards ('e', 'u', 'l', 'b'), reversing gives 'blue'
            final_words.append("".join(reversed(word_container)))
            word_container.clear()

        i -= 1

    return " ".join(final_words)


"""

Space optimized approach: 
In python strings are immutable, so we can not have a O(1) space approach. But the idea is to have whole string reversed
and then find out the starting and ending point of a word and then reverse it using the helper reverse function.

"""


if __name__ == "__main__":
    s = '    the sky is blue '
    print(reverse_words(s))
