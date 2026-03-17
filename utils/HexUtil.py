class HexUtil:
    """Hex 转换工具类，提供 hex 字符串与数组之间的转换功能"""

    @staticmethod
    def bytes_to_hex(data: bytes | bytearray) -> str:
        """将字节数组转换为 hex 字符串

        Args:
            data: 字节数组

        Returns:
            hex 字符串（小写）
        """
        return data.hex()

    @staticmethod
    def hex_to_bytes(hex_str: str) -> bytes:
        """将 hex 字符串转换为字节数组

        Args:
            hex_str: hex 字符串（可包含空格，自动清理）

        Returns:
            字节数组
        """
        hex_str = hex_str.replace(' ', '').replace(':', '')
        return bytes.fromhex(hex_str)

    @staticmethod
    def string_to_hex(s: str, encoding: str = 'utf-8') -> str:
        """将字符串转换为 hex 字符串

        Args:
            s: 输入字符串
            encoding: 字符编码，默认 utf-8

        Returns:
            hex 字符串
        """
        return s.encode(encoding).hex()

    @staticmethod
    def hex_to_string(hex_str: str, encoding: str = 'utf-8') -> str:
        """将 hex 字符串转换为普通字符串

        Args:
            hex_str: hex 字符串
            encoding: 字符编码，默认 utf-8

        Returns:
            原始字符串
        """
        hex_str = hex_str.replace(' ', '').replace(':', '')
        return bytes.fromhex(hex_str).decode(encoding)
