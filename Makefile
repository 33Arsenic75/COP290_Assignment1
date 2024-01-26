# Makefile

.PHONY: clean

clean:
	@if [ -d historical_data ]; then \
		rm -r historical_data; \
	fi
	mkdir historical_data
	python3 generate_historical_data.py
