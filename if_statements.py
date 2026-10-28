# geeft 3 cijfers voor verschilende vaken
cijferVak1 = 4
cijferVak2 = 4
cijferVak3 = 10

# gemidelde cijger van de drie vakkwn berekenen
gemideldeCijfer = (cijferVak1 + cijferVak2 + cijferVak3) / 3

#controleerd of geen een cijfer lager is dan een vier en als dat waar is print 'Gezakt!'
if cijferVak1 < 4 or cijferVak2 < 4 or cijferVak3 < 4:
    print("Gezakt!")
#kijkr oh het gemidelde hoger of gelijk is aan een 5.5 en als dat waar is print 'Geslaagd!'
elif gemideldeCijfer >= 5.5:
    print("Geslaagd!")
#als bijde if statements niet waar zijn print hij 'gezakt' omdat het gemedelde cijfer lager is dan een 5.5
else:
    print("Gezakt!")