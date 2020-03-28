
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main ()

{

vector<vector<int>> store1;

cout << store1.size() << endl;

store1.push_back({0});


cout << store1.size() << endl;

store1.push_back({2, 4, 5, 45, 33});


cout << store1.size() << endl;
cout << store1.at(1)[0] << endl;


cout << store1[1].size() << endl;



}