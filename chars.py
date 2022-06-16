import random

mage = {
  "Hp": 75,
  "Atk": 2,
  "True_Atk": 15,
  "Def": 10,
  "Mana": 15,
  "Mana_Potions": 5
  
}
knight = {
  "Hp": 95,
  "Atk": 25,
  "True_Atk": 0,
  "Def": 15,
  "Health_Potions": 5
}
tank = {
  "Hp": 125,
  "Atk": 10,
  "True_Atk": 0,
  "Def": 30,
  "Mana": 0,
  "Shield_Uses": 5
  
}
class enemy:
  def name():
    return "mage"

def check_if_par(self):
    if (self % 2) == 0:
      return True
      
class mage:
  def fireball(enemy):
    mage["Mana"] = mage["Mana"]-random.randint(3)
    placeholder_1=mage["Mana"]
    
    atk = random.randint(4,6) + mage["True_Atk"]
    print(f"You make a fireball out of thin air and yeet it at your opponent, dealing {atk}")
    print(f"You have {placeholder_1} left")
    return atk
    
  def heal():
    if mage["Hp"] > 75:
      extra_hp = mage["Hp"] = mage["Hp"] + (random.randint(6,12)  % random.randint(69,80))
    else: 
      extra_hp = mage["Hp"] = mage["Hp"] + (random.randint(5,7)  % random.randint(69,80))
    print(f"You cast yourself a healing spell, getting {extra_hp} more hp")
    
  def study():
    placeholder_1 = mage["True_Atk"]
    mage["True_Atk"] = random.randint(2,6) + mage["True_Atk"]
    Tru_Atacc = mage["True_Atk"] - placeholder_1
    print(f"You study dark arts, your True Damage increases by {Tru_Atacc}")
    
  def punch():
    atk = mage["Atk"]
    print(f"You hit your opponent with your flimsy arms, dealing {atk}")
    return atk
  def mana_potion():
    #only if your mana is 0
    mage["Mana_Potion"] = mage["Mana_Potion"] - 1
    mage["Mana"] = mage["Mana"] + 6


      
class knight:
  def stab():
    atk = random.randint(3,5) + knight["Atk"]
    print(f"You stab your opponent with your sword, dealing {atk}")
    return atk
    
  def heal():
    if knight[Health_Potions] == 0: 
      print("You don't have any health potions left")
    else:
      if knight["Hp"] > 95:
        extra_hp = knight["Hp"] = knight["Hp"] + (random.randint(5,8) % random.randint(80,100))
      else: 
        extra_hp = knight["Hp"] = knight["Hp"] + (random.randint(2,6) % random.randint(80,100))
      knight[Health_Potions] = knight[Health_Potions] - 1
      print(f"You drink a health potion, recovering {extra_hp} Hp")
      print(f"Potions left: {knight[Health_Potions]}")
    
  def atk_up():
    knight["Atk"] = random.randint(3,5) + knight["Atk"]
    Atk = knight["Atk"]
    print(f"You sharpen your blade, your attack increases to {Atk}")
    
  def berserk():
    knight["Hp"] = knight["Hp"] - (random.randint(30, 50) % 95)
    atk = knight["Atk"]*2
    print(f"You go Guts mode, dealing a whopping {atk}")
    return atk  