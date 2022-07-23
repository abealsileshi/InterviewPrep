#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
/*
https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
*/

int diagonalDifference(vector<vector<int>> arr) {
    int posDiag = 0; 
    int negDiag = 0;
    int res = 0; 
    int size = arr.size() -1;
    
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j < arr.size(); j++){
            if(i == j){
                negDiag += arr[i][j];
            }
            if(i+j == size){
                posDiag += arr[i][j];
            }
        }
    }
    res = abs(negDiag - posDiag);
    cout << "neg diag " << negDiag << endl;
    cout << "pos diag " << posDiag << endl;
        cout << arr.size() << endl;

    return res;
}

int main(){
    vector <int> a = {1, 2, 3};
    vector <int> b = {4, 5, 6};
    vector <int> c = {9, 8, 9};
    vector <vector <int>> vec;
    
    vec.push_back(a);
    vec.push_back(b);
    vec.push_back(c);

    int res = diagonalDifference(vec);
    cout << " This is the result: " << res << endl;

}