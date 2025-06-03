#include <bits/stdc++.h>

using namespace std;

int main(){
    // math function
    // accumulate
    vector<int> v = {1, 2, 3, 4, 5};
    cout << accumulate(v.begin(), v.end(), 0) << endl; // 15
    vector<double> v2 = {1.1, 2.2, 3.3, 4.4, 5.5};
    cout << accumulate(v2.begin(), v2.end(), double(1)) << endl; // 17.5

    // product of all elements in a vector
    std::vector<int> factors{2, 4, 29};
    double product = std::accumulate(
        factors.begin(), factors.end(), int{1},
        [](int a, int b) { return a * b; }
    );
    // Result: 232
    // starting from 1, 1*2 = 2, 2*4 = 8, 8*29 = 232

    // Concatenate 
    std::string CommaSeparate(std::string const& left, std::string const& right) {
        return left + "," + right;
    }

    // ...
    std::vector<std::string> names{"Mal", "Kira", "Dax"};
    std::string line = std::accumulate(
        names.begin(), names.end(),
        std::string{"Josh"}, CommaSeparate
    );
    // Result: Josh,Mal,Kira,Dax


    // execution policy
    // parallel execution
    vector<int> v3(1000000, 1);
    cout << accumulate(v3.begin(), v3.end(), 0) << endl; // 1000000
    cout << accumulate(v3.begin(), v3.end(), 0, plus<int>(), execution::par) << endl; // 1000000

    // complex number
    std::vector<std::complex<int>> vec = {{2, 3}, {4, 5}, {10, -30}};
    int imag_sum = std::accumulate(
        vec.begin(), vec.end(), int{0},
        [](int x, std::complex<int> y) {
            return x + y.imag();
    });
    // Result: -22    
    return 0;
}



#include <random>
#include <iostream>

int main() {
    // Create a random_device object to generate a random seed
    std::random_device rd;

    // Initialize the Mersenne Twister 64-bit random number generator with the seed
    std::mt19937_64 gen(rd());

    // Create a uniform integer distribution in the range [1, 6]
    std::uniform_int_distribution<> dist(1, 6);

    // Generate 20 random numbers using the distribution
    for (int i{0}; i < 20; ++i) {
        // Generate a random number and output it, followed by a space
        std::cout << dist(gen) << " ";  // Output a random number in the range [1, 6]
    }

    // Print a newline at the end
    std::cout << std::endl;

    // uniform_int_distribution (a,b) -> [a,b]
    // uniform_real_distribution (a,b) -> [a,b)
    // normal_distribution (mean, std_dev)
    // bernoulli_distribution (p) -> true with probability p
    // binomial_distribution (n, p) -> number of successes in n trials with probability p
    // poisson_distribution (mean) -> number of events in a fixed interval with mean rate
    // exponential_distribution (lambda) -> time between events with rate lambda
    // gamma_distribution (alpha, beta) -> sum of alpha exponential random variables with rate beta
    // weibull_distribution (a, b) -> time until event with shape a and scale b

    // valarray
    // valarray is a class template that represents an array of values.
    // It is designed to be a simpler and more efficient alternative to the vector class for some use cases.
    

    // c-style array
    int arr[5] = {1, 2, 3, 4, 5};
    int arr[5] = {1, 2, 3}; // {1, 2, 3, 0, 0}
    int arr[5] = {}; // {0, 0, 0, 0, 0}
    int arr[] = {1, 2, 3, 4, 5}; // size 5
    int arr[] = {1, 2, 3}; // size 3
    int arr[] = {}; // size 0
    int arr[5]; // uninitialized
    

    return 0;
}
