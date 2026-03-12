import random
import time
import os
import hashlib

CHEAT_PASSWORD_HASH = "2430568851915ea5c2ba11bbe2c2257d1a52ca008f6e1db9ce40afa92b438e80"

def verifier_mdp(saisie):
    return hashlib.sha256(saisie.encode()).hexdigest() == CHEAT_PASSWORD_HASH

# ─────────────────────────────────────────
#  LANGUES
# ─────────────────────────────────────────

LANG = "en"  # English by default

TEXTES = {
    "en": {
        "press_enter":        "Press Enter to continue...",
        "choose_lang":        "Choose your language / Choisissez votre langue",
        "lang_en":            "[1] English",
        "lang_fr":            "[2] Français",
        "menu_title":         "Shadow of the Dragon",
        "menu_sub":           "A text adventure game",
        "menu_new":           "[1] New game",
        "menu_quit":          "[2] Quit",
        "menu_invalid":       "  Invalid choice.",
        "menu_bye":           "\n  Goodbye! ⚔️\n",
        "ask_name":           "What is your name, adventurer?",
        "default_name":       "Hero",
        "welcome":            "  Welcome, {}! Your quest begins...",
        "intro":              "  A dragon threatens the kingdom. Only you can stop it.\n",
        "stats_hp":           "  HP        : {}/{}",
        "stats_atk":          "  Attack    : {}",
        "stats_def":          "  Defense   : {}",
        "stats_gold":         "  Gold      : {} 💰",
        "stats_xp":           "  XP        : {}/{}",
        "stats_inv":          "  Inventory : {}",
        "stats_empty":        "empty",
        "levelup":            "\n🌟 LEVEL {}! Your stats increased!",
        "potion_used":        "  🧪 You drink a potion and recover {} HP!",
        "potion_none":        "  You have no potions!",
        "map_title":          "🗺️  World Map",
        "map_where":          "  Where do you want to go?\n",
        "map_1":              "  [1] 🌲 Dark Forest     (combat)",
        "map_2":              "  [2] 🏘️  Village          (rest & shop)",
        "map_3":              "  [3] 🏚️  Ancient Ruins    (combat + loot)",
        "map_4":              "  [4] 🏰 Dragon's Castle  (final boss)",
        "map_5":              "  [5] 📊 View my stats",
        "map_6":              "  [6] 🚪 Quit",
        "map_cheat":          "  [C] 🎮 Cheat panel",
        "map_invalid":        "  Invalid choice.",
        "gameover":           "\n  💀 GAME OVER — {} has fallen in battle.",
        "gameover_level":     "  You reached level {}.",
        "bye":                "  Goodbye, adventurer!",
        "combat_title":       "⚔️  COMBAT: {} vs {}",
        "combat_appears":     "  A {} appears! (HP: {} | ATK: {})\n",
        "combat_action":      "\n  What do you do?",
        "combat_1":           "  [1] Attack",
        "combat_2":           "  [2] Use a potion",
        "combat_3":           "  [3] Flee",
        "combat_hit":         "  💥 You hit {} for {} damage!",
        "combat_recv":        "  😤 {} hits you for {} damage!",
        "combat_backstab":    "  😤 {} stabs you in the back: {} damage!",
        "combat_opening":     "  😤 {} takes the opening: {} damage!",
        "combat_flee_ok":     "  🏃 You successfully flee!",
        "combat_flee_fail":   "  ❌ Can't escape!",
        "combat_invalid":     "  Invalid action.",
        "combat_win":         "\n  🏆 Victory! You defeat {}!",
        "combat_xp_gold":     "  +{} XP | +{} 💰",
        "combat_lose":        "\n  💀 You were defeated by {}...",
        "forest_title":       "🌲 The Dark Forest",
        "forest_intro1":      "You venture into a dense forest. The trees hide the sun.",
        "forest_intro2":      "A shadow leaps from the bushes...\n",
        "forest_search":      "\nSearching the forest, you find something...",
        "forest_potion":      "  🧪 You found a Healing Potion!",
        "forest_sword":       "  🗡️  You found a rusty old sword... but usable.",
        "village_title":      "🏘️  The Village of Stonehollow",
        "village_intro1":     "You arrive in a lively little village.",
        "village_intro2":     "A tavern, a blacksmith and a merchant await you.\n",
        "village_action":     "\n  What do you do?",
        "village_1":          "  [1] Go to the merchant",
        "village_2":          "  [2] Rest at the tavern (20 💰)",
        "village_3":          "  [3] Talk to villagers",
        "village_4":          "  [4] Leave the village",
        "shop_title":         "🛒 Merchant",
        "shop_gold":          "\n  Your gold: {} 💰\n",
        "shop_1":             "  [1] Healing Potion     — 15 💰",
        "shop_2":             "  [2] Sword upgrade      — 30 💰 (+5 attack)",
        "shop_3":             "  [3] Wooden shield      — 25 💰 (+3 defense)",
        "shop_4":             "  [4] Back",
        "shop_potion_bought": "  Potion purchased!",
        "shop_sword_bought":  "  Sword upgraded! +5 attack",
        "shop_shield_bought": "  Shield purchased! +3 defense",
        "shop_no_gold":       "  Not enough gold!",
        "tavern_rest":        "  🍺 You rest and recover 50 HP.",
        "tavern_no_gold":     "  You don't have enough gold.",
        "rumors": [
            "  « Beware the Castle of the East... the dragon slumbers there. »",
            "  « They say a legendary sword is hidden in the ruins. »",
            "  « The king offers a reward for the dragon's head! »",
        ],
        "ruins_title":        "🏚️  The Ancient Ruins",
        "ruins_intro1":       "Collapsed stones, extinguished torches...",
        "ruins_intro2":       "At the end of a corridor, an armed figure blocks your path.\n",
        "ruins_win":          "\n  In a dusty chest, you find a LEGENDARY SWORD!",
        "ruins_win2":         "  +10 permanent attack!",
        "castle_title":       "🏰 The Dragon's Castle",
        "castle_intro1":      "Walls blackened by fire, the air smells of sulfur.",
        "castle_intro2":      "You climb the spiral staircase to the throne room...\n",
        "castle_intro3":      "RAAAAARRGH! THE DRAGON SPOTS YOU!\n",
        "castle_win1":        "\n  The dragon collapses with one last roar.",
        "castle_win2":        "  A golden light fills the hall...",
        "castle_win3":        "\n  🎉 YOU SAVED THE KINGDOM! 🎉",
        "castle_win4":        "  The king rewards you with a legendary gift.",
        "castle_win5":        "\n  Thanks for playing, {}!\n",
        "cheat_locked":       "\n  🔒 Restricted access — Password required",
        "cheat_wrong":        "  ❌ Wrong password.",
        "cheat_title":        "🎮  CHEAT PANEL  —  DEV MODE          ",
        "cheat_stats":        "\n  Current stats:",
        "cheat_hp":           "  ❤️  HP      : {}/{}",
        "cheat_atk":          "  ⚔️  Attack  : {}",
        "cheat_def":          "  🛡️  Defense : {}",
        "cheat_gold":         "  💰 Gold    : {}",
        "cheat_lvl":          "  ⭐ Level   : {}",
        "cheat_inv":          "  🎒 Inventory: {}",
        "cheat_empty":        "empty",
        "cheat_menu": """
  ─────────────────────────────────────────
  [1] 💰 Give gold
  [2] ❤️  Full HP
  [3] ⚔️  Boost attack
  [4] 🛡️  Boost defense
  [5] 🧪 Add potions
  [6] 💀 One-shot mode (attack = 9999)
  [7] 🏆 Level up
  [8] 👑 MAX EVERYTHING (god mode)
  [9] 🔄 Reset stats
  [0] ❌ Close cheat panel
  ─────────────────────────────────────────""",
        "cheat_how_much_gold":  "  How much gold? > ",
        "cheat_gold_added":     "  ✅ +{} gold! You now have {} 💰",
        "cheat_hp_full":        "  ✅ HP maxed out! ({}/{})",
        "cheat_how_much_atk":   "  How many attack points to add? > ",
        "cheat_atk_done":       "  ✅ Attack → {}!",
        "cheat_how_much_def":   "  How many defense points to add? > ",
        "cheat_def_done":       "  ✅ Defense → {}!",
        "cheat_how_many_pot":   "  How many potions? > ",
        "cheat_pot_done":       "  ✅ +{} potion(s) added!",
        "cheat_oneshot":        "  ✅ ONE-SHOT MODE on! Attack = 9999 💥",
        "cheat_levelup":        "  ✅ You are now level {}!",
        "cheat_god":            "  ✅ GOD MODE on! You are INVINCIBLE 👑",
        "cheat_reset_confirm":  "  Reset stats? (y/n) > ",
        "cheat_reset_yes":      "y",
        "cheat_reset_done":     "  ✅ Stats reset.",
        "cheat_invalid":        "  Invalid choice.",
        "invalid_number":       "  ❌ Invalid number.",
        "enemy_wolf":           "Black Wolf",
        "enemy_knight":         "Cursed Knight",
        "enemy_dragon":         "Ancient Dragon",
        "item_potion":          "Healing Potion",
    },
    "fr": {
        "press_enter":        "Appuie sur Entrée pour continuer...",
        "choose_lang":        "Choose your language / Choisissez votre langue",
        "lang_en":            "[1] English",
        "lang_fr":            "[2] Français",
        "menu_title":         "L'Ombre du Dragon",
        "menu_sub":           "Un jeu d'aventure textuel",
        "menu_new":           "[1] Nouvelle partie",
        "menu_quit":          "[2] Quitter",
        "menu_invalid":       "  Choix invalide.",
        "menu_bye":           "\n  Au revoir ! ⚔️\n",
        "ask_name":           "Quel est ton nom, aventurier ?",
        "default_name":       "Héros",
        "welcome":            "  Bienvenue, {} ! Ta quête commence...",
        "intro":              "  Un dragon menace le royaume. Seul toi peux l'arrêter.\n",
        "stats_hp":           "  PV        : {}/{}",
        "stats_atk":          "  Attaque   : {}",
        "stats_def":          "  Défense   : {}",
        "stats_gold":         "  Or        : {} 💰",
        "stats_xp":           "  XP        : {}/{}",
        "stats_inv":          "  Inventaire: {}",
        "stats_empty":        "vide",
        "levelup":            "\n🌟 NIVEAU {} ! Tes stats augmentent !",
        "potion_used":        "  🧪 Tu bois une potion et récupères {} PV !",
        "potion_none":        "  Tu n'as pas de potion !",
        "map_title":          "🗺️  Carte du Monde",
        "map_where":          "  Où veux-tu aller ?\n",
        "map_1":              "  [1] 🌲 Forêt Sombre     (combat)",
        "map_2":              "  [2] 🏘️  Village           (repos & achats)",
        "map_3":              "  [3] 🏚️  Ruines Anciennes  (combat + butin)",
        "map_4":              "  [4] 🏰 Château du Dragon (boss final)",
        "map_5":              "  [5] 📊 Voir mes stats",
        "map_6":              "  [6] 🚪 Quitter",
        "map_cheat":          "  [C] 🎮 Cheat panel",
        "map_invalid":        "  Choix invalide.",
        "gameover":           "\n  💀 GAME OVER — {} est tombé au combat.",
        "gameover_level":     "  Tu as atteint le niveau {}.",
        "bye":                "  À bientôt, aventurier !",
        "combat_title":       "⚔️  COMBAT : {} vs {}",
        "combat_appears":     "  Un {} apparaît ! (PV: {} | ATQ: {})\n",
        "combat_action":      "\n  Que fais-tu ?",
        "combat_1":           "  [1] Attaquer",
        "combat_2":           "  [2] Utiliser une potion",
        "combat_3":           "  [3] Fuir",
        "combat_hit":         "  💥 Tu frappes {} pour {} dégâts !",
        "combat_recv":        "  😤 {} te frappe pour {} dégâts !",
        "combat_backstab":    "  😤 {} te frappe dans le dos : {} dégâts !",
        "combat_opening":     "  😤 {} profite de l'ouverture : {} dégâts !",
        "combat_flee_ok":     "  🏃 Tu réussis à fuir !",
        "combat_flee_fail":   "  ❌ Impossible de fuir !",
        "combat_invalid":     "  Action invalide.",
        "combat_win":         "\n  🏆 Victoire ! Tu bats {} !",
        "combat_xp_gold":     "  +{} XP | +{} 💰",
        "combat_lose":        "\n  💀 Tu as été vaincu par {}...",
        "forest_title":       "🌲 La Forêt Sombre",
        "forest_intro1":      "Tu t'aventures dans une forêt dense. Les arbres cachent le soleil.",
        "forest_intro2":      "Une silhouette surgit des buissons...\n",
        "forest_search":      "\nEn fouillant la forêt, tu trouves quelque chose...",
        "forest_potion":      "  🧪 Tu trouves une Potion de soin !",
        "forest_sword":       "  🗡️  Tu trouves une vieille épée rouillée... mais utilisable.",
        "village_title":      "🏘️  Le Village de Pierrecreux",
        "village_intro1":     "Tu arrives dans un petit village animé.",
        "village_intro2":     "Une taverne, un forgeron et un marchand t'attendent.\n",
        "village_action":     "\n  Que fais-tu ?",
        "village_1":          "  [1] Aller chez le marchand",
        "village_2":          "  [2] Te reposer à la taverne (20 💰)",
        "village_3":          "  [3] Parler aux villageois",
        "village_4":          "  [4] Quitter le village",
        "shop_title":         "🛒 Marchand",
        "shop_gold":          "\n  Ton or : {} 💰\n",
        "shop_1":             "  [1] Potion de soin      — 15 💰",
        "shop_2":             "  [2] Amélioration épée   — 30 💰 (+5 attaque)",
        "shop_3":             "  [3] Bouclier de bois    — 25 💰 (+3 défense)",
        "shop_4":             "  [4] Retour",
        "shop_potion_bought": "  Potion achetée !",
        "shop_sword_bought":  "  Épée améliorée ! +5 attaque",
        "shop_shield_bought": "  Bouclier acheté ! +3 défense",
        "shop_no_gold":       "  Pas assez d'or !",
        "tavern_rest":        "  🍺 Tu te reposes et récupères 50 PV.",
        "tavern_no_gold":     "  Tu n'as pas assez d'or.",
        "rumors": [
            "  « Méfie-toi du Château de l'Est... le dragon y sommeille. »",
            "  « On dit qu'une épée légendaire est cachée dans les ruines. »",
            "  « Le roi offre une récompense pour la tête du dragon ! »",
        ],
        "ruins_title":        "🏚️  Les Ruines Anciennes",
        "ruins_intro1":       "Des pierres effondrées, des torches éteintes...",
        "ruins_intro2":       "Au fond d'un couloir, une silhouette armée te barre la route.\n",
        "ruins_win":          "\n  Dans un coffre poussiéreux, tu trouves une ÉPÉE LÉGENDAIRE !",
        "ruins_win2":         "  +10 attaque permanente !",
        "castle_title":       "🏰 Le Château du Dragon",
        "castle_intro1":      "Les murs noircis par le feu, l'air sent le soufre.",
        "castle_intro2":      "Tu montes les escaliers en spirale jusqu'à la salle du trône...\n",
        "castle_intro3":      "RAAAAARRGH ! LE DRAGON T'APERÇOIT !\n",
        "castle_win1":        "\n  Le dragon s'effondre dans un dernier rugissement.",
        "castle_win2":        "  Une lumière dorée envahit la salle...",
        "castle_win3":        "\n  🎉 TU AS SAUVÉ LE ROYAUME ! 🎉",
        "castle_win4":        "  Le roi t'offre une récompense légendaire.",
        "castle_win5":        "\n  Merci d'avoir joué, {} !\n",
        "cheat_locked":       "\n  🔒 Accès restreint — Mot de passe requis",
        "cheat_wrong":        "  ❌ Mauvais mot de passe.",
        "cheat_title":        "🎮  CHEAT PANEL  —  MODE DEV          ",
        "cheat_stats":        "\n  Stats actuelles :",
        "cheat_hp":           "  ❤️  PV      : {}/{}",
        "cheat_atk":          "  ⚔️  Attaque : {}",
        "cheat_def":          "  🛡️  Défense : {}",
        "cheat_gold":         "  💰 Or      : {}",
        "cheat_lvl":          "  ⭐ Niveau  : {}",
        "cheat_inv":          "  🎒 Inventaire: {}",
        "cheat_empty":        "vide",
        "cheat_menu": """
  ─────────────────────────────────────────
  [1] 💰 Donner de l'or
  [2] ❤️  Remplir les PV
  [3] ⚔️  Booster l'attaque
  [4] 🛡️  Booster la défense
  [5] 🧪 Ajouter des potions
  [6] 💀 One-shot mode (attaque = 9999)
  [7] 🏆 Monter de niveau
  [8] 👑 TOUT MAX  (mode god)
  [9] 🔄 Remettre à zéro les stats
  [0] ❌ Fermer le cheat panel
  ─────────────────────────────────────────""",
        "cheat_how_much_gold":  "  Combien d'or ? > ",
        "cheat_gold_added":     "  ✅ +{} or ! Tu as maintenant {} 💰",
        "cheat_hp_full":        "  ✅ PV au maximum ! ({}/{})",
        "cheat_how_much_atk":   "  Combien de points d'attaque à ajouter ? > ",
        "cheat_atk_done":       "  ✅ Attaque → {} !",
        "cheat_how_much_def":   "  Combien de points de défense à ajouter ? > ",
        "cheat_def_done":       "  ✅ Défense → {} !",
        "cheat_how_many_pot":   "  Combien de potions ? > ",
        "cheat_pot_done":       "  ✅ +{} potion(s) dans l'inventaire !",
        "cheat_oneshot":        "  ✅ ONE-SHOT MODE activé ! Attaque = 9999 💥",
        "cheat_levelup":        "  ✅ Tu es maintenant niveau {} !",
        "cheat_god":            "  ✅ MODE GOD activé ! Tu es INVINCIBLE 👑",
        "cheat_reset_confirm":  "  Remettre à zéro ? (o/n) > ",
        "cheat_reset_yes":      "o",
        "cheat_reset_done":     "  ✅ Stats remises à zéro.",
        "cheat_invalid":        "  Choix invalide.",
        "invalid_number":       "  ❌ Nombre invalide.",
        "enemy_wolf":           "Loup Noir",
        "enemy_knight":         "Chevalier Maudit",
        "enemy_dragon":         "Dragon Ancien",
        "item_potion":          "Potion de soin",
    }
}

