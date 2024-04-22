#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
def strings(array_of_strings):
    count = 0 
    for stringg in array_of_strings:
        if len(stringg) >= 2 and stringg[0] == stringg[-1]:
            count += 1 
    return count

samplelist = ['aba','hah','wer']
result = strings(samplelist)
print(result)