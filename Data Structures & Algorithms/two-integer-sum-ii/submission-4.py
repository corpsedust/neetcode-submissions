class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        second = len(numbers) - 1
        first = 0
        
        while second > first:
            if numbers[first] + numbers[second] < target:
                first += 1
            elif numbers[first] + numbers[second] > target:
                second -= 1
            else:
                return [first + 1, second+1]