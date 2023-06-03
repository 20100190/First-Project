class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return None


    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed_num = int(str(abs(x))[::-1])
        if x < 0:
            reversed_num *= -1
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack






