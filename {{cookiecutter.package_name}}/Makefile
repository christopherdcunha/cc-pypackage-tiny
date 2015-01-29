.PHONY: clean-pyc clean-build docs

help:
	@echo "clean - remove build artifacts and python artifacts"
	@echo "docs - generate sphinx html documentation"
	@echo "env - make a virtualenv and activate it"
	@echo "lint - check style with flake8"
	@echo "test - run tox"

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	sh -c ". ./.env/bin/activate; flake8 --exclude=.tox,.env"

test:
	sh -c ". ./.env/bin/activate; tox --skip-missing-interpreters"

env:
	rm -rf ./.env/
	virtualenv .env
	./.env/bin/pip install --upgrade pip
	./.env/bin/pip install --upgrade setuptools wheel
	./.env/bin/pip install flake8 pytest tox
	./.env/bin/pip install sphinx alabaster
	. ./.env/bin/activate

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/build/html/index.html
