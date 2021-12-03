with open("challenge3.txt", "r") as binaries:
    binlist = binaries.read().split()
# part 1
zeros = None
ones = None
for i in binlist:
    if(i.startswith("0")):
        zeros = zeros + 1
    else:
        ones = ones + 1
if(zeros > ones):
    # do thing
    print("part 1:", zeros)