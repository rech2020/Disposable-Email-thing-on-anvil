from ._anvil_designer import SendTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Send(SendTemplate):
  def __init__(self, address, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    self.from_address = address
    self.address_label.text = address

  def home_lnk_click (self, **event_args):
    # This method is called when the link is clicked
    open_form('Home')

  def send_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('send_message',
      to_address=self.to_address_box.text,
      from_address=self.from_address,
      from_name=self.from_name_box.text,
      subject=self.subject_box.text,
      html=self.text_quill.get_html(),
      )

  