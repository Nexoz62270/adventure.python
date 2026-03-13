import random
import time
import os
import hashlib

CHEAT_PASSWORD_HASH = "2430568851915ea5c2ba11bbe2c2257d1a52ca008f6e1db9ce40afa92b438e80"

def verifier_mdp(saisie):
    return hashlib.sha256(saisie.encode()).hexdigest() == CHEAT_PASSWORD_HASH

LANG = "en"

TEXTES = {
    "en": {
        "press_enter": "Press Enter to continue...",
        "choose_lang": "Choose your language / Choisissez votre langue",
        "lang_en": "[1] English", "lang_fr": "[2] Français",
        "menu_title": "Shadow of the Dragon", "menu_sub": "A text adventure game",
        "menu_new": "[1] New game", "menu_quit": "[2] Quit",
        "menu_invalid": "  Invalid choice.", "menu_bye": "\n  Goodbye! ⚔️\n",
        "ask_name": "What is your name, adventurer?", "default_name": "Hero",
        "welcome": "  Welcome, {}! Your quest begins...",
        "intro": "  A dragon threatens the kingdom. Only you can stop it.\n",
        "stats_hp": "  HP        : {}/{}", "stats_atk": "  Attack    : {}",
        "stats_def": "  Defense   : {}", "stats_gold": "  Gold      : {} 💰",
        "stats_xp": "  XP        : {}/{}", "stats_inv": "  Inventory : {}",
        "stats_class": "  Class     : {}",
        "stats_empty": "empty", "levelup": "\n🌟 LEVEL {}! Your stats increased!",
        "potion_used": "  🧪 You drink a potion and recover {} HP!",
        "potion_none": "  You have no potions!",
        "map_title": "🗺️  World Map", "map_where": "  Where do you want to go?\n",
        "map_1": "  [1] 🌲 Dark Forest       (3 levels)",
        "map_2": "  [2] 🏘️  Village            (rest & shop)",
        "map_3": "  [3] 🏚️  Ancient Ruins      (3 levels)",
        "map_4": "  [4] ❄️  Ice World          (3 levels)",
        "map_5": "  [5] 🌋 Lava World          (3 levels)",
        "map_6": "  [6] 🍭 Candy World         (3 levels)",
        "map_7": "  [7] 🏰 Dragon's Castle     (final boss)",
        "map_8": "  [8] 📊 View my stats",
        "map_9": "  [9] 🚪 Quit",
        "map_cheat": "  [C] 🎮 Cheat panel",
        "map_invalid": "  Invalid choice.",
        "gameover": "\n  💀 GAME OVER — {} has fallen in battle.",
        "gameover_level": "  You reached level {}.",
        "bye": "  Goodbye, adventurer!",
        "combat_title": "⚔️  COMBAT: {} vs {}",
        "combat_appears": "  {} appears! (HP: {} | ATK: {})\n",
        "combat_action": "\n  What do you do?",
        "combat_1": "  [1] Attack",
        "combat_2": "  [2] Use a potion",
        "combat_3": "  [3] Flee",
        "combat_hit": "  💥 You hit {} for {} damage!",
        "combat_recv": "  😤 {} hits you for {} damage!",
        "combat_backstab": "  😤 {} stabs you in the back: {} damage!",
        "combat_opening": "  😤 {} takes the opening: {} damage!",
        "combat_flee_ok": "  🏃 You successfully flee!",
        "combat_flee_fail": "  ❌ Can't escape!",
        "combat_invalid": "  Invalid action.",
        "combat_win": "\n  🏆 Victory! You defeat {}!",
        "combat_xp_gold": "  +{} XP | +{} 💰",
        "combat_lose": "\n  💀 You were defeated by {}...",
        "combat_crit": "  💥✨ CRITICAL HIT! {} damage!",
        "combat_double": "  ⚡ Double strike! {} + {} damage!",
        "combat_lifesteal": "  🩸 You drain {} HP from {}!",
        "combat_heal_turn": "  💚 You regenerate {} HP!",
        "combat_stun": "  ⚡ {} is stunned and can't attack!",
        "wave_intro": "\n  ⚔️  Wave {}/{} — {} approaches!",
        "wave_clear": "  ✅ Wave cleared!", "level_intro": "\n  📍 Level {}/3",
        "level_clear": "\n  ✅ Level {} complete!",
        "world_clear": "\n  🏆 World cleared! Champion of {}!",
        "loot_potion": "  🧪 You found a Healing Potion!",
        "loot_gold": "  💰 You found {} gold!",
        "loot_atk": "  ⚔️  Attack +{}!",
        "loot_def": "  🛡️  Defense +{}!",
        # Classes
        "roll_class_title": "🎲 CLASS ROLL",
        "roll_class_intro": "The gods decide your destiny...",
        "roll_class_result": "  You rolled: {} {}!",
        "roll_class_desc": "  {}",
        "roll_class_stats": "  HP: {} | ATK: {} | DEF: {}",
        # Zones
        "forest_title": "🌲 Dark Forest", "forest_intro": "A dense, dangerous forest...",
        "forest_e1": "Forest Rat", "forest_e2": "Wild Boar", "forest_e3": "Dark Elf",
        "forest_boss": "Black Wolf",
        "village_title": "🏘️  The Village of Stonehollow",
        "village_intro1": "You arrive in a lively little village.",
        "village_intro2": "A tavern, a blacksmith and a merchant await you.\n",
        "village_action": "\n  What do you do?",
        "village_1": "  [1] Go to the merchant",
        "village_2": "  [2] Rest at the tavern (20 💰)",
        "village_3": "  [3] Talk to villagers",
        "village_4": "  [4] Leave the village",
        "shop_title": "🛒 Merchant", "shop_gold": "\n  Your gold: {} 💰\n",
        "shop_1": "  [1] Healing Potion     — 15 💰",
        "shop_2": "  [2] Sword upgrade      — 30 💰 (+5 attack)",
        "shop_3": "  [3] Wooden shield      — 25 💰 (+3 defense)",
        "shop_4": "  [4] Back",
        "shop_potion_bought": "  Potion purchased!",
        "shop_sword_bought": "  Sword upgraded! +5 attack",
        "shop_shield_bought": "  Shield purchased! +3 defense",
        "shop_no_gold": "  Not enough gold!",
        "tavern_rest": "  🍺 You rest and recover 50 HP.",
        "tavern_no_gold": "  Not enough gold.",
        "rumors": [
            "  « Beware the Castle of the East... the dragon slumbers there. »",
            "  « A legendary sword is hidden in the ruins. »",
            "  « The king offers a reward for the dragon's head! »",
            "  « The Ice World is guarded by a fearsome Snow Queen... »",
            "  « They say the Lava Dragon melts everything in its path! »",
            "  « The Candy World looks sweet but hides deadly enemies! »",
        ],
        "ruins_title": "🏚️  Ancient Ruins", "ruins_intro": "Collapsed stones, dark corridors...",
        "ruins_e1": "Skeleton", "ruins_e2": "Zombie", "ruins_e3": "Dark Mage",
        "ruins_boss": "Cursed Knight",
        "ruins_win": "\n  In a dusty chest you find a LEGENDARY SWORD!",
        "ruins_win2": "  +10 permanent attack!",
        "ice_title": "❄️  Ice World", "ice_intro": "Frozen tundra, deadly blizzards...",
        "ice_e1": "Ice Bat", "ice_e2": "Frozen Wolf", "ice_e3": "Ice Golem",
        "ice_boss": "Snow Queen",
        "ice_win": "\n  The Snow Queen shatters into a thousand crystals!",
        "ice_win2": "  Frostblade found! +8 ATK, +4 DEF!",
        "lava_title": "🌋 Lava World", "lava_intro": "Rivers of lava, scorching heat...",
        "lava_e1": "Fire Imp", "lava_e2": "Salamander", "lava_e3": "Lava Titan",
        "lava_boss": "Lava Dragon",
        "lava_win": "\n  The Lava Dragon collapses into cooling rock!",
        "lava_win2": "  Emberblade found! +12 ATK!",
        "candy_title": "🍭 Candy World", "candy_intro": "Everything looks sweet... but deadly!",
        "candy_e1": "Gummy Bear", "candy_e2": "Candy Witch", "candy_e3": "Chocolate Knight",
        "candy_boss": "Caramel King",
        "candy_win": "\n  The Caramel King melts into a sticky puddle!",
        "candy_win2": "  Sugar Staff found! +6 ATK, +6 DEF!",
        "castle_title": "🏰 The Dragon's Castle",
        "castle_intro1": "Walls blackened by fire, the air smells of sulfur.",
        "castle_intro2": "You climb the spiral staircase to the throne room...\n",
        "castle_intro3": "RAAAAARRGH! THE DRAGON SPOTS YOU!\n",
        "castle_win1": "\n  The dragon collapses with one last roar.",
        "castle_win2": "  A golden light fills the hall...",
        "castle_win3": "\n  🎉 YOU SAVED THE KINGDOM! 🎉",
        "castle_win4": "  The king rewards you with a legendary gift.",
        "castle_win5": "\n  Thanks for playing, {}!\n",
        "enemy_dragon": "Ancient Dragon", "item_potion": "Healing Potion",
        # Cheat panel
        "cheat_locked": "\n  🔒 Restricted access — Password required",
        "cheat_wrong": "  ❌ Wrong password.",
        "cheat_title": "🎮  CHEAT PANEL  —  DEV MODE          ",
        "cheat_stats": "\n  Current stats:",
        "cheat_hp": "  ❤️  HP      : {}/{}",
        "cheat_atk": "  ⚔️  Attack  : {}", "cheat_def": "  🛡️  Defense : {}",
        "cheat_gold": "  💰 Gold    : {}", "cheat_lvl": "  ⭐ Level   : {}",
        "cheat_inv": "  🎒 Inventory: {}", "cheat_empty": "empty",
        "cheat_menu": """
  ─────────────────────────────────────────
  [1] 💰 Give gold          [6] 💀 One-shot mode
  [2] ❤️  Full HP            [7] 🏆 Level up
  [3] ⚔️  Boost attack       [8] 👑 GOD MODE
  [4] 🛡️  Boost defense      [9] 🔄 Reset stats
  [5] 🧪 Add potions        [C] 🎭 Change class
  [0] ❌ Close
  ─────────────────────────────────────────""",
        "cheat_class_title": "🎭 CHANGE CLASS",
        "cheat_class_pick": "  Choose your class (1-7) > ",
        "cheat_class_done": "  ✅ Class changed to {} {}! Stats reset.",
        "cheat_class_invalid": "  ❌ Invalid class number.",
        "cheat_how_much_gold": "  How much gold? > ",
        "cheat_gold_added": "  ✅ +{} gold! You now have {} 💰",
        "cheat_hp_full": "  ✅ HP maxed! ({}/{})",
        "cheat_how_much_atk": "  How many attack points? > ",
        "cheat_atk_done": "  ✅ Attack → {}!",
        "cheat_how_much_def": "  How many defense points? > ",
        "cheat_def_done": "  ✅ Defense → {}!",
        "cheat_how_many_pot": "  How many potions? > ",
        "cheat_pot_done": "  ✅ +{} potion(s) added!",
        "cheat_oneshot": "  ✅ ONE-SHOT MODE! Attack = 9999 💥",
        "cheat_levelup": "  ✅ Now level {}!",
        "cheat_god": "  ✅ GOD MODE! INVINCIBLE 👑",
        "cheat_reset_confirm": "  Reset stats? (y/n) > ",
        "cheat_reset_yes": "y", "cheat_reset_done": "  ✅ Stats reset.",
        "cheat_invalid": "  Invalid choice.", "invalid_number": "  ❌ Invalid number.",
    },
    "fr": {
        "press_enter": "Appuie sur Entrée pour continuer...",
        "choose_lang": "Choose your language / Choisissez votre langue",
        "lang_en": "[1] English", "lang_fr": "[2] Français",
        "menu_title": "L'Ombre du Dragon", "menu_sub": "Un jeu d'aventure textuel",
        "menu_new": "[1] Nouvelle partie", "menu_quit": "[2] Quitter",
        "menu_invalid": "  Choix invalide.", "menu_bye": "\n  Au revoir ! ⚔️\n",
        "ask_name": "Quel est ton nom, aventurier ?", "default_name": "Héros",
        "welcome": "  Bienvenue, {} ! Ta quête commence...",
        "intro": "  Un dragon menace le royaume. Seul toi peux l'arrêter.\n",
        "stats_hp": "  PV        : {}/{}", "stats_atk": "  Attaque   : {}",
        "stats_def": "  Défense   : {}", "stats_gold": "  Or        : {} 💰",
        "stats_xp": "  XP        : {}/{}", "stats_inv": "  Inventaire: {}",
        "stats_class": "  Classe    : {}",
        "stats_empty": "vide", "levelup": "\n🌟 NIVEAU {} ! Tes stats augmentent !",
        "potion_used": "  🧪 Tu bois une potion et récupères {} PV !",
        "potion_none": "  Tu n'as pas de potion !",
        "map_title": "🗺️  Carte du Monde", "map_where": "  Où veux-tu aller ?\n",
        "map_1": "  [1] 🌲 Forêt Sombre       (3 niveaux)",
        "map_2": "  [2] 🏘️  Village             (repos & achats)",
        "map_3": "  [3] 🏚️  Ruines Anciennes    (3 niveaux)",
        "map_4": "  [4] ❄️  Monde de Glace      (3 niveaux)",
        "map_5": "  [5] 🌋 Monde de Lave        (3 niveaux)",
        "map_6": "  [6] 🍭 Monde de Bonbon      (3 niveaux)",
        "map_7": "  [7] 🏰 Château du Dragon    (boss final)",
        "map_8": "  [8] 📊 Voir mes stats",
        "map_9": "  [9] 🚪 Quitter",
        "map_cheat": "  [C] 🎮 Cheat panel",
        "map_invalid": "  Choix invalide.",
        "gameover": "\n  💀 GAME OVER — {} est tombé au combat.",
        "gameover_level": "  Tu as atteint le niveau {}.",
        "bye": "  À bientôt, aventurier !",
        "combat_title": "⚔️  COMBAT : {} vs {}",
        "combat_appears": "  {} apparaît ! (PV: {} | ATQ: {})\n",
        "combat_action": "\n  Que fais-tu ?",
        "combat_1": "  [1] Attaquer",
        "combat_2": "  [2] Utiliser une potion",
        "combat_3": "  [3] Fuir",
        "combat_hit": "  💥 Tu frappes {} pour {} dégâts !",
        "combat_recv": "  😤 {} te frappe pour {} dégâts !",
        "combat_backstab": "  😤 {} te frappe dans le dos : {} dégâts !",
        "combat_opening": "  😤 {} profite de l'ouverture : {} dégâts !",
        "combat_flee_ok": "  🏃 Tu réussis à fuir !",
        "combat_flee_fail": "  ❌ Impossible de fuir !",
        "combat_invalid": "  Action invalide.",
        "combat_win": "\n  🏆 Victoire ! Tu bats {} !",
        "combat_xp_gold": "  +{} XP | +{} 💰",
        "combat_lose": "\n  💀 Tu as été vaincu par {}...",
        "combat_crit": "  💥✨ COUP CRITIQUE ! {} dégâts !",
        "combat_double": "  ⚡ Double frappe ! {} + {} dégâts !",
        "combat_lifesteal": "  🩸 Tu draines {} PV à {} !",
        "combat_heal_turn": "  💚 Tu régénères {} PV !",
        "combat_stun": "  ⚡ {} est étourdi et ne peut pas attaquer !",
        "wave_intro": "\n  ⚔️  Vague {}/{} — {} arrive !",
        "wave_clear": "  ✅ Vague terminée !", "level_intro": "\n  📍 Niveau {}/3",
        "level_clear": "\n  ✅ Niveau {} terminé !",
        "world_clear": "\n  🏆 Monde terminé ! Champion de {} !",
        "loot_potion": "  🧪 Tu trouves une Potion de soin !",
        "loot_gold": "  💰 Tu trouves {} pièces d'or !",
        "loot_atk": "  ⚔️  Attaque +{} !",
        "loot_def": "  🛡️  Défense +{} !",
        "roll_class_title": "🎲 TIRAGE DE CLASSE",
        "roll_class_intro": "Les dieux décident de ton destin...",
        "roll_class_result": "  Tu obtiens : {} {} !",
        "roll_class_desc": "  {}",
        "roll_class_stats": "  PV: {} | ATQ: {} | DEF: {}",
        "forest_title": "🌲 Forêt Sombre", "forest_intro": "Une forêt dense et dangereuse...",
        "forest_e1": "Rat des Bois", "forest_e2": "Sanglier Sauvage", "forest_e3": "Elfe Noir",
        "forest_boss": "Loup Noir",
        "village_title": "🏘️  Le Village de Pierrecreux",
        "village_intro1": "Tu arrives dans un petit village animé.",
        "village_intro2": "Une taverne, un forgeron et un marchand t'attendent.\n",
        "village_action": "\n  Que fais-tu ?",
        "village_1": "  [1] Aller chez le marchand",
        "village_2": "  [2] Te reposer à la taverne (20 💰)",
        "village_3": "  [3] Parler aux villageois",
        "village_4": "  [4] Quitter le village",
        "shop_title": "🛒 Marchand", "shop_gold": "\n  Ton or : {} 💰\n",
        "shop_1": "  [1] Potion de soin      — 15 💰",
        "shop_2": "  [2] Amélioration épée   — 30 💰 (+5 attaque)",
        "shop_3": "  [3] Bouclier de bois    — 25 💰 (+3 défense)",
        "shop_4": "  [4] Retour",
        "shop_potion_bought": "  Potion achetée !",
        "shop_sword_bought": "  Épée améliorée ! +5 attaque",
        "shop_shield_bought": "  Bouclier acheté ! +3 défense",
        "shop_no_gold": "  Pas assez d'or !",
        "tavern_rest": "  🍺 Tu te reposes et récupères 50 PV.",
        "tavern_no_gold": "  Pas assez d'or.",
        "rumors": [
            "  « Méfie-toi du Château de l'Est... le dragon y sommeille. »",
            "  « Une épée légendaire est cachée dans les ruines. »",
            "  « Le roi offre une récompense pour la tête du dragon ! »",
            "  « Le Monde de Glace est gardé par une terrifiante Reine des Neiges... »",
            "  « Le Dragon de Lave fond tout sur son passage ! »",
            "  « Le Monde de Bonbon semble doux mais cache des ennemis mortels ! »",
        ],
        "ruins_title": "🏚️  Ruines Anciennes", "ruins_intro": "Des pierres effondrées, des couloirs sombres...",
        "ruins_e1": "Squelette", "ruins_e2": "Zombie", "ruins_e3": "Mage Noir",
        "ruins_boss": "Chevalier Maudit",
        "ruins_win": "\n  Dans un coffre poussiéreux tu trouves une ÉPÉE LÉGENDAIRE !",
        "ruins_win2": "  +10 attaque permanente !",
        "ice_title": "❄️  Monde de Glace", "ice_intro": "Toundra gelée, blizzards mortels...",
        "ice_e1": "Chauve-Souris Givrée", "ice_e2": "Loup Glacé", "ice_e3": "Golem de Glace",
        "ice_boss": "Reine des Neiges",
        "ice_win": "\n  La Reine des Neiges se brise en mille cristaux !",
        "ice_win2": "  Lame de Givre trouvée ! +8 ATQ, +4 DEF !",
        "lava_title": "🌋 Monde de Lave", "lava_intro": "Des rivières de lave, une chaleur écrasante...",
        "lava_e1": "Diablotin de Feu", "lava_e2": "Salamandre", "lava_e3": "Titan de Lave",
        "lava_boss": "Dragon de Lave",
        "lava_win": "\n  Le Dragon de Lave s'effondre en roche refroidie !",
        "lava_win2": "  Lame de Braise trouvée ! +12 ATQ !",
        "candy_title": "🍭 Monde de Bonbon", "candy_intro": "Tout semble sucré... mais mortel !",
        "candy_e1": "Ours en Gomme", "candy_e2": "Sorcière Sucrée", "candy_e3": "Chevalier Chocolat",
        "candy_boss": "Roi Caramel",
        "candy_win": "\n  Le Roi Caramel fond en une flaque collante !",
        "candy_win2": "  Bâton de Sucre trouvé ! +6 ATQ, +6 DEF !",
        "castle_title": "🏰 Le Château du Dragon",
        "castle_intro1": "Les murs noircis par le feu, l'air sent le soufre.",
        "castle_intro2": "Tu montes les escaliers en spirale jusqu'à la salle du trône...\n",
        "castle_intro3": "RAAAAARRGH ! LE DRAGON T'APERÇOIT !\n",
        "castle_win1": "\n  Le dragon s'effondre dans un dernier rugissement.",
        "castle_win2": "  Une lumière dorée envahit la salle...",
        "castle_win3": "\n  🎉 TU AS SAUVÉ LE ROYAUME ! 🎉",
        "castle_win4": "  Le roi t'offre une récompense légendaire.",
        "castle_win5": "\n  Merci d'avoir joué, {} !\n",
        "enemy_dragon": "Dragon Ancien", "item_potion": "Potion de soin",
        "cheat_locked": "\n  🔒 Accès restreint — Mot de passe requis",
        "cheat_wrong": "  ❌ Mauvais mot de passe.",
        "cheat_title": "🎮  CHEAT PANEL  —  MODE DEV          ",
        "cheat_stats": "\n  Stats actuelles :",
        "cheat_hp": "  ❤️  PV      : {}/{}",
        "cheat_atk": "  ⚔️  Attaque : {}", "cheat_def": "  🛡️  Défense : {}",
        "cheat_gold": "  💰 Or      : {}", "cheat_lvl": "  ⭐ Niveau  : {}",
        "cheat_inv": "  🎒 Inventaire: {}", "cheat_empty": "vide",
        "cheat_menu": """
  ─────────────────────────────────────────
  [1] 💰 Donner de l'or     [6] 💀 One-shot mode
  [2] ❤️  Remplir les PV    [7] 🏆 Monter de niveau
  [3] ⚔️  Booster l'attaque [8] 👑 MODE GOD
  [4] 🛡️  Booster la défense [9] 🔄 Reset stats
  [5] 🧪 Ajouter potions    [C] 🎭 Changer de classe
  [0] ❌ Fermer
  ─────────────────────────────────────────""",
        "cheat_class_title": "🎭 CHANGER DE CLASSE",
        "cheat_class_pick": "  Choisis ta classe (1-7) > ",
        "cheat_class_done": "  ✅ Classe changée en {} {} ! Stats réinitialisées.",
        "cheat_class_invalid": "  ❌ Numéro de classe invalide.",
        "cheat_how_much_gold": "  Combien d'or ? > ",
        "cheat_gold_added": "  ✅ +{} or ! Tu as maintenant {} 💰",
        "cheat_hp_full": "  ✅ PV au max ! ({}/{})",
        "cheat_how_much_atk": "  Combien de points d'attaque ? > ",
        "cheat_atk_done": "  ✅ Attaque → {} !",
        "cheat_how_much_def": "  Combien de points de défense ? > ",
        "cheat_def_done": "  ✅ Défense → {} !",
        "cheat_how_many_pot": "  Combien de potions ? > ",
        "cheat_pot_done": "  ✅ +{} potion(s) dans l'inventaire !",
        "cheat_oneshot": "  ✅ ONE-SHOT MODE ! Attaque = 9999 💥",
        "cheat_levelup": "  ✅ Niveau {} !",
        "cheat_god": "  ✅ MODE GOD ! INVINCIBLE 👑",
        "cheat_reset_confirm": "  Remettre à zéro ? (o/n) > ",
        "cheat_reset_yes": "o", "cheat_reset_done": "  ✅ Stats remises à zéro.",
        "cheat_invalid": "  Choix invalide.", "invalid_number": "  ❌ Nombre invalide.",
    }
}

