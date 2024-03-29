#include <iostream>
#include <limits.h>
#include <vector>

using namespace std;
// ### BEST TIME TO BUY AND SELL STOCK
// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day 
// in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = INT_MAX;
        int max_profit = 0;

        for (int price: prices) {
            min_price = min(min_price, price);
            max_profit = max(max_profit, price - min_price);
        }

        return max_profit;
    }
};

// ### BEST TIME TO BUY AND SELL STOCK 1.5

// Kadane's Algorithm

// Same as Best Time to Buy and Sell Stock I but we are given the difference array of prices
// eg - for {1, 7, 4, 11}, we will get {0, 6, -3, 7}

// Suppose we have original array:
// [a0, a1, a2, a3, a4, a5, a6]

// what we are given here(or we calculate ourselves) is:
// [b0, b1, b2, b3, b4, b5, b6]

// where,
// b[i] = 0, when i == 0
// b[i] = a[i] - a[i - 1], when i != 0

// suppose if a2 and a6 are the points that give us the max difference (a2 < a6)
// then in our given array, we need to find the sum of sub array from b3 to b6.

// b3 = a3 - a2
// b4 = a4 - a3
// b5 = a5 - a4
// b6 = a6 - a5

// adding all these, all the middle terms will cancel out except two
// i.e.

// b3 + b4 + b5 + b6 = a6 - a2

// a6 - a2 is the required solution.

// so we need to find the largest sub array sum to get the most profit

class Solution {
    public:
        int maxProfit(vector<int>& differences) {
            int max_curr = 0, max_so_far = 0;
            for (int i = 0; i < differences.size(); i++) {
                max_curr = max(0, max_curr += differences[i]);
                max_so_far = max(max_curr, max_so_far);
            }
            return max_so_far;
        }
}

// ### BEST TIME TO BUY AND SELL STOCK II

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

// Find and return the maximum profit you can achieve.

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

// Used Greedy not DP

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int profit = 0;
        bool bought = false;
        for (int i = 0; i < prices.size() - 1; i++) {
            
            // buying at minimas i.e the lowest dip in price before which it starts rising again
            if (bought == false && prices[i] < prices[i + 1]) {
                profit -= prices[i];
                bought = true;
            }
            // selling at maximas i.e the highest rise in price before which it starts descreasing again
            else if (bought == true && prices[i] > prices[i + 1]){
                profit += prices[i];
                bought = false;
            }

            cout << bought << " " << prices[i] << " " << profit << endl;
        }

        if (bought == true && prices[prices.size() - 1] >= prices[prices.size() - 2]) {
            profit += prices[prices.size() - 1];
        }

        return profit;
        
    }
};

// ### BEST TIME TO BUY AND SELL STOCK III

// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// Find the maximum profit you can achieve. You may complete at most two transactions.

// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();

        vector<vector<vector<int>>> dp (length, vector<vector<int>> (2, vector<int> (2, -1)));

        function <int(int, int, int)> f = [&] (int i, int buy, int cap) -> int {
            // f(i, buy, cap) -> maximum profit that can be achieved from day i to n - 1.       
            if (i == length)
                return 0;
            
            if (cap == -1)
                return 0;

            if (dp[i][buy][cap] != -1)
                return dp[i][buy][cap];
            //2 choices - can buy (if buy == 0), then sell or rest
            // cannot buy (if buy == 1), then sell or rest

            if (buy == 0) {
                int buyStock =  f(i + 1, 1 - buy, cap) - prices[i];
                int rest = f(i + 1, buy, cap);
                return dp[i][buy][cap] = max(buyStock, rest);
            }

            else {
                int sell = prices[i] + f(i + 1, 1 - buy, cap - 1);
                int rest = f(i + 1, buy, cap);
                return dp[i][buy][cap] = max(sell, rest);
            }
        };

        return f(0, 0, 1);
    }

    int maxProfit(vector<int>& prices) {
       // https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/solutions/39611/is-it-best-solution-with-on-o1/


    }


};

// ### BEST TIME TO BUY AND SELL STOCK WITH COOLDOWN

// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock
//  multiple times) with the following restrictions:

// After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int length = prices.size();

        vector<vector<int>> dp (length, vector<int> (3, -1));

        return f(prices, dp, 0, 0);
    }


    int f(vector<int>& prices, vector<vector<int>>& dp, int i, int state) {
        //f(i, state) -> maximum profit that can be achieved from day i to n - 1
        if (i == prices.size())
            return 0;

        if (dp[i][state] != -1)
            return dp[i][state];
        
        if (state == 0) {
            // state == can buy
            int buy = f(prices, dp, i + 1, state + 1) - prices[i]   ;
            int rest = f(prices, dp , i + 1, state);
            return dp[i][state] = max(buy, rest);
        }

        if (state == 1) {
            // state == can sell
            int sell = f(prices, dp, i + 1, state + 1) + prices[i];
            int rest = f(prices, dp, i + 1, state);
            return dp[i][state] = max(sell, rest);
        }

        if (state == 2) {
            // state == cooldown
            return dp[i][state] = f(prices, dp, i + 1, 0);
        }

        return 0;
    }
};

// ### BEST TIME TO BUY AND SELL STOCK WITH TRANSACTION FEE

// You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

// Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

// Top Down DP

// think in terms of states. canBuy and canSell are two states. and buy, sell, rest are operations on them.

class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int length = prices.size();

        vector<vector<int>> dp (length, vector<int> (2, -1));

        return f(prices, dp, 0, 0, fee);
    }


    int f(vector<int>& prices, vector<vector<int>>& dp, int i, int state, int fee) {
        //f(i, state) -> maximum profit that can be achieved from day i to n - 1
        if (i == prices.size())
            return 0;

        if (dp[i][state] != -1)
            return dp[i][state];
        
        if (state == 0) {
            // state == can buy
            int buy = f(prices, dp, i + 1, 1 - state, fee) - prices[i]   ;
            int rest = f(prices, dp , i + 1, state, fee);
            return dp[i][state] = max(buy, rest);
        }

        if (state == 1) {
            // state == can sell
            int sell = f(prices, dp, i + 1, 1 - state, fee) + prices[i] - fee;
            int rest = f(prices, dp, i + 1, state, fee);
            return dp[i][state] = max(sell, rest);
        }

        return 0;
    }
};

