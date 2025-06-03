#pragma once

#include "func.hpp"
#include <vector>
#include <string>
#include <algorithm> // For std::transform

template <typename T>
std::vector<T> MaxVector(const std::vector<T>& vec1, const std::vector<T>& vec2) {
    size_t maxSize = std::max(vec1.size(), vec2.size());
    std::vector<T> result(maxSize);

    std::transform(result.begin(), result.end(), result.begin(),
                   [&, i = size_t{0}](auto&) mutable -> T {
                       T val1 = (i < vec1.size()) ? vec1[i] : T();
                       T val2 = (i < vec2.size()) ? vec2[i] : T();

                       T value;
                       if (i >= vec1.size()) {
                           value = vec2[i]; // Take the remaining elements of vec2
                       } else if (i >= vec2.size()) {
                           value = vec1[i]; // Take the remaining elements of vec1
                       } else {std::vector<T> result(maxSize);                         
                           value = std::max(val1, val2); // Take the maximum of the two
                       }
                       ++i; 
                       return value;
                   });

    return result;
}
