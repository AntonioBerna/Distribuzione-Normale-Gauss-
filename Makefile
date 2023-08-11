PYC=pyinstaller
SRCS=main.py
TARGET=pippo
PYFLAGS=--onefile -n $(TARGET) -p $(VIRTUAL_ENV) --hidden-import=PIL._tkinter_finder

all:
	$(PYC) $(PYFLAGS) $(SRCS)

.PHONY: clean run

run:
	./dist/$(TARGET)

clean:
	$(RM) -r dist/ build/ $(TARGET).spec