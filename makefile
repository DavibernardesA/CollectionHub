format-all-files:
	pre-commit run --all-files

up:
	docker compose up
	py src/app.py

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d
	py src/app.py
