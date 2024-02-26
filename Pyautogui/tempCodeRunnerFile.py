
while(distance >= 0):
    pyt.dragRel(distance, 0, 2,button="left")
    distance -= 20
    pyt.dragRel(0, distance, duration=1.5,button="left")
    pyt.dragRel(-distance, 0, duration=1.5,button="left")
    distance -= 20
    pyt.dragRel(0, -distance, duration=1.5,but