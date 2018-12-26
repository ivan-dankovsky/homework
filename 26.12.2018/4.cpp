/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int x;
    cin >> x;
    
    int n;
    cin >> n;
    int *a = new int[n];
    for(int i = 0; i < n; i++)
    cin >> a[i];
    
    int *y = new int[n];
    y[0] = a[n-1];
    for(int i = 1; i < n; i++)
    {
        y[i] = y[i-1]*x + a[n-i-1];
    }
    cout << "P(x) = " << y[n-1];
    return 0;
}
