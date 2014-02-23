"""
Test patchy.py
"""
from patchy import patch

def hello_world():
    """
    Prints Hello World
    """
    print "Start"
    print "Hello World"
    print "End"

@patch(hello_world)
def hello_planet():
    """@@ -7,13 +7,14 @@\n llo_\n-wor\n+p\n l\n-d\n+anet\n ():%0A\n@@ -38,21 +38,22 @@\n s Hello \n-Wor\n+P\n l\n-d\n+anet\n %0A    %22%22%22\n@@ -92,13 +92,14 @@\n llo \n-Wor\n+P\n l\n-d\n+anet\n %22%0A  \n"""
    pass

def fib(n):
    """
    Calculates the Fibonacci sequence.
    """
    seq = [1, 1]
    for i in xrange(0, n):
        seq.append(seq[i] + seq[i + 1])
    return seq

@patch(fib)
def fib2(n):
    """@@ -4,13 +4,14 @@\n  fib\n+2\n (n):%0A\n     \n@@ -76,14 +76,14 @@\n  = %5B\n-1\n+2\n , \n-1\n+2\n %5D%0A"""
    pass
