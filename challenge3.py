with open("challenge3.txt", "r") as binaries:
    binlist = binaries.read().split()
# part 1
zeros = 0
ones = 0
twozeros = 0
twoones = 0
threezeros = 0
threeones = 0
fourzeros = 0
fourones = 0
fivezeros = 0
fiveones = 0
for i in binlist:
    if(i.startswith("0")):
        zeros = zeros + 1
    if(i.startswith("1")):
        ones = ones + 1
    if(i[1] == "0"):
        twozeros = twozeros + 1
    if(i[1] == "1"):
        twoones = twoones + 1
    if(i[2] == "0"):
        threezeros = threezeros + 1
    if(i[2] == "1"):
        threeones = threeones + 1
    if(i[3] == "0"):
        fourzeros = fourzeros + 1
    if(i[3] == "1"):
        fourones = fourones + 1
    if(i[4] == "0"):
        fivezeros = fivezeros + 1
    if(i[4] == "1"):
        fiveones = fiveones + 1
if(zeros != None and ones != None and twozeros != None and twoones != None and threezeros != None and threeones != None and fourzeros != None and fourones != None and fivezeros != None and fiveones != None):
    if(zeros > ones):
        # do thing
        dig1 = "0"
    else:
        dig1 = "1"
    if(twozeros > twoones):
        dig2 = "0"
    else:
        dig2 = "1"
    if(threezeros > threeones):
        dig3 = "0"
    else:
        dig3 = "1"
    if(fourzeros > fourones):
        dig4 = "0"
    else:
        dig4 = "1"
    if(fivezeros > fiveones):
        dig5 = "0"
    else:
        dig5 = "1"

    gamma = str(dig1) + str(dig2) + str(dig3) + str(dig4) + str(dig5)

# epsilon
zeros = 0
ones = 0
twozeros = 0
twoones = 0
threezeros = 0
threeones = 0
fourzeros = 0
fourones = 0
fivezeros = 0
fiveones = 0
for i in binlist:
    if(i.startswith("0")):
        zeros = zeros + 1
    if(i.startswith("1")):
        ones = ones + 1
    if(i[1] == "0"):
        twozeros = twozeros + 1
    if(i[1] == "1"):
        twoones = twoones + 1
    if(i[2] == "0"):
        threezeros = threezeros + 1
    if(i[2] == "1"):
        threeones = threeones + 1
    if(i[3] == "0"):
        fourzeros = fourzeros + 1
    if(i[3] == "1"):
        fourones = fourones + 1
    if(i[4] == "0"):
        fivezeros = fivezeros + 1
    if(i[4] == "1"):
        fiveones = fiveones + 1
if(zeros != None and ones != None and twozeros != None and twoones != None and threezeros != None and threeones != None and fourzeros != None and fourones != None and fivezeros != None and fiveones != None):
    if(zeros < ones):
        # do thing
        dig1 = "0"
    else:
        dig1 = "1"
    if(twozeros < twoones):
        dig2 = "0"
    else:
        dig2 = "1"
    if(threezeros < threeones):
        dig3 = "0"
    else:
        dig3 = "1"
    if(fourzeros < fourones):
        dig4 = "0"
    else:
        dig4 = "1"
    if(fivezeros < fiveones):
        dig5 = "0"
    else:
        dig5 = "1"

    epsilon = str(dig1) + str(dig2) + str(dig3) + str(dig4) + str(dig5)
    finalint = int(epsilon, 2) * int(gamma, 2)
    print(finalint)