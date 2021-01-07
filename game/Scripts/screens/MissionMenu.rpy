default destinationLabel = None #用于传递任务开始时进入的章节

# 任务开始菜单
screen MissionStartWindow:
    default showButton = False #用于取消按钮的发光显示
    modal True
    frame:
        at WindowPopOut(0.15,0.15)
        background "UI/MissionStartWindow/framework.png"
        xcenter 0.5 ycenter 0.5
        xysize(1491,839)
        add "UI/MissionStartWindow/missionName.png" xcenter 0.5 ycenter 0.1 at WindowPopOut(0.15,0.15)
        add "UI/MissionStartWindow/status.png" xalign 0.1 yalign 0.65 at WindowPopOut(0.15,0.15)
        add "UI/MissionStartWindow/head.png" xalign 0.93 yalign 0.22 at WindowPopOut(0.15,0.15)
        vbox:
            xalign 0.88 yalign 0.45
            add "UI/MissionStartWindow/holder.png" at WindowPopOut(0.15,0.15)
            spacing 55
            add "UI/MissionStartWindow/moreinfo.png" at WindowPopOut(0.15,0.15)

        # 设置退出按钮
        imagebutton:
            auto "UI/MissionStartWindow/MissionStartWindowClose_%s.png"
            xcenter 0.95 ycenter 0.08
            action SetVariable("destinationLabel", None), Hide("MissionStartWindow")

        # 设置开始按钮
        imagebutton:
            idle "UI/MissionStartWindow/missionStart_idle.png"
            hover "UI/MissionStartWindow/missionStart_idle.png"
            xcenter 0.716 ycenter 0.852
            focus_mask True
            action Show("ConfirmWindow") #调用确认窗口，决定要跳转的流程位置
            hovered SetScreenVariable("showButton", True) #鼠标移动到按钮上时调用变量使按钮发光
            unhovered SetScreenVariable("showButton", False) #鼠标移动到按钮上时调用变量使按钮停止发光
            at WindowPopOut(0.15,0.15)
        showif showButton: #设置按钮发光
            add "UI/MissionStartWindow/missionStart_hover.png" xcenter 0.716 ycenter 0.852 #按钮光芒图片


# 确认菜单
screen ConfirmWindow:

    # 设置样式
    modal True
    zorder 2000
    add "UI/MissionStartWindow/confirmWindowFramework.png" xcenter 0.5 ycenter 0.5 at WindowPopOut(0.15,0.15)
    fixed:
        at WindowPopOut(0.15,0.15)
        xcenter 0.5 ycenter 0.5
        xysize (624,359)
        add "UI/MissionStartWindow/ConfirmWindowTitle.png" xcenter 0.5 ycenter 0.226

        # 设置按钮
        imagebutton: #确认按钮
            at WindowPopOut(0.15,0.15)
            xcenter 0.5 ycenter 0.575
            auto "UI/MissionStartWindow/ConfirmWindowConfirm_%s.png"
            focus_mask True
            action [Hide("ConfirmWindow"), Hide("MissionStartWindow"), If(destinationLabel!=None, Jump(destinationLabel))]
        imagebutton: #取消按钮
            at WindowPopOut(0.15,0.15)
            xcenter 0.5 ycenter 0.805
            auto "UI/MissionStartWindow/ConfirmWindowCancel_%s.png"
            focus_mask True
            action Hide("ConfirmWindow")
