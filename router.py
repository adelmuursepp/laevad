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
    print('2- Mine mangu')
    print('3- Lopeta mang')
    print('9- prindi molemad ruudustikud')




  def route_action(self, action):
    if action == 1:
      print('Kui pikka laeva sa soovid lisada?')
      pikkus = int(input())
      self.controller.add_laev(pikkus)

    elif action == 2:
      print('Sa tegid midagi muud')
      self.controller.mine_mangu()
    elif action == 3:
      print('Sa lopetasid mangu')
      running = False
      print(running)
    elif action == 9:
      self.controller.prindimolemad()


  def run(self):
    print("Tere tulemast mangu")
    print('\n')
    while running:
      self.display_tasks()
      action = int(input())
      self.route_action(action)


