import anvil.server
import anvil.http

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:


@anvil.server.callable
def auto_location():
  send_url = 'https://ipinfo.io/'
  r = anvil.http.request(send_url, json=True)
  return r