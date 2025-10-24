import json

class api_request:
    data = {}
    def __init__(self, request):
        self.data = json.loads(request.body)
    def dumps(self):
        return json.dumps(self.data)