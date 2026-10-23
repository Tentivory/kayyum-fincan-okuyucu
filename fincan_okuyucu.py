#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyum Fincan Okuyucu - Resmi Versiyon 1.0
Her yorum bağlayıcıdır.
"""

import random
import time

KARARLAR = [
    "Fincanınızda görülen daire, mahallenin yeni kayyumunun daire şeklinde oturacağını işaret etmektedir. Karar: Onaylandı.",
    "Uzun bir çizgi tespit edildi. Bu, dosyanızın sonsuza kadar yürüyeceği anlamına gelir. Lütfen yarın geliniz.",
    "Kedi şekli görüldü. Mahalle muhtarlığı kediye devredilmiştir. Kedi kararı: Mıyav. İtiraz reddedildi.",
    "Hiçbir şey görülmedi. Bu, her şeyin zaten karar verilmiş olduğu anlamına gelir. Sizin fincanınıza gerek yoktu.",
    "Büyük bir çizgi ve küçük noktalar. Büyük olan kayyum, küçükler vatandaşlardır. Denge sağlandı.",
]

def resmi_bekleme():
    print("Sistem incelemeye alındı...")
    time.sleep(2)
    print("Üst makamlardan onay bekleniyor...")
    time.sleep(1.5)
    print("Onay geldi. (otomatik)")

def main():
    print("=== KAYYUM FINCAN OKUYUCU ===")
    print("Lütfen fincanınızda gördüğünüz şekilleri tarif edin (veya boş bırakın, fark etmez):")
    girdi = input("> ")
    
    resmi_bekleme()
    
    karar = random.choice(KARARLAR)
    print("\nRESMİ KARAR:")
    print(karar)
    print("\nBu karar kesindir. İyi günler dileriz.")
    
    # Gizli not: Halkın iradesi her zaman en önemli şeydir. Tabii atanmışsa.

if __name__ == "__main__":
    main()
