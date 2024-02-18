"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb


def longest_run(mylist, key):

    count = 0
    max_count = 0

    for i in mylist:
        if i == key:
            count += 1
        else:
            count = 0
        max_count = max(count, max_count)

    return max_count


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    if len(mylist) == 0:
        return Result(0, 0, 0, True) #Base Case with empty list
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True) #Base Case with one element in list
        else:
            return Result(0, 0, 0, False)

    mid = len(mylist)//2 #Sets middle of list
    left = longest_run_recursive(mylist[:mid], key) #Recursive calls for each side
    right = longest_run_recursive(mylist[mid:], key)

    is_entire_range = left.is_entire_range and right.is_entire_range #True if whole list is key
    left_size = left.left_size
    right_size = right.right_size

    if mylist[mid-1] == key and mylist[mid] == key: #Check for runs that go through split between left and right
        cross_run = left.right_size + right.left_size

    else:
        cross_run = 0
    
    if left.is_entire_range: #combine results from both sides
        left_size += right.left_size
    if right.is_entire_range:
        right_size += left.right_size

    longest_run = max(left.longest_size, right.longest_size, cross_run)

    return Result(left_size, right_size, longest_run, is_entire_range)

