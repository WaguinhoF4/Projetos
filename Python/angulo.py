import math

angulo = float(input("Digite o Valor do Angulo: "))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(
    f"Angulo:{angulo}°, Seno:{seno:.2f}, Cosseno:{cosseno:.2f}, Tangente:{tangente:.2f}")
