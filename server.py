"""
    Server Side main Logic
"""
import socket, threading, keyboard
from .rHTTP import HttpRequest

class ThreadMapper:
    def thread_mapper(self, client_socket, addr) :
        with client_socket:
            request = client_socket.recv(1024).decode('utf-8')
            load_request = HttpRequest(request, self.views_list, self.host, self.port)
            response = load_request.handle()
            print(f"[-] {addr[0]}:{addr[1]} {load_request.path} {load_request.method} --> {load_request.status_code}")
            client_socket.sendall(response)


    def keyboard_thread(self) : 
        keyboard.wait('ctrl+c')  # Wait for Ctrl+C to be pressed
        self.stop_server.set()
        print("Closing Server...")

class Server(ThreadMapper):

    def __init__(
            self, 
            views_list,
            host : str = 'localhost', 
            port : int = 8080, 
        ):
        self.host = host
        self.port = port
        self.views_list = views_list
        self.__url = f"http://{self.host}:{self.port}/"
        self.stop_server = threading.Event()
        threading.Thread(
            target=self.keyboard_thread,
        ).start()

    def run(self) : 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print(f"[+] Server is listening on {self.__url}")
            
            while not self.stop_server.is_set():
                try : 
                    client_socket, addr = server_socket.accept()
                    th = threading.Thread(target=self.thread_mapper, args=(client_socket, addr,))
                    th.start()
                except KeyboardInterrupt:
                    print('[>] Server Quit.')
                    break


