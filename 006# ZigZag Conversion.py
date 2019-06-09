# coding:utf-8

"""
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    Date: 2019/06/05
    By: Fargo
    Difficulty: Medium
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # numRows =1 或 s字符串长度 ＜ numRows 即原字符串
        if numRows == 1 or len(s) < numRows:
            return s

        #
        s_convert = []
        diff = 2 * numRows - 2
        n = len(s)
        k = int(n / diff)

        for i in range(numRows):
            for j in range(k + 2):
                if j > 0 and (j * diff - i) < n and i != 0 and i != numRows-1:
                    s_convert.append(s[j * diff - i])

                if (j * diff + i) < n:
                    s_convert.append(s[j * diff + i])

        return ''.join(s_convert)


print(Solution().convert("ABCDEFG", 5))

