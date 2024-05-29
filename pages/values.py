from random import randrange
from datetime import datetime, timedelta
import string
import random
from .db_page import BasePage
def get_date(date_start, date_end):
    d1 = datetime.strptime(date_start, '%d.%m.%Y')
    d2 = datetime.strptime(date_end, '%d.%m.%Y')
    delta = d2 - d1
    int_delta = delta.days
    random_date = d1 + timedelta(randrange(int_delta))
    return random_date

fis_id = '100167'
rs_id = 95884250
credi_id = 943670256
numbers7 = random.randrange(1000000, 9999999)
clRequestId = str(numbers7) + 'v' + 'fe34-11ee-8f3b-0a580a' + str(random.randrange(100000, 999999))
randomDate = get_date('01.01.1970', '01.12.2004')
others = random.randrange(100000, 999999)
iin = f"{randomDate.strftime('%y%m%d')}{others}"
way4_iin = 760821300239
gender_choice = random.choice(['Женский', 'Мужской'])
if gender_choice == 'Женский':
    fisGender = 'Женский'
    clGender = '2'
    wayGender = 'FEMALE'
else:
    fisGender = 'Мужской'
    clGender = '1'
    wayGender = 'MALE'
imja = ''.join(random.choices(string.ascii_uppercase, k=6))
familija = ''.join(random.choices(string.ascii_uppercase, k=8))
otchestvo = ''.join(random.choices(string.ascii_uppercase, k=10))
data_rozhdenija = randomDate.strftime('%Y-%m-%d')
prezhnjaja_familija = ''.join(random.choices(string.ascii_uppercase, k=10))
clientType = random.choice(['1', '2', '3', '5'])
phone = f"{random.choice(['700', '701', '702', '705', '747', '775'])}{numbers7}"
homePhone = f"{727}{numbers7}"
workPhone = f"{727}{numbers7}"
rezident = random.choice([True, False])
today = datetime.now()
fisObrazovanie = random.choice(['1', '2', '3', '4', '5', '6'])
slObrazovanie = random.choice(['2', '3', '5', '6', '7', '8'])
kodovoe_slovo = ''.join(random.choices(string.ascii_uppercase, k=6))
semejnoe_polozhenie_choice = random.choice(['1', '2', '3'])
numberOfChildren = random.randint(0, 5)
if semejnoe_polozhenie_choice == '1':
    fisSemejnoe_polozhenie = 'женат_замужем'
    clSemejnoe_polozhenie = 6
    numberOfFamilyMembers = str(numberOfChildren + 1)
elif semejnoe_polozhenie_choice == '2':
    fisSemejnoe_polozhenie = 'холост_не_замужем'
    clSemejnoe_polozhenie = 6
    numberOfFamilyMembers = str(numberOfChildren)
else:
    fisSemejnoe_polozhenie = 'разведен_разведена'
    clSemejnoe_polozhenie = 6
    numberOfFamilyMembers = str(numberOfChildren)
addressType = random.randint(1, 2)
strana = random.choice(['22', '44', '45', '46', '47', '48', '49', '5', '51', '83', '84', '86', '87', '88', '89', '9', '90'])
clCountryOfResidence = random.choice(['UZ', 'AZ', 'AF', 'TJ', 'KZ'])
way4Country = random.choice(['KAZ', 'KOR', 'RUS', 'SSD', 'LTU', 'GBR', 'TJK', 'ARG', 'AUS', 'TWN', 'CXR'])
if way4Country == 'KAZ':
    way4_IsResident = True
    way4_tip_dokumenta_choice = random.choice(['A', 'B', 'C'])
else:
    way4_IsResident = False
    way4_tip_dokumenta_choice = random.choice(['D', 'E', 'K'])
email = ''.join(random.choices(string.ascii_uppercase, k=10))
tip_dokumenta_choice = random.choice(['паспорт', 'паспорт'])
if tip_dokumenta_choice == 'удостоверение':
    fisTipDokumenta = '6'
    clTipDokumenta = 'ID_CARD'
    rsTipDokumenta = 8
else:
    fisTipDokumenta = '1'
    clTipDokumenta = 'PASSPORT'
    rsTipDokumenta = 8
paperseries = str(random.randint(100000, 999999))
client_id_list = BasePage().get_id(fis_id, fisTipDokumenta)
document_id = client_id_list['document_id']
nomer = str(random.randint(100000000, 999999999))
randomDocDate = get_date('01.01.2018', '01.05.2024')
data_vydachi = randomDocDate.strftime('%Y-%m-%d')
srok_dejstvija = randomDocDate + timedelta(days=365 * 10 + 2)
organ_vydachi = random.choice(['МЮ РК', 'МВД РК'])
if organ_vydachi == 'МЮ':
    fisOrganVydachi = '1'
    clOrganVydachi = '2'
    rsOrganVydachi = '2'
