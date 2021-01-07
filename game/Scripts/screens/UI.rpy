# 笔记本按钮
screen Notebook(destinationLabel):
    vbox xalign 0.95 yalign 0.0:
        imagebutton:
            auto "UI/Notebook/notebook_%s.png"
            action [SetVariable("destinationLabel", destinationLabel), Show("MissionStartWindow")]
