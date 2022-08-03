pecaum = input().split(" ")

pecadois = input().split(" ")

idpecaum, qtdpecaum, valorpecaum = pecaum

idpecadois, qtdpecadois, valorpecadois = pecadois

total = (int(qtdpecaum)*float(valorpecaum)) + (int(qtdpecadois)*float(valorpecadois))

print(f'VALOR A PAGAR: R$ {total:.2f}')