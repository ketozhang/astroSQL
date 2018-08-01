publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	make clean

clean:
	rm -rf astrosql.egg-info build/ dist/

