from os import environ as ENV
class Globals():
    def __init__(self):
        self._Add = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/add.sh"
        self._Create = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/create.sh"
        self._Select = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/select.sh"
        self._Update = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/update.sh"
        self._Delete = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/delete.sh"
        self._CreateSchema = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/create_schema.sh"
        self._DeleteDatabase = ENV.get('DBMSPATH')+"/TextDB/DBMS/scripts/delete_db.sh"
        self.DBPATH = ENV.get("DBPATH")

