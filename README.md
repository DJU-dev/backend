## Prerequisites
* Python3(3.10 recommended)
* pip

## Installing
Create a **backend** directory on your local machine to store the project repositories

### Setting up the backend
1. Clone the backend repositories inside the **backend** folder
```
git clone https://github.com/DJU-dev/backend.git

```
2. Set up a Environment
* Create venv
```
cd backend
python -m venv venv
```
* Activate venv
##### Windows
```
.\venv\Scripts\activate
```
##### Mac
```
source ./venv/bin/activate
```
4. Install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```
5. Run server locally
```
python manage.py runserver
```
