if __name__ == '__main__':
    # int 整数
    int_num: int = 10
    print('type of int_num:', type(int_num))
    # float 小数
    float_num = 10.0
    # str 字符串
    string: str = "hello"
    string2: str = 'world'
    # bool 布尔
    bool_flag: bool = True

    # list 列表[] 可变
    list_names: list = ['Tom', 'Jerry', 'Mike']
    print(list_names)
    list_names[0] = 'TomAAA'
    print(list_names)

    # tuple 元组() 不可变
    tuple_ids: tuple = (100, 200, 300)
    print(tuple_ids)
    # tuple_ids[0] = 1000 # 运行报错

    # set 集合{}  不可变
    set_schools: set = {'Beijing School', 'Shanghai School', 'Guangzhou School'}
    print(set_schools)
    # set_schools[0] = 'Beijing School AAA' # 运行报错

    # dict 字典
    dict_addresses: dict = {
        'Tom': 'Beijing',
        'Jerry': 'Shanghai',
        'Mike': 'Guangzhou'
    }
    print(dict_addresses)
    dict_addresses['Tom'] = 'BeijingAAA'
    print(dict_addresses)

    # 不可变bytes
    # 使用bytes函数 创建bytes
    bytes_data: bytes = bytes('不可变 This is a immutable bytes', encoding='utf-8')
    print(bytes_data)
    # bytes_data[0] = 'A' # 运行报错

    # 可变bytearray
    # 使用bytearray函数 创建bytearray
    bytearray_data:bytearray = bytearray('可变 This is a mutable bytearray', encoding='utf-8')
    print(bytearray_data)
    bytearray_data[0] = ord('A') # ord()将字符转成ASCII码
    print(bytearray_data)



