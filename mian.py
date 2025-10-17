#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文字冒险游戏（命令行示例）
- Python 3.x
- 玩家通过输入数字进行选择
- 包含简单的状态（生命值、背包）与多个场景切换示例
"""

from typing import Dict, List, Optional

class Player:
    def __init__(self):
        self.hp = 10
        self.inventory: List[str] = []
        self.alive = True

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

class Game:
    def __init__(self):
        self.state = Player()
        self.scenes: Dict[str, Scene] = {}
        self.current_scene: Optional[str] = None

    def add_scene(self, scene: Scene):
        self.scenes[scene.id] = scene

    def set_start(self, scene_id: str):
        self.current_scene = scene_id

    def run(self):
        print("===  Demo ===")
        print("输入数字进行选择；输入 q 退出游戏。\n")

        # 从场景字典中取出目前所在的场景位置
        while self.state.alive and self.current_scene:
            scene = self.scenes[self.current_scene]
            if scene.on_enter:
                scene.on_enter(self.state)
                if not self.state.alive:
                    break

            print(f"[场景：{scene.id}]  HP:{self.state.hp}  背包:{self.state.inventory}")
            print(scene.text)

            # 过滤满足条件的选项（例如需要某物品）
            visible_choices: List[Choice] = []
            for c in scene.choices:
                if c.require is None or c.require in self.state.inventory:
                    visible_choices.append(c)

            if not visible_choices:
                print("\n没有可选项。游戏结束。")
                break

            for i, c in enumerate(visible_choices, start=1):
                req_txt = f"（需要：{c.require}）" if c.require else ""
                print(f"{i}. {c.label} {req_txt}")


            choice_index = self.ask_choice(len(visible_choices))
            if choice_index is None:
                print("再见！")
                return

            chosen = visible_choices[choice_index]
            if chosen.on_pick:
                chosen.on_pick(self.state)
                if not self.state.alive:
                    break

            self.current_scene = chosen.next_scene

        if not self.state.alive:
            print("\n你失去了最后一丝力气……\n=== 游戏结束 ===")
        else:
            print("\n=== 游戏结束 ===")

    @staticmethod
    def ask_choice(n: int) -> Optional[int]:
        while True:
            raw = input("你的选择：").strip().lower()
            if raw == "q":
                return None
            if raw.isdigit():
                k = int(raw)
                if 1 <= k <= n:
                    return k - 1
            print(f"请输入 1~{n} 的数字，或输入 q 退出。")

def build_game() -> Game:
    g = Game()

    # --- 回调函数示例 ---
    def drink_potion(state: Player):
        if "小药剂" in state.inventory:
            state.inventory.remove("小药剂")
            state.hp = min(10, state.hp + 5)
            print("你喝下了小药剂，恢复了 5 点生命。")

    def take_branch(state: Player):
        if "树枝" not in state.inventory:
            state.inventory.append("树枝")
            print("你捡起了一根结实的树枝。")

    def wolf_fight_on_pick(state: Player):
        # 简化战斗——若有树枝则更安全
        if "树枝" in state.inventory:
            print("你挥动树枝击退了野狼，但仍受了点伤。HP -2")
            state.hp -= 2
        else:
            print("你徒手与野狼搏斗，险些丧命。HP -6")
            state.hp -= 6
        if state.hp <= 0:
            state.alive = False

    def cave_enter(state: Player):
        # 进入洞穴时的环境效果
        print("洞内阴冷潮湿，你不由得打了个寒颤。HP -1")
        state.hp -= 1
        if state.hp <= 0:
            state.alive = False

    def loot_chest(state: Player):
        if "旧钥匙" in state.inventory:
            print("你用旧钥匙打开了箱子，获得『月影匕首』！")
            state.inventory.append("月影匕首")
        else:
            print("箱子上了锁，你需要一把钥匙。")

    # --- 场景 ---
    g.add_scene(Scene(
        id_="村口",
        text=(
            "黎明的雾气尚未散去，你站在村口的告示牌前。\n"
            "据说北边的森林最近不太平，而东边的洞穴里似乎藏着什么。\n"
            "你背包里只有一瓶『小药剂』。"
        ),
        choices=[
            Choice("前往北边的『密林』", "密林"),
            Choice("去东边的『石洞』", "石洞入口"),
            Choice("原地整理状态（喝药）", "村口", on_pick=drink_potion),
        ],
        on_enter=lambda s: s.inventory.append("小药剂") if "小药剂" not in s.inventory else None
    ))

    g.add_scene(Scene(
        id_="密林",
        text=(
            "密林深处，传来低低的咆哮声。\n"
            "你看见一只野狼正盯着你，旁边地上有一根掉落的树枝。"
        ),
        choices=[
            Choice("捡起树枝", "密林", on_pick=take_branch),
            Choice("与野狼搏斗", "林间空地", on_pick=wolf_fight_on_pick),
            Choice("悄悄撤回村口", "村口"),
        ]
    ))

    g.add_scene(Scene(
        id_="林间空地",
        text=(
            "你摆脱了野狼的追击，来到一处空地。\n"
            "一位旅商正收拾行囊，看到你后示意可以交易。"
        ),
        choices=[
            Choice("与旅商交谈，购买『旧钥匙』", "林间空地", on_pick=lambda s: s.inventory.append("旧钥匙") if "旧钥匙" not in s.inventory else print("你已经有了旧钥匙。")),
            Choice("返回村口", "村口"),
            Choice("向东前往石洞", "石洞入口"),
        ]
    ))

    g.add_scene(Scene(
        id_="石洞入口",
        text=(
            "石洞口漆黑如墨，墙面湿滑。你能听到滴水声回响。\n"
            "一条更深的通道向里延伸。"
        ),
        choices=[
            Choice("点着火把深入洞穴（需要：树枝）", "洞穴深处", require="树枝"),
            Choice("硬着头皮摸黑前进", "洞穴深处"),
            Choice("回村口休整", "村口"),
        ]
    ))

    g.add_scene(Scene(
        id_="洞穴深处",
        text=(
            "你来到洞穴深处，一只古旧的箱子静静躺在石台上。\n"
            "墙壁上刻着模糊的月纹。"
        ),
        choices=[
            Choice("尝试打开箱子（需要：旧钥匙）", "洞穴深处", require="旧钥匙", on_pick=loot_chest),
            Choice("强行撬开箱子（可能受伤）", "终章-月影", on_pick=lambda s: setattr(s, 'hp', s.hp - 4) or print('你划伤了手臂。HP -4')),
            Choice("转身离开", "村口"),
        ],
        on_enter=cave_enter
    ))

    g.add_scene(Scene(
        id_="终章-月影",
        text=(
            "当你揭开箱盖，一道幽蓝的光芒涌出。\n"
            "『月影匕首』在你手中颤动，仿佛与心跳同频。"
        ),
        choices=[
            Choice("带着战利品返回村口（需要：月影匕首）", "结局-归途", require="月影匕首"),
            Choice("空手而归", "结局-归途"),
        ]
    ))

    g.add_scene(Scene(
        id_="结局-归途",
        text=(
            "你踏上归途。无论手中是否握有战利品，\n"
            "你知道黎明之外，还有更广阔的边境等待探索……"
        ),
        choices=[
            Choice("重新开始", "村口"),
            Choice("退出游戏", "", on_pick=lambda s: setattr(s, 'alive', False)),
        ]
    ))

    g.set_start("村口")
    return g

if __name__ == "__main__":
    game = build_game()
    game.run()