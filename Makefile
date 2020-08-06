## Make file for superprime


all: hello square cube

force: 
	touch *.cu
	make all

hello:  hello.cu
	nvcc hello.cu -o ./bin/hello
	./bin/hello
	
square:  square.cu
	nvcc square.cu -o ./bin/square
	./bin/square	
	
cube:  cube.cu
	nvcc cube.cu -o ./bin/cube
	./bin/cube	

atomictest: atomictest.cu 
	nvcc atomictest.cu I./include -o ./bin/atomictest
	./bin/atomictest
