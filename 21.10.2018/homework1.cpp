#include <iostream>
using namespace std;

int GCD(int a, int b){
    if (b == 0) return a;

    return GCD(b, a % b);
}


struct Rational{
    int m;
    int n;

    Rational(int a, int b = 1){
        int gcd = GCD(a, b);

        m = a/gcd;
        n = b/gcd;

        cout << "constructor is working" << endl;
    }

    Rational operator=(Rational R){
        m = R.m;
        n = R.n;
        cout << "operator= is working" << endl;
    }

    bool operator==(Rational R){
        cout << "operator== is working" << endl;
        if (R.m == m && R.n == n)
            return true;
        else
            return false;
    }

    bool operator>(Rational R){
        int p = R.n;
        int q = R.m;

        cout << "operator> is working"  << endl;

        if (m*p > q*n)
            return true;
        else
            return false;
    }

    bool operator< (Rational R){
        cout << "operator< is working" << endl;

        if (*this > R || *this == R)
            return false;
        else
            return true;
    }

    bool operator>= (Rational R){
        cout << "operator>= is working" << endl;

        if(*this == R || *this > R)
            return true;
        else
            return false;
    }

    bool operator <= (Rational R){
        cout << "operator<= is working" << endl;

        if (*this == R || *this < R)
            return true;
        else
            return false;
    }

    Rational operator+=(Rational R){
        int temp = n;
        n *= R.n;
        m *= R.n;
        m += R.m*temp;
        int gcd = GCD(m, n);
        m /= gcd;
        n /= gcd;
        return *this;
    }

    Rational operator+(Rational R){
        int a = m*R.n;
        int b = R.m*n;
        int c = R.n*n;
        return Rational(a+b, c);
    }

    void print(){
        cout << m << "/" << n;
    }
};


int main(){

    Rational a = Rational(100, 50);
    Rational b = Rational(33, 15);
    Rational c = a;
    cout << "a = "; a.print(); cout << endl;
    cout << "b = "; b.print(); cout << endl;

    cout << "a == b: " << (a == b) << endl;
    cout << "a > b: " << (a > b) << endl;
    cout << "a < b: " << (a < b) << endl;
    cout << "a >= b: " << (a >= b) << endl;
    cout << "a <= b: " << (a <= b) << endl;
    cout << "a + b: "; (a + b).print(); cout << endl;
    cout << "a += b: "; a += b; cout << endl;
    cout << "a = "; a.print(); cout << endl;
}
