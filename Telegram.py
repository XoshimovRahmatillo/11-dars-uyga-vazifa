from abc import ABC, abstractmethod
import json
from datetime import datetime
import time
import random


class Telegram:
    def __init__(self, nomi):
        self.nomi = nomi
        self.xabarlar = ""
        self.yozishmalar_holati = "bo'sh"
        self.suhbat_vaqti = None

    def malumotlarni_korish(self):
        print(f"Foydalanuvchi ismi: {self.nomi}")
        print(f"Xabar matni: {self.xabarlar if self.xabarlar else 'Xabar yo\'q'}")
        print(f"Xabar holati: {self.yozishmalar_holati}")
        print(f"Xabar vaqti: {self.suhbat_vaqti if self.suhbat_vaqti else 'Vaqt kiritilmagan'}")
        print()

    def xabar_jonatish(self, qabul_qiluvchi, xabar):
        self.xabarlar = xabar
        qabul_qiluvchi.xabarlar = xabar
        self.suhbat_vaqti = datetime.now().strftime("%d-%b %H:%M:%S")
        qabul_qiluvchi.suhbat_vaqti = self.suhbat_vaqti
        self.yozishmalar_holati = "jo'natilmoqda"
        qabul_qiluvchi.yozishmalar_holati = "qabul qilindi"

    def yozishmalarni_oqish(self):
        if self.xabarlar:
            self.yozishmalar_holati = "o'qilyapti"
            print(f"{self.nomi} o'ziga kelgan xabarni o'qiyapti: '{self.xabarlar}'", datetime.now().strftime("%d-%b %H:%M:%S"))
        else:
            print(f"{self.nomi} uchun xabar yo'q.")

    def ochirish(self):
        if self.xabarlar:
            confirm = input(f"{self.nomi}, xabarni o'chirishni xohlaysizmi? (ha/yo'q): ").lower()
            if confirm == 'ha':
                print(f"{self.nomi} xabarni o'chirdi: '{self.xabarlar}'")
                self.xabarlar = ""
                self.yozishmalar_holati = "bo'sh"
            else:
                print(f"{self.nomi} xabarni o'chirish rad etildi.")
        else:
            print(f"{self.nomi} uchun o'chiriladigan xabar yo'q.")

    

    def kantakt_qidirish(self):
        contact_found = random.choice([True, False])
        if contact_found:
            contact_name = input("Kontakt nomini kiriting: ")
            return Telegram(contact_name)
        else:
            print("Kontakt topilmadi.")
            return None
        
    def __str__(self):
        return self.nomi
    
    def __repr__(self):
        return self.nomi


foydalanuvchi1 = Telegram(input("Ismingizni kiriting: "))

foydalanuvchi2 = foydalanuvchi1.kantakt_qidirish()

while True:
    print("1.Kontakt qidirish\n2. Kontaktga xabar yozish\n3.Kontaktni o'chirish\n4.Chiqish")
    tanla=int(input("Bu kontakt bilan qandey ish amalga oshirmoqchisiz?"))
    
    match tanla:
        case 1:
            k_name=input("Kontaktni kiriting: ")
            print(Telegram.kantakt_qidirish(k_name))
        case 2:
            foydalanuvchi1.xabar_jonatish(foydalanuvchi2, input("Yubormoqchi bo'lgan matningizni kiriting: "))
            foydalanuvchi2.yozishmalarni_oqish()
        case 3:
            k_name=input("Kontaktni kiriting: ")
            print(Telegram.ochirish(k_name))
        case 4:
            print("Xabar yuborish jarayoni tugadi, Telegramdan chqishingiz mumkin")
            break
