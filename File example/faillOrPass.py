with open("students.txt") as f:
    with open("passed.txt","w") as g:
        with open ("failed.txt","w") as k:
            icerik = f.readlines()
            m=0
            for satir in icerik :
                if m == 0:
                    m+=1
                    continue
                satir = satir.replace("\n" , "")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad)-1].replace("-"," ")
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                vize1 = int(notlar[0])
                vize2 = int(notlar[1])
                final = int(notlar[2])
                ortalama = vize1*0.3 + vize2*0.3 + final*0.4
                bolum = satir[bosluk_indexleri[0] + 1 : bosluk_indexleri[-1]]

                if ortalama >= 70 and final >=70:
                    g.write(ad)
                    g.write(" " * (25-len(ad)))
                    g.write(soyad)
                    g.write(" " * (25-len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25-len(bolum)))
                    g.write(str(round(ortalama,1)))
                    g.write(" " * 21)
                    g.write("Gecti")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (25-len(ad)))
                    k.write(soyad)
                    k.write(" " * (25-len(soyad)))
                    k.write(bolum)
                    k.write(" " * (25-len(bolum)))
                    k.write(str(round(ortalama,1)))
                    k.write(" " * 21)
                    k.write("Kaldi")
                    k.write("\n")