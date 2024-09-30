import socket

def tcp_client(server_ip='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
      client.socket.connect((server_ip, server_port))
      print(f"Connected to TCP server at {server_ip}:{server_port}")

      while True: 
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
          break

        client_socket.sendall(message.encode())
        data = client.socket.recv(1024)
        print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
  tcp_client()
