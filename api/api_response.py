from django.http import JsonResponse

# api response abstraction
class api_response:
    response = {"status": False, "msg": "INTERNAL_ERROR"}
    
    def set_value(self, name, value):
        self.response[name] = value

    def ok(self, msg):
        self.set_value("status", True)
        self.set_value("msg", msg)

    def fail(self, msg):
        self.set_value("status", False)
        self.set_value("msg", msg)

    def get_response(self):
        return JsonResponse(self.response)

    def __init__(self):
        pass