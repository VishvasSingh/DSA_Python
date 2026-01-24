
"""
https://leetcode.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.


"""

def max_no_of_balloons(text: str) -> int:
    # 1. Count frequency of all letters
    char_count = {}
    for each_char in text:
        char_count[each_char] = char_count.get(each_char, 0) + 1

    # 2. Check ingredients.
    # For 'l' and 'o', we divide by 2 because we need 2 per word.
    b = char_count.get('b', 0)
    a = char_count.get('a', 0)
    l = char_count.get('l', 0) // 2
    o = char_count.get('o', 0) // 2
    n = char_count.get('n', 0)

    # 3. The limiting factor determines the answer
    return min(b, a, l, o, n)





if __name__ == "__main__":
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    print(max_no_of_balloons(text))