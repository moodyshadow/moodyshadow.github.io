"""
Hardcoded Diablo 4 Build Knowledge Base
Contains builds, gear, skills, and strategies for all classes
"""

BUILDS = {
    "barbarian": {
        "damage": {
            "name": "Whirlwind Bleed Barb",
            "description": "High-speed AOE build with bleed stacking",
            "difficulty": "Medium",
            "playstyle": "Aggressive melee",
            "key_skills": ["Whirlwind", "Bleed", "War Cry"],
            "legendary_items": [
                "Andariel's Visage",
                "Ancestral Chains",
                "Oblivion's Edge"
            ],
            "unique_items": ["Doedre's Despair"],
            "stats_priority": ["Crit Chance", "Bleed Damage", "Attack Speed"],
            "pros": ["High DPS", "Great AOE", "Fun playstyle"],
            "cons": ["Low survivability", "Melee range required"],
            "budget_friendly": True
        },
        "tank": {
            "name": "Immortal Shield Barb",
            "description": "Ultra-defensive build with shield mastery",
            "difficulty": "Easy",
            "playstyle": "Defensive tank",
            "key_skills": ["Shield Bash", "Threatening Shout", "Parry"],
            "legendary_items": [
                "Andariel's Visage",
                "Durability Shield",
                "Ancestral Chains"
            ],
            "unique_items": [],
            "stats_priority": ["Armor", "Resistances", "Life"],
            "pros": ["Very tanky", "Great crowd control", "Beginner friendly"],
            "cons": ["Lower DPS", "Slower clear"],
            "budget_friendly": True
        },
        "hybrid": {
            "name": "Upheaval Barb",
            "description": "Balanced damage and defense with Upheaval",
            "difficulty": "Medium",
            "playstyle": "Balanced fighter",
            "key_skills": ["Upheaval", "Shout", "Slam"],
            "legendary_items": [
                "Andariel's Visage",
                "Gravitational Surge",
                "Aspects of Might"
            ],
            "unique_items": [],
            "stats_priority": ["Damage", "Armor", "Life"],
            "pros": ["Balanced stats", "Flexible", "Solid all-rounder"],
            "cons": ["Jack of all trades, master of none"],
            "budget_friendly": False
        }
    },
    "sorceress": {
        "damage": {
            "name": "Frozen Orb Sorceress",
            "description": "Elemental AOE damage with freeze crowd control",
            "difficulty": "Medium",
            "playstyle": "Ranged caster",
            "key_skills": ["Frozen Orb", "Ice Shards", "Frost Nova"],
            "legendary_items": [
                "Tal Rasha's Tome",
                "Andariel's Visage",
                "Mathael's Might"
            ],
            "unique_items": ["Crescent Moon"],
            "stats_priority": ["Cold Damage", "Crit Chance", "Intelligence"],
            "pros": ["Great crowd control", "High damage", "Safe distance"],
            "cons": ["Resource management", "Cold immunity mobs"],
            "budget_friendly": False
        },
        "tank": {
            "name": "Ice Armor Sorceress",
            "description": "Defensive caster with barrier management",
            "difficulty": "Hard",
            "playstyle": "Defensive support",
            "key_skills": ["Ice Armor", "Teleport", "Frost Nova"],
            "legendary_items": [
                "Andariel's Visage",
                "Arcane Conduit",
                "Tal Rasha's Tome"
            ],
            "unique_items": [],
            "stats_priority": ["Barrier", "Resistances", "Intelligence"],
            "pros": ["Tanky for a sorceress", "Great survival"],
            "cons": ["Lower DPS", "Difficult playstyle"],
            "budget_friendly": False
        }
    },
    "necromancer": {
        "damage": {
            "name": "Blood Surge Necro",
            "description": "High single-target damage with blood magic",
            "difficulty": "Easy",
            "playstyle": "Ranged caster",
            "key_skills": ["Blood Surge", "Corpse Explosion", "Bone Prison"],
            "legendary_items": [
                "Uber Andariel's Visage",
                "Deathless Visage",
                "Bloodless Scream"
            ],
            "unique_items": ["Death's Embrace"],
            "stats_priority": ["Damage", "Life", "Essence"],
            "pros": ["Easy to play", "Great damage", "Resource efficient"],
            "cons": ["Limited crowd control", "Requires corpses"],
            "budget_friendly": True
        },
        "support": {
            "name": "Minion Master Necro",
            "description": "Summon-based build with army of undead",
            "difficulty": "Medium",
            "playstyle": "Summoner",
            "key_skills": ["Raise Skeleton", "Golem", "Command Undead"],
            "legendary_items": [
                "Andariel's Visage",
                "Viscious Blood Sigil",
                "Bloodless Scream"
            ],
            "unique_items": [],
            "stats_priority": ["Life", "Minion Damage", "Intelligence"],
            "pros": ["Lazy playstyle", "Great for AFK grinding", "Safe"],
            "cons": ["Lower personal DPS", "Minion AI limitations"],
            "budget_friendly": True
        }
    },
    "druid": {
        "damage": {
            "name": "Tornado Druid",
            "description": "Shapeshifting werewolf with tornado skills",
            "difficulty": "Medium",
            "playstyle": "Melee shapeshifter",
            "key_skills": ["Tornado", "Pulverize", "Maul"],
            "legendary_items": [
                "Andariel's Visage",
                "Ancestral Chains",
                "Storm Swell"
            ],
            "unique_items": [],
            "stats_priority": ["Attack Speed", "Damage", "Life"],
            "pros": ["High damage", "Great AOE", "Mobile"],
            "cons": ["Squishy", "Resource management"],
            "budget_friendly": False
        },
        "tank": {
            "name": "Earthen Bulwark Druid",
            "description": "Bear form with nature's defense",
            "difficulty": "Easy",
            "playstyle": "Defensive shapeshifter",
            "key_skills": ["Earthen Bulwark", "Landslide", "Ursine Strength"],
            "legendary_items": [
                "Andariel's Visage",
                "Durability Shield",
                "Stone Guard"
            ],
            "unique_items": [],
            "stats_priority": ["Armor", "Life", "Resistances"],
            "pros": ["Very tanky", "Easy to play", "Great sustain"],
            "cons": ["Lower damage", "Slow clear speed"],
            "budget_friendly": True
        }
    },
    "rogue": {
        "damage": {
            "name": "Poison Cutthroat Rogue",
            "description": "Dual wield poison expertise damage",
            "difficulty": "Hard",
            "playstyle": "Aggressive melee",
            "key_skills": ["Poison Imbuement", "Dual Wield", "Shadow Clone"],
            "legendary_items": [
                "Andariel's Visage",
                "Ancestral Chains",
                "Shadow Blight"
            ],
            "unique_items": ["Doedre's Despair"],
            "stats_priority": ["Poison Damage", "Crit Chance", "Attack Speed"],
            "pros": ["High single-target DPS", "Great evasion", "Fun"],
            "cons": ["Squishy", "Requires good gear", "Complex rotation"],
            "budget_friendly": False
        },
        "support": {
            "name": "Shadow Assassin Rogue",
            "description": "Stealth and burst damage",
            "difficulty": "Hard",
            "playstyle": "Hit and run",
            "key_skills": ["Shadow Clone", "Death Trap", "Smoke Grenade"],
            "legendary_items": [
                "Andariel's Visage",
                "Shadow Blight",
                "Ancestral Chains"
            ],
            "unique_items": [],
            "stats_priority": ["Crit Damage", "Attack Speed", "Evasion"],
            "pros": ["Burst damage", "Safe playstyle", "High skill ceiling"],
            "cons": ["Squishy", "Gear dependent", "Hard to master"],
            "budget_friendly": False
        }
    }
}

