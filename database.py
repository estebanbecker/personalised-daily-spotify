import os
import os.path
import user
import pickle


class Database:
    
    path = ""

    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_path(self):
        return self.path

    def get_user(self, user):
        
        if os.path.isfile(self.path + "/" + user + ".p"):
            return pickle.load(open(self.path + "/" + user + ".p", "rb"))
    
        return None
    
    def save_user(self, user):
        
        pickle.dump(user, open(self.path + "/" + user.get_id() + ".p", "wb"))