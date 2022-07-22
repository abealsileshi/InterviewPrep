#include "linkedList.hpp"

int main(){
    LinkedList * ll = new LinkedList();
    ll->addNode(1);
    ll->addNode(2);
    ll->addNode(3);
    ll->addNode(4);
    ll->addNode(5);
    ll->printLL();
    ll->find(30);

    node n,n2,n3,n4;
    n.data = 99;
    n.next = &n2;
    n2.data = 199;
    n2.next = &n3;
    n3.data =299;
    n3.next = NULL;

    //printing addresses (they are the same)
    cout << (n2.next) << endl;
    cout << &n3 << endl;


}