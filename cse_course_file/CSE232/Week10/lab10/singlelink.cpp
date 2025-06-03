#include<iostream>
#include<sstream>
#include<stdexcept>
#include<string>
#include<algorithm>

#include "singlelink.hpp"

SingleLink::SingleLink(int dat) {
  head_ = new Node(dat);
  tail_ = head_;
}

SingleLink::SingleLink() {
  head_ = nullptr;
  tail_ = nullptr;
}

void SingleLink::append_back(int dat) {
  //*next_ = nullptr;
  Node* new_node = new Node(dat);
  if (tail_ ==  nullptr) {
    head_ = tail_ = new_node;
  } else {
    tail_->next_ = new_node;
    tail_ = new_node;
  }
}

std::ostream & operator<<(std::ostream &out, const SingleLink &s) {
  Node* current_node = s.head_;
  while(current_node != nullptr) {
    if (current_node->next_ != nullptr){
      out << current_node->data_ << ", ";
    }else if(current_node->next_ == nullptr){
      out << current_node->data_;
    }
    current_node = current_node->next_;
  }
  return out;
}

bool SingleLink::del(int val) {
    Node* current_node = head_;
    Node* previous_node = nullptr;

    while (current_node != nullptr) {
        if (current_node->data_ == val) {
            // Case 1: Deleting the head node
            if (current_node == head_) {
                head_ = current_node->next_;
                if (head_ == nullptr) {  // If head_ is now nullptr, the list is empty
                    tail_ = nullptr;
                }
            } 
            // Case 2: Deleting any other node
            else {
                previous_node->next_ = current_node->next_;
                if (current_node->next_ == nullptr) {  // If deleting the last node
                    tail_ = previous_node;
                }
            }

            delete current_node;  // Free memory of the deleted node
            return true;  // Return true to indicate successful deletion
        }

        // Move to the next node in the list
        previous_node = current_node;
        current_node = current_node->next_;
    }

    return false;  // Return false if the value was not found
}

Node & SingleLink::operator[](size_t index) {
  Node* current_node = head_;
  size_t counter = 0;
  while(current_node != nullptr) {
    if (counter == index) {
      return *current_node;
    }
    current_node = current_node->next_;
    counter++;
  }
  throw std::out_of_range("you are out of RANGE!!!");
}