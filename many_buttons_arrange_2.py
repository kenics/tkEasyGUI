"""
### Many Buttons example arrangement

This example demonstrates how to create a window with many buttons.
Press the buttons in the order of the numbers displayed.
表示された数字の順にボタンを押す
"""

import TkEasyGUI as eg
import random
import pygame

# 1から10 のリストを生成
numbers = []
for i in range(1, 11):
  numbers.append(i)

#1適当な順番に並べる
random.shuffle(numbers)

max_num = 3

# 文字列に変換したリストの先頭から3文字を抽出
numbers_q = numbers[0:max_num]
#表示用にカンマ区切りの文字列にしている
numbers_str = ",".join([str(n) for n in numbers_q])


layout = []

layout.append(
[eg.Text("以下の数字の順に押してください。\n" + numbers_str + "\n")]
)
layout.append(
[eg.Text(size=(10, 1), key='-countdown-')]
)
layout.append(
[eg.Text("\n")]
)
pygame.init()
# 時計オブジェクトの作成
clock = pygame.time.Clock()


# layout.append([eg.Text("\n")])
# define layout --- make 12 buttons
for row in range(1,4):
    layout.append([])
    for col in range(4):
        no = (row - 1)*4+col+1
        btn = eg.Button(str(no), key=f"-button{no}",
                        size=(3, 1), metadata={"no": no})
        layout[row].append(btn)
# add close button
layout.append([eg.HSeparator()])
layout.append([eg.Button("Close")])

# make window
window = eg.Window("Many buttons", layout)

line_num = 0

running = True
start_time = pygame.time.get_ticks()
print(f"start_time:{start_time}")
while running:
    # event loop
    for event, values in window.event_iter():
        # close button
        if event == "Close":
            running = False
            break
        # push number button
        if event.startswith("-button"):
            no = window[event].metadata["no"]
            try:
                index_num = numbers_q.index(no)
            except ValueError:
                index_num = -1
            if index_num == line_num:
                line_num += 1
                window[event].update(disabled=True)
            if max_num == line_num:
                eg.popup("Goal !!")
                break;
        current_time = pygame.time.get_ticks()
        print(f"current_time:{current_time}")
        if current_time - start_time >= 5000:
            print("5秒経過しました")
            start_time = current_time
        clock.tick(60)

window.close()
