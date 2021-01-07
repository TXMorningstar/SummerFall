label Chapter1:
    label .onTheTrain:
        scene bg train with fade
        "一个突然的颠簸，让我从睡梦当中惊醒。"
        "回头一看，后座的男子带着歉意笑了笑，扶正了刚刚滑落的行李。窗外已经有学生陆续离开车厢，走向不远处的学校大门。"
        "已经到站了。"
        "看起来这一觉睡得很平稳。我起身背好书包，离开车厢，加入了他们的行列。"

    label .inClassroom_1:
        show classroom with moveinright
        hide bg train
        "在进入教室的时候，大部分人都已经来齐，教室里嘈杂的聊天声不断，耳边甚至能够听到不少人的叫喊。"
        "当务之急是找到自己的座位。这么就没来学校，都快记不清位置在哪了。"
        play sound "sounds/knock.ogg"
        pause 1.0
        "身后传来了敲门板的声音，教室里突然安静下来。"
        "“回到各自的位置上去。”"
        "转身，是一张面无表情的脸。"
        T3 "[P1]，你的座位在后面。"
        "我匆忙地溜到了后方，但那里只剩下一个靠窗的座位了。空位旁的男生注视着他。"
        P1 "不好意思，借过一下。"
        "男生起身，让开了一条道，我迅速地坐到了位置上，感觉前方老师的视线从自己身上挪开，松了口气。"
        "座位旁是一位之前从未见过的男生，大概是我走后新来的转校生吧。男生一直向我这里望着，像是想要说什么一样。"
        T3 "好了，上课。"
        T3 "都把书翻到114页。"
        R3 "你是……新来的吗？"





# label Chapter1:
#     label .onTheTrain:
#         scene pure_black
#         "单调的铁轨碰撞声，在漫长的隧道中无限蔓延着"
#         "即使是闭着眼睛，也能感受到隧道灯一盏接着一盏向列车的后方远去，就像我的过去，变得越来越远"
#         "而我的前面，则是一片崭新的未来"
#         "列车强烈的晃动了一下，似乎是有预感的，我睁开了眼睛。几乎是同时，列车从隧道中钻出，漫长的黑暗终于迎来了尾声。"
#         scene bg train with fade
#         me "唔"
#         "刺眼的阳光从车窗中透进来，我不得不用手挡住还没适应的眼睛"
#
#         Z1 "前方到站：Z市二十节点学院站，请要下车的旅客在列车右侧做好准备"
#         Z1 "祝节点学院的学子们一路顺风"
#         "我的眼睛渐渐地适应了外面的亮光，我尝试着把手放下，向窗外望去"
#         "首先映入眼帘的，就是远处被大片绿地包围住的学校了"
#         "远远望去，可以看见为开学做准备的学生们正在进进出出，形成了一片人海"
#         "C1给我介绍这所学校的时候，我还半信半疑的……但是这个学校，看起来真的很厉害啊"
#         me "不愧是节点学院啊，这不比我那个破初中好看多了？"
#         stop music
#         play music "audio/ringtone.mp3" loop
#         pause 1.0
#         show obj phone at right with easeinbottom
#         pause 1.0
#         "手机响了起来"
#         stop music
#         C1 "喂，新生报名的时间就快截止了，到站之后，要快点行动起来啊！"
#         C1 "嘻嘻，要是让我等久了，你的日子可就不好过了呢……"
#         hide obj phone with easeoutbottom
#         pause 1.0
#         "说起来，她好像还是这里的学生会副会长来着？"
#         me "唉，又要被长不大的前辈“照顾”了"
#         jump Chapter1.inFrontOfTheGate
#
#     label .inFrontOfTheGate:
#         scene bg gate with dissolve
#         C1 "喂————看这里！"
#         show c1 smile at right with moveinright
#         C1 "你迟到了两分零七秒，已经错过了入学时间。现在，要对你实行延期记过处理！"
#         me "哦，放过我吧，副会长大人，我已经以最快地速度赶来报道了……"
#         C1 "喔~嚯嚯嚯嚯嚯嚯，这是不可能的，接受现实吧"
#         me "不————"
#         show c2 confuse at left with moveinleft
#         C2 "诶，这位小学弟迟到了吗？"
#         C2 "我的表里明明显示的是他来的更早了的说……"
#         C1 "会长，别说出来嘛，我都快把他唬住了"
#
#
#         menu:
#             "也就只有你这么天真的人才会觉得自己能唬住人了":
#                 call .choice1
#             "啊，我没有迟到吗？真是太好了！":
#                 call .choice2
#
#
#         C2 "呵呵……你们的关系可真好啊"
#         C1 "那是，我和小学弟在以前的学校就认识了"
#         C2 "诶，是这样吗？"
#         C2 "但你从来没叫过他的名字，我还以为……"
#         me "你看，连会长都发表意见了，别叫我学弟了啊，很丢人的"
#         C1 "嗯？但是你的确是我的学弟啊"
#         me "……"
#         C2 "……"
#         C2 "咳咳，总而言之，既然你已经准备好了，那我们就赶快去教室报道吧"
#         jump .inClassroom
#
#
#         label .choice1:
#             C1 "我不听我不听，wryyyyyyyyyy"
#             return
#         label .choice2:
#             C1 "学弟你演的太假了，你是想尬死我然后继承我的遗产吗？"
#             "你的遗产可能也就只有几只传家宝玩偶了"
#             C1 "嗯？你刚刚在想什么？"
#             me "什么都没想哦"
#             C1 "放屁，你的眼神已经把你彻底出卖了，看腿！"
#             me "啊————————"
#             return
#
#
# label .inClassroom:
#     scene corridor with fade
#     C2 "这里就是你的教室了"
#     C2 "我的引导工作已经结束了。那么，请容我先告辞了"
#     C1 "再见了，小学弟~"
#     pause 2.0
#     "站在教室外，可以听到教室里老师正在向同学讲事情"
#     "……"
#     menu:
#         "进去吧":
#             pass
#     play sound "sounds/knock.ogg"
#     pause 5.0
#     T2 "请进"
#
#     show classroom with moveinright
#     hide corridor
#     T2 "这位是本学期新转来的同学……"
#     T2 "说\"转\"应该不大准确，但是意思都差不多，你们理解就行了"
#     T2 "好了，你先给大家做个自我介绍吧"
#     me "同学们好"
#     python:
#         playername=renpy.input("我的名字是")
#         playername = playername.strip() or "羊绒差"
#     "[playername]" "今年8岁了"
#     window hide
#     show screen AssignmentStatus
#     pause
#     "[playername]" "以上"
#     return
