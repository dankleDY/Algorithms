Recursion in data structures

1. Linked List addSorted

<template T>
class LinkedList {
    private:
    class Node{
        public:
        T data;
        Node* next;
        Node* prev;
        Node(const T&d):data(d),next(NULL),prev(NULL){}
        Node(const T&d, Node* n):data(d),next(n){
            if(n!=NULL){
                prev=n->prev;
            }
            else{
                prev=NULL;
            }
        }
    }

    Node* addSorted(const T& data, Node * curr){ 
        if(curr==NULL || data < curr->data){
            return new Node(data,curr);
        }
        curr->next=addSorted(data,curr->next);
        return curr;
    }
    // This recursion equals to a while loop (while curr!=NULL && data > curr->data : curr=curr->next)

    public:
    void addSorted(const T& data){
        head=addSorted(data,head);
    }
}

2. Add to a BST

Node* add(Node * curr, int data){
    if(curr==NULL){
        Node * ans= new Node(data);
        return ans;
    }
    else{
        if(data<curr->data){
            Node* newleft = add(curr->left,data);
            curr->left=newleft;
        }
        else{
            Node* newright = add(curr->right,data);
            curr->right=newright;
        }
        return curr;
    }
}

// This equals to the following none recursion method
// A perfect practise for pointer understanding

void add(int data){
    Node ** curr= & root;
    while(*curr != NULL){
        if(data < (*curr)->data){
            curr=&(*curr)->left; //curr points to left child
        }
        else{
            curr=&(*curr)->right;
        }
    }
    *curr=new Node(data); // not curr but *curr
}

3. BST traversal

void printInorder(Node * curr){
    if(curr!=NULL){
        printInorder(curr->left);
        cout<<curr->data<<" ";
        printInorder(curr->right);
    }
}
