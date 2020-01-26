// https://www.hackerrank.com/contests/amazon/challenges/shortest-sub-segment

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;



string subsegment(string para, int number1, string words[])
{

/*
	int start1[number1][para.length()] = {-1}; // occurence of first element;
	int end1[number1][para.length()] = {-1};
*/


	int start1[number1] = {-1}; // occurence of first element;
	int end1[number1] = {-1};


	for (int i = 0; i < number1; ++i)
	{
		int pos = para.find(words[i]);

		//cout << pos << endl;
		//cout << pos+words[i].length();

		int occurence = 0;

		start1[i][occurence] = pos;
		end1[i][occurence] = pos+words[i].length();


		if (pos != string::npos)
		{}

	}

	for (int i = 0; i < number1; ++i)
	{
		cout << start1[i] << " " << end1[i] << endl;
	}

	sort(start1);


	for (int i = 0; i < number1; ++i)
	{
		cout << start1[i] << endl;
	}



	return "still not done";

}



int main(int argc, char const *argv[])
{
	int number1;
	string para;

	getline (cin, para);

	cin >> number1;
	string words[number1];

	for (int i = 0; i < number1; ++i)
	{
		cin >> words[i];
	}

	cout << subsegment(para, number1, words);


	return 0;
}



