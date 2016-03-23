from os import environ as ENV
from os.path import abspath  as ABSPATH
from os.path import dirname as DIR
from sys import path as SYSPATH

ENV['DBPATH'] = ABSPATH(DIR(__file__)) + "/db/"
SYSPATH.append(ENV.get("DBPATH"))
ENV['MODELPATH'] = ABSPATH(DIR(__file__)) + "/models/"
SYSPATH.append(ENV.get("MODELPATH"))

from DBMS import *