else:
    fisOrganVydachi = '2'
    clOrganVydachi = '1'
    rsOrganVydachi = '2'
reg_address_id = client_id_list['reg_address_id']
fact_address_id = client_id_list['fact_address_id']
nazvanie_regiona = random.choice(['Жетысуская область', 'Улытауская область', 'Алматинская область'])
if nazvanie_regiona == 'Жетысуская область':
    fisNazvanie_regiona = 'Жетысуская область'
    clNazvanie_regiona = 272850
    districtCode = 95
    rajon_oblasti = 'Коксуский'
    cityCode = 45324
    gorod = 'Ескелді Би'
    tip_ulicy = 'микрорайон'
    streetType = '1'
elif nazvanie_regiona == 'Улытауская область':
    fisNazvanie_regiona = 'Улытауская область'
    clNazvanie_regiona = 272851
    districtCode = 188
    rajon_oblasti = 'Сатпаев'
    cityCode = 84058
    gorod = 'г.Сатпаев'
    tip_ulicy = 'проспект'
    streetType = '2'
else:
    fisNazvanie_regiona = 'Алматинская область'
    clNazvanie_regiona = 205
    districtCode = 143
    rajon_oblasti = 'Талгарский'
    cityCode = 46424
    gorod = 'г.Талгар'
    tip_ulicy = 'улица'
    streetType = '5'
postalCode = random.randrange(110000, 119999)
sinceDate = get_date('01.01.2022', '01.05.2024')
typeOfResidence = random.randrange(1, 5)
ulica = ''.join(random.choices(string.ascii_uppercase, k=8))
nomer_doma = str(random.randrange(1, 541))
nomer_kvartiry = str(random.randrange(1, 241))
nazvanie_strany = random.choice(['Казахстан', 'Кыргызстан', 'Узбекстан', 'Турменистан', 'Таджикистан'])

contact_id = client_id_list['contact_id']
contact_person1_mphone = f"{708}{numbers7}"
contact_person1_hphone = f"{717}{numbers7}"
contact_person2_mphone = f"{777}{numbers7}"
contact_person2_hphone = f"{721}{numbers7}"
contact_person3_mphone = f"{707}{numbers7}"
contact_person3_hphone = f"{725}{numbers7}"
kontaktnoe_lico1 = ''.join(random.choices(string.ascii_uppercase, k=6))
kontaktnoe_lico2 = ''.join(random.choices(string.ascii_uppercase, k=6))
kontaktnoe_lico3 = ''.join(random.choices(string.ascii_uppercase, k=6))
tip_otnoshenija = random.choice(['1', '2', '3', '4', '5', '6'])
employment_id = client_id_list['employment_id']
rod_zanjatosti = str(random.randrange(1, 41))
bin_organizacii = str(random.randrange(100000000000, 999999999999))
sfera_dejatelnosti = str(random.randrange(12, 31))
naimenovanie_rabotodatelja = ''.join(random.choices(string.ascii_uppercase, k=10))
bankruptcyStatus = random.choice(['Bankrupt_10', 'Bankrupt_20', 'Bankrupt_50'])
employmentType = random.choice(['1', '2', '3'])
if employmentType == '1':
    activitySphere = 'O84'
    occupation = '25'
    economicSector = '2'
    contractType = '1'
elif employmentType == '2':
    activitySphere = 'B5'
    occupation = '14'
    economicSector = '7'
    contractType = '2'
else:
    activitySphere = 'S96'
    occupation = '23'
    economicSector = '6'
    contractType = '2'
a = 0


# print(type(familija))
# print(type(imja))
# print(type(otchestvo))
# print(type(nomer))
# print(type(organ_vydachi_choice))
# print(type(randomDocDate.strftime('%d.%m.%Y')))
# print(type(srok_dejstvija.strftime('%d.%m.%Y')))
# print(type(gorod))
# print(type(data_rozhdenija))
# print('values today ' + today.strftime('%m/%d/%Y'))
# print(type(wayGender))
# print(type(familija))
# print(type(imja))
# print(type(phone))
# print(type(kodovoe_slovo))
# print(type(gorod))
# print(type(nazvanie_regiona))
# print(type(rajon_oblasti))
# print(type(gorod))
# print(type(ulica))
# print(type(nomer_doma))
# print(type(nomer_kvartiry))



