from main import Hero


class Medic(Hero):
    def __init__(self, name, health, hill, mana):
        super().__init__(name, health)
        self.hill = hill
        self.mana = mana

    def hilling(self):
        self.health += self.hill
        return f'New health: {self.health}'

    def action(self):
        a = super().action()
        b = self.hilling()
        return a, b

    def minus_mana(self):
        self.mana -= 15
        return self.mana

medic = Medic('Алиса', 100, 20, 100)

print(medic.action())
print(medic.hilling())
print(medic.rest())
print(medic.introduce())
print(medic.minus_mana())




































