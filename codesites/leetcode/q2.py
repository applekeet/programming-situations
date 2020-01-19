# leetcode


class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		def fac(yy: int) -> int:
			if yy <= 1:
				return 1
			return yy * fac(yy-1)
		return (fac((m-1)+(n-1)/(fac(m-1)*fac(n-1)))

d=Solution()
d.uniquePaths(5, 5)
