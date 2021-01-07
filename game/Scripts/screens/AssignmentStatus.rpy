# 属性选择界面
screen AssignmentStatus():

    # 定义所需变量
    default buttonSelected = {"pg1" : None, "pg2": None, "pg3" : None, "pg4" : None} #玩家按下按钮后更改此变量，由于变量是NoneType所以有一些限制
    default buttonHovered = {"pg1" : 0, "pg2" : 0, "pg3" : 0, "pg4" : 0} #玩家将鼠标放在按钮后更改此变量，在玩家按下按钮前获取玩家想要输入的按钮
    default buttonSensitive = {"pg1" : 0, "pg2" : 0, "pg3" : 0, "pg4" : 0} #玩家按下按钮后更改此变量，用于控制按钮的sensitive属性，由于Selected的NoneType限制因此需要此字典
    default statusPoint_total = 5 #属性点总数，更改此变量以改变属性点初始数量
    default statusPoint = statusPoint_total #属性点数值，会根据玩家选择的按钮更改
    default statusPage = 0 #属性页，用于记录属性页面的页码，用于翻页时判断
    default showPgupDiscription = False #用于显示“向上翻页”的提示
    default showPgdwDiscription = False #用于显示“向下翻页”的提示
    default upDown = "down" #用于判断属性页应播放的动画

    modal True

    timer 0.5 action SetScreenVariable("statusPage", statusPage + 1) #进入界面后0.5秒后显示第一页进入的动画


    frame:
        # 界面的样式与动画
        xcenter 0.5 ycenter 0.5
        xysize(1491,839)
        background "UI/AssignmentStatus/framework.png"
        at WindowPopOut(0.15,0.20)



        # 左侧选项栏 ###########################################################
        #######################################################################

        # 使用下面定义的其它界面来显示属性页，传入必要的参数
        showif statusPage == 1:
            use StatusPg1(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive)
        showif statusPage == 2:
            use StatusPg2(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive)
        showif statusPage == 3:
            use StatusPg3(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive)
        showif statusPage == 4:
            use StatusPg4(upDown,buttonSelected)



        # 中部特性解释栏 #######################################################
        #######################################################################
        add "UI/AssignmentStatus/statusInfoFramework.png":
            xcenter 0.65 ycenter 0.5

        # 视窗内的详细信息
        # 使用多个视窗，否则无法控制动画
        showif buttonSelected["pg1"] == 0:
            viewport:
                xcenter 0.65 ycenter 0.5
                area(0.495,0.13,450,550)
                draggable True
                mousewheel True
                add "UI/AssignmentStatus/word.png"
                at Slide(0.15,0.15,10,-100)
        elif buttonSelected["pg1"] == 1:
            viewport:
                xcenter 0.65 ycenter 0.5
                area(0.495,0.13,450,550)
                draggable True
                mousewheel True
                add "UI/AssignmentStatus/word.png"
                at Slide(0.15,0.15,10,-100)
        elif buttonSelected["pg1"] == 2:
            viewport:
                xcenter 0.65 ycenter 0.5
                area(0.495,0.13,450,550)
                draggable True
                mousewheel True
                add "UI/AssignmentStatus/word.png"
                at Slide(0.15,0.15,10,-100)
        elif buttonSelected["pg1"] == 3:
            viewport:
                xcenter 0.65 ycenter 0.5
                area(0.495,0.13,450,550)
                draggable True
                mousewheel True
                add "UI/AssignmentStatus/word.png"
                at Slide(0.15,0.15,10,-100)


        # 右侧属性点显示+翻页按钮 ##############################################
        #######################################################################

        # 设置一片鼠标区域使“向上/下翻页提示消失”
        # 这样的话，即使按钮处于insensitive状态也可以使翻页提示消失
        vbox:
            pos(0.892,0.09)
            mousearea:
                area(0, 0, 112, 127)
                focus_mask "UI/AssignmentStatus/button/pgupBtn_idle.png"
                unhovered SetScreenVariable("showPgupDiscription", False)
            null height 435
            mousearea:
                area(0, 0, 112, 127)
                focus_mask "UI/AssignmentStatus/button/PgdwBtn_idle.png"
                unhovered SetScreenVariable("showPgdwDiscription", False)

        # 向上/下翻页的按钮以及属性点
        vbox:
            pos(0.892,0.09)
            # 向上翻页按钮
            imagebutton:
                auto "UI/AssignmentStatus/button/pgupBtn_%s.png"
                focus_mask True
                insensitive "UI/AssignmentStatus/button/pgupBtn_insensitive.png"
                hovered [SetScreenVariable("showPgupDiscription", True), SetScreenVariable("upDown", "up")]
                action [SetScreenVariable("statusPage", (statusPage-1)), If(statusPage <= 2, SetScreenVariable("showPgupDiscription", False))] #翻页，如果快翻到最后一页了就禁止翻页
                sensitive statusPage > 1 #配合action来防止玩家翻到不允许翻到的页面

            null height 52

            # 属性点显示
            vbox:
                add "UI/AssignmentStatus/Skillpoint.png"
                text "[statusPoint]":
                    font "font/TsangerYuMo.ttf"
                    size 105
                    xanchor 1.0
                    xoffset 115
                xoffset 3 #为了好看所以向右偏移一点点

            null height 38

            # 向下翻页按钮
            imagebutton:
                auto "UI/AssignmentStatus/button/PgdwBtn_%s.png"
                insensitive "UI/AssignmentStatus/button/PgdwBtn_insensitive.png"
                focus_mask True
                hovered [SetScreenVariable("showPgdwDiscription", True), SetScreenVariable("upDown", "down")]
                action [SetScreenVariable("statusPage", (statusPage+1)), If(statusPage >= 3, SetScreenVariable("showPgdwDiscription", False))]
                sensitive statusPage < 4

        # 向上/下翻页的提示信息
        showif showPgupDiscription:
            add "UI/AssignmentStatus/button/pgupDiscription.png" pos(0.898,0.244) at Slide(0.15,0.0,20,20)
        showif showPgdwDiscription:
            add "UI/AssignmentStatus/button/pgdwDiscription.png" pos(0.898,0.74) at Slide(0.15,0.0,-20,-20)

    # 调试时用于显示变量的文本，会显示与窗口最左下角#############################
    # 需要的话就解除注释#######################################################
    # vbox:
    #     xalign 0.0 yalign 1.0
    #     text "page:[statusPage]"
    #     text "upDown:[upDown]"
    #     text "statusPoint_total:[statusPoint_total]"
    #     text "statusPoint[statusPoint]"


