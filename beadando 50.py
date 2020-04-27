n=int(input("Utszakasz hossza (km)= "))                                     #bekerjuk az utszakasz hosszat
m=int(input("Megengedett sebesseg (km/h)= "))                               #bekerjuk az engedelyezett sebesseget
rendszam_lista=[]                                                           #letrehozunk 2 ures listat a kesobbi ertekek tarolasara
sebesseg_lista=[]
while True:
    ir=input("Ido, rendszamtabla: ")                                        #bekerunk ket idopontot es egy rendszamtablat (6 jegy)
    if ir=="end":                                                           #"end" eseten a ciklus kilep
        break
    ir2=ir.split(" ")                                                       #az idopontot es rendszamot felosztjuk
    ido1 = int(ir2[0]) * 3600 + int(ir2[1]) * 60 + int(ir2[2])              #kiszamoljuk az elso idopontot (az utszakasz kezdese)
    ido2 = int(ir2[3]) * 3600 + int(ir2[4]) * 60 + int(ir2[5])              #kiszamoljuk a masodik idopontot (az utszakasz vege)
    idohossz=(ido2-ido1)/3600                                               #mennyi ido alatt hagyta el az adott utszakaszt
    sebesseg=n/idohossz                                                     #sebesseg kiszamolasa (utszakasz/ido)
    if sebesseg>m:                                                          #ha a sebesseg nagyobb mint a megengedett,
        sebesseg_lista.append(sebesseg)                                     #akkor listazzuk a sebesseget es rendszamot
        rendszam_lista.append(ir2[6])
for i in range (len(rendszam_lista)):                                       #bejarjuk valamelyik lista hosszat (egyenloek), es kiirjuk
    print (rendszam_lista[i],str(f'{sebesseg_lista[i]:.2f}')+"km/h")        #a szukseges rendszamokat & sebessegeket
