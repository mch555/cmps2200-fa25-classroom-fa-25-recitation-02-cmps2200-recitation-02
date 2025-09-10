# CMPS 2200  Recitation 02

**Name (Team Member 1):**___Maeren Hay______________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO**
f(n) = 1:
recurrence: W(n) = aW(n/b)+1
asymptotic behavior: W(n) = Θ(n) for a=b=2
from code: W(1)=1, W(2)=3, W(4)=7
observation: there is linear growth and the code matches the theoretical prediction

f(n)= log n:
recurrence: W(n)= aW(n/b) + log n
asymptotic behavior: W(n)= Θ(n) for a =b=2
from code: W(1)=1, W(2)=2.69, W(4)=6.77
observation: bit faster linear growth and it matches my expectation

f(n) = n:
recurrence: W(n)= aW (n/b)+ n
asymptotic behavior: W(n)= Θ(nlogn) for a=b=2
from code:W(1)=1, W(2)=4, W(4)=12
observation: grows similarly to nlogn, and matches my expectation



- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

**TODO**
Relation       Asymptotic Behavior        Example
c<log_b a          Θ(n^{log_b a})           a=2, b=2, c=0.5->W(n)~n
c=log_b a          Θ(n^c log n)             a=2, b=2, c=1 -> W(n)~ nlogn
c>log_b a          Θ(n^c)                   a=2, b=2, c=2 -> W(n)~ n^2

- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
While analzying the span, the recursive calls can run i parallel because we aways have 'a' processors available. This changed the recurrence relation from W(n)=aW (n/b)+f(n) to S(n)= S(n/b)+f(n)

f(n)=1:
recurrence: S(n)= S(n/2)+1
-> S(n)=Θ(logn)

f(n)=logn:
recurrence: S(n)=S(n/2)+logn
-> S(n)= Θ((logn)^2)

f(n)=n:
recurrence: S(n)= S(n/2)+n
-> S(n)= Θ(n)

after implementing span_calc and running test_compare_span the empirical values mathced the asymptotic prediction
f(n)=1 span grew logarithmically
f(n)=logn span grew like (logn)^2
and f(n)=n span grew linearly in n
