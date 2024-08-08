import pygame
import re
import MusicAndIrc
import time
import CN

# 波特率
CN.baudrate = 9600
print(CN.baudrate)
# 歌词文件路径
lrc_file = "./Irc/折风渡夜.lrc"
# 歌曲文件路径
music_file = "./Music/折风渡夜.mp3"



Irc = MusicAndIrc.parse_irc_file(lrc_file)
MusicAndIrc.StartMusic(music_file)

start_time = time.perf_counter()
Irc_now = 0
length = len(Irc)
try:
    for i in range(length):
        if Irc[i][1] == "":
            Irc.remove(Irc[i])
except:
    pass
print(Irc)
while True:
    elapsed_time = time.perf_counter() - start_time
    if Irc_now < len(Irc):
        if elapsed_time >= Irc[Irc_now][0]:
            if Irc[Irc_now][1]:
                print(Irc[Irc_now])
                if len(Irc[Irc_now][1]) > 0:  # 确保字符串有内容
                    MusicAndIrc.Send_CN_Text(Irc[Irc_now][1])
            else:
                print("Empty string, skipping Send_CN_Text")
            Irc_now = Irc_now + 1

# MusicAndIrc.Send_CN_Text("明天会更好")
# MusicAndIrc.send_hex_data('FF')
# MusicAndIrc.send_hex_data('12')
# MusicAndIrc.send_hex_data('FE')
# CN.send_bitmap_to_stm32(ttf)
