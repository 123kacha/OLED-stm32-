import re
import time

import pygame
import serial
import CN

bytesize = serial.EIGHTBITS  # 数据位: 5, 6, 7, 8
parity = serial.PARITY_NONE  # 校验位: PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE
stopbits = serial.STOPBITS_ONE  # 停止位: STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
print(CN.baudrate)
ser = serial.Serial('COM5', CN.baudrate, timeout=1, bytesize=bytesize, parity=parity, stopbits=stopbits)
def Send_CN_Text(Text):
    send_hex_data('CD')
    for i in Text:
        send_hex_data('FF')
        # print('FF')
        for j in CN.Chinese_to_hex(i):
            send_hex_data(str(j)[2:])
            # print(str(j)[2:].upper())
        send_hex_data('FE')
        # print('FE')
    time.sleep(0.05)
    send_hex_data('AB')


def parse_irc_file(file_path):
    """
    解析IRC文件并将时间和歌词以元组形式存入列表中。

    参数:
    file_path -- IRC文件的路径

    返回:
    包含时间和歌词的元组列表
    """
    pattern = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2})\](.*)')
    lyrics = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.match(line)
            if match:
                minutes = int(match.group(1))
                seconds = int(match.group(2))
                hundredths = int(match.group(3))
                lyric = match.group(4).strip()
                time_in_seconds = minutes * 60 + seconds + hundredths / 100
                lyrics.append((time_in_seconds, lyric))

    return lyrics

def StartMusic(MusicSource):
    # 初始化pygame
    pygame.init()

    # 初始化mixer
    pygame.mixer.init()

    # 加载音乐文件
    pygame.mixer.music.load(MusicSource)

    # 播放音乐
    pygame.mixer.music.play()

    # # 保持程序运行直到音乐播放完毕
    # while pygame.mixer.music.get_busy():
    #     pygame.time.Clock().tick(10)

def send_hex_data(data):
    if isinstance(data, str):
        data = bytes.fromhex(data)
    elif isinstance(data, list):
        data = bytes(data)
    ser.write(data)
    # time.sleep(0.005)
    # print(f"已发送: {data.hex()}")
# send_hex_data('FF')
# time.sleep(0.1)
# send_hex_data('13')
# time.sleep(0.1)
# send_hex_data('14')
# time.sleep(0.01)
# send_hex_data('15')
# time.sleep(0.01)
# send_hex_data('16')
# time.sleep(0.01)
# send_hex_data('17')
# time.sleep(0.01)
