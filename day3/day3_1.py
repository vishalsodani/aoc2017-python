def print_result(num, start_row, start_col):
    if num == 347991:
        print(str(start_row) + ", " + str(start_col))

start_num = 1
start_row = 0
start_col = 0
add_num = 3

for i in range(2, 591):
    pattern = 'LDR'
    if i % 2 == 0:
        pattern = 'RUL'
    step = add_num - 2
    # #import pdb;pdb.set_trace()
    #total_loop = add_num
    
    #import pdb;pdb.set_trace()
    for j in range(0, 1):
        start_reducing = True
        for direction in pattern:
            if direction == 'R': 
                if  i % 2 == 0:
                    start_col += 1
                    start_num += 1
                    print_result(start_num, start_row, start_col)
                    # print(start_num)
                    # print(str(start_row) + ", " + str(start_col))
                else:
                    r_reduce = True
                    for down in range(0, step):
                        if start_col == 0:
                            r_reduce = False
                        if start_col >= 0 and r_reduce == False:
                            start_col += 1
                            start_num += 1
                            print_result(start_num, start_row, start_col)
                            #print(start_num)
                            #print(str(start_row) + ", " + str(start_col))
                        else:
                            start_col -= 1
                            start_num += 1
                            print_result(start_num, start_row, start_col)
                            #print(start_num)
                            #print(str(start_row) + ", " + str(start_col))
            u_reduce = True
            for down in range(0, step):
                if direction == 'U' and i % 2 == 0:
                    if u_reduce and start_row != 0:
                        start_row -= 1
                        start_num += 1
                        print_result(start_num, start_row, start_col)
                        #print(str(start_row) + ", " + str(start_col))
                        if start_row == 0:
                            u_reduce = False
                    else:
                        start_row += 1
                        start_num += 1
                        print_result(start_num, start_row, start_col)
                        #print(str(start_row) + ", " + str(start_col))

            if direction == 'L':
                l_reduce = True
                if i%2 == 0:
                    for down in range(0, step):
                        if l_reduce:
                            start_col -= 1
                            start_num += 1
                            print_result(start_num, start_row, start_col)
                            #print(str(start_row) + ", " + str(start_col))
                            if start_col == 0:
                                l_reduce = False
                        else:
                            start_col += 1
                            start_num += 1
                            print_result(start_num, start_row, start_col)
                            #print(str(start_row) + ", " + str(start_col))
                else:
                    start_col += 1
                    start_num += 1
                    print_result(start_num, start_row, start_col)
                    #print(start_num)
                    #print(str(start_row) + ", " + str(start_col))
            d_reduce = True
            for down in range(0, step):
                if direction == 'D':
                    if start_row > 0 and d_reduce:
                        start_row -= 1
                        start_num += 1
                        print_result(start_num, start_row, start_col)
                        #print(start_num)
                        #print(str(start_row) + ", " + str(start_col))
                        if start_row == 0:
                            d_reduce = False
                    else:
                        start_row += 1
                        start_num += 1
                        print_result(start_num, start_row, start_col)
                        #print(start_num)
                        #print(str(start_row) + ", " + str(start_col))
                
                    # if start_row == 0:
                    #     start_row += 1
                        
                    # else:
                    #     if start_row == 1:
                    #         start_row = 0
                    #         start_num += 1
                    #         print(start_num)
                    #         print(str(start_row) + ", " + str(start_col))
                    #     else:
                    #         start_row -= 1
                    #         start_num += 1
                    #         print(start_num)
                    #         print(str(start_row) + ", " + str(start_col))
            
            
        
    add_num += 1
    
