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

void SingleLink::SwapFirst2() {
    if (!head_ || !head_->next_) return;  // Not enough elements to swap
    Node *temp = head_->next_; // temporary node to store the second node
    head_->next_ = temp->next_; // first node now points to the third node
    temp->next_ = head_; // second node now points to the first node
    head_ = temp; // second node is now the head
}

void SingleLink::SwapLast2() {
    // If the list has less than 2 elements, swapping last two is not possible
    if (head_ == nullptr || head_->next_ == nullptr) {
        return;
    }

    // Find the second to last node and the last node
    Node* prev = nullptr;
    Node* curr = head_;
    while (curr->next_ != nullptr) {
        prev = curr;
        curr = curr->next_;
    }

    // At this point, prev is the second to last node, and curr is the last node
    if (prev != nullptr) {
        std::swap(prev->data_, curr->data_);
    }
}





// Rule of three stuff, I won't even touch this
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

