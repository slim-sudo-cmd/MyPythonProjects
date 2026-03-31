

import json

PeopleString = '''
{
   "People": [
      {"name":"John Bush",
       "phone":"123456789",
       "email":["johnbush@gmail.com",john12@gmail.com],
       "has_licence":true
      },
      {
       "name":"quis Pappy",
       "phone":"757221056",
       "email":null,
       "has_license":false
      }
   ]
}
'''

data = json.loads(PeopleString)
print(data)
