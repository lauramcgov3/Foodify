SHELL := /bin/sh 

venv:
	python3.6 -m venv ./env; \
	env/bin/pip install --upgrade pip; \
	env/bin/pip install -r requirements.txt;
	env/bin/pip install psycopg2-binary;

clean_venv:
	rm -rf ./env;

clean: 
	find . -name "*.pyc" -print 0 | xargs -0 rm -rf; 
	find . -name "__pycache__" -print 0 | xargs -0 rm -rf; 
