current_position = 0
skip_length = 0
input_List = []
for num in range(0, 256):
    input_List.append(num)
input_list_length = len(input_List)
input_string = "206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3"
input_lengths = []
for character in input_string:
    input_lengths.append(ord(character))
input_lengths.append(17)
input_lengths.append(31)
input_lengths.append(73)
input_lengths.append(47)
input_lengths.append(23)

for round in range(0, 64):
    for i in range(0, len(input_lengths)):
        traverse_sublist_length = input_lengths[i]
        sublist = []
        for j in range(0, traverse_sublist_length):
            pickup_index = current_position + j
            if pickup_index >= input_list_length:
                pickup_index = pickup_index - input_list_length
            sublist.append(input_List[pickup_index])
            
        sublist.reverse()
        for k in range(0, traverse_sublist_length):
            insert_index = current_position + k
            if insert_index >= input_list_length:
                insert_index = insert_index - input_list_length
            input_List[insert_index] = sublist[k]
        
        current_position_move = traverse_sublist_length + skip_length

        for move in range(0, current_position_move):
            current_position += 1
            if current_position > input_list_length:
                current_position = current_position - input_list_length

        skip_length += 1

dense_hash = []
a=0
b=16
for slot in range(0, 255, 16):
    list_is = input_List[a:b]
    a=b
    b=b+16
    xor_result = None
    for j in range(0, 16, 2):
        if not xor_result:
            xor_result = list_is[j] ^ list_is[j+1]
        else:
            xor_result = xor_result ^ list_is[j] ^ list_is[j+1]
    dense_hash.append(xor_result)

final_result = ''
print(dense_hash)
for num in dense_hash:
    final_result = final_result + hex(num)[2:]

print(final_result)


    
        

