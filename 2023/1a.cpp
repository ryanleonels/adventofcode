#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>

using namespace std;

int n;
string line;

int getNum(int pos) {
    if (line[pos] >= '1' && line[pos] <= '9') return (line[pos] - '0');
    if ((pos <= n-3) && (line.substr(pos,3).compare("one") == 0)) return 1;
    if ((pos <= n-3) && (line.substr(pos,3).compare("two") == 0)) return 2;
    if ((pos <= n-5) && (line.substr(pos,5).compare("three") == 0)) return 3;
    if ((pos <= n-4) && (line.substr(pos,4).compare("four") == 0)) return 4;
    if ((pos <= n-4) && (line.substr(pos,4).compare("five") == 0)) return 5;
    if ((pos <= n-3) && (line.substr(pos,3).compare("six") == 0)) return 6;
    if ((pos <= n-5) && (line.substr(pos,5).compare("seven") == 0)) return 7;
    if ((pos <= n-5) && (line.substr(pos,5).compare("eight") == 0)) return 8;
    if ((pos <= n-4) && (line.substr(pos,4).compare("nine") == 0)) return 9;
    return 0;
}

int main()
{
    int l, r, sum = 0;
    // input
    freopen("1.in", "r", stdin);
    while (getline(cin, line)) {
        n = line.length();
        l = 0; while (!getNum(l)) l++;
        r = n-1; while (!getNum(r)) r--;
        sum += (getNum(l)*10);
        sum += getNum(r);
    }
    // output
    cout << sum;
    return 0;
}
