// https://codeforces.com/problemset/problem/1368/A

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

	for (auto it: v1)
	{
		int z = 0;
		while (it[0] <= it[2] && it[1] <= it[2])
		{
			if (it[0] < it[1])
			{
				/* code */
				it[0] += it[1];
			}
			else
			{
				it[1] += it[0];
			}
			z++;
			//cout << it[0] << "--" << it[1] << "--" << z << endl;
		}
		cout << z << endl;
	}

	/* cout << v1;
	for (auto it1: v1)
	{
		for (auto x: it1)
		{
			cout << x << endl;
		}
	}
	*/

	return 0;
}






