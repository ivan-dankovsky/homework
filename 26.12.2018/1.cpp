/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <cstdlib> 

using namespace std;
int F(int *arr, int left, int right, int k)
{
	int x;
	int i = left;
	int j = right;
	int mid;
	while (true)
	{
		mid = ((left + right) - (left + right) % 2) / 2;
		while (mid >= arr[i])
			i++;
		while (mid <= arr[j])
			j++;
		if (arr[i] < arr[j])
		{
			x = arr[i];
			arr[i] = arr[j];
			arr[j] = x;
		}
		if (i > j)
			break;
	}

	if (k == mid)
		return arr[mid];
	if (right - left < 4)
		return(arr[k]);
	else
		{
	if (k < mid)
		F(arr, left, mid, k);

	if (k > mid)
		F(arr, mid, right, k);
		}
}
int main()
{
	int n;
	cin >> n;
	cout << endl;
	int *Array = new int[n];
	for (int q = 0; q < n; q++)
		cin >> Array[q];
		cout << endl;
		int K;
		cin >> K;
		
	cout << F(Array, 0, n-1, K);
	system("pause");
		return 0;
}
