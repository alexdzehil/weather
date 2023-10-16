deps:
	pip-compile requirements.in
	pip-sync requirements.txt

dev-deps:
	pip-compile requirements.in
	pip-compile dev-requirements.in
	pip-sync requirements.txt dev-requirements.txt
