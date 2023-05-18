class home:
    floors=10
    flats=100
    ent=2 #подъезды
    s=85 #средняя площадь
    ffes=(flats/ent)/floors
    la=flats*s #общая жилая площадь
    sh=1000 #площадь участка земли
    la_sh=la/sh
    def ffe (self):
        print("Квартир на этаже :", home.ffes)
    def living_area (self):
        print("Отношение жилой площади к площади дома :", home.la_sh)

class cottage(home):
    floors = 3
    room = 18
    s = 32  # средняя площадь комнат
    ffes = room / floors
    la = room * s  # общая жилая площадь
    sh = 600  # площадь участка земли
    la_sh = la / sh
    def ffe (self):
        print("Комнат на этаже :", cottage.ffes)
    def living_area (self):
        print("Отношение жилой площади к площади дома :", cottage.la_sh)

class skyscraper(cottage):
    floors = 40
    flats = 160
    s = 76  # средняя площадь квартир
    ffes = flats / floors
    la = flats * s  # общая жилая площадь
    sh = 900  # площадь участка земли
    la_sh = la / sh
    def ffe (self):
        print("Квартир на этаже :", skyscraper.ffes)
    def living_area (self):
        print("Отношение жилой площади к площади дома :", skyscraper.la_sh)

home_a=home()
print("Многоквартирный дом :")
home_a.ffe()
home_a.living_area()
print('\n')
cottage_a=cottage()
print("Коттедж :")
cottage_a.ffe()
cottage_a.living_area()
print('\n')
skyscraper_a=skyscraper()
print("Небоскреб :")
skyscraper_a.ffe()
skyscraper_a.living_area()
print('\n')
print("Разница между площадями домов")
if home.sh>cottage.sh:
    r1=home.sh-cottage.sh
    print("Многоквартирный дом и коттедж :", r1)
else:
    r1 = (home.sh - cottage.sh)*(-1)
    print("Многоквартирный дом и коттедж :", r1)

if cottage.sh>skyscraper.sh:
    r1=cottage.sh-skyscraper.sh
    print("Коттедж и небоскреб :", r1)
else:
    r1 = (cottage.sh - skyscraper.sh)*(-1)
    print("Коттедж и небоскреб :", r1)

if home.sh>skyscraper.sh:
    r1=home.sh-skyscraper.sh
    print("Многоквартирный дом и небоскреб :", r1)
else:
    r1 = (home.sh - skyscraper.sh)*(-1)
    print("Многоквартирный дом и небоскреб :", r1)


print('\n')
print("Dop")
class dop:
    classes=40
    people=880
    a=people/classes #сколько человек будет в одном классе
    def s (self,spot_in_class): #spot_in_class количество мест в классе
        if spot_in_class>=dop.a:
            print("Все поместятся в аудитории!")
        else:
            print("Не все поместятся в аудитории")
        print("Человек в одной аудитории :", dop.a)
dop_a=dop()
dop_a.s(22)
class dop2(dop):
    classes=40
    floors=4
    e=classes/floors #сколько аудиторий на одном этаже
    def p (self):
        print("Количество аудиторий на этаже :", dop2.e)
dop2_a=dop2()
dop2_a.p()