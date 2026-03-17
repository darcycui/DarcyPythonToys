from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from utils.HexUtil import HexUtil


#
# 使用 cryptography 实现 AES-CTR 模式加密
# |<--------- 128 位 --------->|
# |--- 整个 128 位作为计数器 ---|
# |  1234567812345678 (初始值) |
# 与 Java 默认实现一致

def main():
    key = b'1234567812345678'  # 密钥，b
    iv = b'1234567812345678'  # iv 96 位
    text = b'abcdefghijklmnhi'  # 需要加密的内容 -+

    print("原文：", text)

    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(iv),  # nonce + 初始计数器值
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    en_text = encryptor.update(text) + encryptor.finalize()
    print("密文：", HexUtil.bytes_to_hex(en_text))
    # 密文： 0cce7f3282219d8853a5e704fc8a4089

    # 解密需要重新创建 encryptor
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(iv + b'\x00\x00\x00\x00'),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    den_text = decryptor.update(en_text) + decryptor.finalize()
    print("明文：", den_text)


if __name__ == '__main__':
    main()
