CC := gcc
CFLAGS := -std=c11 -shared -Wall -Wextra -Wpedantic -Werror

PROGRAM := cnumlib.dll

SRCS := $(wildcard *.c)
OBJS := $(patsubst %.c,%.o,$(wildcard *.c))


$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) -o ../Test_Module/$(PROGRAM) $(OBJS)

$(OBJS): $(SRCS)
	$(CC) -c $(CFLAGS) $(SRCS)

clean:
	rm -rf $(wildcard *.o)