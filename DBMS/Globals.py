from os import environ as ENV
class Globals():
    def __init__(self):
        self._Add = ENV.get('DBMSPATH')+"/DBMS/scripts/add.sh"
        self._Create = ENV.get('DBMSPATH')+"/DBMS/scripts/create.sh"
        self._Select = ENV.get('DBMSPATH')+"/DBMS/scripts/select.sh"
        self._Update = ENV.get('DBMSPATH')+"/DBMS/scripts/update.sh"
        self._Delete = ENV.get('DBMSPATH')+"/DBMS/scripts/delete.sh"
        self.DBPATH = ENV.get("DBPATH")

