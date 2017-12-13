from collections import Counter

good_p = 0
bad_p = 0
problem_input = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj"""


input_data = problem_input.split('\n')

for item in input_data:
    
    cnt = Counter()
    break_outside = False
    split_ct = item.split(' ')
    split_ct_length = len(split_ct)
    start_at = 0
    for d in split_ct:
        if break_outside:
            break
        d_length = len(d)
        start_at += 1
        cnt[d] += 1
        if cnt[d] > 1:
            #print(d)
            bad_p += 1
            break
        
        for j in range(start_at, split_ct_length):
            item_chk = split_ct[j]
            item_chk_length = len(item_chk)
            if item_chk_length == d_length:
                print('checking %s' % item_chk_length)
                print('checking %s against %s' % (item_chk, d))
                itc = ''.join(sorted(item_chk))
                dtc = ''.join(sorted(d))
                if itc == dtc :
                    print("found anagram %s %s", (itc,dtc))
                    bad_p += 1
                    break_outside = True
                    break

print(len(input_data))
print(bad_p)
print(len(input_data)-bad_p)

#last incorrect 314