# How To Run
To start this app you need to:
1. Clone this repo and move to project
```sh
git clone https://github.com/ApostL78/PublishingCO.git && cd PublishingCO
```
2. Create and activate `venv`
```sh
python3 -m venv venv && source ./venv/bin/activate
```
3. Install requirements
```sh
pip install -r requirements.txt
```
4. Run server and migrate
```sh
python manage.py runserver && python manage.py migrate
```
