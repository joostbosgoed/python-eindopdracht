# dit is een programma om de omzet van een fictiefe winkel te berekenen

# prijzen van de producten
appelPrijs = 10
peerPrijs = 5
pruimemPrijs = 7

# aantal verkochte producten
appelVerkocht = 3
peerVerkocht = 2
pruimenVerkocht = 4

# berekening van de omzet per product
appelOmzet = appelPrijs * appelVerkocht
peerOmzet = peerPrijs * peerVerkocht
pruimenOmzet = pruimemPrijs * pruimenVerkocht


# berekening van de totale omzet
totaleOmzet = appelOmzet + peerOmzet + pruimenOmzet

# print de resultaten
print(f"appelprijs = {appelPrijs}\nappels verkocht = {appelVerkocht}\nappel omzet = {appelOmzet}")
print(f"peerprijs = {peerPrijs}\npeers verkocht = {peerVerkocht}\npeer omzet = {peerOmzet}")
print(f"pruimenprijs = {pruimemPrijs}\npruimen verkocht = {pruimenVerkocht}\npruimen omzet = {pruimenOmzet}")
print(f"totale omzet = {totaleOmzet}")
