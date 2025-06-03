/**
 * CSE 232 - Coding Exam [Final]
 * Version "Green"
 * 
 * Do not edit this document unless otherwise instructed.
 * It will be hard to come back and fix it later.
 * Below contains the list of questions, their descriptions, 
 *      the functions and specifications required to complete them, 
 *      and starting code (if applicable).
 */

/**
 * 1. ManyWords
 * 
 * Write a main.cpp and header file -> you start with blank files
 * 
 * The program takes in standard input, multi-lined (so test in Codio),
 *      and for a given line, first, we need to count the number of words
 *      in the line. Then, we need to output back that line with the number.
 * 
 * However, not just by outputting each line back!!! We need to output the
 *     lines in order of the number of words in the line. So, the line with
 *     the fewest words should be output first, and the line with the most
 *     words should be output last.
 * 
 * Additionally, if two lines have the same number of words, then output
 *    them in the order they were input.
 * 
 * Sample Tests:
 * "This is a test" -> "4: This is a test"
 * "This is a tester message
 *  
 *  Why no lines before? Watch out.
 *  wedsdfsdfsd"
 * 
 * ->
 * 
 * 0: 
 * 1: wedsdfsdfsd
 * 4: This is a tester message
 * 6: Why no lines before? Watch out.
 */

// header.hpp
// main.cpp

/**
 * 2. SingleLink (Swap)
 * 
 * Write the implementation of two member functions, respectively called SwapFirst2
 *    and SwapLast2 in the implementation file and header file for the SingleLink class.
 * -> You are given the SingleLink class in both the header and implementation files (provided below).
 * 
 * Remember the SingleLink class from the course, this is based on that.
 * We need create our member functions so that they swap the first/last two elements.
 * Additionally, if there is only one element, then do nothing.
 * 
 * However, if there are three or more elements, and we have swapped the 
 *      last two elements, then also swap the first two elements.
 * 
 * Sample Tests:
 * SingleLink sl;
 * sl.append_back(1);
 * sl.append_back(2);
 * sl.append_back(3);
 * 
 * sl.SwapFirst2();
 * assert(sl[0].data_ == 2);
 * assert(sl[1].data_ == 1);
 * 
 * sl.SwapLast2();
 * assert(sl[1].data_ == 3);
 * assert(sl[2].data_ == 1);
 * 
 * 
 * SingleLink sl2;
 * sl2.append_back(1);
 * sl2.SwapFirst2();
 * assert(sl2[0].data_ == 1);
 * 
 * 
 * SingleLink sl3;
 * sl3.append_back(1);
 * sl3.SwapLast2();
 * assert(sl3[0].data_ == 1);
 * 
 * SingleLink sl4;
 * sl4.append_back(1);
 * sl4.append_back(2);
 * sl4.append_back(3);
 * sl4.SwapLast2();
 * assert(sl4[0].data_ == 3);
 * assert(sl4[1].data_ == 1);
 * assert(sl4[2].data_ == 2);
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
 * 3. AlphabetPosition
 * 
 * Write a main.cpp and header file (if needed) -> you start with blank files
 * 
 * The program must take in standard input, and we need to take only a single
 *      character. The character will be from (a-z) or (A-Z). So, no need to
 *      worry about other characters.
 * 
 * The alphabet can be zero-indexed. When we do so, a is 0, b is 1, c is 2, and so on.
 * Additionally, we don't care about case. So, A is the same as a.
 * Simply output the position of the character in the alphabet.
 * 
 * Sample Tests:
 * assert(AlphabetPosition('a') == 0);
 * assert(AlphabetPosition('b') == 1);
 * assert(AlphabetPosition('Z') == 25);
 */

// main.cpp

