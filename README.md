# rAPI
    Powerfull tool to build fast, easy and scalable APIs.



### Installation

```
git clone https://github.com/RadwanHegazy/rAPI
```


```
pip insatll keyboard
```

### Create `rAPI` Server


```python
# my_rapi_file.py

# Import Libs
from rAPI.server import Server
from rAPI.views import View, APIDocs

# Create your endpoint
class IndexView (View) :
    url = "/" # url of the endpoint
    method = "GET" # endpoint method

    # NOTE: important to call get_response func and must return tuple as you see.
    def get_response(self) -> tuple[str, int]:
        data = {
            'name' : 'radwan',
            'age' : 19
        }
        return data, 200


# Another endpoint to implement POST method with custom fields
class PostView(View) : 
    url = "/auth/login/"
    method = 'POST'
    fields = {
        'username' : str,
        'password' : str,
    }
  
    def get_response(self) -> tuple[str, int]:
        if self.is_valid_fields() : 
            return self.request.data, 200
        return self.errors() ,400
    
# add your endpoints in views_list 
views_list=[
    IndexView,
    PostView
]

# define an api docs for automatically descripe your APIs
class UserDefineApiDocs(APIDocs) :
    url = "/docs/"
    views_list = views_list

# must do that to can see the result in /docs/ endpoints
views_list.extend([UserDefineApiDocs])

# load the view_list to the server to see it
# you can also set host and port.
# default host is localhost and default port is 8080
server = Server(
    views_list=views_list
)

# run the server
server.run()

```

### Run Server

```
python my_rapi_file.py
```

### Fun Fact
    when i trying to test the server for implement 1000 request, i found 
    that rAPI tooks 1.88s on the other side django rest framework tooks 2.01s,
    Not very huge difference but still faster 😉.