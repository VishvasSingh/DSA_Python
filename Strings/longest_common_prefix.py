from typing import List

"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""


"""
Optimized approach: Vertical scanning
"""

def longest_common_prefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    base_str = strs[0]
    common_prefix = ""
    for index, char in enumerate(base_str):
        for each_str in strs:
            if len(each_str) <= index or each_str[index] != char:
                return common_prefix

        common_prefix += char

    return common_prefix


"""
The "Interviewer" Trick (Sorting Method): There is a clever way to solve this that writes fewer lines of code (though it changes the time complexity slightly due to sorting).

If you sort the array of strings alphabetically, you only need to compare the first string and the last string.

Why? Sorting groups strings with similar prefixes. If the first and last strings share a prefix, every string in between must also share it.

Example: ["flower", "flow", "flight"]

Sorted: ["flight", "flow", "flower"]

Compare "flight" vs "flower". Common: "fl". Done.


def longest_common_prefix_sorted(strs: List[str]) -> str:
    if not strs:
        return ""
        
    # Sort the strings
    strs.sort()
    
    # Compare only the first and last
    first = strs[0]
    last = strs[-1]
    
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]
    
    
Vertical Scanning approach is actually faster O(N) than Sorting O(N log N)) for very large arrays.

"""




if __name__ == "__main__":
    strs = ["ab","a"]
    print(longest_common_prefix(strs))