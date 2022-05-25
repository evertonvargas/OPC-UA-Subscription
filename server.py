from opcua import Server
from time import sleep
from random import randint

def mock_data_to_server(speed, temperature):
    while True:
        speed.set_value(randint(10, 35))
        temperature.set_value(randint(35, 80))
        sleep(2)
        print(f"Dado enviado")

def main():
  server = Server()
  root = server.get_objects_node() 
  speed = root.add_variable("ns=1; s=Speed", "Speed", 0)
  temperature = root.add_variable("ns=2; s=Temperature", "Temperature", 0)
  server.start()
  mock_data_to_server(speed, temperature)

if __name__ == "__main__":
    main()