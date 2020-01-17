from view import View

class Controller:
  global i
  i = 0

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



  def add_laev(self):
    global i
    place = self.view.ask_place(i)
    i += 1
    x,y = self.get_indeces(place)
    self.inimene[x][y]['laev'] = True




  def get_indeces(self,place):
    y = int(place[1])
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'I']
    x = letters.index(place[0])
    return(x, y)











