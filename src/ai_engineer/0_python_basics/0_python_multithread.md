
Just go back to the basics.

In a computer you have hardware:
- CPU is composed of CORES (4+ cores per CPU)
- CORES make the real work and each core can work in parallel
- LOGICAL CORES are shown to the OS when cpu supports MULTITHREAD (logical cores are almost interleaved on the same core)

Then the OS has some concepts:
- Process
- Thread

One process has a reserved space of memory, a main thread and a pool of threads that share this space. 
Threads are the minimal executable unit for OS. 
Scheduling threads is on behalf of OS. 
OS can interleave multiple Threads in the same core and can distribute threads across cores (a thread can occupy just one CORE at a time)

Runtimes (.NET RUNTIME, CPYTHON, ...) have a concept:
- Task

Task is a unit of work and can be assigned by the runtime to a thread in order to use CPU time.

In .NET when you use async/await, each async task can be assigned to a different thread of the thread pool and potentially run in parallel. 
- if you block an async task you're wasting a thread from the threadpool and this leads to thread starvation.

In Python when you use async/await, each async task shares the same thread, that thread is also shared by the loop itself that controls async tasks.  
- if you execute blocking I/O or CPU work in an async task you're blocking the whole async/await mechanism (the loop only receives the control back when you await)

In Python:
- async/await ->
    - concurrent: ONE thread shared by every request and also by the loop (interleaves at each await)
    - parallel: Never
- threads -> 
    - concurrent: separate thread, interleaves at each GIL release (e.g. blocking I/O, C extensions as Numpy, Pytorch, ...)
    - parallel: whenever GIL is released, because the releasing thread can keep working while another python thread can run python code on a different core
- processes -> 
    - parallel: separate process with its own thread pool, separate interpreter and GIL