# 属性页1 ######################################################################
###############################################################################
screen StatusPg1(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive):
    if upDown == "down":
        fixed:
            at Slide(0.15, 0.15, 50, -50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg1", 3)
                    action [SetDict(buttonSelected, "pg1", 3),
                    SetDict(buttonSensitive, "pg1", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg1", 2)
                    action [SetDict(buttonSelected, "pg1", 2),
                    SetDict(buttonSensitive, "pg1", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg1", 1)
                    action [SetDict(buttonSelected, "pg1", 1),
                    SetDict(buttonSensitive, "pg1", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg1", 0)
                    action [SetDict(buttonSelected, "pg1", 0),
                    SetDict(buttonSensitive, "pg1", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 0
    if upDown == "up":
        fixed:
            at Slide(0.15, 0.15, -50, 50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg1", 3)
                    action [SetDict(buttonSelected, "pg1", 3),
                    SetDict(buttonSensitive, "pg1", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg1", 2)
                    action [SetDict(buttonSelected, "pg1", 2),
                    SetDict(buttonSensitive, "pg1", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg1", 1)
                    action [SetDict(buttonSelected, "pg1", 1),
                    SetDict(buttonSensitive, "pg1", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg2"]-buttonSensitive["pg3"] >= 3
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg1", 0)
                    action [SetDict(buttonSelected, "pg1", 0),
                    SetDict(buttonSensitive, "pg1", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonHovered["pg1"]-buttonSensitive["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg1"] == 0


screen StatusPg2(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive):
    if upDown == "down":
        fixed:
            at Slide(0.15, 0.15, 50, -50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg2", 3)
                    action [SetDict(buttonSelected, "pg2", 3),
                    SetDict(buttonSensitive, "pg2", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg2", 2)
                    action [SetDict(buttonSelected, "pg2", 2),
                    SetDict(buttonSensitive, "pg2", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 2
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg2", 1)
                    action [SetDict(buttonSelected, "pg2", 1),
                    SetDict(buttonSensitive, "pg2", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 1
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg2", 0)
                    action [SetDict(buttonSelected, "pg2", 0),
                    SetDict(buttonSensitive, "pg2", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 0
    if upDown == "up":
        fixed:
            at Slide(0.15, 0.15, -50, 50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg2", 3)
                    action [SetDict(buttonSelected, "pg2", 3),
                    SetDict(buttonSensitive, "pg2", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg2", 2)
                    action [SetDict(buttonSelected, "pg2", 2),
                    SetDict(buttonSensitive, "pg2", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 2
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg2", 1)
                    action [SetDict(buttonSelected, "pg2", 1),
                    SetDict(buttonSensitive, "pg2", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg3"] >= 1
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg2", 0)
                    action [SetDict(buttonSelected, "pg2", 0),
                    SetDict(buttonSensitive, "pg2", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonHovered["pg2"]-buttonSensitive["pg3"]))]
                    selected buttonSelected["pg2"] == 0



screen StatusPg3(buttonHovered,statusPoint_total,statusPoint,upDown,buttonSelected,buttonSensitive):
    if upDown == "down":
        fixed:
            at Slide(0.15, 0.15, 50, -50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg3", 3)
                    action [SetDict(buttonSelected, "pg3", 3),
                    SetDict(buttonSensitive, "pg3", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg3", 2)
                    action [SetDict(buttonSelected, "pg3", 2),
                    SetDict(buttonSensitive, "pg3", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 2
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg3", 1)
                    action [SetDict(buttonSelected, "pg3", 1),
                    SetDict(buttonSensitive, "pg3", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 1
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg3", 0)
                    action [SetDict(buttonSelected, "pg3", 0),
                    SetDict(buttonSensitive, "pg3", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 0
    if upDown == "up":
        fixed:
            at Slide(0.15, 0.15, -50, 50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)

            # 左侧按钮显示
            vbox:
                xpos 0.05 ypos 0.05
                spacing 80
                add "UI/AssignmentStatus/heading.png"
                add "UI/AssignmentStatus/3cost.png"
                add "UI/AssignmentStatus/2cost.png"
                add "UI/AssignmentStatus/1cost.png"
                add "UI/AssignmentStatus/0cost.png"
            vbox:
                xpos 0.125 ypos 0.245
                spacing 86
                textbutton "在图书馆到处翻书狂啃":
                    hovered SetDict(buttonHovered, "pg3", 3)
                    action [SetDict(buttonSelected, "pg3", 3),
                    SetDict(buttonSensitive, "pg3", 3),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 3
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 3
                textbutton "打球，看电影，逛街":
                    hovered SetDict(buttonHovered, "pg3", 2)
                    action [SetDict(buttonSelected, "pg3", 2),
                    SetDict(buttonSensitive, "pg3", 2),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 2
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 2
                textbutton "窝在家里打电动":
                    hovered SetDict(buttonHovered, "pg3", 1)
                    action [SetDict(buttonSelected, "pg3", 1),
                    SetDict(buttonSensitive, "pg3", 1),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 1
                    sensitive statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"] >= 1
                textbutton "看抖音快手网络小说":
                    hovered SetDict(buttonHovered, "pg3", 0)
                    action [SetDict(buttonSelected, "pg3", 0),
                    SetDict(buttonSensitive, "pg3", 0),
                    SetScreenVariable("statusPoint", (statusPoint_total-buttonSensitive["pg1"]-buttonSensitive["pg2"]-buttonHovered["pg3"]))]
                    selected buttonSelected["pg3"] == 0

screen StatusPg4(upDown,buttonSelected):
        fixed:
            at Slide(0.15,0.15,50,50)
            xcenter 0.5 ycenter 0.5
            xysize(1491,839)
            vbox:
                xpos 0.05 ypos 0.05
                add "UI/AssignmentStatus/heading4.png"

                null height 100

                imagebutton:
                    auto "UI/AssignmentStatus/button/confirmBtn_%s.png"
                    xoffset 150
                    insensitive "UI/AssignmentStatus/button/confirmBtn_insensitive.png"
                    sensitive buttonSelected["pg1"] != None and buttonSelected["pg2"] != None
                    action Hide("AssignmentStatus")

                null height 220

                add "UI/AssignmentStatus/line.png" xoffset 30

                null height 10

                add "UI/AssignmentStatus/detaledInfo/endPrompt.png" xoffset 30
