import datetime
from time import sleep
import PySimpleGUI as sg

def count_down() -> str:
    """来年までの秒数を文字列で返す関数"""
    new_year = datetime.date.today().year + 1
    dt_new_year = datetime.datetime(year=new_year, month=1, day=1, hour=0)
    dt_now = datetime.datetime.now()

    return f'来年まであと {int((dt_new_year - dt_now).total_seconds())} 秒'


# GUIレイアウト設定
layout = [
    [sg.Text(size=(21, 1), font=('小塚ゴシックPro B',24), key='-countdown-')],
]

# Window作成
window = sg.Window('来年まであと何秒？', layout)

# イベントループ
while True:
    #100ms毎にtimeout_keyを返す
    event, _ = window.read(timeout=100, timeout_key='-timeout-')

    if event == None: # Windowの✕ボタンが押されたときにループを抜ける
        break
    elif event in '-timeout-': #eventに'-timeout'が設定されたら
        window['-countdown-'].update(count_down()) #カウントダウンタイマーを更新
        
# GUIを閉じて終了する
window.close
