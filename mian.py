#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文字冒险游戏（命令行示例）
- Python 3.x
- 玩家通过输入数字进行选择
- 包含简单的状态（生命值、背包）与多个场景切换示例
"""

from typing import Dict, List, Optional
from Structure import Player, Scene, Choice
import GameCreator
# class Player:
#     def __init__(self):
#         self.hp = 10
#         self.inventory: List[str] = []
#         self.alive = True



if __name__ == "__main__":
    game = GameCreator.build_game()
    game.run()