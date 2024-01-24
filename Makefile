# Makefile

.PHONY: clean

clean:
	@if [ -d historial_data ]; then \
		rm -r historial_data; \
	fi
	mkdir historial_data
	python3 generate_historial_data.py
