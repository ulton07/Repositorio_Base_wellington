primeiro_bimestre = float(input("Digte sua nota do primeiro bimestre : "))
segundo_bimestre = float(input("Digte sua nota do segundo bimestre : "))
terceiro_bimestre = float(input("Digte sua nota do terceiro bimestre : "))
quaro_bimestre = float(input("Digte sua nota do quarto bimestre : "))

media = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quaro_bimestre) /4

if media >= 7.0:
    print("aprovado")
elif media >= 5.0:
    print("recuperacao")
else:
    print("reprovado")