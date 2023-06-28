##############
def fold_left(function, acc, iter):
    match iter:
        case []:
            return acc
        case [head, *tail]:
            return fold_left(function, function(acc, head), tail)
##############


def forall(pred, iter):
    return fold_left((lambda x,y : x and pred(y)), True, iter)

def exists(pred, iter):
    return fold_left((lambda x,y : x or pred(y)), True, iter)

def atleast(n, pred, iter):
    return fold_left((lambda x,y : x + int(pred(y))), 0, iter) >= n

def atmost(n, pred, iter):
    return fold_left((lambda x,y : x + int(pred(y))), 0, iter) <= n

if __name__=="__main__":
    print(forall(lambda x : x%2==0, [2,4,6,8]))
    print(exists(lambda x : x%2==0, [1,2,5,7,9]))
    print(atleast(2, lambda x : x%2==0, [1,2,5,8,9]))
    print(atmost(1, lambda x : x%2==0, [1,2,5,8,9]))
