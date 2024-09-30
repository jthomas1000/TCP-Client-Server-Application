import socket

def tcp_server(host='127.0.0.1', port=65432) :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket :
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data) #Echo back the received data

if __name__ == "__main__":
    tcp_server()
