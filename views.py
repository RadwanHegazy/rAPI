""" 
    Server views and rendering api.
"""

from abc import ABC, abstractmethod
from typing import Any
from rHTTP import HttpRequest

class View (ABC) : 
    request:HttpRequest = None
    method:str = ""
    field:dict = {}
    url:str = ""

    @abstractmethod
    def get_response(self) -> tuple[str, int] : ...
