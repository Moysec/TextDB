# TextDB
A text-based simple db and dbms for small amount of data


### Installation
Clone this repository to your project directory. 

```bash
cd your/project/path
git clone https://github.com/Moysec/TextDB.git
```

Now add below to your __init__.py file or your project's starting point.
```python
from os import environ
from os.path import abspath
from os.path import dirname
from sys import path

environ['DBMSPATH'] = abspath(dirname(__file__)) + "/TextDB"
path.append(environ.get('DBMSPATH'))

import TextDB
```


### Usage
```python
import TextDB

dbdict = {"name": "Johnny B. Good",
          "email": "johnny@bgood.com",
          "tel": "+123456789"}
db = TextDB.DBMS("users", dbdict)
dbresult = db.add()
print dbresult
```

### License
[The MIT License (MIT)](LICENSE.md)
Copyright &copy; 2016 <a href="https://github.com/Moysec/" target="_blank">Moysec LLC</a>.
