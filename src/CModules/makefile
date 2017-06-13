
CC := gcc32
CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Werror
LINKERFLAGS := -shared

PROGRAM := libnum.dll

SRCS := $(wildcard *.c)
OBJS := $(patsubst %.c, %.o, $(wildcard *.c)) #addInt_.obj


$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) -o ../$(PROGRAM) $(LINKERFLAGS) $(OBJS)

$(OBJS): $(SRCS)
	$(CC) -c $(CFLAGS) $(SRCS)

clean:
	rm -rf $(wildcard *.o | *.obj)
	rm -rf $(wildcard ../*.dll)