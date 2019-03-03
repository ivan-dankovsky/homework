/* */
#include <iostream>
using namespace std;
struct Node {
double data;
Node* next = NULL;
};
class double_stack{
private:
    Node* head;
public:
    double_stack(): head(NULL)
    {}
    void push_bck(double x){
    Node* temp = new Node;
    temp ->data = x;
    temp ->next = head;
    head = temp;
    }
    double pop_bck(){
    if(head == NULL){
        cout<<"stack is empty";
        return 0;
    }
    double x = head ->data;
    Node* temp = head;
    head = head ->next;
    delete temp;
    return x;
    }
    ~double_stack(){
    while(head != NULL){
        Node* temp = head;
        head = head ->next;
        delete temp;
    }
    cout<<" destructor is working ";
    }
};
int main(){
    double_stack a;
    a.push_bck(4);
    a.push_bck(5);
    a.push_bck(6);
    a.push_bck(7);
    a.push_bck(8);
    cout<<a.pop_bck();
return 0;
}
