class Solution:
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum2 = -(nums[left] + nums[right])
                
                if sum2 < val:
                    right -= 1
                elif sum2 > val:
                    left += 1
                elif sum2 == val:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # left has already been moved forward, so you are comparing if previous was duplicate or not (for which you already made the entry)
                    # same for right
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return triplets