def t(cle, *args):
    texte = TEXTES[LANG].get(cle, f"[{cle}]")
    if args:
        return texte.format(*args)
    return texte

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
    choix = input("\n  > ").strip()
    if choix == "2":
        LANG = "fr"
    else:
        LANG = "en"

# ─────────────────────────────────────────
#  CHEAT PANEL
# ─────────────────────────────────────────

def cheat_panel(joueur):
    clear()
    print(t("cheat_locked"))
    mdp = input("  > ").strip()
    if not verifier_mdp(mdp):
        print(t("cheat_wrong"))
        pause()
        return

    while True:
        clear()
        print("\n╔══════════════════════════════════════════╗")
        print(f"║   {t('cheat_title')}║")
        print("╚══════════════════════════════════════════╝")
        print(t("cheat_stats"))
        print(t("cheat_hp",   joueur.pv, joueur.pv_max))
        print(t("cheat_atk",  joueur.attaque))
        print(t("cheat_def",  joueur.defense))
        print(t("cheat_gold", joueur.or_))
        print(t("cheat_lvl",  joueur.niveau))
        inv = ', '.join(joueur.inventaire) if joueur.inventaire else t("cheat_empty")
        print(t("cheat_inv", inv))
        print(t("cheat_menu"))

        choix = input("\n  > ").strip()

        if choix == "1":
            montant = input(t("cheat_how_much_gold")).strip()
            if montant.isdigit():
                joueur.or_ += int(montant)
                print(t("cheat_gold_added", montant, joueur.or_))
            else:
                print(t("invalid_number"))
            pause()
        elif choix == "2":
            joueur.pv = joueur.pv_max
            print(t("cheat_hp_full", joueur.pv_max, joueur.pv_max))
            pause()
        elif choix == "3":
            val = input(t("cheat_how_much_atk")).strip()
            if val.isdigit():
                joueur.attaque += int(val)
                print(t("cheat_atk_done", joueur.attaque))
            else:
                print(t("invalid_number"))
            pause()
        elif choix == "4":
            val = input(t("cheat_how_much_def")).strip()
            if val.isdigit():
                joueur.defense += int(val)
                print(t("cheat_def_done", joueur.defense))
            else:
                print(t("invalid_number"))
            pause()
        elif choix == "5":
            nb = input(t("cheat_how_many_pot")).strip()
            if nb.isdigit():
                for _ in range(int(nb)):
                    joueur.inventaire.append(t("item_potion"))
                print(t("cheat_pot_done", nb))
            else:
                print(t("invalid_number"))
            pause()
        elif choix == "6":
            joueur.attaque = 9999
            print(t("cheat_oneshot"))
            pause()
        elif choix == "7":
            joueur.niveau_suivant()
            print(t("cheat_levelup", joueur.niveau))
            pause()
        elif choix == "8":
            joueur.pv_max  = 9999
            joueur.pv      = 9999
            joueur.attaque = 999
            joueur.defense = 999
            joueur.or_     = 99999
            for _ in range(10):
                joueur.inventaire.append(t("item_potion"))
            print(t("cheat_god"))
            pause()
        elif choix == "9":
            confirm = input(t("cheat_reset_confirm")).strip().lower()
            if confirm == t("cheat_reset_yes"):
                joueur.pv = 100; joueur.pv_max = 100
                joueur.attaque = 15; joueur.defense = 5
                joueur.or_ = 10; joueur.niveau = 1
                joueur.xp = 0; joueur.inventaire = []
                print(t("cheat_reset_done"))
            pause()
        elif choix == "0":
            break
        else:
            print(t("cheat_invalid"))
            pause()

