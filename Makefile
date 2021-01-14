# print message if target is not specified
message: 
	echo -e '\e[1;31mPlease specify what to make\e[0m'

# ----------------------------------------------------------------------
# upload package
upload_test: pre_upload pypi_test
upload_package: pre_upload 

.PHONY: pre_upload
pre_upload:
	# update pip
	python -m pip install --upgrade pip

	# update packages
	python -m pip install --upgrade setuptools twine wheel 

	# build package
	python setup.py sdist bdist_wheel

# upload to test pypi
pypi_test:
	python -m twine upload --skip-existing -r testpypi dist/*


# ----------------------------------------------------------------------
# test package with tests in test folder
# test_package:
# 	# python setup.py install
# 	cd tests
# 	python -m unittest discover
# The discover keyword tells unittest to find any files with the name of test_*.py and run the unittests inside them.

# ----------------------------------------------------------------------
# targets for python class scripts
.PHONY: python_classes
python_classes: greet

greet:
	python llutils/Greetings.py