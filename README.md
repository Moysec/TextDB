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
The MIT License (MIT)
Copyright &copy; 2016 Moysec LLC.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
