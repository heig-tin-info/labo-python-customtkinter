from .view import MainPage
from .presenter import Presenter
from .model import Camera

import sys
model = Camera()
app = MainPage()
presenter = Presenter()
app.mainloop()
sys.exit(0)