# ─────────────────────────────────────────
#  CLASSES
# ─────────────────────────────────────────

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.pv = 100; self.pv_max = 100
        self.attaque = 15; self.defense = 5
        self.or_ = 10; self.inventaire = []
        self.niveau = 1; self.xp = 0; self.xp_prochain = 50

    def est_vivant(self): return self.pv > 0

    def attaquer(self, cible):
        degats = max(1, self.attaque + random.randint(-3, 5) - cible.defense)
        cible.pv -= degats
        return degats

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
        titre(f"⚔️  {self.nom} — {label} {self.niveau}")
        print(t("stats_hp",  self.pv, self.pv_max))
        print(t("stats_atk", self.attaque))
        print(t("stats_def", self.defense))
        print(t("stats_gold", self.or_))
        print(t("stats_xp",  self.xp, self.xp_prochain))
        inv = ', '.join(self.inventaire) if self.inventaire else t("stats_empty")
        print(t("stats_inv", inv))

    def utiliser_potion(self):
        potion = t("item_potion")
        if potion in self.inventaire:
            self.inventaire.remove(potion)
            self.soigner(40)
            lent(t("potion_used", 40))
            return True
        lent(t("potion_none"))
        return False


class Ennemi:
    def __init__(self, nom, pv, attaque, defense, xp, or_):
        self.nom = nom; self.pv = pv; self.pv_max = pv
        self.attaque = attaque; self.defense = defense
        self.xp = xp; self.or_ = or_

    def est_vivant(self): return self.pv > 0

    def attaquer(self, cible):
        degats = max(1, self.attaque + random.randint(-2, 4) - cible.defense)
        cible.pv -= degats
        return degats

