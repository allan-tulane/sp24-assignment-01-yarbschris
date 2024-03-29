

# CMPS 2200 Assignment 1

**Name:**Christopher Yarbro


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
Yes, $2^{n+1} = 2 * 2^{n}$, so there is some c > 2 for which $c * 2^{n} > 2^{n + 1}$. Therefore $2^{n+1} \in O(2^n)$
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  
.  No, because $2^{2^n}$ grows significantly faster than $(2^n)$ as n increases, and there is no constant c for which $2^{2^n} < c * (2^n)$.
Polynomial growth is faster than logarithmic growth.
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  

.  No, polynomial growth is faster than logarithmic growth, so $n^{1.01}$ grows significantly faster than $\mathrm{log}^2 n$ as n increases, and there is no constant c for which $n^{1.01}$ < $c * \mathrm{log}^2 n$ as n approaches infinity
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  Yes, because $n^{1.01}$ grows faster than $\mathrm{log}^2 n$, and for something to be $\in \Omega(\mathrm{log}^2 n)$, it must grow as fast or faster than $\mathrm{log}^2 n$.
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, again, polynomial growth is faster than logarithmic growth, so $\sqrt{n}$ grows faster than $\mathrm{log} n^3$, and there is no constant c for which $\sqrt{n}$ < c * $\mathrm{log} n^3$ as n approaches infinity. 
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
Yes, because $\sqrt{n}$ grows faster than $\mathrm{log}^2 n$, and for something to be $\in \Omega(\mathrm{log}^2 n)$, it must grow as fast or faster than $\mathrm{log}^2 n$.

2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`
 
def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function recursively calculates the xth term of the Fibonacci Sequence. The base cases are one and zero. 
If the input is greater than 1, then foo is run on every fibonacci term less than x until the function tries to do foo(1) or foo(0), at 
which point the function returns the base case and adds up all of the terms that had been found recursively to return the xth term of the fibonacci sequence.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  Work and Span are both linear:
Work: O(n)
Span: O(n)
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  The Work of this algorithm is also O(n). The algorithm divides the list in half at each step. The total work done at a level of the tree
is equal to the list's length at that level, so when this is all added it, the work is proportional to then lengths above.
.  
.  
.  The span of this algorithm is equal to the longest critical path in the recursion tree, since the the each node branches in half at 
each recursion, the depth of the tree is log base 2 of n, however, since the function is not parallelized, it waits until both sides have been completed to combine the results and continue, so the span remains proportional to the length of the list, making the span O(n).
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  The total work of this algorithm remains O(n), because no matter how many threads are running the algorithm, the same number of elements must be analyzed.

However, the span does benefit, with each recursive call spawning a new thread, the span becomes the longest critical path in the recursion tree as discussed earlier, so the new span is O(log n)
.  
.  
.  
.  
.  

