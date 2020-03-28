/*
https://www.geeksforgeeks.org/samsung-rd-bangalore-interview-experience-lateral-hire-6-month-experience/

There is a highway that has damages at N (4<=N<=100) locations. Each damage location is represented by a number a (0<=a<=10000). You need to repair these damages with Asphalt. The damage is repaired with these rules:

Asphalt can be spread on the road with a minimum stretch of K (1<=K<=10000) i.e. each time you put asphalt, it will be spread to k consecutive locations. eg. if the damage is at locations 2, 5 and K=3 then the first asphalt spread is from 0-2 or 1-3 or 2-4 and the second is from 3-5 or 4-6 or 5-7.
You need to spread minimum Asphalt to repair all damaged locations of the road. For the above example, the minimum asphalt required is 4 units ( 2-4 and 3-5) because 3-4 is overlapping.
Example test cases:



Input:-

N K

A[0] A[1] …….. A[N-1]

Output:-

Minimum Asphalt area to repair all damages.

1.

10 2

0 10 2 12 4 14 6 16 8 18

output: 15

2.

4 3

3 9 11 8

output: 7

3.

8 3

2 7 20 5 19 9 6 22

output: 12

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, K;

    cin >> N; // number of damaged spots
    cin >> K; // length of asphalt stretch

    vector<int> a;
    int input;

    for (int i = 0; i < N; i++)
    {
        cin >> input;
        a.push_back(input);
    }

    /*
    // just printing
    for (int i = 0; i < N; i++)
    {
        cout << a[i];
    }
    */

    // sorting the list of spots.
    // chooosing the spots which are closer
    /*

    create pair of numbers between which
    the all spots can be filled with overlapping
    asphalt

    then next part of asphalt will come in next pair

    */ 

   sort(a.begin(), a.end());


   for (int i = 0; i < N; i++)
    {
        cout << a[i] << endl;
    }


   bool sequence = 0;
   int initialPeg = -1;
   int lengthCount = 0;
   // just printing
    for (int i = 1; i < N; i++)
    {
        if ((a[i] - a[i-1]) <= K)
        {
            cout << "in" << endl;
            if (!sequence) // if sequence has just started
            {
                initialPeg = a[i-1];
                sequence = 1;
            }
            else // if sequence is continued
            {
                if (i == (N-1)) // if it is the last element
                {
                    int diff = a[i] - initialPeg;
                    lengthCount += (diff+1);
                }
                if ()
            }
        }
        else
        {
            cout << "out" << endl;
            if (sequence)  // if sequence ends here
            {
                int diff = a[i-1] - initialPeg;
                lengthCount += (diff+1);
            }
            else // if previous element was also single
            {
                lengthCount += K;
                if (i == (N-1)) // if it is the last element
                {
                    lengthCount += K;
                }
            }
            sequence = 0;
        }
        cout << "Total length " << lengthCount << endl;
        cout << "initial peg mark " << initialPeg << endl;
    }
    
}

