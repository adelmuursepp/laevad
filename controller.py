import random
from view import View

class Controller:
  global i, kuljepikkus
  i = 0 # laevad arv, kui palju inimene tahab panna
  kuljepikkus = 10
  def __init__(self):
    self.view = View()

    self.arvuti = []
    self.inimene = []

    for nr1 in range(kuljepikkus): # loob inimese ja arvuti mänguväljade ühe dimensiooni
      self.arvuti.append([])
      self.inimene.append([])

      for nr2 in range(kuljepikkus): # loob inimese ja arvuti mänguväljade teise dimensiooni
        self.arvuti[nr1].append({'pomm': False, 'laev': False})
        self.inimene[nr1].append({'pomm': False, 'laev': False})


    '''self.arvuti = [ [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}]
    ]

    self.inimene = [ [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}],
    [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
    {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}]
    ]'''

    self.inimeselaevad = []

    global i_tervedlaevad  # naitab, mitu ruutu inimese ruudustikus on kaetud tervete laevadega
    i_tervedlaevad = 0
    global a_tervedlaevad  # naitab, mitu ruutu arvuti ruudustikus on kaetud tervete laevadega
    a_tervedlaevad = 0

  def add_laev(self, pikkus):
    self.view.naitaruudustikku(self.inimene, self.arvuti)
    ruudud = []
    laevaerror = False
    for i in range(pikkus):
      if laevaerror == False:
        place = self.view.ask_place(i+1)
        x,y = self.get_indeces(place)


        pos1 = [x-1, y]
        pos2 = [x+1, y]
        pos3 = [x, y-1]
        pos4 = [x,  y+1]
        pos5 = [x-1, y-1]
        pos6 = [x+1,y+1]
        pos7 = [x+1, y-1]
        pos8 = [x-1,y+1]
        positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8] # korvalolevad laevad, mida peab kontrollima

        for pos in positions:
          try:
            if self.inimene[pos[0]][pos[1]]['laev'] == True:
              print('Palun vali teine laev')
              ruudud = []
              laevaerror = True
              break
          except:
            pass
        ruudud.append([x,y])
        if len(ruudud) == pikkus:
          print(ruudud)
          for ruuduke in ruudud:
            print('enne panemist list on', ruuduke[0])
            self.inimene[ruuduke[0]][ruuduke[1]]['laev'] = True
            i_tervedlaevad += 1




    self.inimeselaevad.append(pikkus)
    self.view.naitaruudustikku(self.inimene, self.arvuti)


  def mine_mangu(self):

    # tee arvutile laevad
    self.genereeri_arvuti_laevad()
    # naita ruudustikku
    self.view.naitaruudustikku(self.inimene, self.arvuti)
    mang_labi = False


    # inimene pommitab
    while mang_labi == False:
      self.inimenepommitab()
      if a_tervedlaevad == 0:
        mang_labi = True
      elif i_tervedlaevad == 0:
        mang_labi = True

    # if self.arvuti[x][y]['laev'] == True: # Kui oli laev, siis naita korvalolevaid laeva ruute
    #   self.uuri_umber(x,y)
      self.arvutipommitab()
      if a_tervedlaevad == 0:
        mang_labi = True
      elif i_tervedlaevad == 0:
        mang_labi = True

  #def uuri_umber(self, x, y):


  def genereeri_arvuti_laevad(self):

      self.inimeselaevad.sort()
      self.inimeselaevad.reverse()

      for laev in self.inimeselaevad:
        punkt = [random.randint(0, kuljepikkus - 1), random.randint(0, kuljepikkus - 1)]
        # oletame, et koordinaadid on [2; 3]

        suund = random.randint(0, 1)
        # suund = 0 => suund paremale
        # suund = 1 => suund alla
        counter = 1
        if suund == 0:
          for ruut in range(laev):
            try:
              if self.arvuti[punkt[0]][punkt[1] + ruut]['laev'] is False:
                counter += 1
              #else:
               # self.genereeri_arvuti_laevad()
            except IndexError:
              self.genereeri_arvuti_laevad()

          if counter == laev:
            for ruut in range(laev):
              self.arvuti[punkt[0]][punkt[1] + ruut]['laev'] = True
              a_tervedlaevad += 1
            counter += 1

        if suund == 1:
          for ruut in range(laev):
            try:
              if self.arvuti[punkt[0]+ruut][punkt[1]]['laev'] is False:
                counter += 1
              #else:

               # self.genereeri_arvuti_laevad()
            except IndexError:
              self.genereeri_arvuti_laevad()

          if counter == laev:
            for ruut in range(laev):
              print([punkt[0],punkt[1] + ruut])
              self.arvuti[punkt[0]][punkt[1] + ruut]['laev'] = True

            counter += 1

  def arvutipommitab(self):
      x =random.randint(0, kuljepikkus)
      y =random.randint(0, kuljepikkus)
      self.inimene[x][y]['pomm'] = True
      self.view.naitaruudustikku(self.inimene, self.arvuti)
      if self.arvuti[x][y]['laev'] == True:
        i_tervedlaevad -= 1

      if self.inimene[x][y]['laev'] == True:
        i_tervedlaevad -= 1
        pos1 = [max(0, x-1), y]
        pos2 = [min(10, x+1), y]
        pos3 = [x, max(0, y-1)]
        pos4 = [x, min(10, y+1)]
        positions = [pos1, pos2, pos3, pos4] # korvalolevad laevad, mida peab kontrollima

        for pos in positions:
          if self.inimene[pos[0]][pos[1]]['laev'] == False:
            self.inimene[pos[0]][pos[1]]['pomm'] = True

        pos5 = [max(0, x-1), max(0, y-1)]
        pos6 = [min(10, x+1), min(10, y+1)]
        pos7 = [min(10, x+1), max(0, y-1)]
        pos8 = [max(0, x-1), min(10, y+1)]

        positions2 = [pos5, pos6, pos7, pos8] # diagonaalis olevad laevad

        for pos in positions2:
          self.inimene[pos[0]][pos[1]]['pomm'] == True


      self.inimenepommitab()

  def inimenepommitab(self):
      pommiruut = self.view.ask_pomm()
      x,y = self.get_indeces(pommiruut)
      self.arvuti[x][y]['pomm'] = True
      self.view.naitaruudustikku(self.inimene, self.arvuti)

      if self.arvuti[x][y]['laev'] == True:
        a_tervedlaevad -= 1
        pos1 = [max(0, x-1), y]
        pos2 = [min(10, x+1), y]
        pos3 = [x, max(0, y-1)]
        pos4 = [x, min(10, y+1)]
        positions = [pos1, pos2, pos3, pos4] # korvalolevad laevad, mida peab kontrollima

        for pos in positions:
          if self.arvuti[pos[0]][pos[1]]['laev'] == False:
            self.arvuti[pos[0]][pos[1]]['pomm'] = True

        pos5 = [max(0, x-1), max(0, y-1)]
        pos6 = [min(10, x+1), min(10, y+1)]
        pos7 = [min(10, x+1), max(0, y-1)]
        pos8 = [max(0, x-1), min(10, y+1)]

        positions2 = [pos5, pos6, pos7, pos8] # diagonaalis olevad laevad

        for pos in positions2:
          self.arvuti[pos[0]][pos[1]]['pomm'] == True

      self.arvutipommitab()


  def get_indeces(self,place):
    y = int(place[1])-1
    print("y on", y)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    x = letters.index(place[0])
    print("x on", x)
    return(y,x)


  def prindimolemad(self):
    self.view.ajutisedruudud(self.inimene, self.arvuti)

