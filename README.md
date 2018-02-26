# playing-with-python
I am having trouble with indentation in python, you have to be wary of whitespaces.
I learned how to do multiple line Strings. Either use non-indentation on the lines after the first as such :

ex

def print_lines():
    print("You have to watch out to not indent
on the subsequent lines")

If you want to skip lines you can use to line / :

ex

def print_lines():
    print("You can go to /
    line1 /
    line2 / line3 / etc...")

I added some exception handling and learned how to do that. Cool.
I was wondering if you could add several exceptions to a pass but realized that would be a bad idea as you would be able to identify which exception was caught.
