#include <iostream>
#include <bitset>
#include <string>
#include <sstream>

/*
Реализуйте структуру IpAddress для работы с IPv4 адресацией. Структура
должна хранить информацию об IP и маске, а также уметь вычислять адрес
подсети, номер компьютера в сети, следующий/предыдущий адрес. В
программе должно присутствовать описание структуры и программа
показывающая работоспособность структуры
*/

using namespace std;

struct IpAddress{
    unsigned short ip[4];
    unsigned short mask[4];

    IpAddress(unsigned short i[4], unsigned short m[4]){
        for (int j=0; j <= 3; j++){
            mask[j] = m[j];
            ip[j] = i[j];
        }
    }

    void print(){
        cout << ip[0] << "." << ip[1] << "." << ip[2] << "." << ip[3] << endl;
    }

    void print_mask(){
        for (int i=0; i <= 3; i++){
            cout << mask[i];
            if (i != 3) cout << ".";
        }
        cout << endl;
    }

    IpAddress next(){
        unsigned short ip_temp[4];
        for (int i=0; i<=3; i++)
            ip_temp[i] = ip[i];
        if (ip[3] + 1 <= 255){
            ip_temp[3] += 1;
        }
        else if (ip[2] + 1 <= 255){
            ip_temp[2] += 1;
        } else if (ip[1] + 1 <= 255){
            ip_temp[1] += 1;
        } else if (ip[0] + 1 <= 255) {
            ip_temp[0] += 1;
        }
        return IpAddress(ip_temp, mask);
    }
    IpAddress previous(){
        unsigned short ip_temp[4];
        for (int i=0; i<=3; i++)
            ip_temp[i] = ip[i];
        if (ip[3] - 1 >= 0){
            ip_temp[3] -= 1;
        }
        else if (ip[2] - 1 >= 0){
            ip_temp[2] -= 1;
        } else if (ip[1] - 1 >= 0){
            ip_temp[1] -= 1;
        } else if (ip[0] - 1 >= 0) {
            ip_temp[0] -= 1;
        }
        return IpAddress(ip_temp, mask);
    }


    void print_binary(){
        for (int i=0; i<=3; i++){
            cout << bitset<8>(ip[i]).to_string();
            if (i != 3) cout << ".";
        }
        cout << endl;
    }

    void print_hex(){
        cout << hex;
        for (int i=0; i<=3; i++){
            cout << ip[i];
            //if (i != 3) cout << ".";
        }
        cout << endl;
    }

};

int main(){
    unsigned short t_1[4] = {125, 125, 125, 125};
    unsigned short t_2[4] = {255, 255, 255, 255};
    IpAddress test = IpAddress(t_1, t_2);

    test.print();
    test.print_mask();

    test.next().print();
    test.previous().print();
    test.print_binary();
    test.print_hex();
    return 0;
}
