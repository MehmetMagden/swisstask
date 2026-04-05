.PHONY: build up down restart logs ps status clean

build:
	sudo docker-compose build

up:
	sudo docker-compose up -d
	@echo "[OK] SwissTask API started -> http://localhost:5000"

down:
	sudo docker-compose down
	@echo "[STOP] SwissTask API stopped"

restart:
	sudo docker-compose restart

logs:
	sudo docker-compose logs --tail=20 -f

ps:
	sudo docker-compose ps

status:
	@echo "=== Container Status ==="
	sudo docker-compose ps
	@echo "=== Recent Logs ==="
	sudo docker-compose logs --tail=10

clean:
	sudo docker-compose down -v
	sudo docker system prune -f
	@echo "[CLEAN] Cleaned up"