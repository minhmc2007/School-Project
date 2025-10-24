import os
import json

# protecting from path traversal
def path_normalize(path):
    path.replace("\\", "/")
    path.replace("//", "/")
    path.replace("..", "")
    path.replace("~", "")

    return path

class web_router:
    shouldCache = False
    permissions_dict = []
    file_cache = []
    def __init__(self, shouldCache):
        self.shouldCache = shouldCache
    def find_folder_permission(self, path):
        return next((d for d in self.permissions_dict if path in d), None)
    def find_file_cached(self, path):
        return next((d for d in self.file_cache if path in d), None)
    def check_folder_permission(self, path):

        # manually check
        res = {}
        perm = self.find_folder_permission(path)
        if perm == None:
            try:
                f = open('settings.json', 'r', encoding='utf-8')
                data = json.load(f)
                res[path] = data
            except:
                return False
            # caching the permission
            if self.shouldCache:
                self.permissions_dict.append(res)

    def routing(self, path):
        path = path_normalize(path)
        path = "./frontend/" + path

        # route to index.html on path
        if os.path.isdir(path):
            path += "/index.html"

        print("route to file", path)

        if os.path.isfile(path=path):            
            # check is cached
            cached_file = self.find_file_cached(path)
            try:
                if cached_file == None:
                    with open(path, "r") as f:
                        content = f.read()
                        if self.shouldCache:
                            self.file_cache.append({path: content})
                        
                        return content

                    return cached_file
            except:
                return "404"
        
        return 404
            
            