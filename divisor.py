ourdivisor = 10
ourdividend = 50
quotient = 0
tempnumber = 0

sign = (-1 if((ourdividend < 0) ^ (ourdivisor < 0)) else 1);

for i in range(31, -1, -1):
    if tempnumber + (ourdivisor << 1) <= ourdividend:
        tempnumber += ourdivisor << 1
        quotient |= 1 << i
print("final quotient is", quotient)
