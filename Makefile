test:
	python -m pytest --cov --cov-report=json:coverage --ctrf report.json

build:
	python -m build

clean:
	rm -rf coverage report.json dist/

change:
	pip install git-changelog
	git-changelog > CHANGELOG.md

dev:
	flask --app ./src/manager run

routes:
	flask --app ./src/manager routes