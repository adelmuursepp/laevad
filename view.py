class View:

  def ask_place(object, i):
    print(f'Vali {i} laeva ruut (nt. A4)')
    print('>>')
    return input()

  global tahestik
  tahestik = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


  def naitaruudustikku(self, inimene, arvuti):
    # "." tähendab tühja teadmata ruutu
    # "x" tähendab põhja laskmata laeva
    # "X" tähendab põhja lastud ruutu
    # "*" mööda lastud ruutu
    # --> tähed A, B, C, ...
    # ülevalt alla numbrid 1, 2, 3, ...
    kuva1 = ''
    suurimarv = str(len(inimene) + 1)  # näitab suurima kohanumbriga rea numbrit

    kuva1 += ' ' * (len(suurimarv) + 1)

    for taht in range(len(inimene)): # teeb ülemisele reale tähed
      kuva1 += tahestik[taht % len(tahestik)] + ' '
    kuva1 += '\n'
    kuva1.strip()
    for rida in range(len(inimene)):
      kuva1 += ' ' * (len(suurimarv) - len(str(rida + 1))) + str(rida + 1) + ' '  # loob vasakule poole numbritest tulba

      for ruut in inimene[rida]:
        if ruut['pomm'] is False:
          if ruut['laev'] is False:
            kuva1 += '. '
          else:
            kuva1 += 'x '
        else:
          if ruut['laev'] is False:
            kuva1 += '* '
          else:
            kuva1 += 'X '
      kuva1.strip()
      kuva1 += '\n'

    kuva2 = ''
    suurimarv = str(len(arvuti) + 1)  # näitab suurima kohanumbriga rea numbrit

    kuva2 += ' ' * (len(suurimarv))
    for taht in range(len(arvuti)):  # teeb ülemisele reale tähed
      kuva2 += tahestik[taht % len(tahestik)] + ' '
    kuva2 += '\n'
    kuva2.strip()

    for rida in range(len(arvuti)):
      kuva2 += ' ' * (len(suurimarv) - len(str(rida + 1))) + str(rida + 1) + ' '  # loob vasakule poole numbritest tulba
      for ruut in arvuti[rida]:
        if ruut['pomm'] is False:
          if ruut['laev'] is False:
            kuva2 += '. '
          else:
            kuva2 += '. '
        else:
          if ruut['laev'] is False:
            kuva2 += '* '
          else:
            kuva2 += 'X '

      kuva2.strip()
      kuva2 += '\n'

    print("Inimene: \n", kuva1, "Arvuti: \n", kuva2)

  def ask_pomm(self):
      print(f'Vali ruut, mida soovid pommitada (nt. A4)')
      print('>>')
      return input()


  def ajutisedruudud(self, inimene, arvuti):
        # "." tähendab tühja teadmata ruutu
        # "x" tähendab põhja laskmata laeva
        # "X" tähendab põhja lastud ruutu
        # "*" mööda lastud ruutu
        # --> tähed A, B, C, ...
        # ülevalt alla numbrid 1, 2, 3, ...
        print('inimene')
        kuva1 = ''
        suurimarv = str(len(inimene) + 1)  # näitab suurima kohanumbriga rea numbrit

        kuva1 += ' ' * (len(suurimarv) + 1)

        for taht in range(len(inimene)):  # teeb ülemisele reale tähed
          kuva1 += tahestik[taht % len(tahestik)] + ' '
        kuva1 += '\n'
        kuva1.strip()
        for rida in range(len(inimene)):
          kuva1 += ' ' * (len(suurimarv) - len(str(rida + 1))) + str(
            rida + 1) + ' '  # loob vasakule poole numbritest tulba

          for ruut in inimene[rida]:
            if ruut['pomm'] is False:
              if ruut['laev'] is False:
                kuva1 += '. '
              else:
                kuva1 += 'x '
            else:
              if ruut['laev'] is False:
                kuva1 += '* '
              else:
                kuva1 += 'X '
          kuva1.strip()
          kuva1 += '\n'

        print('\n')

        # siit algab arvuti ruudustiku loomine
        print('arvuti ')

        kuva2 = ''
        suurimarv = str(len(arvuti) + 1)  # näitab suurima kohanumbriga rea numbrit

        kuva2 += ' ' * (len(suurimarv))
        for taht in range(len(arvuti)):  # teeb ülemisele reale tähed
          kuva2 += tahestik[taht % len(tahestik)] + ' '
        kuva2 += '\n'
        kuva2.strip()

        for rida in range(len(arvuti)):
          kuva2 += ' ' * (len(suurimarv) - len(str(rida + 1))) + str(
            rida + 1) + ' '  # loob vasakule poole numbritest tulba
          for ruut in arvuti[rida]:
            if ruut['pomm'] is False:
              if ruut['laev'] is False:
                kuva2 += '. '
              else:
                kuva2 += 'x '
            else:
              if ruut['laev'] is False:
                kuva2 += '* '
              else:
                kuva2 += 'X '

          kuva2.strip()
          kuva2 += '\n'

        print("inimene\n",kuva1,"arvuti\n", kuva2)

