# in this we use two pointer technique and find length which is minimum of value at those two pointer and width is subtract of that
# two pointer and calculate area and find max of it but if first pointer has less height than last pointer then first increases else
# right increases 
class Solution(object):
    def maxArea(self, height):
        n = len(height)
        max_water = 0
        i = 0
        j = n-1
        while i < j:
            length = min(height[i],height[j])
            width = j-i
            water = length*width
            max_water = max(max_water,water)
            if height[i] < height[j]:
                i +=1
            else:
                j -= 1
        return max_water
