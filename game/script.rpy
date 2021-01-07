# LOGO播放
label splashscreen:
    play sound maintitle loop
    show logo with fade
    pause 1.7
    hide logo with fade
    pause 0.2
    show warnings with fade
    hide logo
    pause 2.5
    hide warnings with fade
    return



# 点击“开始游戏后开始运行以下脚本”
label start:
    # hide screen Notebook
    # show screen Notebook("start")
    stop sound fadeout 5.0 #停止主界面正在播放的bgm
    python:
        P1 = None
        while P1 == None:
            P1 = renpy.input("请输入你的名字")
            P1 = P1.strip() or None
    jump Chapter1 #跳转至章节一的开头
