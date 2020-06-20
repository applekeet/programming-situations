
// compile
// g++ -o main main.cpp --std=c++14

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	int x, input;

	cin >> x;

	// 2d vector
	std::vector<std::vector<int>> v1;

	// single row vector
	std::vector<int> v;

	for (int qq = 0; qq < x; ++qq)
	{
		v.clear();
		for (int i = 0; i < 3; ++i)
		{
			cin >> input;
			v.push_back(input);
		}
		v1.push_back(v);
	}

	for (auto it1: v1)
	{
		for (auto x: it1)
		{
			cout << x << endl;
		}
	}

	return 0;
}






