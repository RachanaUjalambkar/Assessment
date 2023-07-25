import copy
print("enter a string",end = '-')
string = input()
listInput = [char for char in string]
asciConverted = []
result = []
for i in listInput:
    asciConverted.append(ord(i))                    #To get ASCII values of all characters in string
cop = copy.copy(asciConverted)
for pos,ele in enumerate(asciConverted):
    if(pos == 0):
        if(ele % 2 != 0):                    # To check whether 1st element is odd
            continue
    else:
        if(str(ele).isascii()):              #To check whether the given value is valid ASCII value
            if(pos + 1 == len(asciConverted)):        #To check if last element is even and change it to 83
                asciConverted[pos] = ele = 83
            if(ele % 2 == 0):
                valuee = ele % 7
                newe = asciConverted[pos+1] + valuee
                if(str(newe).isascii()):
                    asciConverted[pos+1] = newe
                else:
                    asciConverted[pos+1] = 83
            else:
                if(cop[pos-1] == asciConverted[pos-1]):  # To check whether the previous element is already changed
                    valueo = ele % 5
                    newo = asciConverted[pos-1] - valueo
                    if(str(newo).isascii()):
                        asciConverted[pos-1] = newo
                    else:
                        asciConverted[pos-1] = 83

                else:
                    continue
        else:
            asciConverted[pos] = 83 #If the new number is an invalid ASCII value, replace it with 83.
            continue
for i in asciConverted:
    result.append(chr(i))
print("".join(result))

