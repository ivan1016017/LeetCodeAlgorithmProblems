function maxProfit(prices: number[]): number {
    let i = 0;
    let peak = 0;
    let valley = 0;
    const lenPrices = prices.length;
    let result = 0;

    while (i < lenPrices - 1) {
        while (i < lenPrices - 1 && prices[i] >= prices[i + 1]) {
            i++;
        }
        valley = prices[i];

        while (i < lenPrices - 1 && prices[i] <= prices[i + 1]) {
            i++;
        }
        peak = prices[i];

        result += peak - valley;
    }

    return result;
};        
