/* */
#include <iostream>
#include <string>
using namespace std;
struct Node {
string str;
Node* next = NULL;
};
class queue_string{
private:
    Node* head;
public:
    queue_string(): head(NULL){};
    void push(string a){
    Node* temp = new Node;
    temp ->str = a;
    temp ->next = head;
    head = temp;
    }
    void pop(){
    if(head == NULL){
        cout<<"queue_string is empty";
    }
    Node* temp = head;
    while(temp ->next){
        temp = temp ->next;
    }
   head = head ->next;
   cout<<temp ->str;
   delete temp;
    }
    ~queue_string(){
    while(head != NULL){
        Node* temp = head;
        head = head ->next;
        delete temp;
    }
    cout<<" destructor is working ";
    }
};
int main(){
    queue_string b;
    string a;
    cin>>a;
    b.push(a);
    b.pop();

return 0;
}
