def longest_substring(a_string, hops):
    result = 0
    result2 = 0
    for i in range(len(a_string)):
        if hops == a_string[i]:
            result = result + 1
            if result > result2:
                result2 = result
        else:
            result = 0
    return result2

final = longest_substring('akaaakaaaaakaa', 'a')

print(final)
