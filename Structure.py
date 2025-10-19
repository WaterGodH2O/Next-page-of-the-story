from typing import Dict, List, Optional
class Player:
    def __init__(self, name = "Steve", age = "20"):
        self.name = name
        self.age = age
        self.inventory = []
        self.hp = 10
        self.alive = True

    def backpackContent(self):
        return self.backpack

class NPC:
    def __init__(self, name = "BlankNPC", age = "20"):
        self.name = name
        self.age = age
        self.inventory = []
        self.hp = 10
        self.alive = True

        self.background = "some text maybe?"

    def backpackContent(self):
        return self.backpack

    def chatWith(self, player: Player):
        return


class Choice:
    def __init__(self, label: str, next_scene: str, require: Optional[str] = None, on_pick=None):
        """
        label: 选项描述
        next_scene: 下一个场景ID
        require: 需要背包里有某个物品才显示该选项
        on_pick: 选中该选项时执行的回调函数 (state: Player) -> None
        """
        self.label = label
        self.next_scene = next_scene
        self.require = require
        self.on_pick = on_pick

class Scene:
    def __init__(self, id_: str, text: str, choices: List[Choice], on_enter=None):
        """
        id_: 场景ID
        text: 场景叙述文本
        choices: 可供选择的选项列表
        on_enter: 进入场景时执行的回调函数 (state: Player) -> None
        """
        self.id = id_
        self.text = text
        self.choices = choices
        self.on_enter = on_enter