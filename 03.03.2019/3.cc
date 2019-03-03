/* */
#include <iostream>
using namespace std;
struct Node {
char data;
Node* next = NULL;
Node* prev = NULL;
};
class char_deque{
private:
    Node* head;
    Node* tail;
public:
    char_deque(): head(NULL), tail(NULL){
    }
    void push_frt(char x){
        Node* temp = new Node;
    temp ->prev = NULL;
          temp ->data = x;
        if(head != NULL){
            head ->prev = temp;
            temp ->next = head;
            head = temp;
        }
        else{
            temp ->next = NULL;
            tail = temp;
            head = tail;
        }
    }
    void push_bck(char x){
        Node* temp = new Node;
    temp ->next = NULL;
       temp ->data = x;
        if(tail != NULL){
            tail ->next = temp;
            temp ->prev = tail;
            tail = temp;
        }
        else{
            temp ->prev = NULL;
            tail = temp;
            head = tail;
        }
    }
    void pop_frt(){
    if(head == NULL){
        cout<<" char_deque is empty";
    }
    else{
    char x = head ->data;
    cout<<x;
    head = head ->next;
    }
    }
    void pop_bck(){
    if(head == NULL){
        cout<<" char_deque is empty";
    }
    else{
    char x = tail ->data;
    cout<<x;
    tail = tail ->prev;
    }
    }
    ~char_deque(){
    while(head != NULL){
        Node* temp = head;
        head = head ->next;
        delete temp;
    }
    cout<<" destructor is working ";
    }
};
int main()
{
    char_deque a;
 char b, m, c, d;
    cin>>b;
     cin>>m;
      cin>>c;
       cin>>d;

a.push_frt(b);

a.push_frt(m);

a.push_frt(c);

a.push_frt(d);
a.pop_bck();
return 0;
}
