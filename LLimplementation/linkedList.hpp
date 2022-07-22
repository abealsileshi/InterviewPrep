#include <iostream>

using namespace std;

struct node{
    int data;
    node * next;
};

class LinkedList{
    private:
    node * head;
    node * tail;


    public:
    LinkedList();
    bool isEmpty();
    void addNode(int val);
    node * find(int val);
    void printLL();

};
