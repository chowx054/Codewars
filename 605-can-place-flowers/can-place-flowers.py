class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 1
        res = 0

        for i in flowerbed:
            if i == 0:
                count += 1
            else:
                res += int( (count-1)//2 )
                count = 0
        
        res += int(count/2)

        return res >= n