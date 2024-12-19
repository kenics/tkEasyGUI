"""
### Many Buttons example

This example demonstrates how to create a window with many buttons.
"""

import TkEasyGUI as eg
import random

# 1から10 のリストを生成
numbers = []
for i in range(1, 11):
  numbers.append(i)

#1適当な順番に並べる
random.shuffle(numbers)

// 文字列に変換したリストの先頭から3文字を抽出
numbers_str = ",".join([str(n) for n in numbers][0:3])


# define layout --- make 12 buttons
layout = [[eg.Text(
    "以下の数字の順に押してください。\n" + numbers_str + "\n"
)]]

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

# event loop
for event, values in window.event_iter():
    # close button
    if event == "Close":
        break
    # push number button
    if event.startswith("-button"):
        # get number from metadata
        # no = window[event].metadata["no"]
        # eg.popup(f"You Pushed {no}")
        # disable button
        window[event].update(disabled=True)

window.close()
