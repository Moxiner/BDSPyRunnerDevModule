# coding=utf-8
"""
PYRunner辅助开发模块

作者：student_2333
后续协助开发：我什么都布吉岛

根据pyr源代码和wiki编写

如有错误请指正

// 2021.4.4更新：适配pyr1.3

// 2021.4.4b2更新：适配pyr1.3.4

// 2021.4.5更新：修正newThread函数名错误

// 2021.4.20更新：适配pyr1.4.1

// 2021.4.27更新：增加插件开发模板

// 2021.5.12更新：修正一些小错误，添加setTimeout函数，移除newThread函数

// 2021.6.5更新：适配pyr1.4.5

// 2021.6.7更新：适配pyr1.5.0

// 2021.6.14更新：适配pyr1.5.4以及一些小更改

// 2021.8.5更新：适配pyr1.6.1以及一些小更改

// 2021.8.5b2更新：修正了一些小错误

// 2021.8.5b3更新：修正了disconnect的参数错误

// 2021.8.6更新：适配pyr1.6.3

// 2022.1.14更新：适配pyr1.9.0正式版 【我什么都布吉岛补充＆修改】新增一堆API及修改部分API

QQ:3076823485

E-mail:lgc2333@126.com

Telegram:@lgc2333
"""
from typing import Optional, Callable, Any


