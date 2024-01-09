from ._anvil_designer import InboxTemplate
from anvil import *
import anvil.server
import tables
from tables import app_tables

class Inbox (InboxTemplate):
  def __init__(self, address, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.address = address
    
    self.refresh()
    
  def refresh(self):
    messages = anvil.server.call('get_messages', self.address)
    self.repeating_panel_1.items = messages
    self.n_msgs_lbl.text = "%d messages" % len(messages)
    

  def refresh_lnk_click (self, **event_args):
    # This method is called when the link is clicked
    self.refresh()

  def home_lnk_click (self, **event_args):
    # This method is called when the link is clicked
    open_form('Home')

  def address_label_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass


