def LucasNum(start, stop, step):
    """ (int,int,int) -> list of integers

    Input: This function is passed start (>= 0), stop (>start), and step (>= 1) values that define a sequence of numbers.
    Output: This function returns a list of the corresponding Lucas Numbers.

    >>>LucasNum(0,6,1)
    [2, 1, 3, 4, 7, 11]
    >>>LucasNum(2,6,2)
    [3, 7]
    """
    def Lucas(num):
        if num == 0 :
            result = 2
        elif num == 1:
            result = 1
        else:
            result  = Lucas(num-1)+Lucas(num-2)
        return result
    numbers = range(start, stop, step)
    numb = []
    for number in numbers:
        numb.append(number)
    output = []
    for n in numb:
        output.append(Lucas(n))
    return output