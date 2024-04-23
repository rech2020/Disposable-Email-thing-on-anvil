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

@anvil.email.handle_message
def handle_incoming_emails(msg):
  msg_row = app_tables.messages.add_row(
      from_address=msg.envelope.from_address, 
      to_address=msg.envelope.recipient,
      text=msg.text, 
      html=msg.html,
      when=datetime.now()
    )
  for a in msg.attachments:
    a_row=app_tables.attachments.add_row(
      message=msg_row, 
      attachment=a
    )
    msg_row['attachements']+=[a_row]

@anvil.server.callable
def get_messages(address):
  return app_tables.messages.search(to_address=address)

@anvil.server.callable
def send_message(to_address,from_address,from_name,subject,html,attachements=None):
  anvil.email.send(
  to=to_address,
  from_address=from_address,
  from_name=from_name,
  subject=subject,
  html=html,
  attachments=attachements
)