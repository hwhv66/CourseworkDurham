CC = icpc

CFLAGS = -I. -O3 -std=c++11

LIBS = -lm

OBJ = solution-mpi.o

make: $(OBJ) 
	$(CC) $(OBJ) $(LIBS) $(CFLAGS) -o assignment

clean:
	rm *.o
	rm *.vtp
	rm *.pvd
