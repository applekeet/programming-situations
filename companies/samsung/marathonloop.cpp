
#include <iostream>
#include <vector>
#include <utility>

using namespace std;


vector<int> answerLoops;

int loopCheck(int a, int b)
{
    if (a == b)
    {
        return 0;
    }

    vector<vector<int>> store1;

    for (int i = 0; i < store1.size(); i++)
    {
        /* one row */
        if(store1[i].back() == a)
        {
            store1[i].push_back(b);
        }
    }
    
}

int main() 
{
    int T; // test cases    
    int M,N;
    vector<pair<int, int>> edges;

    cin >> T;
    cout << T;

    for (int i = 0; i < T; i++)
    {
        /* code */
        edges.clear();
        answerLoops.clear();

        cout << "HI" <<endl;

        M = 0;
        N = 0;


        cin >> M; // number of nodes (junctions)
        cin >> N; // number of edges (street)


        cout << "HI  meee" <<endl;

        cout << M << N;



        cout << "HI me too" <<endl;


        for (int j = 0; j < N; j++)
        {
            
            int qq, rr;

            cin >> qq;
            cin >> rr;

            edges.push_back(make_pair(qq, rr));

        }

        for (int j = 0; j < N; j++)
        {
            

            cout << edges[j].first;
            cout << edges[j].second;

            loopCheck(edges[j].first, edges[j].second);

        }

        answerLoops;  // will have all the nodes in loop.

        

        // need to check if a loop in 
        // present in the bag of loops(answerLoops).





    }
    

    return 0;

}

