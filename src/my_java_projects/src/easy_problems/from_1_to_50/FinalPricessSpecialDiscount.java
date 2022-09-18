package easy_problems.from_1_to_50;

public class FinalPricessSpecialDiscount implements Numbers{
    public int[] finalPrices(int[] prices) {

        int len_prices = prices.length;

        for (int i = 0; i < len_prices; i++){
            for (int j = i + 1; j < len_prices; j++){
                if (prices[i] >= prices[j]){
                    prices[i] = prices[i] - prices[j];
                    break;
                }
            }
        }

        return prices;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class which has methods that do not return numbers");
    }
}
