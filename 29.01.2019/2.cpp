#include <iostream>

using namespace std;

class Array 
{
private:
	int *arr;
	int m;
public:
	Array(int n)
	{
		m = n;
		arr = new int[n];
		for (int i = 0; i < n; i++) arr[i] = 0;
	}

	void change(int j, int x)
	{
		arr[j] = x;
	}

	void shift(int k)
	{
		int *data = new int[m];
		for (int i = 0; i < m-k; i++)
		{
			data[i + k] = arr[i];
		}
		
		int j = 0;
		for (int i = k; i < m; i++)
		{
			data[j] = arr[i];
			j++;
		}
	}

	int get_arr(int j)
	{
		return arr[j];
	}

	
};
int main()
{
	int n;
	cin >> n;
	Array p(n);
	int j, x;
	cin >> j; cin >> x;

	for (int i = 0; i < n; i++)
	{
		p.change(i, i+1);
		cout << p.get_arr(i);
	}
	
	int k; cin >> k;

	p.shift(k);

	for (int i = 0; i < n; i++)	cout << p.get_arr(i);
	
}
