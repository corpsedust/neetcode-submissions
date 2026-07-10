class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            elif row[0] <= target and row[-1] > target:
                l, r = 0, len(row) - 1
        
                while l <= r:
                    m = (l + r) // 2
                
                    if row[m] < target:
                        l = m+1
                    elif row[m] > target:
                        r = m-1
                    else:
                        return True

            elif row[0] == target or row[-1] == target:
                return True
            else:
                return False
        return False 