# ─────────────────────────────────────────
#  COMBAT
# ─────────────────────────────────────────

def combat(joueur, ennemi):
    titre(t("combat_title", joueur.nom, ennemi.nom))
    lent(t("combat_appears", ennemi.nom, ennemi.pv, ennemi.attaque))

    while joueur.est_vivant() and ennemi.est_vivant():
        pct   = int((joueur.pv / joueur.pv_max) * 20)
        pct_e = int((ennemi.pv / ennemi.pv_max) * 20)
        you   = "You" if LANG == "en" else "Toi"
        print(f"\n  {you:<6} [{'█'*pct}{'░'*(20-pct)}] {joueur.pv}/{joueur.pv_max} HP")
        print(f"  {ennemi.nom[:6]:<6} [{'█'*pct_e}{'░'*(20-pct_e)}] {ennemi.pv}/{ennemi.pv_max} HP")
        print(t("combat_action"))
        print(t("combat_1"))
        print(t("combat_2"))
        print(t("combat_3"))
        print(t("map_cheat"))

        choix = input("\n  > ").strip().upper()

        if choix == "C":
            cheat_panel(joueur)
            continue
        elif choix == "1":
            d = joueur.attaquer(ennemi)
            lent(t("combat_hit", ennemi.nom, d))
            if ennemi.est_vivant():
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
#  ZONES
# ─────────────────────────────────────────

