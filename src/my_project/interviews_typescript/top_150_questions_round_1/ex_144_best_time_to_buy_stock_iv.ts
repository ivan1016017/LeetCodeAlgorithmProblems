function maxProfitIV(k: number, prices: number[]): number {
    const n = prices.length;
    if (n === 0 || k === 0) return 0;

    if (k >= Math.floor(n / 2)) {
        let profit = 0;
        for (let i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
        }
        return profit;
    }

    const buy: number[] = new Array(k + 1).fill(-Infinity);
    const sell: number[] = new Array(k + 1).fill(0);

    for (const price of prices) {
        for (let j = 1; j <= k; j++) {
            buy[j] = Math.max(buy[j], sell[j - 1] - price);
            sell[j] = Math.max(sell[j], buy[j] + price);
        }
    }

    return sell[k];
};