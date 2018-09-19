#Ashley Rackley / HW3 / 9/18/2018

#decode1 = 0x0140
#decode2 = 0x0640
#decode3 = 0x0960
#decode4 = 0x0c80

MF = .03125
decode1 = int("0x0140",16)
decode1 = decode1*MF
print (decode1)

decode2 = int("0x0640",16)
decode2 = decode2*MF
print (decode2)

decode3 = int("0x0960",16)
decode3 = decode3*MF
print (decode3)

decode4 = int("0x0c80",16)
decode4 = decode4*MF
print (decode4)

