import board
import serial
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

baudrate = 9600
def display_image(image):
    # 转换为numpy数组并显示图像
    plt.imshow(image, cmap='gray')
    plt.axis('off')  # 隐藏坐标轴
    plt.show()


def create_chinese_bitmap(text, font_path, font_size):
    # 创建图像对象
    font = ImageFont.truetype(font_path, font_size)
    image = Image.new('1', (font_size, font_size), color=0)
    draw = ImageDraw.Draw(image)

    # 绘制文本
    draw.text((0, 0), text, font=font, fill=1, align='right')

    # 按列提取图像数据
    bitmap = []
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            bitmap.append(pixel)

    return bitmap

def TurnToByte(hex_value):
    binary_string = bin(hex_value)[2:].zfill(8)  # 去掉 '0b' 前缀，并填充到8位
    binary_list = [int(bit) for bit in binary_string]
    return bytes(binary_list)


def bitmap_to_hex(bitmap):
    # print(len(bitmap))
    number_list = []
    number = ""
    length = int(len(bitmap) / 8)
    for j in range(length):
        for i in range(8):
            # print(j * 8 + i)
            number += str(bitmap[j*8+i])
            # print(number)
        number = number[::-1]
        number_list.append(number)
        number = ""
    number_list2 = []
    for i in range(length):
        if i % 2 == 0:
            number_list2.append(number_list[i])
    for i in range(length):
        if i % 2 != 0:
            number_list2.append(number_list[i])
    # 转换为十六进制表示
    return number_list2

def binary_list_to_hex(binary_list):
    hex_list = []
    for binary_str in binary_list:
        # 将二进制字符串转换为整数
        # print(binary_str)
        decimal_value = int(binary_str, 2)
        hex_value = f"0x{decimal_value:02X}"
        hex_list.append(hex_value)
    return hex_list

def chinese_to_hex(text):
    create_chinese_bitmap()

font_path = "C:\Windows\Fonts\simsun.ttc"
text = "你"
bitmap = create_chinese_bitmap(text, font_path, 16)
# 将bitmap转换为字节数据
# send_bitmap_to_stm32(TurnToByte(0xff))
# send_bitmap_to_stm32(bitmap_bytes)
# send_bitmap_to_stm32(TurnToByte(0xfe))

def ShowBitmap(Bitmap):
    for i in range(16):
        # 提取16个字节
        row = Bitmap[i * 16:(i + 1) * 16]

        # 将每个字节转换为十进制整数并打印
        row_dec = [f'{byte:2}' for byte in row]  # 3位宽度，右对齐
        # print(''.join(row_dec))
# for i in range(16):
#     # 提取16个字节
#     row = bitmap_bytes[i * 16:(i + 1) * 16]
#
#     # 将每个字节转换为十进制整数并打印
#     row_dec = [f'{byte:2}' for byte in row]  # 3位宽度，右对齐
#     print(''.join(row_dec))
def Chinese_to_hex(text):
    bitmap = create_chinese_bitmap(text,"C:\Windows\Fonts\simsun.ttc",16)
    return binary_list_to_hex(bitmap_to_hex(bitmap))



