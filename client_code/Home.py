from ._anvil_designer import HomeTemplate
from anvil import *
import tables
from tables import app_tables
import anvil.server

def get_ip():
  send_url = 'https://ipinfo.io/json'
  r = anvil.http.request(send_url, json=True)
  return r

class Home (HomeTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    try: self.re = get_ip()
    except: pass
      

    try: print(f"user with id {self.r} has opened this website")
    except: print("user which id i failed to get due to that website being bushes has opened this website")
    # Any code you write here will run when the form opens.

  def button_1_click (self, **event_args):
    # This method is called when the button is clicked
    open_form('Inbox', self.address_box.text + "@disposableemailthingy.anvil.app")
    try: print(f"user with ip {self.re['ip']} has opened Inbox page with email {self.address_box.text+'@disposableemsilthingy.anvil.app'}")
    except: print(f"user has opened {self.address_box.text+'@disposableemailthingy.anvil.app'}")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Send', self.address_box.text + "@disposableemailthingy.anvil.app")
    try: print(f"user with ip {self.re['ip']} has opened Send page with email {self.address_box.text+'@disposableemsilthingy.anvil.app'}")
    except: print(f"user has opened {self.address_box.text+'@disposableemailthingy.anvil.app'}")

  def address_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass




