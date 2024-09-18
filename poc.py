"""
Given a string S of lowercase English letters, the task is to find the index of the first non-repeating character.
 If there is no such character, return -1.

Input: S = “geeksforgeeks”
Output: 5
Explanation: ‘f’ is the first character in the string which does not repeat.

Input: “aabbccc”
Output: -1
Explanation: All the characters in the given string are repeating
"""

""" Two Egg Drop problem with dynamic programming. """


# class Solution:
#     def twoEggDrop(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         for i in range(1, n + 1):
#             dp[i] = dp[i - 1] + 1
#             for j in range(1, i):
#                 dp[i] = min(dp[i], 1 + max(j - 1, dp[i - j]))
#         return dp[n]

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dag_nums = [1] * len(nums)
#
#         for rev_index in range(len(nums) - 1, -1, -1):
#             for index in range(rev_index + 1, len(nums)):
#                 if nums[rev_index] < nums[index]:
#                     dag_nums[rev_index] = max(dag_nums[rev_index], 1 + dag_nums[index])
#
#         return max(dag_nums)


# class Solution:
#     def maxHeight(self, cuboids: List[List[int]]) -> int:
#         # Cuboids: [Width, Length, Height]
#         for c in cuboids:
#             c.sort()
#         cuboids.sort()
#         df = [0] * len(cuboids)
#         for i in range(1, len(cuboids)):
#             df[i] = cuboids[i][2]
#             for j in range(i):
#                 # if all([cuboids[i][k] <= cuboids[j][k] for k in range(3)]):
#                 if cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
#                     df[i] = max(df[i], df[j] + cuboids[i][2])
#
#         return max(df)


class Solution:
    def numDecodings(self, code: str) -> int:
        # 226 -> BZ(2 26) VF(22 6) BBF(2 2 6)
        if not code or '0' in code[0]:
            return 0

        dp = [0] * (len(code) + 1)
        dp[0] = 1
        dp[1] = 1

        # decoding_methods = 1  # default method is all single digits
        for i in range(2, len(code) + 1):
            two_digits = int(code[i - 2:i])
            if 26 >= two_digits >= 10:
                dp[i] += dp[i - 1]
            elif int(code[i - 1]) != 0:
                dp[i] += dp[i - 1]

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings('10'))
