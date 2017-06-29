# -*- coding: utf-8 -*-
class bots(dict):
    """"""

    def __init__(self):
        """"""
        dict.__init__(self)


# --------------KBEngine模块的成员属性--------------------------------
# 这是正运行在当前脚本环境的组件。（至今为止）可能值有'cell', 'base', 'client', 'database', 'bot' 和 'editor'。
# 这是一个只读变量,最好不要给他赋值
component = "bot"

#
bots = bots()


# ----------------KBEngine模块的成员函数--------------------------------------
def addBots(reqCreateAndLoginTotalCount, reqCreateAndLoginTickCount=0, reqCreateAndLoginTickTime=0):
    """
    功能说明：
        向服务端添加机器人。
        例子:
        # 这里是使用addBots的一个例子
                import KBEngine

                # 一次性向服务器添加5个机器人（瞬时完成）
                KBEngine.addBots( 5 )

                # 一共向服务器添加1000个机器人，每次添加5个，每次添加所用时间(s)
                KBEngine.addBots( 1000, 5, 10 )
    参数：
    :param reqCreateAndLoginTotalCount:integer，向服务器添加的机器人总数。
    :param reqCreateAndLoginTickCount:integer，每次向服务器添加的机器人数量。
    :param reqCreateAndLoginTickTime:integer，每次添加所用时间(秒)。
    :return:
    """
    pass


def callback(initialOffset, callbackObj):
    """
    功能说明：
        册一个回调，回调函数callbackObj触发，回调函数将在"initialOffset"秒后被执行。
        例子:
        # 这里是使用callback的一个例子
                import KBEngine

                # 增加一个定时器，1秒后执行
                KBEngine.callback( 1, onCallbackfun )

            def onCallbackfun( ):
                print "onCallbackfun called“
    参数：
        :param initialOffset:float，指定回调从注册到回调的时间间隔（秒）。
        :param callbackObj:function，指定的回调函数对象。
    返回:
        :return:integer，该函数返回callback的内部id，这个id可用于cancelCallback移除回调。
    """
    pass


def cancelCallback(id):
    """
    功能说明：
        函数cancelCallback用于移除一个注册但还未触发的回调，移除后的回调不再执行。如果cancelCallback函数使用一个无效的id（例如已经移除），将会产生错误。
        到KBEngine.callback参考回调的一个使用例子。
        参数：
    :param id:integer，它指定要移除的回调id。
    :return:
    """
    pass


def genUUID64():
    """
    功能说明：
        该函数生成一个64位的唯一ID。
        注意：这个函数依赖于Cellapps服务进程启动参数gus，请正确设置启动参数保持唯一性。
        另外如果gus超过65535则该函数只能在当前进程上保持唯一性。
        用途：
            多个服务进程上产生唯一物品ID并且在合服时不会产生冲突。
            多个服务进程上产生一个房间ID，不需要进行唯一性校验。
    :return:返回一个64位的integer。
    """
    pass


def getWatcher(path):
    """
    功能说明：
        从KBEngine调试系统中获取一个监视变量的值。
        例子：在baseapp1的Python命令行输入:
            >>>KBEngine.getWatcher("/root/stats/runningTime")
            12673648533
            >>>KBEngine.getWatcher("/root/scripts/players")
            32133
    参数：
        :param path:string，该变量的绝对路径包括变量名(可以在GUIConsole的watcher页查看)。
    返回：
        :return:该变量的值。
    """
    pass


def getWatcherDir(path):
    """
    功能说明：
        从KBEngine调试系统中获取一个监视目录下的元素列表(目录、变量名)。
        例子：在baseapp1的Python命令行输入:
            >>>KBEngine.getWatcher("/root")
            ('stats', 'objectPools', 'network', 'syspaths', 'ThreadPool', 'cprofiles', 'scripts', 'numProxices', 'componentID', 'componentType', 'uid', 'numClients', 'globalOrder', 'username', 'load', 'gametime', 'entitiesSize', 'groupOrder')
    参数：
        :param path:string，该变量的绝对路径(可以在GUIConsole的watcher页查看)。
    返回：
        :return:监视目录下的元素列表(目录、变量名)。
    """
    pass


