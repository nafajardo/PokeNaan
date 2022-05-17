# Author: Nicholas Fajardo

import random
from Utilities.Errors import IncorrectInput

# General Rarity (Cannot Evolve
class Rare:
    # Constructor (Creates the chain)
    # Chain | INT | Identifies the beginning chain (1/2)
    # Rarity | BOOL | Identifies if its rare or not
    def __init__(self, chain, rarity):
        
        # All PokeNaan are able to evolve from these base types
        self.EVOL_C1 = ("Undercooked", "Baked", "Burnt")
        self.EVOL_C2 = ("Frozen", "Baked", "Stale")
        # Baked PokeNaan can, very rarely, evolve to either of these
        self.RAREEVOL_C1 = ("Blessed", "Divine", "Holy")
        self.RAREEVOL_C2 = ("Cursed", "Possessed", "Evil")

        # Assign properties of rarity
        self.index = 0
        self.rarity = rarity
        self.chain = chain
        self.moldy = False

    def error_check(self, chain, rarity):
        if type(chain) != int or type(rarity) != bool:
            raise IncorrectInput("Wrong Input | Must be INT, BOOL")
        elif chain not in (1, 2):
            raise IncorrectInput("Wrong Input | Chain must be 1-2")
        else:
            return True

    def __str__(self):
        if self.rarity:
            return "RARITY DESC: \n" + "NAME: " + eval("self.RAREEVOL_C" + str(self.chain) + "[" + self.index + "]")
        else:
            return "RARITY DESC: \n" + "NAME: " + eval("self.EVOL_C" + str(self.chain) + "[" + self.index + "]")

# Rarity that has an Evolve Feature
class EvolRare(Rare):
    def __init__(self, chain, rarity):
        # If no errors in input
        if self.error_check(chain, rarity):
            # Create XP Pools for Chain
            self.c1_pool = 0.0
            self.c2_pool = 0.0
            self.rc1_pool = 0.0
            self.rc2_pool = 0.0

            # Create XP Pool Ceiling for Evolutions
            self.ceiling = 100.0
            self.ceiling_range = 5.0

    # Evolve considering its chain pool
    def evolve(self):
        # Check level for non-rare PokeNaan
        if self.index < 3 and not self.rarity:
            # If the C1 pool is in range of the ceiling AND C2 pool is in range of the ceiling
            if (self.c1_pool > self.ceiling + self.ceiling_range and
                    self.c2_pool > self.ceiling + self.ceiling_range):

                # Assign to a new chain randomly
                self.chain = random.randint(1, 2)

                # Reset pools
                self.reset_pools()

            elif (self.c1_pool in range(self.ceiling - self.ceiling_range, self.ceiling + self.ceiling_range) or
                    self.c2_pool in range(self.ceiling - self.ceiling_range, self.ceiling + self.ceiling_range)):

                # Reset pools
                self.reset_pools()
            pass
        # Level up Rare PokeNaan
        elif self.index < 3 and self.rarity:
            if self.rc1_pool >= self.ceiling:
                pass
            elif self.rc2_pool >= self.ceiling:
                pass
            pass
        # Change PokeNaan to Moldy State if its not in a moldy state
        elif not self.moldy:
            self.moldy = True
            self.index = self.index + 1

    # Reset XP Pools
    def reset_pools(self):
        self.c1_pool = 0.0
        self.c2_pool = 0.0
        self.rc1_pool = 0.0
        self.rc2_pool = 0.0

# General Move Format
class Move:
    # Constructor (Creates the move, atk or def)
    # Name | STR | Name of the move
    # Stat | INT | How much this deals/heals
    # Cost | INT | How many turn points this move costs
    # Rare | RARE | Rare class type
    def __init__(self, name, stat, cost, rare):
        # Asserting that the typed fed in are correct
        self.name = name
        self.stat = stat

    def error_check(self, name, stat, cost, rare):
        if type(name) != str or type(name) != int or type(cost) != int:
            raise IncorrectInput("Wrong Input | Must be STR, INT, INT")
        elif len(name) < 3 or not name.isalpha():
            raise IncorrectInput("Name must be at least three characters and only Alpha")
        elif stat < 1 or cost < 0:
            raise IncorrectInput("Stat must be >= 1, and cost must be >= 0")
        elif type(rare) != Rare:
            raise IncorrectInput("Rarity must be a rarity type")
        else:
            return True

    def __str__(self):
        return self.name + " | Damage: " + self.damage

# Attack Move
class Attack(Move):
    def __init__(self, name, damage, cost, atk_type):
        super(self, name, damage, cost)
        if type(atk_type) != str and type():
            self.type = type

# PokeNaan Class
class Pokenaan:
    def __init__(self, name, type, attacks):
        self.name = name
        self.type = type
        self.hp = 200
        self.deff = 50
        self.attacks = attacks

    def evolve(self):
        pass

    def attack(self):
        return self.hp / 2

    def block(self, damage):
        if damage > self.deff:
            self.hp = self.hp - damage + self.deff
            self.deff = 0
        else:
            self.deff = self.deff - damage

    def heal(self):
        pass

    def __str__(self):
        return self.name + " | type: " + self.type
        pass
