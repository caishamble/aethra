/**
 * CSE 232 - Coding Exam [Final]
 * Version "White"
 * 
 * Do not edit this document unless otherwise instructed.
 * It will be hard to come back and fix it later.
 * Below contains the list of questions, their descriptions, 
 *      the functions and specifications required to complete them, 
 *      and starting code (if applicable).
 */

/**
 * 1. Calculator
 * 
 * Write a program in main.cpp -> you start with blank files
 * 
 * You need to take in mathematical expressions from standard input
 * Output the result of that expression to output.
 * The expressions are only for summing(+) and subtracting(-).
 * 
 * Sample Tests:
 * "9 + 5" -> 14
 * "9 - 5" -> 4
 */

// main.cpp that might work
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string input;
    getline(cin, input);
    stringstream ss(input);
    int num1, num2;
    char op;
    ss >> num1 >> op >> num2;
    if (op == '+') {
        cout << num1 + num2 << endl;
    } else if (op == '-') {
        cout << num1 - num2 << endl;
    }
    return 0;
}

/**
 * 2. SingleLink (merge)
 * 
 * We have a class named SingleLink previously discussed in class.
 * I’ve implemented the class and provided a header, but there is one 
 *      method that I haven’t implemented (and it is the only new method you 
 *      need to provide)
 * 
 * Very similar to a problem, count, that returns the number of elements 
 *      that match a provided character.
 * 
 * We need to create a method that merges two SingleLink objects together.
 * This will add all the elements from the other SingleLink to the end of
 *     the current SingleLink. Additionally, the other SingleLink should be
 *     empty after the merge.
 * 
 * Sample Tests:
 * Each object is basically a list. 

A = 1, 2, 3
B = 5, 6, 7

After the Merge A will be 1,2,3,5,6,7 and B will be cleaned
 */

// SingleLink.hpp
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
        void merge(SingleLink &other); // THIS IS THE POSSIBLE ANSWER

        friend std::ostream& operator<<(std::ostream &out, const SingleLink &s);
        bool del(int val);
        Node& operator[](size_t index);
        
        // Rule of three stuff
        ~SingleLink();
        SingleLink(const SingleLink &);
        SingleLink& operator=(SingleLink);
};

// SingleLink.cpp
#include "Singlelink.hpp"
#include <iostream>
#include <stdexcept>

SingleLink::SingleLink() : head_(nullptr), tail_(nullptr) {}

SingleLink::SingleLink(int dat) {
    Node *newNode = new Node(dat);
    head_ = tail_ = newNode;
}

void SingleLink::append_back(int dat) {
    Node *newNode = new Node(dat);
    if (!head_) {  // List is empty
        head_ = tail_ = newNode;
    } else {
        tail_->next_ = newNode;  // Link the last node to new node
        tail_ = newNode;          // Update the tail pointer
    }
}

std::ostream& operator<<(std::ostream& os, const SingleLink& sl) {
    Node* current = sl.head_;  // Accessing the head node correctly

    if (current != nullptr) {
        os << current->data_;  // Output the first element
        current = current->next_;

        while (current != nullptr) {
            os << ", " << current->data_;  // Output the rest with a comma separator
            current = current->next_;
        }
    }

    return os;
}

// this is the answer here, you need to add a merge member function
void Merge(SingleLink& other) {
    if (head_ == nullptr) {
        head_ = other.head_;
        other.head_ = nullptr;
        return;
    }
    Node* curr = head_;
    while (curr->next_ != nullptr) {
        curr = curr->next_;
    }
    curr->next_ = other.head_;
    other.head_ = nullptr;
}

bool SingleLink::del(int val) {
    if (!head_) return false;  // Empty list case

    // If the head node is the one to delete
    if (head_->data_ == val) {
        Node *temp = head_;
        head_ = head_->next_;
        delete temp;
        if (!head_) tail_ = nullptr;  // List is now empty
        return true;
    }

    // Traverse the list to find the node to delete
    Node *current = head_;
    while (current->next_ && current->next_->data_ != val) {
        current = current->next_;
    }

    // If the node was found
    if (current->next_) {
        Node *temp = current->next_;
        current->next_ = temp->next_;
        if (temp == tail_) tail_ = current;  // Update tail if necessary
        delete temp;
        return true;
    }
    return false;  // Value not found
}

