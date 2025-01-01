format:
	pre-commit run --all-files

up:
	docker compose up

build:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose down
	docker compose up
