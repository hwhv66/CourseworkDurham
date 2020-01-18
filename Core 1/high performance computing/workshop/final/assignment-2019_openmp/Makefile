CC = icpc

CFLAGS = -I. -O3 -std=c++11 -fopenmp

LIBS = -lm

OBJ = assignment-2019_openmp.o

make: $(OBJ) 
	$(CC) $(OBJ) $(LIBS) $(CFLAGS) -o assignment

clean:
	rm *.o
	rm *.vtp
	rm *.pvd