def t(cle, *args):
    texte = TEXTES[LANG].get(cle, f"[{cle}]")
    return texte.format(*args) if args else texte

# ─────────────────────────────────────────
#  CLASSES DU JEU
# ─────────────────────────────────────────

CLASSES = {
    "en": [
        {
            "nom": "Archer", "emoji": "🏹",
            "desc": "Good attack, low defense. 15% crit chance (x1.5 damage).",
            "pv": 90, "attaque": 17, "defense": 4,
            "capacite": "crit"
        },
        {
            "nom": "Assassin", "emoji": "🗡️",
            "desc": "High attack, low HP. Second strike deals half damage.",
            "pv": 80, "attaque": 19, "defense": 3,
            "capacite": "double"
        },
        {
            "nom": "Knight", "emoji": "🛡️",
            "desc": "High HP and defense. Solid and reliable.",
            "pv": 120, "attaque": 14, "defense": 9,
            "capacite": "none"
        },
        {
            "nom": "Mage", "emoji": "🔮",
            "desc": "High magic attack. Fragile but powerful.",
            "pv": 80, "attaque": 21, "defense": 3,
            "capacite": "none"
        },
        {
            "nom": "Healer", "emoji": "🩺",
            "desc": "Regenerates 5 HP every turn. Well-rounded stats.",
            "pv": 100, "attaque": 15, "defense": 6,
            "capacite": "regen"
        },
        {
            "nom": "Necromancer", "emoji": "💀",
            "desc": "Drains 15% of damage dealt as HP from enemies.",
            "pv": 90, "attaque": 17, "defense": 5,
            "capacite": "lifesteal"
        },
        {
            "nom": "Thunder", "emoji": "⚡",
            "desc": "20% chance to stun the enemy (they skip their turn).",
            "pv": 95, "attaque": 16, "defense": 5,
            "capacite": "stun"
        },
    ],
    "fr": [
        {
            "nom": "Archer", "emoji": "🏹",
            "desc": "Bonne attaque, défense faible. 15% de chance de coup critique (x1.5 dégâts).",
            "pv": 90, "attaque": 17, "defense": 4,
            "capacite": "crit"
        },
        {
            "nom": "Assassin", "emoji": "🗡️",
            "desc": "Attaque élevée, PV faibles. La 2e frappe inflige la moitié des dégâts.",
            "pv": 80, "attaque": 19, "defense": 3,
            "capacite": "double"
        },
        {
            "nom": "Chevalier", "emoji": "🛡️",
            "desc": "PV et défense élevés. Solide et fiable.",
            "pv": 120, "attaque": 14, "defense": 9,
            "capacite": "none"
        },
        {
            "nom": "Mage", "emoji": "🔮",
            "desc": "Attaque magique élevée. Fragile mais puissant.",
            "pv": 80, "attaque": 21, "defense": 3,
            "capacite": "none"
        },
        {
            "nom": "Soigneur", "emoji": "🩺",
            "desc": "Régénère 5 PV chaque tour. Stats équilibrées.",
            "pv": 100, "attaque": 15, "defense": 6,
            "capacite": "regen"
        },
        {
            "nom": "Nécromancien", "emoji": "💀",
            "desc": "Vole 15% des dégâts infligés sous forme de PV.",
            "pv": 90, "attaque": 17, "defense": 5,
            "capacite": "lifesteal"
        },
        {
            "nom": "Foudre", "emoji": "⚡",
            "desc": "20% de chance d'étourdir l'ennemi (il rate son tour).",
            "pv": 95, "attaque": 16, "defense": 5,
            "capacite": "stun"
        },
    ]
}

