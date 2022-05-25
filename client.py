from opcua import Client

class ButtonHandler(object):
    def datachange_notification(self, node, val, data):
      print(f"Estado recebido: "+str(val))

def connect_client():
    client=Client("opc.tcp://localhost:4840")
    client.connect()

    return client

def main():
  client = connect_client()
  button_var = client.get_node("ns=1;s=Speed")
  handler = ButtonHandler()
  sub = client.create_subscription(500, handler)
  sub.subscribe_data_change(button_var)

if __name__ == "__main__":
    main()