def scriptLogType(logType):
    """
    功能说明：
        设置当前Python.print输出的信息类型(参考: KBEngine.LOG_TYPE_*)。
    :param logType:
    :return:
    """
    pass


# 回调函数
def onInit(isReload):
    """
    功能说明：
        当引擎启动后初始化完所有的脚本后这个接口被调用。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    参数：
    :param isReload:bool，是否是被重写加载脚本后触发的。
    :return:
    """
    pass


def onFinish():
    """
    功能说明：
        进程关闭会回调此函数。
        注意：该回调接口必须实现在入口模块(kbengine_defs.xml->entryScriptFile)中。
    :return:
    """
    pass


class MAILBOX(object):
    """"""

    def __init__(self):
        """"""
        object.__init__(self)


class CELLDATADICT(dict):
    """"""

    def __init__(self):
        """"""
        dict.__init__(self)


class Entities(dict):
    """"""

    def __init__(self):
        """"""
        dict.__init__(self)


class PyClientApp(object):
    """
    类Entity的实例代表着在client上的游戏对象。
    一个Entity可以通过MAILBOX访问在base和cell应用程序上的等价的实体。这需要一组远程调用的函数（在实体的.def文件里指定）。
    """

    def __init__(self):
        """"""
        object.__init__(self)
        self.__entities = Entities()

    # -------------KBEngine.Entity类的成员属性-------------------------------------------
    @property
    def id(self):
        """"""
        return 0

    @property
    def entities(self):
        """
        entities是一个字典对象，包含当前进程上所有的实体。
        """
        return self.__entities

    def getSpaceData(self, key):
        """
        功能说明：
            获取指定key的space数据。
            space数据由用户在服务端通过setSpaceData设置。
        参数：
            :param key:string，一个字符串关键字。
        返回：
            :return:string，指定key的字符串数据。
        """
        pass

    def onDestroy(self):
        """
        实体被销毁时调用。
        :return:
        """
        pass

    def onEnterWorld(self):
        """
        如果实体非客户端控制实体，则表明实体进入了服务端上客户端控制的实体的AOI范围，此时客户端可以看见这个实体了。
        如果实体是客户端控制的实体则表明该实体已经在服务端创建了cell并进入了space。
        :return:
        """
        pass

    def onLeaveWorld(self):
        """
        如果实体非客户端控制实体，则表明实体离开了服务端上客户端控制的实体的AOI范围，此时客户端看不见这个实体了。
        如果实体是客户端控制的实体则表明该实体已经在服务端销毁了cell并离开了space。
        :return:
        """
        pass

    def onEnterSpace(self):
        """
        客户端控制的实体进入了一个新的space。
        :return:
        """
        pass

    def onLeaveSpace(self):
        """
        客户端控制的实体离开了当前的space。
        :return:
        """
        pass


