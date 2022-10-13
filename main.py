from ctypes import CDLL, c_double
import os
import math


def main():
    so_file = "./test.so"
    if os.name == "nt":
        so_file = "./test.dll"

    lib = CDLL(so_file)
    assert lib.square(10) == 100, "Cannot validate V square()."

    lib.sqrt_of_sum_of_squares.restype = c_double
    assert lib.sqrt_of_sum_of_squares(c_double(1.1), c_double(2.2)) == math.sqrt(1.1*1.1 + 2.2*2.2), "Cannot validate V sqrt_of_sum_of_squares()."

    hello = lib.hello("zztkm")
    print(hello)
    print("end")


if __name__ == "__main__":
    main()