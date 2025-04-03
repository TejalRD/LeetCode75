class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newFlowerbed = [0] + flowerbed + [0] #add extra 0 at start and end of the original array
        
        for i in range(1,len(newFlowerbed)-1): #skip 1st and last element since that is added extra
            if newFlowerbed[i-1]==0 and newFlowerbed[i]==0 and newFlowerbed[i+1]==0:
                newFlowerbed[i]=1
                n = n-1
        return n<=0

        