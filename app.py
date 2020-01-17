from router import Router
from controller import Controller

controller = Controller()
router = Router(controller)

router.run()