class Entity(object):
    """
    Entity类，旧版为player和actor指针

    如果获取或设置信息失败会抛异常

    name属性与perm属性有setter，可以直接entity.name="xxx"修改，其他属性不行

    Q:属性是储存在每个对象里吗？那样会不会很耗内存？

    A:不是，对象只存了一个实体指针，取属性时通过指针获取，相比老版本的getPlayerInfo，这种取属性的做法更加高效而且易于使用Entity的成员函数

    tip:mc模块dict在pyr1.5.4版加入该对象，可以用代码实例化该对象，传入一个现有Entity对象即可复制一份
    """

    def __init__(self, entity: Entity):
        ...

    @property
    def getName(self) -> str:
        """实体名字（可修改）"""
        ...

    @getName.setter
    def setName(self):
        ...

    @property
    def getUuid(self) -> str:
        """玩家UUID"""
        ...

    @property
    def getXuid(self) -> str:
        """玩家XUID"""
        ...

    @property
    def getPos(self) -> tuple[float, float, float]:
        """实体坐标"""
        ...

    @property
    def getDimensionId(self) -> int:
        """实体维度ID(0主世界,1地狱,2末地)"""
        ...

    @property
    def isStanding(self) -> bool:
        """实体是否站立在方块上"""
        ...

    @property
    def isSneaking(self) -> bool:
        """实体是否潜行"""

    @property
    def getTypeID(self) -> int:
        """实体类型"""
        ...

    @property
    def getTypeName(self) -> str:
        """实体类型名称"""
        ...

    @property
    def getNBT(self) -> str:
        """实体nbt json数据"""
        ...

    @property
    def getHealth(self) -> int:
        """实体当前生命"""
        ...

    @property
    def getMaxHealth(self) -> int:
        """实体最大生命"""
        ...

    @property
    def getPermissions(self) -> int:
        """玩家权限值（可修改，有0,1,2,3,4）"""
        ...

    @getPermissions.setter
    def setPermissions(self, perm: int):
        """设置玩家权限值（可修改，有0,1,2,3,4）"""
        ...

    @property
    def getPlatformOnlineId(self) -> str:
        """设备id（uuid字符串，可检测玩家是否由win10登录）"""
        ...

    @property
    def getPlatform(self) -> int:
        """设备类型（可检测玩家是否由安卓登录）"""
        ...

    @property
    def getIP(self) -> str:
        """玩家ip地址"""
        ...

    def getAllItem(self) -> Optional[str]:
        """
        获取玩家所有物品

        返回json文本，包含键：Inventory, EndChest, Armor, OffHand, Hand

        :return: 玩家物品信息
        """
        ...

    def setAllItem(self, items: str):
        """
        设置玩家所有物品

        :param items: json文本，格式同GetAllItem，当某键不存在时不设置
        """
        ...

    def setHand(self, item: str):
        """
        设置主手物品

        :param item: 物品信息json文本 例{"Count1": 1,"Damage2":0,"Name8":"minecraft:netherite_sword","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"下界合金剑"},"ench9":[{"id2":9,"lvl2": 5},{"id2":13,"lvl2":2}]}}
        """
        ...

    def addItem(self, item: str):
        """
        给予玩家物品

        :param item: 物品信息json文本 例{"Count1": 1,"Damage2":0,"Name8":"minecraft:netherite_sword","WasPickedUp1":0,"tag10":{"RepairCost3":3,"display10":{"Name8":"下界合金剑"},"ench9":[{"id2":9,"lvl2": 5},{"id2":13,"lvl2":2}]}}
        """
        ...

    def removeItem(self, slot: int, num: int):
        """
        移除玩家物品

        :param slot: 背包格子
        :param num: 移除数量
        """
        ...

    def teleport(self, x: float, y: float, z: float, dimension_id: int):
        """
        传送实体到指定位置

        :param x: X轴坐标
        :param y: Y轴坐标
        :param z: Z轴坐标
        :param dimension_id: 维度id 0为主世界 1为下界 2为末地
        """
        ...

    def sendText(self, message: str, mode: int):
        """
        向玩家发送各种消息

        消息类型: Raw = 0 Chat = 1 JukeboxPopup = 4 SystemMessage = 6 Whisper = 7 Announcement = 8 TextObject = 9

        :param message: 消息内容
        :param mode: 消息类型
        """
        ...

    def runCommandAs(self, command: str):
        """
        模拟玩家发出指令

        :param command: 要执行的指令
        """
        ...

    def resendAllChunks(self):
        """
        刷新玩家区块
        """
        ...

    def disconnect(self, msg: str):
        """
        断开玩家连接(相当于kick)

        :param msg: 提示消息
        """
        ...

    def getScore(self, object_name: str) -> Optional[int]:
        """
        获取玩家计分板分数

        :param object_name: 计分板名称
        :return: 分数
        """
        ...

    def setScore(self, object_name: str, count: int):
        """
        设置玩家计分板分数

        :param object_name: 计分板名称
        :param count: 设置的分数指
        """
        ...

    def addScore(self, object_name: str, count: int):
        """
        添加玩家的计分板分数

        :param object_name: 计分板名称
        :param count: 增加的分数值
        """
        ...

    def reduceScore(self, object_name: str, count: int):
        """
        添加玩家的计分板分数

        :param object_name: 计分板名称
        :param count: 减少的分数值
        """
        ...

    def getLevel(self) -> Optional[int]:
        """获取等级"""
        ...

    def addLevel(self, level: int):
        """
        增加玩家经验值

        :param level: 增加等级
        """
        ...

    def transferServer(self, ip: str, port: int):
        """
        传送玩家到指定服务器

        :param ip: 服务器IP
        :param port: 服务器端口
        """
        ...

    def sendCustomForm(self, form: str, callBack: ()):
        """
        向指定的玩家发送一个自定义表单
        例 player.sendCustomForm('{"content":[{"type":"label","text":"普通文本"},{"placeholder":"输入框","default":"默认值","type":"input","text":""},{"default":true,"type":"toggle","text":"开关"},{"min":0.0,"max":10.0,"step":1.0,"default":0.0,"type":"slider","text":"游标滑块"},{"default":1,"steps":["项目1","项目2","项目3"],"type":"step_slider","text":"矩阵滑块"},{"default":1,"options":["项目1","项目2","项目3"],"type":"dropdown","text":"下拉框"}],"type":"custom_form","title":"自定义窗体标题"}', 函数名)

        :param form: 表单json文本
        :param callBack: 回调函数，接收两个参数分别是 player:Entity ,selected_data: str
        """
        ...

    def sendSimpleForm(self, title: str, content: str, buttons: list[str], imageUrl: list[str], callBack: ()):
        """
        向指定的玩家发送一个简单表单
        例 player.sendSimpleForm('这是title', '这是Content：', ['按钮1','按钮2'],['图片Url路径1',‘图片Url路径2’])

        :param title: 表单标题
        :param content: 表单内容
        :param buttons: 表单按钮内容
        :param imageUrl: 表单图片路径
        :param callBack: 回调函数，接收两个参数分别是 player:Entity ,selected_item:int
        """
        ...

    def sendModalForm(self, title: str, content: str, button1: str, button2: str, callBack: ()):
        """
        向指定的玩家发送一个模式对话框
        例 player.sendModalForm('没有第三个选项', '请选择：', '生存', '死亡')

        :param title: 表单标题
        :param content: 表单内容
        :param button1: 按钮1标题
        :param button2: 按钮2标题
        :param callBack: 回调函数，接收两个参数分别是 player:Entity ,selected_item:int
        """
        ...

    def setSideBar(self, title: str, data: str):
        """
        设置玩家自定义侧边栏

        :param title: 侧边栏标题
        :param data: json格式侧边栏内容 例：{"我的数值是0":0, "我是2哒":2, "我是第几行？":3}
        """
        ...

    def removeSideBar(self):
        """
        移除玩家自定义侧边栏

        :param self: 目标玩家
        """
        ...

    def setBossBar(self, title: str, percent: float):
        """
        设置玩家Boss条

        :param title: Boss条标题
        :param percent: 血量百分比(min:0,max:1)
        """
        ...

    def removeBossBar(self, title: str):
        """
        移除玩家Boss条

        :param title: 要移除的Boss条标题
        """
        ...

    # 已移除
    # def setSize(self, f1: float, f2: float):
    #     """
    #     设置玩家大小
    #
    #     ----
    #
    #     [常年失踪]hào好吃の饼干 19:56:11
    #
    #     setsize两个float代表啥 没看出来@twoone3
    #
    #     twoone3 19:56:49
    #
    #     不知道
    #
    #     twoone3 19:56:50
    #
    #     没用过
    #
    #     :param f1: 未知
    #     :param f2: 未知
    #     """
    #     ...

    def addTag(self, tag: str):
        """
        增加标签

        :param tag: 标签
        """
        ...

    def removeTag(self, tag: str):
        """
        移除标签

        :param tag: 标签
        """
        ...

    def getTags(self) -> list[str]:
        """
        获取玩家所有标签

        :return: 标签列表
        """
        ...

    def kill(self):
        """杀死实体"""


