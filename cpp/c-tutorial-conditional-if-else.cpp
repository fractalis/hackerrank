#include <bits/stdc++.h>
#include <string>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string number_map[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    if (n > 9) {
        cout << "Greater than 9";
    } else {
        cout << number_map[n-1];
    }


    return 0;
}

