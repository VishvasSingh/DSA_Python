from typing import List


"""
https://leetcode.com/problems/zigzag-conversion/description/


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


"""

"""
Initial code

def zigzag_conversion(s: str, rows: int) -> str:
    result = []
    for i in range(rows):
        result.append([])
    i = 0
    downwards = True
    char_index = 0
    while char_index < len(s):
        if i == rows:
            downwards = False
            i -= 2 if i-2 >= 0 else 1

        if i == 0:
            downwards = True

        if downwards:
            result[i].append(s[char_index])
            i += 1

        else:
            for index, each_row_values in enumerate(result):
                if index == i:
                    each_row_values.append(s[char_index])
                else:
                    each_row_values.append("")

            i -= 1

        char_index += 1

    final_result = ""
    for each_row in result:
        final_result += "".join(each_row)

    return final_result
"""



"""
Optimized and clean code:



"""


def zigzag_conversion(s: str, numRows: int) -> str:
    # Edge case: If 1 row, no zigzagging is possible
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list of strings for each row
    rows = [""] * numRows

    curr_row = 0
    step = 1  # 1 means down, -1 means up

    for char in s:
        rows[curr_row] += char

        # If we hit the top or bottom, reverse the step
        if curr_row == 0:
            step = 1
        elif curr_row == numRows - 1:
            step = -1

        curr_row += step

    return "".join(rows)





if __name__ == "__main__":
    string = "ABC"
    print(zigzag_conversion(string, 2))