def getBDSVersion() -> int:
    """
    返回一个当前加载平台的版本号

    :return: 版本代号
    """
    ...


def logout(message: str):
    """
    向控制台发送输出消息

    :param message: 消息内容
    """
    ...


def runCommand(command: str):
    """
    从控制台发送命令

    :param command: 命令内容
    """
    ...


def setListener(event: str, function: Callable[[Any], Optional[bool]]):
    """
    设置监听器

    注:当只回传一个数据时，仅传递值而不传递字典

    监听器列表见 https://github.com/twoone-3/BDSpyrunner/wiki/Listener

    附带插件开发模板含所有监听器

    :param event: 监听器名称
    :param function: 回调函数
    """
    ...


def registerCommand(command: str, callBack: (), description: str):
    """
    添加指令说明

    :param command: 设置说明的指令
    :param callBack: 注册的这个命令被执行时，自动调用的回调函数。
    :param description: 指令说明
    """
    ...


def getPlayerByXuid(xuid: str) -> Entity:
    """
    根据xuid寻找玩家

    成功返回玩家Entity对象，失败报错

    :param xuid: 玩家xuid
    :return:玩家Entity对象
    """
    ...


def getPlayerList() -> list[Entity]:
    """
    获取在线玩家列表

    返回玩家Entity对象列表

    :return: 玩家列表
    """
    ...


# 已移除
# def setDamage(damage: int):
#     """
#     注：此函数仅在生物受伤onMobHurt监听下调用才能生效
#
#     设置生物受伤的伤害值
#
#     :param damage: 伤害值
#     """
#     ...


def setServerMotd(motd: str):
    """
    设置服务器motd(显示在服务器名称下方)

    :param motd: motd内容
    """
    ...


def getBlock(x: int, y: int, z: int, dimension_id: int) -> Optional[dict]:
    """
    获取指定位置的方块信息

    成功返回字典{'blockname':str,'blockid':int}

    :param x: x坐标
    :param y: y坐标
    :param z: z坐标
    :param dimension_id: 维度id 1主世界 2下界 3末地
    :return: 方块信息
    """
    ...


