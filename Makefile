.PHONY: test

test:
	docker-compose exec availability python -m unittest test
