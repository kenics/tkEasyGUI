# 時間経過によるイベントのトリガー
# https://runebook.dev/ja/articles/pygame/ref/time

import pygame

W = 1024 / 100
H = 960  / 100

def init_win():
    # 開始画面サイズの計算と画面の作成
    d = pygame.display.get_desktop_sizes()[0]
    scale = min(d[0] * 0.8 // W, d[1] * 0.8 // H)   # 開始倍率
    size = (W * scale, H * scale)   # 開始画面サイズ
    pygame.display.set_mode(size, pygame.RESIZABLE) # 画面作成



pygame.init()

init_win()

# 時計オブジェクトの作成
clock = pygame.time.Clock()

# ゲームループ
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 5秒ごとに何かを行う
    current_time = pygame.time.get_ticks()
    if current_time - start_time >= 5000:
        print("5秒経過しました")
        start_time = current_time

    # ゲームロジックの更新
    # ...

    # 画面の描画
    # ...

    # フレームレートの制御
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
