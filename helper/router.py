from os.path import dirname, join
from kivy.lang import Builder
import re

class Router() : 

    def _route(file_path: str) -> str:
        return join(dirname(__file__), "..", "src/pages", file_path)
    
    def kivyRoute(file_path: str):

        temp_str = file_path
        kv_validation = re.search(r"\.\w+$",temp_str)

        if kv_validation:
            kv_str = kv_validation.group()
            if kv_str != ".kv":
                temp_str += ".kv"
        else:
            temp_str += ".kv"

        kv_path = Router._route(temp_str)

        try :
            Builder.load_file(kv_path)
        except Exception as e :
            print(f"Error Handler Exception : {e}")
            
        