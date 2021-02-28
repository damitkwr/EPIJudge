from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    no_string = str(n)
    returnList = []
    previous_character = no_string[0]
    counter = 1
    if len(no_string) == 1:
        return str(counter)+no_string[0]

    for i in range(1, len(no_string)):
        if no_string[i] != previous_character:
            returnList.append(str(counter))
            returnList.append(previous_character)
            counter = 1
            previous_character = no_string[i]
        else:
            counter += 1        
    
    if returnList[-1] != no_string[-1]:
        returnList.append(str(counter))
        returnList.append(previous_character)
    
    return "".join(returnList)


    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
