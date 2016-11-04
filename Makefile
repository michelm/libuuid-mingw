PREFIX  	?= .
CFLAGS  	:= -fPIC -O3 -g -Wall -I$(PREFIX)/include -I./include -I./src
LINKFLAGS 	:= -L$(PREFIX)/bin -lrpcrt4
MAJOR   	:= 1
NAME    	:= uuid
VERSION 	:= $(MAJOR)
TARGET  	:= lib$(NAME)-$(VERSION)
SOURCES		:= $(wildcard src/*.c)
OBJECTS		:= $(SOURCES:.c=.o)
CC			?= x86_64-w64=mingw32-gcc
AR			?= x86_64-w64=mingw32-ar

all: clean $(OBJECTS)
	$(CC) -shared -o $(TARGET).dll $(OBJECTS) -Wl,--out-implib,$(TARGET).a $(LINKFLAGS)

clean:
	$(RM) *.o *.a *.dll *.la *.so*
	
install: all
	mkdir -p $(PREFIX)/bin
	mkdir -p $(PREFIX)/include/uuid
	cp $(TARGET).dll $(PREFIX)/bin
	cp include/uuid/*.h $(PREFIX)/include/uuid