class Entity:
    """
    类Entity的实例代表着在client上的游戏对象。
    一个Entity可以通过MAILBOX访问在base和cell应用程序上的等价的实体。这需要一组远程调用的函数（在实体的.def文件里指定）。
    """

    def __init__(self):
        """"""
        self.__base = MAILBOX()
        self.__cell = MAILBOX()
        self.__cellData = CELLDATADICT()
        self.__clientapp = PyClientApp()

    # -------------KBEngine.Entity类的成员属性-------------------------------------------
    @property
    def base(self):
        """
        base是用于联系Base实体的mailbox。这个属性是只读的，且如果这个实体没有关联的Base实体时属性是None。
        其他参考：
            Entity.clientEntity
            Entity.allClients
            Entity.otherClients
        类型：
            只读的，MAILBOX
        """
        return self.__base

    @property
    def cell(self):
        """
        cell是用于联系cell实体的MAILBOX。这个属性是只读的，且如果这个base实体没有关联的cell时属性是None。
        类型：
            只读 MAILBOX
        """
        return self.__cell

    @property
    def cellData(self):
        """
        cellData是一个字典属性。每当base实体没有创建它的cell实体时，cell实体的属性会保存在这里。
        如果cell实体被创建，这些用到的值和cellData属性将被删除。
        除了cell实体在实体定义文件里指定的属性外，它还包含position, direction and spaceID。
        """
        return self.__cellData

    @property
    def className(self):
        """"""
        return self.__class__.__name__

    @property
    def clientapp(self):
        """"""
        return self.__clientapp

    @property
    def direction(self):
        """
        这个属性描述的是Entity在世界空间中的朝向，用户可以改变这个属性，数据会同步到客户端。
        :return:Tuple, 其中包含(roll, pitch, yaw)，以弧度表示。
        """
        # 这样返回只是要告诉你他返回的是一个元组,具体内容要看具体实现
        return (0, 0, 0)

    @property
    def id(self):
        """
        id是Entity的对象id。这个id是一个整型，在base，cell和client相关联的实体之间是相同的。
        类型： 只读的，int32
        :return: int32
        """
        return 0

    @property
    def position(self):
        """
        这个实体在世界空间中的坐标(x, y, z)，这个属性可以被用户改变，改变后会同步到客户端。
        需要注意的是，不要引用这个属性，引用这个属性很有可能错误的修改了实体的真实坐标。
        例子：
            self.position.y = 10.0
        如果你想拷贝这个属性值可以使用如下方式：
            import Math
            self.copyPosition = Math.Vector3( self.position )
        :return:Vector3
        Vector3:
            描述和管理3D空間的向量。
            其中有x，y，z三个属性代表不同的轴向。
            脚本中使用的例子：
                import Math
                v = Math.Vector3()
        """
        return None

    @property
    def spaceID(self):
        """
        这个属性是实体所在的空间的ID，cell与客户端这个值都保持一致。
        :return: Integer
        """
        return 0

    @property
    def isOnGround(self):
        """
        如果这个属性的值为True，Entity在地面上，否则为False。
        类型： 只读的， bool
        :return: bool
        """
        return False

    def moveToPoint(self, destination, velocity, distance, userData, faceMovement, moveVertically):
        """
        功能说明：
            直线移动Entity到给定的坐标点，成功或失败会调用回调函数。
            任何实体，在任意时刻只能有一个移动控制器，重复调用任何移动函数将终止之前的移动控制器。
            返回一个可以用于取消这次移动的控制器ID。
            例如：
            Entity.cancelController( movementID )。移动取消还可以调用Entity.cancelController( "Movement" )。当移动被取消之后通知方法将不被调用。

            回调函数如下定义：
                def onMove( self, controllerID, userData ):
                def onMoveOver( self, controllerID, userData ):
                def onMoveFailure( self, controllerID, userData ):

        参看：
            Entity.cancelController
        参数：
            :param destination:Vector3，Entity要移动到的目标位置点
            :param velocity:float，Entity的移动速度，单位m/s
            :param distance:float，距离目标小于该值停止移动，如果该值为0则移动到目标位置。
            :param userData:object，传给通知函数的数据
            :param faceMovement:bool，如果实体面向移动方向则为true。如果是其它机制则为false。
            :param moveVertically:bool，设为true指移动为直线移动，设为false指贴着地面移动。
        返回：
            :return:int，新创建的控制器ID。
        """
        pass

    def cancelController(self, controllerID):
        """
        功能说明：
            函数cancelController停止一个控制器对Entity的影响。它只能在一个real实体上被调用。
        参数：
        :param controllerID:是要取消的控制器的索引，它是一个整型。
                            一个专用的控制器类型的字符串也可以作为它的类型。
                            例如，一次只有一个移动/导航控制器可以被激活，
                            这可以用entity.cancelController( "Movement" )取消。
        :return:
        """
        pass

    def onEnterWorld(self):
        """
        如果实体非客户端控制实体，则表明实体进入了服务端上客户端控制的实体的AOI范围，此时客户端可以看见这个实体了。
        如果实体是客户端控制的实体则表明该实体已经在服务端创建了cell并进入了space。
        :return:
        """
        pass

    def onLeaveWorld(self):
        """
        如果实体非客户端控制实体，则表明实体离开了服务端上客户端控制的实体的AOI范围，此时客户端看不见这个实体了。
        如果实体是客户端控制的实体则表明该实体已经在服务端销毁了cell并离开了space。
        :return:
        """
        pass

    def onEnterSpace(self):
        """
        客户端控制的实体进入了一个新的space。
        :return:
        """

    def onLeaveSpace(self):
        """
        客户端控制的实体离开了当前的space。
        :return:
        """
