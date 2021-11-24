cena_mominsko_party = float(input())
number_love_letters = int(input())
number_vosuchni_rozi = int(input())
number_key_chain = int(input())
number_karikaturi = int(input())
number_kusmeti_iznenada = int(input())

love_letter = 0.6
vosuchna_roza = 7.2
key_chain = 3.6
karikatura = 18.2
kusmet_iznenada = 22

price_love_letters = number_love_letters * love_letter
price_vosuchni_rozi = number_vosuchni_rozi * vosuchna_roza
price_key_chain = number_key_chain * key_chain
price_karikatura = number_karikaturi * karikatura
price_kusmet_iznenada = number_kusmeti_iznenada * kusmet_iznenada
total_sum = price_love_letters + price_vosuchni_rozi + price_key_chain + price_karikatura + price_kusmet_iznenada

number_all_sold = number_love_letters + number_vosuchni_rozi + number_key_chain + number_karikaturi + number_kusmeti_iznenada

if number_all_sold >= 25:
    total_sum *= 0.65

hosting = total_sum * 0.9
difference = abs(hosting - cena_mominsko_party)


if hosting >= cena_mominsko_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
# else:
#     print(f"Not enough money! {left_over_abs} lv needed.")
#Yas. Killed it
