.PHONY: help clean clean-pyc release dist

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr dist-packages-cache/
	rm -fr dist-packages-temp/
	rm -fr *.egg-info
	rm -fr .eggs
	rm -fr .cache

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel --universal

release: dist
	echo "Ensure that you have built the frontend files using Kolibri"
	echo "Uploading dist/* to PyPi, using twine"
	twine upload -s --sign-with gpg2 dist/*

makemessages:
	python -m kolibri manage makemessages -- -l en

compilemessages:
	python -m kolibri manage compilemessages -- -l en > /dev/null

ensurecrowdinclient:
	ls -l crowdin-cli.jar || wget https://crowdin.com/downloads/crowdin-cli.jar # make sure we have the official crowdin cli client

uploadmessages:
	java -jar crowdin-cli.jar upload sources -b `git symbolic-ref HEAD | xargs basename`

downloadmessages:
	java -jar crowdin-cli.jar download -b `git symbolic-ref HEAD | xargs basename`
