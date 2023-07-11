# 0x02. Python - Async Comprehension

## Tasks
### 0. Async Generator

Coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.


### 1. Async Comprehensions

Imports async_generator from the previous task and then creates a coroutine called async_comprehension that takes no arguments.

The coroutine collects 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.


### 2. Run time for four parallel comprehensions

Imports async_comprehension from the previous file and writes a measure_runtime coroutine that executes async_comprehension four times in parallel using asyncio.gather.

measure_runtime measures the total runtime and returns it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
