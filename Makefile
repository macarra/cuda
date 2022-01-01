## Make file for superprime

INCLUDES=--allow-unsupported-compiler

all: hello square cube

force: 
	touch *.cu
	make all

hello:  hello.cu
	nvcc hello.cu -o ./bin/hello $(INCLUDES)
	./bin/hello
	
square:  square.cu
	nvcc square.cu -o ./bin/square $(INCLUDES)
	./bin/square	
	
cube:  cube.cu
	nvcc $(INCLUDES) cube.cu -o ./bin/cube
	./bin/cube	

atomictest: atomictest.cu 
	nvcc atomictest.cu -I./include -o ./bin/atomictest $(INCLUDES)
	./bin/atomictest

transpose: transpose.cu
	nvcc transpose.cu -I./include -o ./bin/transpose $(INCLUDES)
	./bin/transpose