def zone_foret(joueur):
    titre(t("forest_title"))
    lent(t("forest_intro1")); lent(t("forest_intro2"))
    ennemi = Ennemi(t("enemy_wolf"), 40, 12, 2, 20, 5)
    resultat = combat(joueur, ennemi)
    if resultat == "victoire":
        lent(t("forest_search"))
        if random.random() < 0.6:
            joueur.inventaire.append(t("item_potion"))
            lent(t("forest_potion"))
        else:
            lent(t("forest_sword")); joueur.attaque += 2
        return True
    return resultat != "defaite"


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
            titre(t("shop_title"))
            print(t("shop_gold", joueur.or_))
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
            else:
                lent(t("tavern_no_gold"))
        elif choix == "3":
            lent(random.choice(t("rumors")))
        elif choix == "4":
            break
    return True


def zone_ruines(joueur):
    titre(t("ruins_title"))
    lent(t("ruins_intro1")); lent(t("ruins_intro2"))
    ennemi = Ennemi(t("enemy_knight"), 70, 18, 8, 40, 20)
    resultat = combat(joueur, ennemi)
    if resultat == "victoire":
        lent(t("ruins_win")); joueur.attaque += 10; lent(t("ruins_win2")); return True
    return resultat != "defaite"


def zone_chateau(joueur):
    titre(t("castle_title"))
    lent(t("castle_intro1")); lent(t("castle_intro2")); lent(t("castle_intro3"))
    dragon = Ennemi(t("enemy_dragon"), 150, 25, 10, 100, 50)
    resultat = combat(joueur, dragon)
    if resultat == "victoire":
        lent(t("castle_win1")); lent(t("castle_win2"))
        lent(t("castle_win3")); lent(t("castle_win4"))
        lent(t("castle_win5", joueur.nom)); return True
    return resultat != "defaite"

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
    joueur = Personnage(nom)
    lent(t("welcome", nom)); lent(t("intro")); pause()

    zones = {"1": zone_foret, "2": zone_village, "3": zone_ruines, "4": zone_chateau}

    while joueur.est_vivant():
        clear()
        titre(t("map_title")); print(t("map_where"))
        print(t("map_1")); print(t("map_2"))
        print(t("map_3")); print(t("map_4"))
        print(t("map_5")); print(t("map_6"))
        print(t("map_cheat"))

        choix = input("\n  > ").strip().upper()

        if choix == "C":
            cheat_panel(joueur); continue
        elif choix in zones:
            clear()
            vivant = zones[choix](joueur)
            if not vivant:
                lent(t("gameover", joueur.nom))
                lent(t("gameover_level", joueur.niveau)); break
            if choix == "4" and vivant: break
            pause()
        elif choix == "5":
            clear(); joueur.afficher_stats(); pause()
        elif choix == "6":
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