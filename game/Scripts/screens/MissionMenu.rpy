default destinationLabel = None #用于传递任务开始时进入的章节

# 任务开始菜单
screen MissionStartWindow:
    default showButton = False #用于取消按钮的发光显示
    modal True
    frame:
        at WindowIn(0.2)
        background "framework.png"
        xcenter 0.5 ycenter 0.5
        xysize(1491,839)
        add "missionName.png" xcenter 0.5 ycenter 0.1 at WindowIn(0.3)
        add "status.png" xalign 0.1 yalign 0.65 at WindowIn(0.3)
        add "head.png" xalign 0.93 yalign 0.22 at WindowIn(0.3)
        vbox:
            xalign 0.88 yalign 0.45
            add "holder.png" at WindowIn(0.3)
            spacing 55
            add "moreinfo.png" at WindowIn(0.3)

        # 设置退出按钮
        textbutton "Exit":
            xcenter 0.966
            action [SetVariable(destinationLabel, None), ShowTransient("MissionStartWindow_hide", transition = None, exitOnclick = True), Hide("MissionStartWindow")]

        # 设置开始按钮
        imagebutton:
            idle "missionStart_idle.png"
            hover "missionStart_idle.png"
            xcenter 0.716 ycenter 0.852
            focus_mask True
            action Show("ConfirmWindow") #调用确认窗口，决定要跳转的流程位置
            hovered SetScreenVariable("showButton", True) #鼠标移动到按钮上时调用变量使按钮发光
            unhovered SetScreenVariable("showButton", False) #鼠标移动到按钮上时调用变量使按钮停止发光
            at WindowIn(0.3)
        showif showButton == True: #设置按钮发光
            add "missionStart_hover.png" xcenter 0.716 ycenter 0.852 #按钮光芒图片


# 确认菜单
screen ConfirmWindow:

    # 设置样式
    modal True
    zorder 2000
    add "confirmWindowFramework.png" xcenter 0.5 ycenter 0.5 at WindowIn(0.25)
    fixed:
        at WindowIn(0.2)
        xcenter 0.5 ycenter 0.5
        xysize (624,359)
        add "ConfirmWindowTitle.png" xcenter 0.5 ycenter 0.226

        # 设置按钮
        imagebutton: #确认按钮
            at WindowIn(0.3)
            xcenter 0.5 ycenter 0.575
            auto "ConfirmWindowConfirm_%s.png"
            focus_mask True
            action [Hide("ConfirmWindow"), Hide("MissionStartWindow"), ShowTransient("MissionStartWindow_hide")]

        imagebutton: #取消按钮
            at WindowIn(0.3)
            xcenter 0.5 ycenter 0.805
            auto "ConfirmWindowCancel_%s.png"
            focus_mask True
            action [Hide("ConfirmWindow"), ShowTransient("ConfirmWindow_hide")]

# 确认菜单退出动画
# 基本照抄
screen ConfirmWindow_hide:
    modal True
    add "confirmWindowFramework.png" xcenter 0.5 ycenter 0.5 at WindowOut(0.3)
    fixed:
        xcenter 0.5 ycenter 0.5
        xysize (624,359)
        add "ConfirmWindowTitle.png" xcenter 0.5 ycenter 0.226
        imagebutton:
            xcenter 0.5 ycenter 0.575
            auto "ConfirmWindowConfirm_%s.png"
            focus_mask True
            action NullAction() #这里用NullAction防止误触
        imagebutton:
            xcenter 0.5 ycenter 0.805
            auto "ConfirmWindowCancel_%s.png"
            focus_mask True
            action NullAction() #这里用NullAction防止误触

        # 播放退出动画，0.3秒后界面自动隐藏
        at WindowOut(0.3)
    timer 0.4 action Hide("ConfirmWindow_hide")

# 任务开始菜单退出动画
# 基本照抄
screen MissionStartWindow_hide(exitOnclick = False):
        modal True
        frame:
            background "framework.png"
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)
            at WindowOut(0.3)
            add "missionName.png" xcenter 0.5 ycenter 0.1
            add "status.png" xalign 0.1 yalign 0.65
            add "head.png" xalign 0.93 yalign 0.22
            vbox:
                xalign 0.88 yalign 0.45
                add "holder.png"
                spacing 55
                add "moreinfo.png"
            textbutton "Exit" action Hide("MissionStartWindow") xcenter 0.966 #退出按钮##########################################
            imagebutton:
                idle "missionStart_idle.png"
                hover "missionStart_idle.png"
                xcenter 0.716 ycenter 0.852
                focus_mask True
                action Show("ConfirmWindow")
                hovered SetScreenVariable("showButton", True)
                unhovered SetScreenVariable("showButton", False)
            if not exitOnclick:
                use ConfirmWindow_hide

        timer 0.4 action [Hide("MissionStartWindow_hide"), Jump(destinationLabel)]
