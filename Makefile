install:
	cp cflow2dot.py /usr/local/bin/cflow2dot
	cp cflow2dotrc $(HOME)/.cflow2dotrc

test:
	python test.py
