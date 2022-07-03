
## https://leetcode.com/problems/reverse-pairs/


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        len_nums = len(nums)
        count = 0
        for x in range(len_nums - 1, -1, -1):
            # print(nums[x], x)
            for y in range(x - 1, -1, -1):
                if nums[y] > 2 * nums[x]:
                    count = count + 1
        return count

