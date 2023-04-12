// Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 
// bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

//approach - first take transpose of matrix and then reverse the matrix
// done in O(n^2) time and O(1) space i.e inplace solution

#include <iostream>
#include <vector>

using namespace std;


void transpose(vector<vector<int>>& matrix) {
    for (int r = 0; r < matrix.size(); r++) {
        for (int c = r + 1; c < matrix.size(); c++) {
            int temp = matrix[r][c];
            matrix[r][c] = matrix[c][r];
            matrix[c][r] = temp;
        }
    }
}

void reflect(vector<vector<int>>& matrix) {
    for (int r = 0; r < matrix.size(); r++) {
        for (int c = 0; c < matrix.size() / 2; c++) {
            int temp = matrix[r][c];
            matrix[r][c] = matrix[r][matrix.size() - 1 - c];
            matrix[r][matrix.size() - 1 - c] = temp;
        }
    }   
}

void rotate(vector<vector<int>>& matrix) {
    transpose(matrix);
    reflect(matrix);
}

void print(const vector<vector<int>>& matrix) {
	for ( int i = 0; i < matrix.size(); ++i ) {
		for( int j = 0; j < matrix.size(); ++j ) {
		    cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

// I dont get this look into it
// void rotate2( int ** matrix, int N ) {
// 	for( int i = 0; i < N/2; ++i ) {
// 		for( int j = i; j < N-i-1; ++j ) {
// 				int temp = matrix[i][j];
// 				matrix[i][j] = matrix[j][N-i-1];
// 				matrix[j][N-i-1] = matrix[N-i-1][N-j-1];
// 				matrix[N-i-1][N-j-1]= matrix[N-j-1][i];
// 				matrix[N-j-1][i] = temp;
// 		}
// 	}
// }


int main() {
	vector<vector<int>> matrix { 
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

	cout << "Rotated matrix by 90 (clockwise):\n";
	rotate(matrix);
	print(matrix);

	// std::cout << "Rotated matrix again by 90(anticlockwise):\n";
	// rotate2(matrix, N);
	// printMatrix(matrix, N);
	// return 0;
}