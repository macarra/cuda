## Make file for superprime


all: hello add square cube

force: 
	touch *.cu
	make all

hello:  hello.cu
	nvcc hello.cu -o /bin/hello
	/bin/hello
	
add:  add.cu
	nvcc add.cu -o /bin/add
	/bin/add
	
square:  square.cu
	nvcc square.cu -o /bin/square
	/bin/square	
	
cube:  cube.cu
	nvcc cube.cu -o /bin/cube
	/bin/cube	
	
