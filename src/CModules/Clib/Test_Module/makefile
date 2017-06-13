CC := gcc
CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Werror

PROGRAM := test_module.exe

SRCS := $(wildcard *.c)
OBJS := $(patsubst %.c,%.o,$(wildcard *.c))


$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROGRAM) $(OBJS) cnumlib.dll

$(OBJS): $(SRCS)
	$(CC) -c $(CFLAGS) $(SRCS)

clean:
	rm -rf $(wildcard *.o)