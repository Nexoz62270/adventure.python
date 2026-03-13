# ⚔️ Adventure.py — Shadow of the Dragon 🐉

A text-based RPG adventure game built in Python. Roll your class, fight through worlds, level up and defeat the Ancient Dragon to save the kingdom!

---

## 🎮 Features

- 🎲 **Random class roll** at the start — 7 unique classes with special abilities
- ⚔️ **Turn-based combat** with HP bars and class abilities
- 🗺️ **6 worlds** with 3 levels each + a boss — plus a village and final castle
- 🛒 **Shop system** — buy potions, upgrade sword and shield
- 📈 **Leveling system** — gain XP and level up after each fight
- 🌍 **FR / EN language selection** at startup (English by default)
- 🎮 **Secret cheat panel** — press `C` anytime (password protected 🔒)

---

## 🚀 How to play

### Requirements
- Python 3.x — download at [python.org](https://www.python.org)

### Run the game
```bash
python adventure.py
```

Or on Mac/Linux:
```bash
python3 adventure.py
```

---

## 🎲 Classes

| Class | HP | ATK | DEF | Special Ability |
|-------|-----|-----|-----|----------------|
| 🏹 Archer | 90 | 17 | 4 | 15% crit chance (x1.5 damage) |
| 🗡️ Assassin | 80 | 19 | 3 | Strikes twice (2nd hit = half damage) |
| 🛡️ Knight | 120 | 14 | 9 | High HP and defense |
| 🔮 Mage | 80 | 21 | 3 | Highest attack in the game |
| 🩺 Healer | 100 | 15 | 6 | Regenerates 5 HP every turn |
| 💀 Necromancer | 90 | 17 | 5 | Drains 15% of damage as HP |
| ⚡ Thunder | 95 | 16 | 5 | 20% chance to stun the enemy |

> 💡 **Most OP class:** 🔮 Mage — highest raw attack, destroys enemies fast if played well.

---

## 🗺️ Worlds

| World | Enemies | Boss | Difficulty |
|-------|---------|------|------------|
| 🌲 Dark Forest | Forest Rat, Wild Boar, Dark Elf | Black Wolf | ⭐ Easy |
| 🏘️ Village | — | — | Rest & Shop |
| 🏚️ Ancient Ruins | Skeleton, Zombie, Dark Mage | Cursed Knight | ⭐⭐ Medium |
| ❄️ Ice World | Ice Bat, Frozen Wolf, Ice Golem | Snow Queen | ⭐⭐ Medium |
| 🌋 Lava World | Fire Imp, Salamander, Lava Titan | Lava Dragon | ⭐⭐⭐ Hard |
| 🍭 Candy World | Gummy Bear, Candy Witch, Choco Knight | Caramel King | ⭐⭐⭐ Hard |
| 🏰 Dragon's Castle | — | Ancient Dragon | ⭐⭐⭐⭐ Final Boss |

Each world has **3 levels** — enemies get stronger each level. Defeat the boss to clear the world!

---

## 🧪 Shop (Village)

| Item | Effect | Price |
|------|--------|-------|
| Healing Potion | +40 HP | 15 💰 |
| Sword Upgrade | +5 Attack | 30 💰 |
| Wooden Shield | +3 Defense | 25 💰 |
| Tavern Rest | +50 HP | 20 💰 |

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `1` `2` `3` | Choose an option |
| `C` | Open secret cheat panel (password protected) |
| `Enter` | Confirm / continue |

---

## 🎮 Cheat Panel

The cheat panel is hidden and **password protected**. Press `C` at any time during the game to access it.

Inside you can: give gold, refill HP, boost stats, add potions, level up, activate god mode, and **change your class** with full stat reset.

> 🔒 50 followers = I'll DM you the password

---

## 📋 How to contribute

1. Fork this repo
2. Create a branch: `git checkout -b my-feature`
3. Commit: `git commit -m "Add my feature"`
4. Push: `git push origin my-feature`
5. Open a Pull Request

---

## 👑 Author

Made by **Nexoz** — [github.com/Nexoz62270](https://github.com/Nexoz62270)

---

*No external libraries required — pure Python 🐍*
