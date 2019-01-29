#include <iostream>

using namespace std;

class double_vector
{
private:
	double *arr;
	unsigned int size;
	unsigned int capacity;

public:
	double_vector()
	{
		arr = new double[1];
		size = 0;
		capacity = 1;
		arr[0] = 0;
	}

	double_vector(unsigned int n)
	{
		arr = new double[n];
		size = 0;
		capacity = n;
		for (int i = 0; i < n; i++)
			arr[i] = 0;
	}

	double_vector(const double_vector& a)
	{
		double* T = new double[a.capacity];
		for (int i = 0; i < a.capacity; i++)
			T[i] = 0;

		for (int i = 0; i < a.size; i++)
			T[i] = a.arr[i];

		size = a.size;
		capacity = a.capacity;
		arr = T;
		cout << " Copying Constructor is working";
	}

	const double_vector& operator= (const double_vector& a)
	{
		double* T = new double[a.capacity];
		for (int i = 0; i < a.capacity; i++) {
			T[i] = 0;
		}

		for (int i = 0; i < a.size; i++)
			T[i] = a.arr[i];

		size = a.size;
		capacity = a.capacity;
		delete[] arr;
		arr = T;
		cout << " operator = is working";
		return *this;
	}

	double_vector(double* a, unsigned int m)
	{
		delete[]arr;
		arr = a;
		size = m;
		capacity = m;
	}

	void push_bak(int x)
	{
		if (size >= capacity) {
			capacity *= 2;
			double* temp = new double[capacity];
			for (int i = 0; i < capacity; i++) {
				temp[i] = 0;
			}
			for (int i = 0; i < size; i++) {
				temp[i] = arr[i];
			}
			delete[]arr;
			arr = temp;
		}
		arr[size] = x;
		size++;
		cout << " push_bak is working ;";
	}

	double pop_bak()
	{
		double a;
		a = arr[size];
		arr[size] = 0;
		size--;
		cout << " pop_bak is working ;";
		return a;
	}

	double operator[] (unsigned int n)
	{
		cout << " operator [] is working ;";
		return arr[n - 1];
	}

	void print(unsigned int n)
	{
		cout << arr[n - 1];
		cout << " print is working ;";
	}
	void push_frnt(double x)
	{
		if (size >= capacity)
		{
			capacity *= 2;
			double* temp = new double[capacity];
			for (int i = 0; i < capacity; i++) {
				temp[i] = 0;
			}
			temp[0] = x;
			for (int i = 1; i <= size; i++) {
				temp[i] = arr[i - 1];
			}
			delete[]arr;
			arr = temp;
		}
		for (int i = size; i > 0; i--)
			arr[i] = arr[i - 1];

		arr[0] = x;
		size++;
		cout << " push_frnt is working ;";
	}

	double pop_frnt()
	{
		double a;
		a = arr[0];
		for (int i = 0; i < size - 1; i++)
			arr[i] = arr[i + 1];

		size--;
		cout << " pop_frnt is working ;";
		return a;
	}

	~double_vector()
	{
		delete[]arr;
		cout << " destructor is working ;";
	}
};


int main()
{
	double a = 10, b;
	unsigned int n = 10;
	double* j = new double[6];
	for (int i = 0; i < 6; i++)
		j[i] = i;

	double_vector p(n);
	double_vector g(j, 6);
	p.print(n - 3);
	a = p.pop_bak();
	g.print(1);
	for (int i = 0; i < 4; i++)
		g.push_frnt(3);

	g.print(n - 6);
	p = g;
	p.print(2);
	cout << " " << a;
	b = g.pop_frnt();
	cout << " " << b;
	return 0;
}