def setBlock(block: str, x: int, y: int, z: int, dimension_id: int):
    """
    设置指定位置的方块

    :param block: 方块名称
    :param x: x坐标
    :param y: y坐标
    :param z: z坐标
    :param dimension_id: 维度id 1主世界 2下界 3末地
    """
    ...


def getStructure(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, dimension_id: int, ignore_entities: bool,
                 ignore_blocks: bool) -> Optional[str]:
    """
    获取两个坐标之间的结构

    成功返回json字符串，失败返回None

    :param x1: 坐标点1 X轴坐标
    :param y1: 坐标点1 Y轴坐标
    :param z1: 坐标点1 Z轴坐标
    :param x2: 坐标点2 X轴坐标
    :param y2: 坐标点2 Y轴坐标
    :param z2: 坐标点2 Z轴坐标
    :param dimension_id: 维度id 0为主世界 1为下界 2为末地
    :param ignore_blocks: 是否忽略方块
    :param ignore_entities: 是否忽略实体
    :return: 结构json字符串
    """
    ...


def setStructure(struct: str, x: int, y: int, z: int, dimension_id: int, mirror: int, rotation: int):
    """
    从JSON字符串NBT结构数据导出结构到指定地点

    :param struct: 设置结构的数据
    :param x: 坐标点1 X轴坐标
    :param y: 坐标点1 Y轴坐标
    :param z: 坐标点1 Z轴坐标
    :param dimension_id: 维度id 0为主世界 1为下界 2为末地
    :param mirror: 是否镜像放置 0：否  1：是
    :param rotation: 旋转角度
    """


def getStructureBinary(x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, dimension_id: int, ignore_entities: bool,
                       ignore_blocks: bool) -> Optional[str]:
    """
    从指定地点获取二进制NBT结构数据

    成功返回json字符串，失败返回None
    :param ignore_blocks:
    :param ignore_entities:
    :param x1: 坐标点1 X轴坐标
    :param y1: 坐标点1 Y轴坐标
    :param z1: 坐标点1 Z轴坐标
    :param x2: 坐标点2 X轴坐标
    :param y2: 坐标点2 Y轴坐标
    :param z2: 坐标点2 Z轴坐标
    :param dimension_id: 维度id 0为主世界 1为下界 2为末地
    :param ignore_blocks: 是否忽略方块
    :param ignore_entities: 是否忽略实体
    :return: 结构json字符串
    """


def setStructureBinary(struct: str, struct_size: int, x: int, y: int, z: int, dimension_id: int, mirror: int,
                       rotation: int):
    """
    从二进制NBT结构数据导出结构到指定地点

    :param struct: 设置结构的数据
    :param struct_size: 结构大小
    :param x: 坐标点1 X轴坐标
    :param y: 坐标点1 Y轴坐标
    :param z: 坐标点1 Z轴坐标
    :param dimension_id: 维度id 0为主世界 1为下界 2为末地
    :param mirror: 是否镜像放置 0：否  1：是
    :param rotation: 旋转角度
    :return: 结构json字符串
    """


def explode(x: float, y: float, z: float, did: int, power: float, destroy: bool, range: float, fire: bool):
    """

    :param x: X坐标
    :param y: Y坐标
    :param z: Z坐标
    :param did: 维度id 0为主世界 1为下界 2为末地
    :param power: 力量
    :param destroy: 是否摧毁方块
    :param range: 爆炸范围
    :param fire: 是否着火
    """


def spawnItem(itemData: str, x: float, y: float, z: float, did: int):
    """
    根据物品NBT结构和坐标生成物品

    :param itemData: NBT结构的物品
    :param x: X坐标
    :param y: Y坐标
    :param z: Z坐标
    :param did: 维度id 0为主世界 1为下界 2为末地
    """


def isSlimeChunk(x: int, z: int) -> Optional[bool]:
    """
    是否为史莱姆区块

    :param x: X坐标
    :param z: Z坐标
    :return: True 和 False
    """


def setSignBlockMessage(content: str, x: int, y: int, z: int, dimension_id: int):
    """
    设置牌子文字

    :param content: 牌子文字内容
    :param x: 坐标X轴
    :param y: 坐标Y轴
    :param z: 坐标Z轴
    :param dimension_id: 维度id 0为主世界 1为下界 2为末地
    :return:
    """
