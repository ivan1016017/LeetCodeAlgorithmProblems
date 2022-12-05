function maxProfit(prices: number[]): number {

    let minValuePrice: number = 10**6 + 1
    let maxProfit: number = 0

    for (let i = 0; i < prices.length; i++){
        if (prices[i] < minValuePrice){
            minValuePrice = prices[i]
        }
        else if (prices[i] - minValuePrice > maxProfit){
            maxProfit = prices[i] - minValuePrice
        }
    }

    return maxProfit

};