# Makefile

.PHONY: clean

clean:
	@if [ -d data ]; then \
		rm -r data; \
	fi
	mkdir data
	python3 generate_data.py
