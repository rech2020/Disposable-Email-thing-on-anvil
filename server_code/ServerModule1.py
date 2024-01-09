import tables
from tables import app_tables
import anvil.email
import anvil.server

from datetime import datetime

@anvil.email.handle_message
def new_message(msg):
  app_tables.messages.add_row(
    from_address=msg.envelope.from_address,
    to_address=msg.envelope.recipient,
    subject=msg.subject,
    text=msg.text,
    when=datetime.now()
  )
  
@anvil.server.callable
def get_messages(address):
  return app_tables.messages.search(to_address=address)