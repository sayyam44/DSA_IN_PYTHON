def maxProfit(prices):
    #https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    #optimized solution - tc=n,sc=1
    #https://www.youtube.com/watch?v=eMSfBgbiEjk&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=12
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

    # brute force method,tc=n2,sc=1
    # def maxProfit_my_correct_ans(self, prices: List[int]) -> int:
    #     a=min(prices)
    #     ind_a=prices.index(a)
        
    #     b=max(prices[ind_a:])
    #     return (b-a)

