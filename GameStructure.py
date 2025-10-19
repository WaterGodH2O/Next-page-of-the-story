from Structure import Player, Scene, Choice, NPC
from typing import Dict, List, Optional


class Game:
    def __init__(self):
        self.player = Player()
        self.scenes: Dict[str, Scene] = {}
        self.scenes: Dict[str, NPC] = {}
        self.current_scene: Optional[str] = None

    def add_scene(self, scene: Scene):
        self.scenes[scene.id] = scene

    def set_start(self, scene_id: str):
        self.current_scene = scene_id

    def run(self):
        print("===  Demo ===")
        print("输入数字进行选择；输入 q 退出游戏。\n")

        # 从场景字典中取出目前所在的场景位置
        while self.player.alive and self.current_scene:
            scene = self.scenes[self.current_scene]
            if scene.on_enter:
                scene.on_enter(self.player)
                if not self.player.alive:
                    break

            print(f"[场景：{scene.id}]  HP:{self.player.hp}  背包:{self.player.inventory}")
            print(scene.text)

            # 过滤满足条件的选项（例如需要某物品）
            visible_choices: List[Choice] = []
            for c in scene.choices:
                if c.require is None or c.require in self.player.inventory:
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
                chosen.on_pick(self.player)
                if not self.player.alive:
                    break

            self.current_scene = chosen.next_scene

        if not self.player.alive:
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
