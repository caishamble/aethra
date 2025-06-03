#include <iostream>
#include <cassert>
#include <stdexcept>
#include "SingleLink.hpp"

int main() {
    SingleLink sl;
    sl.append_back(1);
    sl.append_back(2);
    sl.append_back(3);

    sl.SwapFirst2();
    assert(sl[0].data_ == 2);
    assert(sl[1].data_ == 1);

    sl.SwapLast2();
    assert(sl[1].data_ == 3);
    assert(sl[2].data_ == 1);

    SingleLink sl2;
    sl2.append_back(1);
    sl2.SwapFirst2();
    assert(sl2[0].data_ == 1);

    SingleLink sl3;
    sl3.append_back(1);
    sl3.SwapLast2();
    assert(sl3[0].data_ == 1);

    SingleLink sl4;
    sl4.append_back(1);
    sl4.append_back(2);
    sl4.append_back(3);
    sl4.SwapLast2();
    assert(sl4[0].data_ == 1);
    assert(sl4[1].data_ == 3);
    assert(sl4[2].data_ == 2);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}