def roll_classe():
    """Tire une classe aléatoire et l'affiche."""
    clear()
    titre(t("roll_class_title"))
    lent(t("roll_class_intro"))
    time.sleep(0.5)
    # Animation de suspense
    for _ in range(6):
        c = random.choice(CLASSES[LANG])
        print(f"\r  🎲 {c['emoji']} {c['nom']}...     ", end='', flush=True)
        time.sleep(0.25)
    classe = random.choice(CLASSES[LANG])
    print()
    lent(t("roll_class_result", classe["emoji"], classe["nom"]))
    lent(t("roll_class_desc", classe["desc"]))
    lent(t("roll_class_stats", classe["pv"], classe["attaque"], classe["defense"]))
    pause()
    return classe

# ─────────────────────────────────────────
#  UTILITAIRES
# ─────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg=None):
    input(f"\n{msg or t('press_enter')}")

def lent(texte, delai=0.03):
    for char in texte:
        print(char, end='', flush=True)
        time.sleep(delai)
    print()

def titre(texte):
    print("\n" + "═" * 50)
    print(f"  {texte}")
    print("═" * 50)

def choisir_langue():
    global LANG
    clear()
    print(f"\n  {t('choose_lang')}\n")
    print(f"  {t('lang_en')}")
    print(f"  {t('lang_fr')}")
    LANG = "fr" if input("\n  > ").strip() == "2" else "en"

