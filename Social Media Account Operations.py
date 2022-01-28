giris_bilgileri={"irem_c":"1234"}
isim=input("isim giriniz:")
if isim in giris_bilgileri.keys():
    a= input("şifre giriniz:")
    if a in giris_bilgileri.values():
        print("giriş başarılı")
        c= True
    else:
        print("giriş başarısız. şifre yanlış")
else:
    print("böyle bir kullanıcı adı bulunamadı.")

menü=("""
1-şifre değiştir
2-kullanıcı adı değiştir
3-hesabı sil
4-çıkış yap
""")

while c:
    print(menü)
    sec=input("seçenek giriniz")
    if sec=="1":
        yenisifre=str(input("yeni şifre giriniz"))
        giris_bilgileri['irem_c']=yenisifre
        print("yeni şifreniz",yenisifre,"olarak değiştirildi")
        print(giris_bilgileri)
    elif sec=="2":
        kullanıcıadı=str(input("yeni kullanıcı adı giriniz"))
        giris_bilgileri[kullanıcıadı]="1234"
        del giris_bilgileri["irem_c"]
        print("yeni kullanıcı adınız",kullanıcıadı,"olarak değiştirildi")
        print(giris_bilgileri)
    elif sec=="3":
        del giris_bilgileri
        print("hesabınız silindi")
    elif sec=="4":
        print("çıkış yapıldı")
        break
