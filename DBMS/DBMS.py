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
        self.key_str = ""
        if len(data_dict) != 0 or data_dict != {}:
            self.data_str = " ".join([str(data_dict[x]) for x in data_dict])
            self.key_str = " ".join([str(x) for x in data_dict])
        if not ISFILE(Globals().DBPATH + "/" + self.db_name + ".db"):
            self.create_db()
            self.create_sch()
        return

    def create_db(self):
        args_list = [Globals()._Create, 
                     self.db_name]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)

    def create_sch(self):
        args_list = [Globals()._CreateSchema,
                    self.db_name,
                    self.key_str]
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


    def select(self, field, data):
 	if not isinstance(field, basestring) or not isinstance(data, basestring):
 	    return {"err": "You cannot do that", "result": None}

        args_list = [Globals()._Select,
                     self.db_name,
                     field, 
                     data]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": stdout}

        if stdout in ["\n", ""]:
            return {"err": None, "result": stdout}
        else:
            result_splt = stdout.strip().split("\n")
            fields=result_splt.pop(0).split(" ")
            result_lst = []
            temp_dict = {}
            for j in range(len(result_splt)): 
                for i in range(len(fields)):
                    temp_dict[fields[i]] = result_splt[j].split(" ")[i]
                result_lst.append(temp_dict)

            return {"err":None, "result": result_lst}
            

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

#    def delete(self):
# 	self.data_str = self.data_str.replace("/", "\/")
#        args_list = [Globals()._Delete,
#                     self.db_name,
#                     self.data_str]
#        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
#        stdout, stderr = process.communicate()
#        if stderr:
#            return {"err": stderr, "result": None}
#
#        if stdout in ["\n", ""]:
#            return {"err": None, "result": "OK"}
#        else:
#            return {"err": stderr, "result": stdout}

    def delete(self, field, data):
 	if not isinstance(field, basestring) or not isinstance(data, basestring):
 	    return {"err": "You cannot do that", "result": None}
 	#self.data_str = self.data_str.replace("/", "\/")
        args_list = [Globals()._Delete,
                     self.db_name,
                     field,
                     data]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": None}

        if stdout in ["\n", ""]:
            return {"err": None, "result": "OK"}
        else:
            return {"err": stderr, "result": stdout}

    def deleteDatabase(self):
        args_list = [Globals()._DeleteDatabase,
                     self.db_name]
        process = SUBPopen(args_list, stdout=SUBPIPE, stderr=SUBPIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return {"err": stderr, "result": None}

        if stdout in ["\n", ""]:
            return {"err": None, "result": "OK"}
        else:
            return {"err": stderr, "result": stdout}
            



















