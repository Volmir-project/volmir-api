cd docker-config
docker compose up --build -d
sleep 10
docker compose exec web python manage.py migrate