GEAR_DATABASE = {
    "helmets": [
        "Andariel's Visage",
        "Crown of the Eternal Torment",
        "Harlot's Crown",
        "Oblivion's Visage"
    ],
    "armor": [
        "Armor of the Eternal Hunt",
        "Flickering Flame",
        "Aspect of the Void"
    ],
    "weapons": [
        "Ancestral Chains",
        "Oblivion's Edge",
        "Scythe of the Unbound",
        "Tyrael's Might"
    ],
    "accessories": [
        "Ring of Starless Skies",
        "Ring of Red Fury",
        "Amulet of the Withered Souls"
    ]
}

def get_build(class_name: str, playstyle: str) -> dict:
    """Retrieve a build from the knowledge base"""
    class_name = class_name.lower()
    playstyle = playstyle.lower()
    
    if class_name in BUILDS and playstyle in BUILDS[class_name]:
        return BUILDS[class_name][playstyle]
    return None

def get_all_builds_for_class(class_name: str) -> dict:
    """Get all available builds for a class"""
    class_name = class_name.lower()
    return BUILDS.get(class_name, {})

def search_builds(keyword: str) -> list:
    """Search builds by keyword"""
    results = []
    keyword = keyword.lower()
    
    for class_name, playstyles in BUILDS.items():
        for playstyle, build in playstyles.items():
            if keyword in build["name"].lower() or keyword in build["description"].lower():
                results.append({
                    "class": class_name,
                    "playstyle": playstyle,
                    "build": build
                })
    
    return results