/**
 * 4. OverUnder
 * 
 * The user is given a computerized jelly bean jar, and they have to guess the number.
 * Write an entire class called OverUnder in a header file, implementation file, and
 *     a main file. -> You start with blank files
 * The class should have the following member functions:
 * 
 * 1. OverUnder() - Constructor
 *     -> Initializes the list to be empty
 * 2. void add(int) - Adds an integer to the list
 *      -> where the user has given a guess of the number of elements in the jar
 * 3. int over(int) - Returns the number of elements in the list that are greater than the given integer
 * 4. int under(int) - Returns the number of elements in the list that are less than the given integer
 * 
 * In main, you need to take in standard input. Each line will only have the guess.
 *     If the guess is -1, then we need to output the number of elements in the list.
 *     Otherwise, we need to add the guess to the list.
 *     When the user enters the correct number of elements in the jar, then we need to halt.
 * 
 * Additionally, watch, as Codio will, in this case, test for leaked memory!
 * 
 * Sample Tests (these might be slightly off, I did not memorize these ones, unfortunately):
 * Input:
 * 10
 * 5
 * 15
 * 25
 * 
 * ->
 * 
 * Output:
 * 0 0
 * 1 0
 * 1 1
 * 2 1
 */

// OverUnder.hpp
// OverUnder.cpp
// main.cpp

/**
 * 5. OnlyLocalEntries
 * 
 * Given the file PhoneBook.hpp (provided below), which contains the class PhoneBook,
 *     write the implementation of the member function OnlyLocalEntries.
 * -> do so in both the seperate implementation file and header file 
 *      (which can be together). (those are given blank)
 * 
 * The function should remove all entries from the phone book that are of the local
 *      area code. The area code is the first three digits of a phone number.
 *      In East Lansing's case, the area code is 517. Therefore, your modified
 *      phone book should only contain entries with the area code 517.
 * 
 * Additionally, if the phone number is not in the correct format (10 digits),
 *     then we should remove that entry as well.
 * 
 * Sample Tests:
 * PhoneBook pb;
 * pb.AddEntry("John", "517-123-4567");
 * pb.AddEntry("Jane", "517-123-4567");
 * pb.AddEntry("Jake", "517-123-4567");
 * pb.AddEntry("Jill", "424-123-4567");
 * pb.AddEntry("James", "081-123-4567");
 * 
 * pb.OnlyLocalEntries();
 * 
 * assert(pb.entries_.size() == 3);
 * assert(pb.entries_[0].name_ == "John");
 * assert(pb.entries_[1].name_ == "Jane");
 * assert(pb.entries_[2].name_ == "Jake");
 * 
 * test using the public member function Display
 */

// PhoneBook.hpp
#pragma once

#include <string>
#include <vector>

struct Entry {
    std::string name_;
    std::string phone_number_;
};

class PhoneBook {
    private:
        std::vector<Entry> entries_;

    public:
        PhoneBook();
        void AddEntry(const std::string &name, const std::string &phone_number);
        void RemoveEntry(const std::string &phone_number);
        void Display() const;

        // what I add
        void OnlyLocalEntries();
        int size() const { return entries_.size(); }

        friend std::ostream& operator<<(std::ostream &out, const PhoneBook &pb);
};

// implementation.cpp
#include "PhoneBook.hpp"

PhoneBook::PhoneBook() {}

void PhoneBook::AddEntry(const std::string &name, const std::string &phone_number) {
    Entry newEntry;
    newEntry.name_ = name;
    newEntry.phone_number_ = phone_number;
    entries_.push_back(newEntry);
}

void PhoneBook::RemoveEntry(const std::string &phone_number) {
    for (size_t i = 0; i < entries_.size(); i++) {
        if (entries_[i].phone_number_ == phone_number) {
            entries_.erase(entries_.begin() + i);
            return;
        }
    }
}

void PhoneBook::Display() const {
    for (size_t i = 0; i < entries_.size(); i++) {
        std::cout << entries_[i].name_ << " " << entries_[i].phone_number_ << std::endl;
    }
}

std::ostream& operator<<(std::ostream &out, const PhoneBook &pb) {
    for (size_t i = 0; i < pb.entries_.size(); i++) {
        out << pb.entries_[i].name_ << " " << pb.entries_[i].phone_number_ << std::endl;
    }
    return out;
}

// header.hpp