#pragma once

#include <iostream>

struct Node {
    public:
        int data_;
        Node *next_;
    
        Node() : data_(0), next_(nullptr) {};
        Node(int d) : data_(d), next_(nullptr) {};
};

class SingleLink {
    private:
        Node *head_;
        Node *tail_;

    public:
        SingleLink();         
        SingleLink(int dat);    
        void append_back(int);

        friend std::ostream& operator<<(std::ostream &out, const SingleLink &s);
        bool del(int val);
        Node& operator[](size_t index);

        void SwapFirst2();
        void SwapLast2();
        
        // Rule of three stuff
        ~SingleLink();
        SingleLink(const SingleLink &);
        SingleLink& operator=(SingleLink);
};