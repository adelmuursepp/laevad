class Router:
  def __init__(self, controller):
    self.controller = controller


  global running, laevad
  running = True
  laevad = 0

  def display_tasks(self):
    print("\n")
    print("Mida sa soovid jargmisena teha?")
    print("1- Lisada laev")
    print('2- Tee midagi muud')
    print('3- Lopeta mang')




  def route_action(self, action):
    if action == 1:
      self.controller.add_laev()
      print('Sa lisasid ruudu')
      print('Vajuta 1, kui soovid laevale lisada ruudu')
      print('Vajuta 2, kui ei soovi laevale ruutu lisada')
      veelruute = int(input())
      if veelruute == 1:
        self.route_action(1)

    elif action == 2:
      print('Sa tegid midagi muud')
    elif action == 3:
      print('Sa lopetasid mangu')
      running = False
      print(running)


  def run(self):
    print("Tere tulemast mangu")
    print('\n')
    while running:
      self.display_tasks()
      action = int(input())
      self.route_action(action)


