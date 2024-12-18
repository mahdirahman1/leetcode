class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        
        for i, orig_price in enumerate(prices):
            for j in range(i+1,len(prices)):
                if prices[j] <= orig_price:
                    answer.append(orig_price-prices[j])
                    break
            else:
                answer.append(orig_price)
        
        return answer