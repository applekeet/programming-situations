
#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main()
{
    int input;

    deque<int> doubleEnd;
    cin >> input;
    
    while(input)
    {
        //doubleEnd.push_back(input);
        doubleEnd.emplace_back(input, 1);
        cin >> input;
    }

    for (int i = 0; i < doubleEnd.size(); i++)
    {
        cout << doubleEnd[i] << endl;
    }
    

}


