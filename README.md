# Movie Theater (Backend)

## Example
- http://localhost/admin/
- http://localhost/api/v1/movies/
- http://localhost/api/v1/movies/00af52ec-9345-4d66-adbe-50eb917f463a/

## How to deploy
> 0. Fill in `.env` files everywhere
> 1. `cd movies_admin/`
> 2. 
```
        python -m venv venv
        source venv/Scripts/activate
        pip install -r requirements/base.txt
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
```
> 2. `cd ..`
> 3. `make build`
> 4. `make start`
> 5. `make start_auth_api`
> 6. For stopping: `make stop`