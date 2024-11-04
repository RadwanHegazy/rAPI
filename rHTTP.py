import json

class HttpRequest:
    __CODES = {
        200 : "200 OK",
        404 : "404 Not Found",
        400 : "400 Bad Request",
        500 : "500 Internal Server Error"
    }

    def __init__(self, request_bytes, views_list, host, port) -> None:
        self.request_bytes = request_bytes
        self.views_list = views_list
        self.host = host
        self.port = port

    @property
    def data (self) -> dict : 
        bytes_data = self.request_bytes.split('\n\r\n')[-1]
        try : 
            json_data = json.loads(bytes_data)
        except json.decoder.JSONDecodeError : 
            json_data = {}
        return json_data
    
    @property
    def query (self) -> dict:
        data = {}
        for k in self.path_query.split("&") : 
            query = k.split('=')
            data[query[0]] = query[1]
            
        return data

    def handle (self) : 
        request_line = self.request_bytes.splitlines()[0]
        self.method, self.path, _ = request_line.split()

        if "?" in self.path:
            self.path, self.path_query  = self.path.split('?')
        
        get_view = None
        for view in self.views_list :
            view = view()
            if view.url == self.path and self.method == view.method:
                get_view = view
                break
        
        # Handle the request based on the path
        if get_view:
            get_view.request = self
            response_data, response_code = get_view.get_response()
            response_body = json.dumps(response_data)
            self.status_code = self.__CODES[response_code or 200]
        else:
            response_body = ""
            self.status_code = self.__CODES[404]

        # Prepare HTTP response
        response = f"HTTP/1.1 {self.status_code}\r\n" \
                f"Content-Type: application/json\r\n" \
                f"Content-Length: {len(response_body)}\r\n" \
                f"\r\n" \
                f"{response_body}"
        
        return response.encode('utf-8')
    