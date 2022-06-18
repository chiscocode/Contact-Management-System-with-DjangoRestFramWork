# Contact Management System with DjangoRestFramWork
The aim of this system is to enable users keep record of his/her contact information on the cloud for easy retrival.


## features include :
--> Authentication
--> Crud Functionality (Create, Read, Update and Delete)
--> Search Functionality

## Endpoint include :
```
localhost:8000/api/contact
```
or

```
http://mlogistic.herokuapp.com/api/contact
```

```
localhost:8000/api/contact/post
```

or

```
http://mlogistic.herokuapp.com/api/contact/post
```

```
localhost:8000/api/contact/update/1
```

or

```
http://mlogistic.herokuapp.com/api/contact/update/1
```


```
localhost:8000/api/contact/delete/1
```

or

```
http://mlogistic.herokuapp.com/api/contact/delete/1
```

```
localhost:8000/api/contact/register
```

or

```
http://mlogistic.herokuapp.com/api/register
```

```
localhost:8000/api/login
```

or

```
http://mlogistic.herokuapp.com/api/login
```

```
localhost:8000/api/logout
```

or

```
http://mlogistic.herokuapp.com/api/logout
```

```
localhost:8000/api/contact/?search=1
```

or

```
http://mlogistic.herokuapp.com/api/contact/?search=1
```


### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/chiscocode/Contact-Management-System-with-DjangoRestFramWork.git

```

--> Move into the directory where we have the project files : 
```bash
cd Contact-Management-System-with-DjangoRestFramWork

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment on windows:
```bash
envname\scripts\activate

```
or 
```
source env/bin/activate
```
 on Mac and Linux.


--> Install the requirements :
```bash
pip install -r requirements.txt

```

Make migrations with: 
```
python manage.py makemigrations
``` 
and then
 ```
python manage.py migrate
```.

## License
MIT License

Copyright (c) 2022 Chukwudifu Patrick Chimezie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE