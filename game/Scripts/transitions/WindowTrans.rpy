# 向一个方向滑动且逐渐消失
transform Slide(use_time=0.15, wait_time=0.0, startPos=20, endPos=-20):
    on show:
        alpha 0.0 yoffset startPos
        time wait_time
        linear use_time alpha 1.0 yoffset 0
    on hide:
        linear use_time alpha 0.0 yoffset endPos

# 窗口弹出动画
transform WindowPopOut(in_time=0.15, out_time=0.15):
    on show:
        alpha 0.0 zoom 0.0
        easein_back in_time alpha 1.0 zoom 1.0
    on hide:
        easeout_back out_time alpha 0.0 zoom 0.0
