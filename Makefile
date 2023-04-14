PYC=pyinstaller
SRCS=main.py
TARGET=pippo
PYFLAGS=--onefile -n $(TARGET) -p $(VIRTUAL_ENV) --hidden-import=PIL._tkinter_finder

all:
	$(PYC) $(PYFLAGS) $(SRCS)

.PHONY: clean

clean:
	$(RM) -r dist/ build/ $(TARGET).spec