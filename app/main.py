import socket  # noqa: F401
from typing import Any


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    conn: socket
    addr: tuple[str, str]

    with conn:
        print('Connected by', addr)
        while True:
            data: bytes = conn.recv(1024)
            decoded_data: str = data.decode("utf-8")
            res = parser(decoded_data)
            if res and res[0] == "GET":
                url_path = res[1]
                print(url_path)
                if url_path == "/":
                    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
                else:
                    conn.send(b'HTTP/1.1 404 Not Found\r\n\r\n')

def parser(data: str) -> list[str]:
    return data.split()


if __name__ == "__main__":
    main()
