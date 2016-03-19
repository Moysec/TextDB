from subprocess import Popen as SUBPopen
from subprocess import PIPE as SUBPIPE
from os import environ as ENV
from os.path import isfile as ISFILE

from Globals import Globals

class DBMS():
    def __init__(self, db_name, data_dict):
        self.db_name = db_name
        self.data_dict = data_dict
        self.data_str = ""
        if len(data_dict) != 0 or data_dict != {}:
            self.data_str = " ".join([str(data_dict[x]) for x in data_dict])

        if not ISFILE(Globals().DBPATH + "/" + self.db_name + ".db"):
            self.create_db()
        return

    def create_db(self):
        args_list = [Globals()._Create, 
                     self.db_name]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)


    def add(self):
        args_list = [Globals()._Add, 
                    self.db_name,
                    self.data_str]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": stdout}

        if stdout in ["\n", ""]:
            return {"err": None, "result": "OK"}
        else:
            return {"err": stderr, "result": stdout}

    def select(self, what=None):
 	if what and self.data_str is "":
	    self.data_str = what
 	elif what and self.data_str is not "":
 	    return {"err": "You cannot do that", "result": None}

        args_list = [Globals()._Select,
                     self.db_name,
                     self.data_str]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": stdout}

        if stdout in ["\n", ""]:
            return {"err": None, "result": stdout}
        else:
            result_splt = stdout.strip().split(" ")
            result_lst = [x.split("$") for x in result_splt]
            return {"err": None, "result": result_lst}

    def update(self, select_flag):
        args_list = [Globals()._Update,
                     self.db_name,
                     select_flag,
                     self.data_str]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": None}

        if stdout in ["\n", ""]:
            return {"err": None, "result": "OK"}
        else:
            return {"err": stderr, "result": None}

    def delete(self):
 	self.data_str = self.data_str.replace("/", "\/")
        args_list = [Globals()._Delete,
                     self.db_name,
                     self.data_str]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": None}

        if stdout in ["\n", ""]:
            return {"err": None, "result": "OK"}
        else:
            return {"err": stderr, "result": stdout}

