#include <iostream>
#include <vector>

int total_path(int xm, int ym, int n, int m) {
    // Create a 2D dp table initialized to 0
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(m + 1, 0));

    // Starting point has 1 unique path (staying there)
    dp[0][0] = 1;

    // Define the restricted points (knight-like moves)
    int x1 = xm - 1, y1 = ym + 2;
    int x2 = xm - 2, y2 = ym + 1;
    int x3 = xm - 2, y3 = ym - 1;
    int x4 = xm - 1, y4 = ym - 2;
    int x5 = xm + 1, y5 = ym - 2;
    int x6 = xm + 2, y6 = ym - 1;
    int x7 = xm + 2, y7 = ym + 1;
    int x8 = xm + 1, y8 = ym + 2;

    // Mark the restricted points in the dp table
    // (assuming the point is within the grid)
    //if (xm >= 0 && xm <= n && ym >= 0 && ym <= m) dp[xm][ym] = 0;
    if (x1 >= 0 && x1 <= n && y1 >= 0 && y1 <= m) dp[x1][y1] = 0;
    if (x2 >= 0 && x2 <= n && y2 >= 0 && y2 <= m) dp[x2][y2] = 0;
    if (x3 >= 0 && x3 <= n && y3 >= 0 && y3 <= m) dp[x3][y3] = 0;
    if (x4 >= 0 && x4 <= n && y4 >= 0 && y4 <= m) dp[x4][y4] = 0;
    if (x5 >= 0 && x5 <= n && y5 >= 0 && y5 <= m) dp[x5][y5] = 0;
    if (x6 >= 0 && x6 <= n && y6 >= 0 && y6 <= m) dp[x6][y6] = 0;
    if (x7 >= 0 && x7 <= n && y7 >= 0 && y7 <= m) dp[x7][y7] = 0;
    if (x8 >= 0 && x8 <= n && y8 >= 0 && y8 <= m) dp[x8][y8] = 0;

    // Fill the dp table by calculating the number of paths
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= m; ++j) {
            // Skip the restricted points
            if ((i == xm && j == ym) ||
                (i == x1 && j == y1) || (i == x2 && j == y2) ||
                (i == x3 && j == y3) || (i == x4 && j == y4) ||
                (i == x5 && j == y5) || (i == x6 && j == y6) ||
                (i == x7 && j == y7) || (i == x8 && j == y8)) {
                dp[i][j] = 0;  // Mark it as restricted
                continue;
            }

            // If not in the first row, add paths from above
            if (i > 0) {
                dp[i][j] += dp[i - 1][j];
            }

            // If not in the first column, add paths from the left
            if (j > 0) {
                dp[i][j] += dp[i][j - 1];
            }
        }
    }

    // The result is the number of ways to reach the bottom-right corner
    return dp[n][m];
}

int main() {
    int xm, ym, n, m;

    std::cin >> n >> m >> xm >> ym;

    int result = total_path(xm, ym, n, m);
    std::cout << result << std::endl;

    return 0;
}