# program to display incrementing values (standard, square, cubed)

def calc(arg):
    val_lst_1 = [item for item in range(1, 5)]
    val_lst_2 = [(item)**2 for item in val_lst_1]
    val_lst_3 = [(item) **3 for item in val_lst_1]

    return val_lst_1, val_lst_2, val_lst_3
    
    
    # print(val_lst_1)
    # print(val_lst_2)
    # print(val_lst_3)

def calc_input():
    # inputs 5-digit int from user 
    int_input = int(input("Please enter a 5 digit integer: "))
    lst = []
    while int_input > 0:
        digit = int_input % 10 # get the last digit 
        lst.append(digit)
        int_input = int_input // 10 # remove the last digit 
    lst.reverse() # reverse the list to get the digits in the correct order
    return lst 


def main():
    a, a2, a3 = calc(1)
    print(f'{"a":>2}\t {"a2":>2}\t {"a3":>2}')
    for item, item2, item3 in zip(a, a2, a3):
        print(f'{item:>2}\t {item2:>2}\t {item3:>2}')
    
    calculation = calc_input()
    print(calculation)
    print(1234 % 100)
        
    
main()


