// Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
// column are set to 0

//my approach
//use 2 arrays (or vectors) as hashmaps to store rows and columns resp where an element is zero 
//in matrix

//O(N * M ) time complexity and O(N + M) space complexity

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int r = matrix.size();
        int c = matrix[0].size();
        

        vector <int> zero_rows(r);
        vector <int> zero_cols(c);

        

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    zero_rows[i] = 1;
                    zero_cols[j] = 1;
                    //zero_cols.push_back(j);
                }
            }
        }

        for (int i = 0; i < matrix.size(); i++){
            cout << zero_rows[i] << " ";
        }

        cout << endl;

        for (int i = 0; i < matrix[0].size(); i++){
            cout << zero_cols[i] << " ";
        }
        
    
        for(int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (zero_rows[i] == 1 || zero_cols[j] == 1)
                    matrix[i][j] = 0;
            }
        }       
    }

    //optimized approach, use the first row and col of matrix as the hashmaps
    // O(N * M) time complexity and O(1) space complexity
    
    /* first iterate through the first row and first col and set 2 flags as true if there are zeros in
        each. 
        then, iterate through rest of the elements and set the hashmaps 0 if the corresponding element is zero.
        then depending on the flags, set the first row and col as 0 
        */

    void setZeroes(vector<vector<int>>& matrix) {
        int r = matrix.size();
        int c = matrix[0].size();
        
        int zero_in_first_r = 0;
        int zero_in_first_c = 0;

        for (int j = 0; j < c; j++) {
            if (matrix[0][j] == 0){
                zero_in_first_r = 1;
                break;
            }
        }

        for (int i = 0; i < r; i++) {
            if (matrix[i][0] == 0){
                zero_in_first_c = 1;
                break;
            }
        }

        cout << zero_in_first_r << " " << zero_in_first_c << endl;

        for (int i = 1; i < r; i++) {
            for (int j = 1; j < c; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }

        // for (int i = 0; i < r; i++){
        //     for (int j = 0; j < c; j++) {
        //         cout << matrix[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        for(int i = 1; i < r; i++) {
            for (int j = 1; j < c; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }

        // for (int i = 0; i < r; i++){
        //     for (int j = 0; j < c; j++) {
        //         cout << matrix[i][j] << " ";
        //     }
        //     cout << endl;
        // }

        if (zero_in_first_r == 1) {
            for (int j = 0; j < c; j++) {
                matrix[0][j] = 0;
            }
        }

        if (zero_in_first_c == 1) {
            for (int i = 0; i < r; i++) {
                matrix[i][0] = 0;
            }
        }   
    }
};


//optimized approach, use the first row and col of matrix as the hashmaps