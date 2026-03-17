from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from utils.HexUtil import HexUtil


#
# 使用 cryptography 实现 AES-CTR 模式加密
# |<-------- 128 位块 ------->|
# |---- 96 位 ----|-- 32 位 --|
# |     Nonce     | Counter  |
# | (你的 iv)     | 从 1 开始 |
# 与 Java 默认实现不一致

def main():
    key = b'1234567812345678'  # 密钥，b
    iv = b'123456781234'  # iv 96 位
    text = b'abcdefghijklmnhi'  # 需要加密的内容 -+

    print("原文：", text)

    # CTR 模式，96 位 nonce + 32 位计数器，计数器从 1 开始（大端）
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(iv + b'\x00\x00\x00\x01'),  # nonce + 初始计数器值
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    en_text = encryptor.update(text) + encryptor.finalize()
    print("密文：", HexUtil.bytes_to_hex(en_text))
    # 密文：da49075cf5001ba77ddd5043195437b5

    # 解密需要重新创建 encryptor
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(iv + b'\x00\x00\x00\x01'),
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    den_text = decryptor.update(en_text) + decryptor.finalize()
    print("明文：", den_text)


if __name__ == '__main__':
    main()
