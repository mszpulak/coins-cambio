# coins-cambio

```bash
pip install virtualenv
python -m venv cambio
source cambio/bin/activate

pip install -r REQUIREMENTS.txt

./manage.py migrate
./manage.py import_data users.csv
````


for simplification it's assumed database tables are empty before importing data and primary keys are created starting from 1
```bash
curl -H 'content-Type: application/json' -X PUT -d '{"change_value": "200"}' http://127.0.0.1:8000/users/1/add_coins
curl -H 'Content-Type: application/json' -X PUT -d '{"change_value": "1200"}' http://127.0.0.1:8000/users/3/


```
