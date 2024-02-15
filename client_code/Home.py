from ._anvil_designer import HomeTemplate
from anvil import *
import tables
from tables import app_tables
import anvil.server

class Home (HomeTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    print(anvil.server.call('auto_location'))
    # Any code you write here will run when the form opens.

  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    open_form('Inbox', self.address_box.text + "@disposableemailthingy.anvil.app")

  def address_box_pressed_enter (self, **event_args):
    # This method is called when the user presses Enter in this text box
    self.button_1_click()