Node& SingleLink::operator[](size_t index) {
    Node *current = head_;
    size_t currentIndex = 0;

    while (current) {
        if (currentIndex == index) return *current;
        current = current->next_;
        currentIndex++;
    }

    throw std::out_of_range("Index out of range");
}

SingleLink::~SingleLink() {
    Node *current = head_;
    while (current) {
        Node *temp = current;
        current = current->next_;
        delete temp;
    }
    head_ = tail_ = nullptr;
}

SingleLink::SingleLink(const SingleLink &other) : head_(nullptr), tail_(nullptr) {
    Node *current = other.head_;
    while (current) {
        append_back(current->data_);
        current = current->next_;
    }
}

SingleLink& SingleLink::operator=(SingleLink other) {
    std::swap(head_, other.head_);
    std::swap(tail_, other.tail_);
    return *this;
}

/**
 * 3. StringMultiply
 * 
 * Write a main.cpp file -> you start with blank files
 * you will have like lists of number and strings e.g. {3, 20, "dog"} , 
 * {4,10, "cat"} and you need to multiply the first two numbers to 
 * determine the biggest area and use this final area to sort those lists
 * 
 * Sample Tests:
 * {3, 20, "dog"} , {4,10, "cat"} -> {60, "dog"}, {40, "cat"}
 */

// main.cpp that might work
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int, string>> list1 = {{3, "dog"}, {20, "cat"}};
    vector<pair<int, string>> list2 = {{4, "dog"}, {10, "cat"}};

    int area1 = list1[0].first * list1[1].first;
    int area2 = list2[0].first * list2[1].first;

    if (area1 > area2) {
        swap(list1[0], list1[1]);
    } else {
        swap(list2[0], list2[1]);
    }

    for (auto &p : list1) {
        cout << "{" << p.first << ", " << p.second << "}, ";
    }
    cout << endl;
    for (auto &p : list2) {
        cout << "{" << p.first << ", " << p.second << "}, ";
    }
    cout << endl;

    return 0;
}

// time

// You need to create a class named Time that has the following members:
// private members: int minute, int hour
// public members:

//Constrctor  Time(int h, int m) - constructor that sets the time to h:m
//Void minuteincrement() - increments the minute by 1
//Void hourincrement() - increments the hour by 1
//std::ostream& operator<<(std::ostream &out, const Time &t) - prints the time in the format hh:mm
//std::istream& operator>>(std::istream &in, Time &t) - reads the time in the format hh:mm

// follow is answer

// main.cpp
#include <iostream>
#include <sstream>
#include "header.hpp"

using namespace std;

int main() {
    Time t(12, 30);
    std::cout << t << std::endl; // 12:30
    t.minuteincrement();
    std::cout << t << std::endl; // 12:31
    t.hourincrement();
    std::cout << t << std::endl; // 1:31

    Time t2(11, 59);
    std::cout << t2 << std::endl; // 11:59
    t2.minuteincrement();
    std::cout << t2 << std::endl; // 12:00
    t2.minuteincrement();
    std::cout << t2 << std::endl; // 12:01

    Time t3(1, 0);
    std::cout << t3 << std::endl; // 1:00
    t3.minuteincrement();
    std::cout << t3 << std::endl; // 1:01

    stringstream iss("12:30");
    iss >> t3;
    std::cout << t3 << std::endl; // 12:30

    return 0;
}

// header.hpp
#pragma once

#include <iostream>

class Time {
    private:
        int minute;
        int hour;

    public:
        Time(int h, int m);
        void minuteincrement();
        void hourincrement();

        friend std::ostream& operator<<(std::ostream &out, const Time &t);
        friend std::istream& operator>>(std::istream &in, Time &t);
};



// implementation.cpp
#include "header.hpp"

Time::Time(int hour, int minute) : hour(hour), minute(minute) {}

void Time::minuteincrement() {
    minute += 1;
    if (minute == 60) {
        minute = minute % 60;
        hour += 1;
        if (hour == 12) {
            hour = hour % 12;
        }
    }
}

void Time::hourincrement() {
    hour += 1;
    if (hour == 12) {
        hour = hour % 12;
    }
}

std::ostream& operator<<(std::ostream &out, const Time &t) {
    if (t.hour < 10) {
        out << "0";
    }
    out << t.hour << ":";
    if (t.minute < 10) {
        out << "0";
    }
    out << t.minute;
    return out;
}

std::istream& operator>>(std::istream &in, Time &t) {
    char colon;
    in >> t.hour >> colon >> t.minute;
    return in;
}
