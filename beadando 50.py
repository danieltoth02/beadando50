n=int(input("Utszakasz hossza (km)= "))
m=int(input("Megengedett sebesseg (km/h)= "))
rendszam_lista=[]
sebesseg_lista=[]
while True:
    ir=input("Ido, rendszamtabla: ")
    if ir=="end":
        break
    ir2=ir.split(" ")
    ido1 = int(ir2[0]) * 3600 + int(ir2[1]) * 60 + int(ir2[2])
    ido2 = int(ir2[3]) * 3600 + int(ir2[4]) * 60 + int(ir2[5])
    idohossz=(ido2-ido1)/3600
    sebesseg=n/idohossz
    if sebesseg>m:
        sebesseg_lista.append(sebesseg)
        rendszam_lista.append(ir2[6])
