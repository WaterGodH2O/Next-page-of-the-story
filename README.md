# Next-page-of-the-story

# 🎮 Multi-Agent Interactive Storytelling Framework  
多智能体交互式故事生成框架  

---

## 📘 Overview | 项目概述

**English**  
This project explores an **AI-driven interactive narrative game framework** that combines **scripted storytelling** with **natural language dialogue**.  
Players can freely converse with AI characters, who dynamically respond and drive the story forward.  
The system integrates **multiple cooperating AI agents**, each responsible for dialogue relevance evaluation, response generation, and narrative control.

**中文简介**  
本项目旨在构建一个结合了**脚本化剧情**与**自然语言交互**的AI驱动互动叙事游戏框架。  
玩家无需选择固定选项，而是可以与虚拟角色自由对话以推动剧情发展。  
系统由**多个协作AI智能体**组成，分别负责对话相关性评估、回复生成以及故事进程控制。

---

## 🧠 System Architecture | 系统架构

| Agent | Description | 中文说明 |
|-------|--------------|----------|
| 🧩 **Relevance Evaluation Model** | Evaluates dialogue relevance and filters off-topic responses. | 评估玩家输入与当前剧情的相关性，防止跑题。 |
| 💬 **Response Generation Model** | Generates dynamic and context-aware replies based on the narrative state. | 生成符合剧情上下文的自然语言回复。 |
| 🎯 **Game Progress Control Model** | Manages story flow, triggers events, and handles scene transitions. | 控制故事进展与场景切换，管理剧情节奏。 |

> All models are based on **pretrained language models** and refined through **instruction-following fine-tuning** and **retrieval-augmented generation (RAG)**.

---

## 🧩 Features | 功能特点

- 🧠 Multi-agent coordination for narrative coherence  
  多智能体协作确保剧情连贯  
- 💬 Natural dialogue interaction with AI characters  
  与AI角色进行自然语言交流  
- 🏗️ Modular and extensible architecture  
  模块化、可扩展的系统结构  
- 📜 Scenario file system for custom stories  
  支持用户自定义剧情文件  
- 🖥️ Command-line or lightweight GUI interface  
  命令行或简易图形界面展示原型  

---

## 📅 Development Plan | 开发计划

| Phase | Description | 状态 |
|-------|--------------|------|
| MVP Stage | Build 3-agent core system + CLI prototype | ✅ In progress |
| Expansion Stage | Add GUI, user-defined stories, and RAG support | 🔜 Planned |
| Evaluation | Performance + Narrative Coherence testing | 🔜 Upcoming |

---

## 🚀 How to Run | 运行方式

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/<your-username>/interactive-storytelling.git
cd interactive-storytelling
