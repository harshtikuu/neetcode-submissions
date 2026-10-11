class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] * left[i-1])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                right[i] = nums[i]
            else:
                right[i] =  right[i+1] * nums[i]
        response = []
        for i in range(len(nums)):
            if i == 0:
                response.append(right[i+1])

            elif i == len(nums)-1:
                response.append(left[i-1])

            else:
                response.append(left[i-1] * right[i+1])
        return response
