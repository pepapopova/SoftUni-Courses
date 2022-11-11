def negative_and_positives(*args):
    sum_negatives = 0
    sum_positives = 0
    for num in args:
        if num > 0:
            sum_positives += num
        else:
            sum_negatives += num
    return sum_positives, sum_negatives


numbers = [int(x) for x in input().split()]
positives, negatives = negative_and_positives(*numbers)  #this * unpacks the list to tuple
print(negatives)
print(positives)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")