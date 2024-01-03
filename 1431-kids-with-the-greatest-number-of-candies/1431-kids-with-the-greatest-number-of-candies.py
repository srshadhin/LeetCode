class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m_c = max(candies)
        for candi in range(len(candies)):
            if candies[candi]+extraCandies >= m_c:
                candies[candi] = True
            else:
                candies[candi] = False
        return candies