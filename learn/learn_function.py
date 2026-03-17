def add(a, b):
    print("__name__=", __name__)
    result = a + b
    print("result=", result)
    return result


if __name__ == "__main__":
    print("learn_function.py 调用函数 add")
    sum_a_b = add(1, 2)
    print("sum=", sum_a_b)
