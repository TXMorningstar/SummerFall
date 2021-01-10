python:
    from python.autotrack import *
    track = AStartrack(16,16)


screen Section(displayable=False,pos):
    imagebutton:
        auto "Maps/move_%s.png"
        action SetScreenVariable("pdPos",pos)

screen OldBuilding():
    default pPos = (0,0)
    default pdPos = None


    add "Maps/S1_OldBuilding/map.png"
    vbox:
        text "[pPos]"
        text "[pdPos]"

    add "Maps/player.png" xcenter 0.5 ycenter 0.5

    grid 10 10:
        xcenter 0.5 ycenter 0.5
        spacing 9

        use Section(True,(0,0))
        use Section(True,(0,1))
        use Section(True,(0,2))
        use Section(True,(0,3))
        use Section(True,(0,4))
        use Section(True,(0,5))
        use Section(True,(0,6))
        use Section(True,(0,7))
        use Section(True,(0,8))
        use Section(True,(0,9))

        use Section(True,(1,0))
        use Section(True,(1,1))
        use Section(True,(1,2))
        use Section(True,(1,3))
        use Section(True,(1,4))
        use Section(True,(1,5))
        use Section(True,(1,6))
        use Section(True,(1,7))
        use Section(True,(1,8))
        use Section(True,(1,9))

        use Section(True,(2,0))
        use Section(True,(2,1))
        use Section(True,(2,2))
        use Section(True,(2,3))
        use Section(True,(2,4))
        use Section(True,(2,5))
        use Section(True,(2,6))
        use Section(True,(2,7))
        use Section(True,(2,8))
        use Section(True,(2,9))

        use Section(True,(3,0))
        use Section(True,(3,1))
        use Section(True,(3,2))
        use Section(True,(3,3))
        use Section(True,(3,4))
        use Section(True,(3,5))
        use Section(True,(3,6))
        use Section(True,(3,7))
        use Section(True,(3,8))
        use Section(True,(3,9))

        use Section(True,(4,0))
        use Section(True,(4,1))
        use Section(True,(4,2))
        use Section(True,(4,3))
        use Section(True,(4,4))
        use Section(True,(4,5))
        use Section(True,(4,6))
        use Section(True,(4,7))
        use Section(True,(4,8))
        use Section(True,(4,9))

        use Section(True,(5,0))
        use Section(True,(5,1))
        use Section(True,(5,2))
        use Section(True,(5,3))
        use Section(True,(5,4))
        use Section(True,(5,5))
        use Section(True,(5,6))
        use Section(True,(5,7))
        use Section(True,(5,8))
        use Section(True,(5,9))

        use Section(True,(6,0))
        use Section(True,(6,1))
        use Section(True,(6,2))
        use Section(True,(6,3))
        use Section(True,(6,4))
        use Section(True,(6,5))
        use Section(True,(6,6))
        use Section(True,(6,7))
        use Section(True,(6,8))
        use Section(True,(6,9))

        use Section(True,(7,0))
        use Section(True,(7,1))
        use Section(True,(7,2))
        use Section(True,(7,3))
        use Section(True,(7,4))
        use Section(True,(7,5))
        use Section(True,(7,6))
        use Section(True,(7,7))
        use Section(True,(7,8))
        use Section(True,(7,9))

        use Section(True,(8,0))
        use Section(True,(8,1))
        use Section(True,(8,2))
        use Section(True,(8,3))
        use Section(True,(8,4))
        use Section(True,(8,5))
        use Section(True,(8,6))
        use Section(True,(8,7))
        use Section(True,(8,8))
        use Section(True,(8,9))

        use Section(True,(9,0))
        use Section(True,(9,1))
        use Section(True,(9,2))
        use Section(True,(9,3))
        use Section(True,(9,4))
        use Section(True,(9,5))
        use Section(True,(9,6))
        use Section(True,(9,7))
        use Section(True,(9,8))
        use Section(True,(9,9))
