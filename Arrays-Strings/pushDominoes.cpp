// ### PUSH DOMINOES
// There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push 
// some of the dominoes either to the left or to the right.

// After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the 
// dominoes falling to the right push their adjacent dominoes standing on the right.

// When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

// For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or 
// already fallen domino.

// You are given a string dominoes representing the initial state where:

// dominoes[i] = 'L', if the ith domino has been pushed to the left,
// dominoes[i] = 'R', if the ith domino has been pushed to the right, and
// dominoes[i] = '.', if the ith domino has not been pushed.
// Return a string representing the final state.

// https://leetcode.com/problems/push-dominoes/description/

class Solution {
public:
    string pushDominoes(string dominoes) {
        //find net force on each domino -> superposition of forces
        // right falling domino only affects those after it
        // left falling domino only affects those before it
        
        // go L -> R and calculate rightward force
        int len = dominoes.size();
        vector<int> net_force (len, 0);
        int apply_force = false;
        int force = len;
        for (int i = 0; i < len; i++) {
            if (dominoes[i] == 'L') {
                apply_force = false;
            }
            if (apply_force) {
                net_force[i] += force;
                force--;      
            }

            if (dominoes[i] == 'R') {
                apply_force = true;
                force = len;
            }
        }

        // go R -> L and calculate leftward force
        apply_force = false;
        force = -len;
        for (int i = len - 1; i >= 0; i--) {
            if (dominoes[i] == 'R') {
                apply_force = false;
            }
            if (apply_force) {
                net_force[i] += force;
                force++;      
            }

            if (dominoes[i] == 'L') {
                apply_force = true;
                force = -len;
            }
        }

        // for (auto f: net_force) {
        //     cout << f << " " << endl;
        // }

        for (int i = 0; i < len; i++) {
            if (net_force[i] > 0) dominoes[i] = 'R';
            if (net_force[i] < 0) dominoes[i] = 'L';
        }

        return dominoes;
    }
};


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        
        k = 0 #key count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in "abcdef": 
                    k += (1 << ord(grid[r][c]) - ord('a'))
                if grid[r][c] == '@': start_r, start_c = r, c

        #print(bin(k))

        q = deque()
        #q(row, col, dist, keys)
        q.append((start_r, start_c, 0, 0))
        #seen(row, col, keys)
        visited.add((start_r, start_c, 0))

        while q:
            r, c, dist, keys = q.popleft()
            #print(r, c, dist, keys, ": ")

            for direction in directions:
                dr, dc = direction
                row, col = r + dr, c + dc


                #neighbour is out of boundary or a wall
                if (row < 0 or col < 0 or
                    row == ROWS or col == COLS or
                    grid[row][col] == '#' or 
                    (row, col, keys) in visited):
                    continue

                #is a lock and we dont have its key, continue
                if (grid[row][col] in 'ABCDEF' and 
                    not (keys & (1 << (ord(grid[row][col]) - ord('A'))))
                ): 
                   # print(grid[row][col], "blocked")
                   # print(dist, grid[row][col])
                    continue
                    

                #is a key
                elif grid[row][col] in 'abcdef':
                    #if that key is not found yet
                    if not (keys & (1 << (ord(grid[row][col]) - ord('a')))):
                        print(bin(keys), end = " ")
                        keys = keys | (1 << (ord(grid[row][col]) - ord('a')))
                        #keys = new_keys
                        print(bin(keys))

                        if keys == k: 
                            return dist + 1
                
                q.append((row, col, dist + 1, keys))
        
        return -1





        return 0    



        

       

