/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
#include <cstdlib> 

using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr = new int[n];
    for(int i = 0; i < n; i++)
    cin >> n;
    int m,l; // para chisel
    int j = 0; //chislo sovpadeni s paroy
    for(int i = 0; i < n; i++)
    {
        if(arr[i] == m)
        j++;
        if(arr[i] == l)
        j++;
    }
    if(j => 2)
    cout << "true";
    else
    cout << "false";
return 0;
}