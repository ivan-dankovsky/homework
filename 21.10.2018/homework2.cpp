#include <iostream>
#include <bitset>

using namespace std;

struct IpAddress{
    unsigned short ip[4];
    unsigned short mask[4];

    string operator<<(){
        return to_string(ip[0]) + "." + to_string(ip[1]) + "." + to_string(ip[2]) + "." + to_string(ip[3])
    }

}

int main(){
    cout << bitset(1).to_string();

    return 0;
}
