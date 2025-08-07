**Cells with Odd Values in a Matrix**

*Difficulty:* **Easy**
Problem Statement
Given an m x n matrix initialized with all zeros and an array indices where each element is a pair [r_i, c_i], increment all cells in row r_i and column c_i by 1 for each pair. Return the number of cells with odd values after all increments.
Constraints:

1 <= m, n <= 50
1 <= indices.length <= 100
0 <= r_i < m
0 <= c_i < n

Example
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: After incrementing row 0, column 1, row 1, and column 1, the matrix has 6 cells with odd values.

Link
LeetCode #1252: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix