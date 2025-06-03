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
        std::cout << dist(gen) << " ";
    }

    // Print a newline at the end
    std::cout << std::endl;

    return 0;
}
