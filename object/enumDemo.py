# coding=utf-8
from enum import Enum


class VIP(Enum):  # 继承Enum类
    YELLOW = 1  # 枚举类型建议使用大小
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW.value)