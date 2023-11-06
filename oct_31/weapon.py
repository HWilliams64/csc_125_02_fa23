class Weapon:
    game_id = 1

    def __init__(self, name, range, action, accuracy, ammo, capacity, weight, length, height, rate):
        self.name = name
        self.range = range
        self.action = action
        self.accuracy = accuracy
        self.weight = weight
        self.length = length
        self.height = height
        self.ammo = ammo
        self.capacity = capacity
        self.rate = rate

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def act(self) -> bool:
        # if the weapon uses ammo
        if self.ammo is not None:
            # if the weapon has ammo left
            if self.ammo > 0:
                self.ammo -= 1
                return True
            else:
                # The weapon has no ammo left we cannot use it
                return False
        else:
            # The weapon does not use ammo so we can use it
            return True

    def reload(self, new_ammo):
        new_ammo = min(self.ammo + new_ammo, self.capacity)
        self.ammo = new_ammo



# knife = Weapon(name="knife", range=24, action="stab", accuracy=1,
#                ammo=None, weight=.5, length=6, height=.5, rate=1)

hand_gun = Weapon(name="Hand Gun", range=50*12, action="shoot", accuracy=.7,
               ammo=16, capacity=16, weight=1, length=6, height=1, rate=1)


print(f"hand_gun game id: {hand_gun.game_id} name: {hand_gun.get_name()}")

for _ in range(18):
    print(f"Use {hand_gun.get_name()} result of usage: {hand_gun.act()}")
hand_gun.reload(4)
print("==== relaod ====")
for _ in range(18):
    print(f"Use {hand_gun.get_name()} result of usage: {hand_gun.act()}")
