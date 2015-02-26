#something something something
def similarity(x, y):
    score = 0
    if x[0] == y[0]: #first letter
        score += 10
    if x[-1] == y[-1]: #last letter
        score += 10
    if len(x) < len(y):
        score += float(len(x))/len(y) * 30
    else:
        score += float(len(y))/len(x) * 30
    ccommon= count_common(x,y)
    unique =count_unique(x,y)
    score += float(ccommon)/unique * 50

    return round(score,3)
	print score

def count_unique(x,y):
    uni_str=""  #start with an empty string
    for char in x: #go through every letter in x
        if char not in  uni_str: #if itis not already in the string
            uni_str += char #add it
    for char in y: # do the same for every letter in y
        if char not in uni_str:
            uni_str += char
    return len(uni_str) #return the number of characters in this str.

def count_common(x,y):
    uni_str=""  #start with an empty string
    count =0
    for char in x: #go through every letter in x
        if char not in  uni_str: #if itis not already in the string
            uni_str += char #add it
    for char in y: # do the same for every letter in y
        if char not in uni_str:
            uni_str += char

    for char in uni_str:
        if char in x and char in y:
            count+= 1
    return count


    """
    for common, you will have to start by getting the unique letters (using the code above)
    go through each of these letters with a for loop
        if the char is in x and in y, add to count
    return count
    """
print similarity("friend", "fred")
assert(similarity("friend","fred")==73.333),"Not quite right"
assert(similarity("eliza", "liz")==48.0),"Not there yet"

print "All tests passed! Contact Mr. Deakyne for further help."