def donner_loot(joueur, loots):
    if not loots:
        return
    loot = random.choice(loots)
    loots.remove(loot)
    loot_type, valeur = loot
    if loot_type == "potion":
        joueur.inventaire.append(t("item_potion")); lent(t("loot_potion"))
    elif loot_type == "gold":
        joueur.or_ += valeur; lent(t("loot_gold", valeur))
    elif loot_type == "atk":
        joueur.attaque += valeur; lent(t("loot_atk", valeur))
    elif loot_type == "def":
        joueur.defense += valeur; lent(t("loot_def", valeur))

# ─────────────────────────────────────────
#  CHEAT PANEL
# ─────────────────────────────────────────

def cheat_panel(joueur):
    clear()
    print(t("cheat_locked"))
    if not verifier_mdp(input("  > ").strip()):
        print(t("cheat_wrong")); pause(); return
    while True:
        clear()
        print("\n╔══════════════════════════════════════════╗")
        print(f"║   {t('cheat_title')}║")
        print("╚══════════════════════════════════════════╝")
        print(t("cheat_stats"))
        print(t("cheat_hp", joueur.pv, joueur.pv_max))
        print(t("cheat_atk", joueur.attaque))
        print(t("cheat_def", joueur.defense))
        print(t("cheat_gold", joueur.or_))
        print(t("cheat_lvl", joueur.niveau))
        inv = ', '.join(joueur.inventaire) if joueur.inventaire else t("cheat_empty")
        print(t("cheat_inv", inv))
        print(t("cheat_menu"))
        choix = input("\n  > ").strip()
        if choix == "1":
            m = input(t("cheat_how_much_gold")).strip()
            if m.isdigit(): joueur.or_ += int(m); print(t("cheat_gold_added", m, joueur.or_))
            else: print(t("invalid_number"))
        elif choix == "2":
            joueur.pv = joueur.pv_max; print(t("cheat_hp_full", joueur.pv_max, joueur.pv_max))
        elif choix == "3":
            v = input(t("cheat_how_much_atk")).strip()
            if v.isdigit(): joueur.attaque += int(v); print(t("cheat_atk_done", joueur.attaque))
            else: print(t("invalid_number"))
        elif choix == "4":
            v = input(t("cheat_how_much_def")).strip()
            if v.isdigit(): joueur.defense += int(v); print(t("cheat_def_done", joueur.defense))
            else: print(t("invalid_number"))
        elif choix == "5":
            n = input(t("cheat_how_many_pot")).strip()
            if n.isdigit():
                for _ in range(int(n)): joueur.inventaire.append(t("item_potion"))
                print(t("cheat_pot_done", n))
            else: print(t("invalid_number"))
        elif choix == "6":
            joueur.attaque = 9999; print(t("cheat_oneshot"))
        elif choix == "7":
            joueur.niveau_suivant(); print(t("cheat_levelup", joueur.niveau))
        elif choix == "8":
            joueur.pv_max = joueur.pv = 9999; joueur.attaque = 999
            joueur.defense = 999; joueur.or_ = 99999
            for _ in range(10): joueur.inventaire.append(t("item_potion"))
            print(t("cheat_god"))
        elif choix == "9":
            if input(t("cheat_reset_confirm")).strip().lower() == t("cheat_reset_yes"):
                joueur.pv = joueur.pv_max = 100; joueur.attaque = 15
                joueur.defense = 5; joueur.or_ = 10
                joueur.niveau = 1; joueur.xp = 0; joueur.inventaire = []
                print(t("cheat_reset_done"))
        elif choix == "0":
            break
        elif choix.upper() == "C":
            # Afficher les 7 classes avec leurs stats
            clear()
            titre(t("cheat_class_title"))
            for i, c in enumerate(CLASSES[LANG], 1):
                print(f"\n  [{i}] {c['emoji']} {c['nom']}")
                print(f"      {c['desc']}")
                print(f"      HP: {c['pv']} | ATQ: {c['attaque']} | DEF: {c['defense']}")
            print()
            choix_classe = input(t("cheat_class_pick")).strip()
            if choix_classe.isdigit() and 1 <= int(choix_classe) <= len(CLASSES[LANG]):
                nouvelle_classe = CLASSES[LANG][int(choix_classe) - 1]
                joueur.classe    = nouvelle_classe
                joueur.capacite  = nouvelle_classe["capacite"]
                joueur.pv_max    = nouvelle_classe["pv"]
                joueur.pv        = nouvelle_classe["pv"]
                joueur.attaque   = nouvelle_classe["attaque"]
                joueur.defense   = nouvelle_classe["defense"]
                joueur.niveau    = 1
                joueur.xp        = 0
                joueur.xp_prochain = 50
                print(t("cheat_class_done", nouvelle_classe["emoji"], nouvelle_classe["nom"]))
            else:
                print(t("cheat_class_invalid"))
        else:
            print(t("cheat_invalid"))
        pause()

