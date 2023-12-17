#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
    int l, n, r, sum = 0;
    string line;
    // input
    freopen("1.in", "r", stdin);
    while (getline(cin, line)) {
        n = line.length();
        l = 0; while (line[l] < '0' || line[l] > '9') l++;
        r = n-1; while (line[r] < '0' || line[r] > '9') r--;
        sum += (line[l]-'0')*10;
        sum += (line[r]-'0');
    }
    // output
    cout << sum;
    return 0;
}
