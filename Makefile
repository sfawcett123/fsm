test:
	python -m pytest --cov --cov-report=json:coverage --ctrf report.json

build:
	python -m build

clean:
	rm -rf coverage report.json dist/
