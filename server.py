# import socket, threading, keyboard, json

# exit_ = False

# def listen_for_exit():
#     global exit_
#     print("Listening for Ctrl+C to exit...")
#     keyboard.wait('ctrl+c')  # Wait for Ctrl+C to be pressed
#     exit_ = True
#     print("Ctrl+C detected! Exiting...")

# def handle_request(request):
#     # Parse the request
#     request_line = request.splitlines()[0]
#     method, path, _ = request_line.split()
    
#     # Handle the request based on the path
#     if path == '/':
#         response_data = {
#             "message": "Hello, World!",
#             "status": "success"
#         }
#         response_body = json.dumps(response_data)
#         status_code = "200 OK"
#     else:
#         response_body = json.dumps({"error": "Not Found"})
#         status_code = "404 Not Found"

#     # Prepare HTTP response
#     response = f"HTTP/1.1 {status_code}\r\n" \
#                f"Content-Type: application/json\r\n" \
#                f"Content-Length: {len(response_body)}\r\n" \
#                f"\r\n" \
#                f"{response_body}"
    
#     return response.encode('utf-8')

# def client_async (client_socket, addr) :
#     with client_socket:
#         print(f"Connection from {addr}")
#         request = client_socket.recv(1024).decode('utf-8')
#         print(f"Request: {request}")

#         response = handle_request(request)
#         client_socket.sendall(response)

# def run_server(host='127.0.0.1', port=8080):
#     global exit_
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen(5)
#         print(f"Server is listening on http://{host}:{port}")

#         try :
#             while not exit_:
#                 client_socket, addr = server_socket.accept()
#                 th = threading.Thread(target=client_async, args=(client_socket, addr,))
#                 th.start()
#         except KeyboardInterrupt:
#             exit_ = True

# if __name__ == '__main__':
#     listener_thread = threading.Thread(target=listen_for_exit)
#     listener_thread.start()
#     run_server()


"""


from rAPI import View, Server

class PostView (View) : 
    url = 'index"
    method = "POST"
    fields = {
        "name" : str,
        "age" : int,
        "is_student" : bool
    }

    def get_response(self, request) -> tuple(dict, int) :
        data = request.collect_data()  # for collection the data depends on fields dict
        print(data.get("name"))
        return data, 200


class GetView (View) : 
    url = "user/get/all/"
    method = "GET"
    fields = {
        "id" : int
        "name" : str,
        "age" : int
    }

    def get_response(self, request) -> tuple(dict, int) : 
        radwan_orm_query = Table().all()
        return self.represent_fields(radwan_orm_query), 200



views_list = [PostView, GetView]

server = Server(host="localhost", port=4444, views_list) # web server and thread mabagerlogic 
server.run()
        

"""

