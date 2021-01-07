# 窗口消失动画
transform WindowOut(windowOut_time):
    easeout_back windowOut_time alpha 0.0 zoom 0.0

    
# 窗口进入动画
transform WindowIn(windowIn_time):
    alpha 0.0 zoom 0.0
    easein_back windowIn_time alpha 1.0 zoom 1.0
