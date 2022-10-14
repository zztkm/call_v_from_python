from ctypes import CDLL, c_char_p, c_double
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

    # 文字列のやり取りテスト
    # デフォルトで C int を返すと仮定されているので
    # 戻り値の型を指定する
    hello = lib.hello
    hello.restype = c_char_p
    res: bytes = hello(b"zztkm")
    print(res)
    print(res.decode("utf-8"))


if __name__ == "__main__":
    main()
