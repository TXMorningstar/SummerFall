label Chapter1:
    label .onTheTrain:
        scene pure_black
        "单调的铁轨碰撞声，在漫长的隧道中无限蔓延着"
        "即使是闭着眼睛，也能感受到隧道灯一盏接着一盏向列车的后方远去，就像我的过去，变得越来越远"
        "而我的前面，则是一片崭新的未来"
        "列车强烈的晃动了一下，似乎是有预感的，我睁开了眼睛。几乎是同时，列车从隧道中钻出，漫长的黑暗终于迎来了尾声。"
        scene bg train with fade
        me "唔"
        "刺眼的阳光从车窗中透进来，我不得不用手挡住还没适应的眼睛"

        Z1 "前方到站：Z市二十节点学院站，请要下车的旅客在列车右侧做好准备"
        Z1 "祝节点学院的学子们一路顺风"
        "我的眼睛渐渐地适应了外面的亮光，我尝试着把手放下，向窗外望去"
        "首先映入眼帘的，就是远处被大片绿地包围住的学校了"
        "远远望去，可以看见为开学做准备的学生们正在进进出出，形成了一片人海"
        "C1给我介绍这所学校的时候，我还半信半疑的……但是这个学校，看起来真的很厉害啊"
        me "不愧是节点学院啊，这不比我那个破初中好看多了？"
        stop music
        play music "audio/ringtone.mp3" loop
        pause 1.0
        show obj phone at right with easeinbottom
        pause 1.0
        "手机响了起来"
        stop music
        C1 "喂，新生报名的时间就快截止了，到站之后，要快点行动起来啊！"
        C1 "嘻嘻，要是让我等久了，你的日子可就不好过了呢……"
        hide obj phone with easeoutbottom
        pause 1.0
        "说起来，她好像还是这里的学生会副会长来着？"
        me "唉，又要被长不大的前辈“照顾”了"
        jump Chapter1.inFrontOfTheGate

    label .inFrontOfTheGate:
        scene bg gate with dissolve
        C1 "喂————看这里！"
        show c1 smile at right with moveinright
        C1 "你迟到了两分零七秒，已经错过了入学时间。现在，要对你实行延期入学处理！"
        return
