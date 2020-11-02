# -*- encoding=utf8 -*-
__author__ = "chocolatedisco"

from airtest.core.api import *

auto_setup(__file__)

#联想智选-签到
def lenovoClubApp():
    home
    start_app("com.lenovo.club.app")
    wait(Template(r"tpl1604215748131.png", record_pos=(0.39, 0.81), resolution=(720, 1280)))
    touch(Template(r"tpl1604215878716.png", record_pos=(0.397, 0.807), resolution=(720, 1280)))
    if exists(Template(r"tpl1604216126981.png", record_pos=(-0.15, -0.578), resolution=(720, 1280))) == False :
         touch(Template(r"tpl1604215907148.png", record_pos=(-0.167, -0.576), resolution=(720, 1280)))
    stop_app("com.lenovo.club.app")

#什么值得买-签到
def smzdmApp():
    home
    start_app("com.smzdm.client.android")
    wait(Template(r"tpl1604228684108.png", record_pos=(0.404, 0.81), resolution=(720, 1280)))


    if exists(Template(r"tpl1604228340165.png", record_pos=(0.394, -0.229), resolution=(720, 1280))):
        touch(Template(r"tpl1604228354091.png", record_pos=(0.396, -0.233), resolution=(720, 1280)))
    touch(Template(r"tpl1604228387877.png", record_pos=(0.399, 0.808), resolution=(720, 1280)))
    if exists(Template(r"tpl1604228407497.png", record_pos=(0.317, -0.599), resolution=(720, 1280))):
        touch(Template(r"tpl1604228418356.png", record_pos=(0.318, -0.596), resolution=(720, 1280)))
    stop_app("com.smzdm.client.android")

#完美人生-签到
def wmrsApp():
    home
    start_app("com.cignacmb.hmsapp")
    wait(Template(r"tpl1604229709011.png", record_pos=(0.001, 0.51), resolution=(720, 1280)),30)
    touch(Template(r"tpl1604229721753.png", record_pos=(0.003, 0.51), resolution=(720, 1280)))
    wait(Template(r"tpl1604229759009.png", record_pos=(-0.271, -0.178), resolution=(720, 1280)))
    if exists(Template(r"tpl1604229771421.png", record_pos=(-0.001, 0.151), resolution=(720, 1280))):
        touch(Template(r"tpl1604229781501.png", record_pos=(0.001, 0.151), resolution=(720, 1280)))
    stop_app("com.cignacmb.hmsapp")
    
#京东-京豆
def jdApp():
    home
    start_app("com.jingdong.app.mall")
    wait(Template(r"tpl1604236331332.png", record_pos=(-0.179, 0.024), resolution=(1080, 1920)))
    touch(Template(r"tpl1604236343464.png", record_pos=(-0.186, 0.018), resolution=(1080, 1920)))
    wait(Template(r"tpl1604236363906.png", record_pos=(0.003, -0.521), resolution=(1080, 1920)))
    touch(Template(r"tpl1604236374277.png", record_pos=(0.014, -0.516), resolution=(1080, 1920)))
    sleep(5.0)
    stop_app("com.jingdong.app.mall")
    
def ksApp():
    home
    start_app("com.kuaishou.nebula")
    wait(Template(r"tpl1604335914241.png", record_pos=(-0.406, -0.755), resolution=(1080, 1920)))
    touch(Template(r"tpl1604335914241.png", record_pos=(-0.406, -0.755), resolution=(1080, 1920)))
    wait(Template(r"tpl1604336057201.png", record_pos=(-0.306, 0.019), resolution=(1080, 1920)))
    touch(Template(r"tpl1604336057201.png", record_pos=(-0.306, 0.019), resolution=(1080, 1920)))
    wait(Template(r"tpl1604336208067.png", record_pos=(-0.297, 0.446), resolution=(1080, 1920)))
    swipe(Template(r"tpl1604336219438.png", record_pos=(-0.299, 0.446), resolution=(1080, 1920)), vector=[0.1165, -0.5629])
    wait(Template(r"tpl1604336276451.png", record_pos=(0.351, 0.527), resolution=(1080, 1920)))
    touch(Template(r"tpl1604336276451.png", record_pos=(0.351, 0.527), resolution=(1080, 1920)))
    sleep(5.0)
    stop_app("com.kuaishou.nebula")
    
def pddApp():
    home
    start_app("com.xunmeng.pinduoduo")
    wait(Template(r"tpl1604336858439.png", record_pos=(0.003, -0.09), resolution=(1080, 1920)))
    touch(Template(r"tpl1604336858439.png", record_pos=(0.003, -0.09), resolution=(1080, 1920)))
    sleep(5.0)
    if exists(Template(r"tpl1604336932155.png", record_pos=(-0.005, 0.3), resolution=(1080, 1920))):
        touch(Template(r"tpl1604336932155.png", record_pos=(-0.005, 0.3), resolution=(1080, 1920)))    
    sleep(5.0)
    if exists(Template(r"tpl1604336993194.png", record_pos=(0.001, 0.143), resolution=(1080, 1920))):
        touch(Template(r"tpl1604336993194.png", record_pos=(0.001, 0.143), resolution=(1080, 1920)))
    sleep(5.0)
    stop_app("com.xunmeng.pinduoduo")
    
lenovoClubApp()
sleep(8.0)

smzdmApp()
sleep(8.0)

wmrsApp()
sleep(8.0)

# jdApp()
# sleep(8.0)

ksApp()
sleep(8.0)

pddApp()
sleep(8.0)






