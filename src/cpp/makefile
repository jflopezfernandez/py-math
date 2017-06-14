
CC := g++
CFLAGS := -std=c++17 -Wall -Wextra -Wpedantic -Werror
LINKERFLAGS := 

PROGRAM := test

SRCS := $(wildcard *.cpp)
OBJS := $(patsubst %.cpp, %.o, $(wildcard *.cpp))


$(PROGRAM): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROGRAM) $(LINKERFLAGS) $(OBJS)

$(OBJS): $(SRCS)
	$(CC) -c $(CFLAGS) $(SRCS)

clean:
	rm -rf $(wildcard *.o | *.obj)
	rm -rf $(wildcard ../*.dll)