#input_problem = [0,2,7,0]
input_problem = [10,3,15,10,5,15,5,15,9,2,5,8,5,2,3,6]
biggest_bank = max(input_problem)
input_problem_length = len(input_problem)
biggest_bank_index = None
config = []
latest_config = None
redistribution_counter = 0
recounter = 0

for i, val in enumerate(input_problem):
    if val == biggest_bank:
        biggest_bank_index = i
        break

start_at = biggest_bank_index + 1
second_loop_endat = biggest_bank_index + 1

while latest_config != config:
    input_problem[biggest_bank_index] = 0
    #print(input_problem)
    while biggest_bank > 0:
        #import pdb;pdb.set_trace()
        for i in range(start_at, input_problem_length):
            if biggest_bank > 0:
                input_problem[i] += 1
                biggest_bank -= 1

        for i in range(0, start_at):
            if biggest_bank > 0:
                input_problem[i] += 1
                biggest_bank -= 1
    #print(input_problem)
    
    redistribution_counter += 1
    #if redistribution_counter > 177:
        #import pdb;pdb.set_trace()
    d = input_problem[:]
    #print(d)
    exit
    config.append(d)
    if config.count(input_problem) > 1:
        recounter += 1
    if config.count(input_problem) == 3:
        print("input: %s" % input_problem)
        break
    
        #print("config is before %s" % config)
       
        #print("config is %s" % config)
    
    biggest_bank = max(input_problem)

    for i, val in enumerate(input_problem):
        #import pdb;pdb.set_trace()
        if val == biggest_bank:
            biggest_bank_index = i
            start_at = biggest_bank_index + 1
            if start_at >= input_problem_length:
                start_at = 0
            break

print(redistribution_counter-recounter+1)
print(recounter-1)