import random
sayı = random.randrange(0,10)
tahmin = int(input("tahmininiz nedir?"))
sayaç=0

while sayaç < 2:
    if tahmin < sayı:
        sayaç += 1
        hak = 3 - sayaç
        print("daha büyük bir sayı tahim ediniz. Kalan hakkınız:", hak)
        tahmin = int(input("tahmininiz nedir?"))
    elif tahmin > sayı:
        sayaç += 1
        hak = 3 - sayaç
        print("daha küçük bir sayı tahim ediniz. Kalan hakkınız:", hak)
        tahmin = int(input("tahmininiz nedir?"))
    else:
        print("tebrikler")
print("oyun bitti!!!") 
print("doğru cevap:",sayı)
    
   