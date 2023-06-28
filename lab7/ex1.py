def acronym(list_of_strings):
    return "".join(map(lambda x : x[0], list_of_strings))

def median(list_of_number):
    def mean_or_elem(even, list_of_number):
        match even:
            case True:
                return (list_of_number.pop(0) + list_of_number.pop(0))/2
            case False:
                return list_of_number.pop(1)
    list_of_number.sort()
    return mean_or_elem((length:=len(list_of_number))%2==0, list_of_number[length//2 - 1:])                

def sqr_Newton(x, epsilon):
    def sqr_Newton_in(x, epsilon, y):
        match abs(y**2 - x) < epsilon:
            case True:
                return y
            case False:
                return sqr_Newton_in(x, epsilon, (y + x/y) / 2)
    return sqr_Newton_in(x, epsilon, x)

def char_finder2(sentence):
    def add_word_to_char(dic, char, word, is_in_dic):
        match is_in_dic:
            case True:
                dic[char] += [word]
            case False:
                dic.update({char : [word]})
        return dic
    def add_word(dic, chars, word):
        match chars:
            case []:
                return dic
            case [head, *tail]:
                return add_word(add_word_to_char(dic, head, word, head in dic), tail, word)
    def add_to_dic(dic, words):
        match words:
            case []:
                return dic
            case [head, *tail]:
                return add_to_dic(add_word(dic, [*head], head), words[1:])
    return add_to_dic({}, sentence.split())


def flatten(not_flat_list):
    def flatten_in(not_flat_list, flat_list):
        match not_flat_list:
            case []:
                return flat_list
            case [head, *tail]:
                return flatten_in(tail, flat_list+flatten_in(head, []))
            case x:
                return [x]
    return flatten_in(not_flat_list, [])

if __name__=="__main__":
    result = acronym(["Zakład", "Ubezpieczeń", "Społecznych"])
    if result:
        print(result)
    else:
        print("Oj coś nie tak")

    print(str(sqr_Newton(3, epsilon = 0.1)))

    print(median([1,2,3,4,5,6,7,8,9]))

    print(char_finder2("on i ona"))

    print(flatten([1, [2, 3], [[4, 5], 6]]))
