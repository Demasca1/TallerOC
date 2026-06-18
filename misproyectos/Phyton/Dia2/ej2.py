notas=[8,9,7,10,6]
vueltas=0
prom=0
for suma in notas:   
    prom=suma+prom
    vueltas=vueltas+1
promfinal=prom/vueltas
print(f"Su promedio es:{promfinal}")