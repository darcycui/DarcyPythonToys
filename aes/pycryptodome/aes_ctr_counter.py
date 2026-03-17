from Crypto.Cipher import AES
from Cryptodome.Util import Counter

from utils.HexUtil import HexUtil

#
# 使用 pycryptodome 加密库 实现 AES-CTR 模式加密
# |<--------- 128 位 --------->|
# |--- 整个 128 位作为计数器 ---|
# |  1234567812345678 (初始值) |
# 与 Java 默认实现一致

def main():
    key = b'1234567812345678'  # 密钥，b
    iv = b'1234567812345678'  # iv 96位
    text = b'abcdefghijklmnhi'  # 需要加密的内容-+

    print("原文：", text)
    # 创建一个aes对象
    # CTR 模式，128 位计数器，初始值为 iv 的值
    counter_iv_int = int.from_bytes(iv, 'big')
    counter = Counter.new(128, initial_value=counter_iv_int)
    aes = AES.new(key, AES.MODE_CTR, counter=counter)
    # AES.MODE_CTR 表示模式
    en_text = aes.encrypt(text)
    print("密文：", HexUtil.bytes_to_hex(en_text))
    # 密文： 0cce7f3282219d8853a5e704fc8a4089
    # 加密明文
    aes = AES.new(key, AES.MODE_CTR, counter=counter)
    # CTR模式下解密需要重新创建一个aes对象
    den_text = aes.decrypt(en_text)
    print("明文：", den_text)


if __name__ == '__main__':
    main()
