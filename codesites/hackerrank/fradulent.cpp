// https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long int n;
    int input;
    int d;
    scanf("%d", &n);
    
    vector<int> values;
    
    for (long int i = 0; i < n; i++)
    {
        /* code */
        cin >> input;
        values.push_back(input);
    }

    cout << values[3] << endl;



}


