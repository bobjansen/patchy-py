patchy.py
=========

Patchy.py allows you to keep define a Python function as the result of another
function and a diff.

How to use?
===========

The easiest way to define patched functions by putting both them in a temporary
file and running patchy.create\_patch() on them like this

    $ edit tmp.py
    $ python
    > import patchy
    > import tmp
    > patch.create_patch(tmp.fun1, tmp.fun2)
      Copy the patch that is
    > exit()
    $ edit tmp.py
      Remove the body of fun2
      Put the patch in the doc string

See test.py for example patched files.


When?
=====
When you just can't keep your code dry.

Why?
====

Why not?

