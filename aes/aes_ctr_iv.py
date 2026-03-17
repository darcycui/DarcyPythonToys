from Crypto.Cipher import AES

from utils.HexUtil import HexUtil


#
# 使用 pycryptodome 加密库 实现 AES-CTR 模式加密
# |<-------- 128 位块 ------->|
# |---- 96 位 ----|-- 32 位 --|
# |     Nonce     | Counter  |
# | (你的 iv)     | 从 1 开始 |
# 与 Java 默认实现不一致

def main():
    key = b'1234567812345678'  # 密钥，b
    iv = b'123456781234'  # iv 96位
    text = b'abcdefghijklmnhi'  # 需要加密的内容-+

    print("原文：", text)
    # 创建一个aes对象
    # CTR 模式，96 位 nonce + 32 位计数器，计数器从 1 开始（大端）
    aes = AES.new(key, AES.MODE_CTR, nonce=iv, initial_value=1)
    # AES.MODE_CTR 表示模式
    en_text = aes.encrypt(text)
    print("密文：", HexUtil.bytes_to_hex(en_text))
    # 密文： da49075cf5001ba77ddd5043195437b5
    # 加密明文
    aes = AES.new(key, AES.MODE_CTR, nonce=iv, initial_value=1)
    # CTR模式下解密需要重新创建一个aes对象
    den_text = aes.decrypt(en_text)
    print("明文：", den_text)


if __name__ == '__main__':
    main()
