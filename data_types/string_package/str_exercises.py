# https://www.w3resource.com/python-exercises/string/

# Write a Python method to count the number of characters (character frequency) in a string.
def count_character_frequency(input:str):
    print('Find char frequency in given input string -',input)
    char_sequence: dict = {}
    for ch in input:
        if ch in char_sequence:
            char_sequence[ch] += 1
        else:
            char_sequence[ch] = 1
    print(char_sequence)

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string
def construct_str_with_first_and_last_2_chars(input:str):
    print('\nConstruct string with first and last 2 chars from given input -',input)
    length=len(input)
    if length>2:
        new_name=input[0:2]+input[length-2:length]
        print('Given input length is less than 2. So Output is',new_name)
    else:
        print('Given input length is less than 2. So Output is empty string.')

# Write a Python program to get a string from a given string where all occurrences of the char have been
# changed to '$', except the first time itself
def string_manipulation(input:str):
    print('String manipulation - Given INPUT-',input)
    temp=input
    for ch in input:
        if input.count(ch)>1:
            initial_index=input.index(ch)
            temp=temp.replace(ch,'$')
            temp_list=list(temp)
            temp_list[initial_index]=ch
            temp="".join(temp_list)
    print('Output-',temp)


def main():
    print('main method execution starts !!')
    #count_character_frequency('google.com')
    #construct_str_with_first_and_last_2_chars('SU')
    #construct_str_with_first_and_last_2_chars('Sundar')
    string_manipulation('abababababc')

if '__main__' == __name__:
    main()
