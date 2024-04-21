class Solution:
    def stoneGame(self, piles) -> bool:
        n = len(piles)

        # 初始化一个n*n的矩阵 dp数组
        dp = [[None] * n for i in range(0, n)]

        # 在三角区域填充
        for i in range(n):
            for j in range(i, n):
                dp[i][j] = [0, 0]

        # 填入base case
        for i in range(0, n):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0

        # 斜着遍历数组
        for l in range(2, n + 1):
            for i in range(0, n-l+1):
                j = l + i - 1


                # 先手选择最左边或最右边的分数
                left = piles[i] + dp[i + 1][j][1]
                right = piles[j] + dp[i][j - 1][1]

                # 套用状态转移方程
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]

        res = dp[0][n - 1]

        return res[0] - res[1] > 0



print(3+4>>1)
print(4>>1)
print((3+4)>>1)
print(3+(4>>1))
