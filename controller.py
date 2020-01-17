import random
from view import View

class Controller:
  global i, kuljepikkus
  i = 0
  kuljepikkus = 10
  def __init__(self):
    self.view = View()

    self.arvuti = [ [{'pomm': False, 'laev': False}, {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False} , {'pomm': False, 'laev': False}, {'pomm': False, 'laev': False},
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
    ]

    self.inimeselaevad = []



  def add_laev(self, pikkus):
    self.view.naitaruudustikku(self.inimene, self.arvuti)
    for i in range(pikkus):
      place = self.view.ask_place(i+1)
      x,y = self.get_indeces(place)
      self.inimene[x][y]['laev'] = True
    self.inimeselaevad.append(pikkus)
    self.view.naitaruudustikku(self.inimene, self.arvuti)

  def mine_mangu(self):
    # tee arvutile laevad
    self.genereeri_arvuti_laevad()
    # naita ruudustikku
    self.view.naitaruudustikku(self.inimene, self.arvuti)

    pommiruut = self.view.ask_pomm()
    x,y = self.get_indeces(pommiruut)
    self.arvuti[x][y]['pomm'] = True
    # if self.arvuti[x][y]['laev'] == True: # Kui oli laev, siis naita korvalolevaid laeva ruute
    #   self.uuri_umber(x,y)
    self.view.naitaruudustikku(self.inimene, self.arvuti)

  #def uuri_umber(self, x, y):


  def genereeri_arvuti_laevad(self):

      self.inimeselaevad.sort()
      self.inimeselaevad.reverse()

      for laev in self.inimeselaevad:
        punkt = [random.randint(0, kuljepikkus - 1), random.randint(0, kuljepikkus - 1)] # tootab ainult kui on uks laev!
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
              else:
                self.genereeri_arvuti_laevad()
            except IndexError:
              self.genereeri_arvuti_laevad()

            if counter == laev:
              for ruut in range(laev):
                self.arvuti[punkt[0]][punkt[1] + ruut]['laev'] = True
              counter += 1

        if suund == 1:
          for ruut in range(laev):
            try:
              if self.arvuti[punkt[0]+ruut][punkt[1]]['laev'] is False:
                counter += 1
              else:
                self.genereeri_arvuti_laevad()
            except IndexError:
              self.genereeri_arvuti_laevad()

            if counter == laev:
              for ruut in range(laev):
                print([punkt[0],punkt[1] + ruut])
                self.arvuti[punkt[0]][punkt[1] + ruut]['laev'] = True
              counter += 1




  def get_indeces(self,place):
    y = int(place[1])
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I']
    x = letters.index(place[0])
    return(x, y)


  def prindimolemad(self):
    self.view.ajutisedruudud(self.inimene, self.arvuti)










