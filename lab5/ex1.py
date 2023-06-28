import ex2
import ex3
import ex4

def read_ssh(file='SSH.log', line_reader=True, function=str, min_level=None):
    logs = []
    with open(file) as f:
        for line in f:
            line_to_dic = ex2.to_dictionery(line)
            logs.append(line_to_dic)
            ex3.show_log(line, min_level)
            if line_reader:
                
                if value := function(line_to_dic):
                    print(value)
            
    if not line_reader:
        print(function(logs))
    return logs

if __name__=='__main__':
    print(read_ssh())
