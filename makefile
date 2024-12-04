format-all-files:
	pre-commit run --all-files

up:
	docker compose up

down:
	docker compose down

restart:
	docker compose down
	docker compose up
