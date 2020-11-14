// https://www.hackerrank.com/challenges/attribute-parser/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 

    int t, q;
    vector<string> text, query;

    cin >> t >> q;
    text.resize(t);
    query.resize(q);
    getline(cin,text[0]);
    for(int i=0; i < t; i++)
    {
        getline(cin,text[i]);
    }
    for(int i=0; i < q; i++)
    {
        getline(cin,query[i]);
    }

    for(auto t1 : text)
    {
        cout << t1 << endl;
    }
    cout << "---";

    for(auto q1 : query)
    {
        cout << q1;
    }

    




    return 0;
}

