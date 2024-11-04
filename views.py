""" 
    Server views and rendering api.
"""

from abc import ABC, abstractmethod
from typing import Any
from rHTTP import HttpRequest

class View (ABC) : 
    request:HttpRequest = None
    request = None
    method:str = ""
    fields:dict[str, Any] = {}
    url:str = ""
    __errors:dict = {}

    @abstractmethod
    def get_response(self) -> tuple[str, int] : ...

    def is_valid_fields (self) : 
        self.__errors.clear()
        fields_keys = self.fields.keys()
        request_data_keys = self.request.data.keys()
        
        for field in fields_keys : 
            if field not in request_data_keys : 
                self.__errors[field] = 'field not found'
        
        return not any(self.__errors)
    

    def errors(self) : 
        return self.__errors
    

class APIDocs (View) :
    method = "GET"
    url = "/__docs__/"
    views_list = []

    def get_response(self) : 
        apis = []
        for view in self.views_list[:-1]: 
            view_obj = view()
            apis.append({
                'url' : view_obj.url,
                'method' : view_obj.method,
                'fields' : list(view_obj.fields.keys()) if view_obj.fields else []
            })

        return apis, 200