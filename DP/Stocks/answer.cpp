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

// ### BEST TIME TO BUY AND SELL STOCK II

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

// Find and return the maximum profit you can achieve.

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int profit = 0;
        bool bought = false;
        for (int i = 0; i < prices.size() - 1; i++) {
            
            if (bought == false && prices[i] < prices[i + 1]) {
                profit -= prices[i];
                bought = true;
            }
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

 