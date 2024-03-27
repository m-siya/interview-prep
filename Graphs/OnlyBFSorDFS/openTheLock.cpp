// 752. Open the Lock

// You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

// The lock initially starts at '0000', a string representing the state of the 4 wheels.

// You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

// Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible

// https://leetcode.com/problems/open-the-lock/description/

#include <unordered_set>
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead_states(deadends.begin(), deadends.end());
        unordered_set<string> visited;

        queue<string> q;
        string state = "0000";
        if (dead_states.find(state) != dead_states.end()) {
            return -1;
        }
        if (state == target) {
            return 0;
        } 
        q.push(state);

        int turns = 0;

        while (!q.empty()) {

            int q_len = q.size();

            for (int k = 0; k < q_len; k++) {
                string curr_state = q.front();
                q.pop();

                for(int i = 0; i < 4; i++) {
                    for (int j = -1; j <= 1; j += 2){
                        string new_state = curr_state;
                        new_state[i] = ((new_state[i] - '0' + j + 10) % 10) + '0';

                        if (visited.find(new_state) != visited.end()) {
                            continue;
                        }
                        if (dead_states.find(new_state) != dead_states.end()) {
                            continue;
                        }
                        if (new_state == target) {
                            return turns + 1;
                        }
                        q.push(new_state);
                        visited.insert(new_state);
                    }              
                }
            }
            turns++;
           // cout << turns<< endl;
        }
        return -1;
        
    }
};