# ─────────────────────────────────────────
#  CLASSES PERSONNAGE & ENNEMI
# ─────────────────────────────────────────

class Personnage:
    def __init__(self, nom, classe):
        self.nom = nom
        self.classe = classe
        self.capacite = classe["capacite"]
        self.pv = classe["pv"]; self.pv_max = classe["pv"]
        self.attaque = classe["attaque"]; self.defense = classe["defense"]
        self.or_ = 10; self.inventaire = []
        self.niveau = 1; self.xp = 0; self.xp_prochain = 50

    def est_vivant(self): return self.pv > 0

    def attaquer(self, cible):
        """Attaque de base + capacité de classe."""
        degats_base = max(1, self.attaque + random.randint(-3, 5) - cible.defense)

        if self.capacite == "crit" and random.random() < 0.15:
            degats_base = int(degats_base * 1.5)
            lent(t("combat_crit", degats_base))
            cible.pv -= degats_base
            return degats_base, False

        elif self.capacite == "double":
            d2 = max(1, degats_base // 2)
            lent(t("combat_double", degats_base, d2))
            cible.pv -= (degats_base + d2)
            return degats_base + d2, False

        elif self.capacite == "lifesteal":
            cible.pv -= degats_base
            vol = max(1, int(degats_base * 0.15))
            self.soigner(vol)
            lent(t("combat_lifesteal", vol, cible.nom))
            return degats_base, False

        elif self.capacite == "stun" and random.random() < 0.20:
            cible.pv -= degats_base
            lent(t("combat_stun", cible.nom))
            return degats_base, True  # True = stun actif

        else:
            cible.pv -= degats_base
            return degats_base, False

    def soigner(self, points):
        self.pv = min(self.pv_max, self.pv + points)

    def gagner_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_prochain:
            self.niveau_suivant()

    def niveau_suivant(self):
        self.niveau += 1
        self.xp -= self.xp_prochain
        self.xp_prochain = int(self.xp_prochain * 1.5)
        self.pv_max += 20; self.pv = self.pv_max
        self.attaque += 3; self.defense += 1
        lent(t("levelup", self.niveau))

    def afficher_stats(self):
        label = "Level" if LANG == "en" else "Niveau"
        titre(f"{self.classe['emoji']} {self.nom} — {label} {self.niveau}")
        print(t("stats_class", f"{self.classe['emoji']} {self.classe['nom']}"))
        print(t("stats_hp", self.pv, self.pv_max))
        print(t("stats_atk", self.attaque))
        print(t("stats_def", self.defense))
        print(t("stats_gold", self.or_))
        print(t("stats_xp", self.xp, self.xp_prochain))
        inv = ', '.join(self.inventaire) if self.inventaire else t("stats_empty")
        print(t("stats_inv", inv))

    def utiliser_potion(self):
        potion = t("item_potion")
        if potion in self.inventaire:
            self.inventaire.remove(potion); self.soigner(40)
            lent(t("potion_used", 40)); return True
        lent(t("potion_none")); return False


class Ennemi:
    def __init__(self, nom, pv, attaque, defense, xp, or_):
        self.nom = nom; self.pv = pv; self.pv_max = pv
        self.attaque = attaque; self.defense = defense
        self.xp = xp; self.or_ = or_

    def est_vivant(self): return self.pv > 0

    def attaquer(self, cible):
        degats = max(1, self.attaque + random.randint(-2, 3) - cible.defense)
        cible.pv -= degats
        return degats

# ─────────────────────────────────────────
#  COMBAT
# ─────────────────────────────────────────

def combat(joueur, ennemi):
    titre(t("combat_title", joueur.nom, ennemi.nom))
    lent(t("combat_appears", ennemi.nom, ennemi.pv, ennemi.attaque))

    while joueur.est_vivant() and ennemi.est_vivant():
        # Regen du Soigneur (seulement si vivant et pas à PV max)
        if joueur.capacite == "regen" and joueur.pv < joueur.pv_max:
            joueur.soigner(5)
            lent(t("combat_heal_turn", 5))

        pct   = int((joueur.pv / joueur.pv_max) * 20)
        pct_e = int((ennemi.pv / ennemi.pv_max) * 20)
        you   = "You" if LANG == "en" else "Toi"
        print(f"\n  {joueur.classe['emoji']}{you:<5} [{'█'*pct}{'░'*(20-pct)}] {joueur.pv}/{joueur.pv_max} HP")
        print(f"  {'👾'}{ennemi.nom[:7]:<7} [{'█'*pct_e}{'░'*(20-pct_e)}] {ennemi.pv}/{ennemi.pv_max} HP")
        print(t("combat_action"))
        print(t("combat_1")); print(t("combat_2"))
        print(t("combat_3")); print(t("map_cheat"))

        choix = input("\n  > ").strip().upper()

        if choix == "C":
            cheat_panel(joueur); continue
        elif choix == "1":
            degats, stun = joueur.attaquer(ennemi)
            if joueur.capacite not in ["crit", "double", "lifesteal", "stun"]:
                lent(t("combat_hit", ennemi.nom, degats))
            if ennemi.est_vivant() and not stun:
                dr = ennemi.attaquer(joueur)
                lent(t("combat_recv", ennemi.nom, dr))
        elif choix == "2":
            joueur.utiliser_potion()
            if ennemi.est_vivant():
                dr = ennemi.attaquer(joueur)
                lent(t("combat_opening", ennemi.nom, dr))
        elif choix == "3":
            if random.random() < 0.5:
                lent(t("combat_flee_ok")); return "fuite"
            else:
                lent(t("combat_flee_fail"))
                dr = ennemi.attaquer(joueur)
                lent(t("combat_backstab", ennemi.nom, dr))
        else:
            lent(t("combat_invalid"))

    if joueur.est_vivant():
        lent(t("combat_win", ennemi.nom))
        joueur.gagner_xp(ennemi.xp)
        joueur.or_ += ennemi.or_
        lent(t("combat_xp_gold", ennemi.xp, ennemi.or_))
        return "victoire"
    lent(t("combat_lose", ennemi.nom))
    return "defaite"

# ─────────────────────────────────────────
#  SYSTÈME DE MONDE À 3 NIVEAUX
# ─────────────────────────────────────────

def monde_a_niveaux(joueur, titre_monde, intro, niveaux_data, boss_data, loots_boss, win1, win2):
    titre(titre_monde)
    lent(intro)
    pause()

    for num_lvl, vagues in enumerate(niveaux_data, 1):
        lent(t("level_intro", num_lvl))
        pause()
        for num_vague, ennemi_data in enumerate(vagues, 1):
            lent(t("wave_intro", num_vague, len(vagues), ennemi_data[0]))
            ennemi = Ennemi(*ennemi_data)
            resultat = combat(joueur, ennemi)
            if resultat == "defaite":
                return False
            lent(t("wave_clear"))
            # Loot entre vagues (50% de chance)
            if random.random() < 0.5:
                joueur.inventaire.append(t("item_potion"))
                lent(t("loot_potion"))
        lent(t("level_clear", num_lvl))
        pause()

    lent(f"\n  ⚠️  BOSS !")
    boss = Ennemi(*boss_data)
    resultat = combat(joueur, boss)
    if resultat == "defaite":
        return False

    lent(win1); lent(win2)
    loots = list(loots_boss)
    donner_loot(joueur, loots)
    lent(t("world_clear", titre_monde))
    return True

# ─────────────────────────────────────────
#  ZONES — ennemis rééquilibrés (-30% PV/ATQ)
# ─────────────────────────────────────────

def zone_foret(joueur):
    niveaux = [
        [(t("forest_e1"), 14, 6,  1, 8,  3),
         (t("forest_e1"), 15, 6,  1, 8,  3)],
        [(t("forest_e2"), 24, 8,  2, 15, 6),
         (t("forest_e2"), 26, 9,  2, 15, 6),
         (t("forest_e3"), 30, 10, 3, 18, 8)],
        [(t("forest_e3"), 34, 11, 3, 20, 10),
         (t("forest_e3"), 36, 11, 3, 20, 10),
         (t("forest_e2"), 28, 10, 2, 18, 8)],
    ]
    boss = (t("forest_boss"), 55, 13, 4, 40, 20)
    loots = [("atk", 3), ("potion", 0), ("gold", 25)]
    return monde_a_niveaux(joueur, t("forest_title"), t("forest_intro"),
                           niveaux, boss, loots, t("loot_atk", 3), t("loot_gold", 25))


def zone_village(joueur):
    titre(t("village_title"))
    lent(t("village_intro1")); lent(t("village_intro2"))
    while True:
        print(t("village_action"))
        print(t("village_1")); print(t("village_2"))
        print(t("village_3")); print(t("village_4"))
        print(t("map_cheat"))
        choix = input("\n  > ").strip().upper()
        if choix == "C":
            cheat_panel(joueur); continue
        elif choix == "1":
            titre(t("shop_title")); print(t("shop_gold", joueur.or_))
            print(t("shop_1")); print(t("shop_2"))
            print(t("shop_3")); print(t("shop_4"))
            a = input("\n  > ").strip()
            if a == "1" and joueur.or_ >= 15:
                joueur.or_ -= 15; joueur.inventaire.append(t("item_potion")); lent(t("shop_potion_bought"))
            elif a == "2" and joueur.or_ >= 30:
                joueur.or_ -= 30; joueur.attaque += 5; lent(t("shop_sword_bought"))
            elif a == "3" and joueur.or_ >= 25:
                joueur.or_ -= 25; joueur.defense += 3; lent(t("shop_shield_bought"))
            elif a in ["1","2","3"]:
                lent(t("shop_no_gold"))
        elif choix == "2":
            if joueur.or_ >= 20:
                joueur.or_ -= 20; joueur.soigner(50); lent(t("tavern_rest"))
            else: lent(t("tavern_no_gold"))
        elif choix == "3":
            lent(random.choice(t("rumors")))
        elif choix == "4":
            break
    return True


def zone_ruines(joueur):
    niveaux = [
        [(t("ruins_e1"), 20, 7,  1, 12, 5),
         (t("ruins_e1"), 22, 7,  1, 12, 5)],
        [(t("ruins_e2"), 30, 10, 3, 18, 8),
         (t("ruins_e2"), 32, 10, 3, 18, 8),
         (t("ruins_e3"), 38, 12, 4, 22, 10)],
        [(t("ruins_e3"), 42, 13, 5, 25, 12),
         (t("ruins_e3"), 44, 13, 5, 25, 12),
         (t("ruins_e2"), 38, 11, 3, 20, 10)],
    ]
    boss = (t("ruins_boss"), 70, 15, 7, 50, 25)
    loots = [("atk", 10), ("potion", 0), ("gold", 30)]
    return monde_a_niveaux(joueur, t("ruins_title"), t("ruins_intro"),
                           niveaux, boss, loots, t("ruins_win"), t("ruins_win2"))


def zone_glace(joueur):
    niveaux = [
        [(t("ice_e1"), 24, 8,  2, 14, 6),
         (t("ice_e1"), 26, 9,  2, 14, 6)],
        [(t("ice_e2"), 38, 12, 4, 22, 10),
         (t("ice_e2"), 40, 12, 4, 22, 10),
         (t("ice_e3"), 48, 14, 6, 28, 14)],
        [(t("ice_e3"), 52, 15, 6, 30, 15),
         (t("ice_e3"), 54, 15, 6, 30, 15),
         (t("ice_e2"), 44, 13, 5, 26, 12)],
    ]
    boss = (t("ice_boss"), 90, 18, 8, 65, 35)
    loots = [("atk", 8), ("def", 4), ("gold", 40)]
    return monde_a_niveaux(joueur, t("ice_title"), t("ice_intro"),
                           niveaux, boss, loots, t("ice_win"), t("ice_win2"))


def zone_lave(joueur):
    niveaux = [
        [(t("lava_e1"), 28, 10, 3, 16, 7),
         (t("lava_e1"), 30, 10, 3, 16, 7)],
        [(t("lava_e2"), 42, 13, 5, 24, 12),
         (t("lava_e2"), 44, 14, 5, 24, 12),
         (t("lava_e3"), 56, 16, 7, 32, 16)],
        [(t("lava_e3"), 60, 17, 8, 35, 18),
         (t("lava_e3"), 62, 17, 8, 35, 18),
         (t("lava_e2"), 52, 15, 6, 30, 15)],
    ]
    boss = (t("lava_boss"), 110, 21, 10, 80, 45)
    loots = [("atk", 12), ("potion", 0), ("gold", 50)]
    return monde_a_niveaux(joueur, t("lava_title"), t("lava_intro"),
                           niveaux, boss, loots, t("lava_win"), t("lava_win2"))


def zone_bonbon(joueur):
    niveaux = [
        [(t("candy_e1"), 26, 8,  2, 14, 6),
         (t("candy_e1"), 28, 8,  2, 14, 6)],
        [(t("candy_e2"), 40, 11, 4, 22, 10),
         (t("candy_e2"), 42, 12, 4, 22, 10),
         (t("candy_e3"), 50, 15, 6, 28, 14)],
        [(t("candy_e3"), 53, 15, 6, 30, 15),
         (t("candy_e3"), 55, 16, 6, 30, 15),
         (t("candy_e2"), 46, 13, 5, 26, 12)],
    ]
    boss = (t("candy_boss"), 98, 20, 9, 72, 40)
    loots = [("atk", 6), ("def", 6), ("gold", 45)]
    return monde_a_niveaux(joueur, t("candy_title"), t("candy_intro"),
                           niveaux, boss, loots, t("candy_win"), t("candy_win2"))


def zone_chateau(joueur):
    titre(t("castle_title"))
    lent(t("castle_intro1")); lent(t("castle_intro2")); lent(t("castle_intro3"))
    dragon = Ennemi(t("enemy_dragon"), 180, 28, 12, 150, 100)
    resultat = combat(joueur, dragon)
    if resultat == "victoire":
        lent(t("castle_win1")); lent(t("castle_win2"))
        lent(t("castle_win3")); lent(t("castle_win4"))
        lent(t("castle_win5", joueur.nom)); return True
    return False

# ─────────────────────────────────────────
#  JEU PRINCIPAL
# ─────────────────────────────────────────

def menu_principal():
    clear()
    print(f"""
╔══════════════════════════════════════════╗
║                                          ║
║      ⚔️   {t('menu_title'):<32}🐉  ║
║                                          ║
║      {t('menu_sub'):<40}║
║                                          ║
╚══════════════════════════════════════════╝
    """)
    print(f"  {t('menu_new')}")
    print(f"  {t('menu_quit')}")
    return input("\n  > ").strip()


def jouer():
    clear()
    lent(t("ask_name"))
    nom = input("  > ").strip() or t("default_name")

    # Roll de classe
    classe = roll_classe()
    joueur = Personnage(nom, classe)

    lent(t("welcome", nom)); lent(t("intro")); pause()

    zones = {
        "1": zone_foret,  "2": zone_village, "3": zone_ruines,
        "4": zone_glace,  "5": zone_lave,    "6": zone_bonbon,
        "7": zone_chateau,
    }

    while joueur.est_vivant():
        clear()
        titre(t("map_title")); print(t("map_where"))
        print(t("map_1")); print(t("map_2")); print(t("map_3"))
        print(t("map_4")); print(t("map_5")); print(t("map_6"))
        print(t("map_7")); print(t("map_8")); print(t("map_9"))
        print(t("map_cheat"))

        choix = input("\n  > ").strip().upper()

        if choix == "C":
            cheat_panel(joueur); continue
        elif choix in zones:
            clear()
            vivant = zones[choix](joueur)
            if vivant is None: vivant = True  # sécurité anti-None
            if not vivant:
                lent(t("gameover", joueur.nom))
                lent(t("gameover_level", joueur.niveau)); break
            if choix == "7" and vivant: break
            pause()
        elif choix == "8":
            clear(); joueur.afficher_stats(); pause()
        elif choix == "9":
            lent(t("bye")); break
        else:
            lent(t("map_invalid"))


def main():
    choisir_langue()
    while True:
        choix = menu_principal()
        if choix == "1":
            jouer(); pause()
        elif choix == "2":
            lent(t("menu_bye")); break
        else:
            lent(t("menu_invalid"))

if __name__ == "__main__":
    main()