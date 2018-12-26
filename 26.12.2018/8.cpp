/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int M;
    cin >> M;
    int *w = new int[N];
    int *c = new int[N];
    for(int i = 1; i < N; i++)
    {
        cout << "вес " << i << " предмета: "; cin << w[i];
        cout << "стоимость " << i << " предмета: "; cin << c[i];
        cout << "\n";
    }
    int **A = new *int[n] //A[N][M]
    for(int i = 0; i < n; i++)
    A[i] = new int[M];
    
    for(int i = 0; i < N; i++)
    A[i][0] = 0;
    for(int i = 0; i < M; i++)
    A[0][i] = 0;
    
    for(int i = 1; i < N; i++)
    {
        for(int j = 1; j < M; i++)
        {
            if(j < w[j])
            A[i][j] = max(A[i-1][j], A[i-1][j-w[j]] + c[i])
        }
    }
    cout << "\n";
    cout << A[N-1][M-1];
    
    return 0;
}
