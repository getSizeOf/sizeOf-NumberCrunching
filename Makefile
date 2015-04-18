.PHONY: clean, run, test, pull, push, update, reqs
clean:
	rm -rf *.pyc
run:
	python cruncher.py
test: run
pull:
	git pull origin master
push:
	git push origin master
update: pull push
reqs:
	pip freeze > requirements.txt

