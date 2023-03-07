from time import sleep
from random import randint

class Hero():
    def __init__(self,name,health,armor,power,weapon,gold,mastery,charm,spirit_armor,block):
        self.name = name
        self.health = health
        self.armor = armor 
        self.power = power 
        self.weapon = weapon
        self.gold = gold
        self.mastery = mastery
        self.charm = charm
        self.spirit_armor = spirit_armor
        self.block = block
        
    
    def print_info(self):
        print('\n')
        print('Статистика:', self.name)
        print('Уровень здоровья:',self.health)
        print('Броня:',self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print('Монет:', self.gold)
        print('Мастерство:',self.mastery)
        print('Амулет:', self.charm)

    def random_events(self):
        event_score = 0
        while event_score != 6:
            while event_score != 2:
                first_random = randint(1,2)
                if first_random == 1 and knight.health > 0:
                    print('\nНа своей дороге вы встретили вора. Он не боится вас, и кажется идет прямо на вас!')
                    thief.print_info()
                    sleep(5)
                    knight.fight(thief)
                    sleep(5)
                elif first_random == 2 and knight.health > 0:
                    knight.get_item()
                    sleep(3)
                    knight.print_info()
                event_score += 1
            if knight.health > 0:
                print('\nПуть к пещере лежит через лес, где правит лишь магия!')
                sleep(3)
                knight.forest_shop()
                knight.print_info()
                while event_score != 4:
                    sleep(3)
                    second_random = randint(1,2)
                    if second_random == 1:
                        print('\nВы только посмотрите на это дерево! Какое оно могущественное! Так оно еще умеет говорить и выращивать колья из своих веток! Стоп... О нет')
                        knight.fight_miniboss(spirit_forest)
                        if knight.health <=0:
                            break
                        else:
                            print('\nВы одержали победу! Идем дальше!')
                            knight.print_info()
                            sleep(5)
                    elif second_random == 2:
                        print('Вы встретили колдуна! Кажется, он не очень рад вас видеть')
                        sleep(3)
                        knight.fight_wizard(water_wizzard)
                        if knight.health <= 0:
                            break
                        else:
                            knight.print_info()
                            sleep(5)
                    event_score += 1
            elif knight.health > 0:
                print('Вы прошли через лес и вошли в пещеру! Вы как никогда близки к победе!')
                sleep(3)
                knight.cave_shop()
                knight.print_info()
                sleep(3)
                while event_score != 6:
                    third_random = randint(1,2)
                    if third_random == 1:
                        knight.fight_wizard(fire_wizzard)
                        if knight.health <= 0:
                            break
                        else:
                            print('Огненный маг убит, а дракон нет. Надо исправлять')
                    if third_random == 2:
                        knight.fight_miniboss(stone_golem)
                    event_score += 1
                knight.cave_shop()
            elif knight.health > 0:
                knight.fight_boss(dragon)
            else:
                break


    def attack(self,enemy):
        double_damage = randint(1,3)
        if self.block < 1:
            if self.mastery >= 2:
                attack_choose = int(input('Какую атаку использовать?\n 1. Оглушающую \n 2.Обычную'))
                if attack_choose == 1:
                    special_attack = randint(1,2)
                    if special_attack == 1:
                        print(self.name + ' спецальную атаку: Оглушение! '+ enemy.name +'не смог уклониться от неё и не сможет провести атаку!')
                        enemy.block += 1
                        enemy.armor -= self.power
                    if enemy.armor <= 0:
                        enemy.health += enemy.armor
                        enemy.armor = 0
                    if enemy.health > 0:
                        print(enemy.name + ' выдержал удар, оставшись с '+ str(enemy.armor) + ' бронёй и '+ str(enemy.health) + ' здоровья')
            if self.mastery < 2 or attack_choose == 2:
                if double_damage == 3:
                    print(self.name + ' нанёс удар по ' + enemy.name + ' с силой ' + str(self.power * 2) +' используя ' + self.weapon+'\n')
                else:
                    print(self.name + ' нанёс удар по ' + enemy.name + ' с силой ' + str(self.power) +' используя ' + self.weapon+'\n')   
                if double_damage == 3:
                    enemy.armor -= self.power * 2
                elif double_damage == 2 or double_damage == 1:
                    enemy.armor -= self.power
                if enemy.armor <= 0:
                    enemy.health += enemy.armor
                    enemy.armor = 0
                if enemy.health > 0:
                    print(enemy.name + ' выдержал удар, оставшись с '+ str(enemy.armor) + ' бронёй и '+ str(enemy.health) + ' здоровья')
        else:
            self.block = self.block - 1


    def fight(self,enemy):
        while self.health and enemy.health > 0:
            self.attack(enemy)
            if enemy.health <= 0:
                print(enemy.name, ' умер в этом бою!\n')
                get_gold = randint(75,100)
                knight.gold += get_gold
                thief.health = 20
                thief.armor = 10
                knight.health += 10
                knight.mastery += 1
                break
            sleep(5)

            enemy.attack(self)
            if self.health <= 0:
                print(self.name,' умер в этом бою!\n')
                break
            sleep(5)

    def forest_shop(self):
        print('Вы нашли магазин гномов! Они нашли не мало хороших вещей.')
        shop = int(input('У них в ассортименте: 1.Меч из корней криста(24 урона)- 100 монет, 2.Броня из криптонила(30 брони, весь физический урон уменьшен в 1,25) - 120 монет,3.Амулет везения(из врагов выпадает как можно больше золота) - 150 монет. 4.Амулет "Вампиризм"(При использовании его, урон нанесённый вами, прибавется к вашему УЗ)- 175 монет 5.Уйти Ваши монеты:'+str(self.gold)))
        while shop != 5: 
            if shop == 1:
                knight.power = 24
                knight.gold = knight.gold - 100
            elif shop == 2:
                knight.armor = 30
                knight.gold = knight.gold - 120
            elif shop == 3:
                self.charm = 'Везение'
                knight.gold = knight.gold - 150 
            elif shop == 4:
                self.charm = 'Вампиризм'
                knight.gold = knight.gold - 175
            knight.print_info()
            shop = int(input('У них в ассортименте: 1.Меч из корней криста(24 урона)- 100 монет, 2.Броня из криптонила(30 брони, весь физический урон уменьшен в 1,25) - 120 монет,3.Амулет везения(из врагов выпадает как можно больше золота) - 150 монет. 4.Амулет "Вампиризм"(При использовании его, урон нанесённый вами, прибавется к вашему УЗ)- 175 монет 5.Уйти Ваши монеты:',str(self.gold)+')'))

    def fight_wizard(self,enemy):
        while self.health and enemy.health > 0:
            enemy.special()
            if self.health <= 0:
                print(self.name,' умер в этом бою!\n')
                break
            self.attack(enemy)
            if enemy.health <= 0:
                print(enemy.name, ' умер в этом бою!\n')
                if self.charm != 'Везение':
                    get_gold = randint(100,150)
                else:
                    get_gold = 150
                knight.gold += get_gold
                water_wizzard.health = 30
                water_wizzard.armor = 10
                fire_wizzard.health = 40
                fire_wizzard.armor = 15
                knight.health += 30
                knight.mastery += 1
                break
            sleep(5)

            enemy.attack(self)
            if self.health <= 0:
                print(self.name,' умер в этом бою!\n')
                break
            sleep(5)

    def special(self):
        special_bot = randint(1,2)
        if self.name == 'Водяной колдун':
            if special_bot == 1:
                water_wizzard.armor += 10
                print('Колдун использовал водяной пузырь! Его броня увеличалась до'+ str(self.armor))
            else:
                water_wizzard.power = 30
                miss_water = randint(1,8)
                if miss_water == 8:
                    knight.armor = 0
                    knight.health = 0
                    print('Колдун использовал волну и попал по вам! Волна была слишком сильная, чтоб устоять и вы умерли')
                elif miss_water <= 3:
                    knight.armor = knight.health - water_wizzard.power/2
                    if knight.armor <= 0:
                        knight.health += enemy.armor
                        knight.armor = 0
                    print('Колдун использовал волну и задел вас! Теперь у вас '+str(knight.armor)+' брони и '+ str(knight.health)+' УЗ')
                else:
                    print('Колдун использовал волну и не попал по вам!')
        elif self.name == 'Огненный маг':
            if special_bot == 1:
                fire_wizzard += 15
                print('Маг использовал магмовый ... гиберболоид? При этом в составе магмы был... тетрогидроксоцинкат натрия??? Такие слова сломали вам голову, а противнику увеличили броню до '+str(fire_wizzard))
            else:
                buff_damage =  randint(2,4)
                fire_wizzard.power += buff_damage
                print('Маг увеличил свой урон до'+str(fire_wizzard.power))
        elif self.name == 'Дух леса':
            if special_bot == 1:
                for i in range(4):
                    quick_attack = randint(4,6)
                    knight.armor = knight.armor - quick_attack
                    if knight.armor <= 0:
                        knight.health += enemy.armor
                        knight.armor = 0
                    print('Древо использовало 4 быстрых удара! Теперь у вас'+str(knight.armor)+' брони и '+str(knight.health))
            else:
                knight.block = 1
                print('Древо взяло вас корнями и вы не можете нанести удар')                



    def get_item(self):
        random_item = randint(1,4)
        if random_item == 1:
            print('Пока вы шли по дороге, вас заинтересовал какая-то броня...\n')
            print('Это призрачная броня!(Броня:10; Весь не физический урон уменьшен в полтора раза)')
            knight.spirit_armor = int(input('Одеть броню?\n 1.Да \n 2.Нет'))
            if knight.spirit_armor == 1:
                knight.armor = 10
        elif random_item == 2:
            print('Вы встретили пустую повозку, где находится 100 монет!')
            knight.gold += 100
        elif random_item == 3:
            print('Вас утомила жажда, как вдруг вы видите колодец! Может испеть водички?')
            decide = int(input('1.Да 2.Нет'))
            poison_water = randint(1,2)
            if decide == 1:
                if poison_water == 1:
                    print('Вам не хорошо...(Вы теряете 10 УЗ)')
                    knight.health = knight.health - 10
                else:
                    print('Вкуснятина! Вам очень хорошо и вы готовы продолжать путешествие!(Вы получили 10 УЗ)')
                    knight.health += 10
        elif random_item == 4:
            print('Вы встретили мастера по боевке с мечом! Он обучивал вас разными приёмами')
            knight.mastery += 1

print('Ваше приключение начинается. Будьте готовы сражаться как никогда! Ведь это будет сложное, но легендарное сражение зла и добра. О вас будут слогать легенды и петь песни!\n')
sleep(8)

knight = Hero('Безымянный рыцарь',50,25,15,'меч',0,0,'-',0,0)
knight.print_info()

thief = Hero('Вор',20,10,10,'кинжал','?',0,'-',0,0)

water_wizzard = Hero('Водяной колдун',30,10,18,'посох','?',0,'-',0,0)

fire_wizzard = Hero('Огненный маг',40,15,24,'посох','?',0,'-',0,0)

spirit_forest = Hero('Дух леса',80,0,20,'ветви и корни','?',0,'-',0,0)

stone_golem = Hero('Голем',5,100,30,'валуны','?',0,'-',0,0)

knight.random_events()
