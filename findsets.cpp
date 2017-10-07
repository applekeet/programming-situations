/*

input:
8 97 5 4 13 12 25
1

output:
16... its a guess

Explanation:
x mod y = k  --- y is on the right of x.

after finding pairs... select sub arrays which have 
atleast one pair in the selected sub array.

*/


#include <iostream>
using namespace std;

int findsubarrays(int *a, int n, int mod){

}

int main()
{
	int n, modulus;
	cin >> n;
	int arr[n];

	for (int i = 0; i < n; ++i)
	{
		/* code */
		cin >> arr[i] ;
	}
	cin >> modulus;

	int result = findsubarrays(int arr[], int n, int modulus);

	cout << result << endl;
	return 0;
}



