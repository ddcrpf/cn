print("""
def divide(div,divisor,rem):
    cur=0
    while True:
        for i in range(len(divisor)):
            rem[cur+i]^=divisor[i]
        while rem[cur]==0 and cur!=len(rem)-1:
            cur+=1
        if len(rem)-cur<len(divisor):
            break
        return rem
data_bit=int(input("ENTER NUMBER OF DATA BITS:"))
data=[int(input(f"Enter data but{i+1}:")) for i in range(data_bit)]

divisor_bit=int(input("ENTER NUMBER OF DIVISOR BITS:"))
divisor=[int(input(f"Enter divisor but{i+1}:")) for i in range(divisor_bit)]

tot_length= data_bit +divisor_bit-1

div= data+[0]* (divisor_bit-1)
rem=div.copy()
crc=[0]*len(div)

print("Dividend (after appending 0's) are :",div)
rem= divide(div,divisor,rem)

crc=[div[i]^rem[i]for i in range(len(div))]
print("\n CRC code:")
print("".join(map(str,crc)))
crc_input= [int(input(f"Enter CRC bit{i+1} of {tot_length}bits:"))for i in range(tot_length)]
for j in range(len(crc)):
    rem[j]==crc[j]
rem= divide(crc,divisor,rem)
error_detected = any(rem[i]!=0 for i in range(len(rem)))
if error_detected:
    print("Error")
else:
    print("No Error")
               

output -- 
Enter number of data bits: 7
Enter data bit: 1
Enter data bit: 0
Enter data bit: 1
Enter data bit: 1
Enter data bit: 0
Enter data bit: 0
Enter data bit: 1
Enter number of bits in divisor: 3
Enter divisor bit: 1
Enter divisor bit: 0
Enter divisor bit: 1
Dividend (after appending 0's): [1, 0, 1, 1, 0, 0, 1, 0, 0]
CRC code: [1, 0, 1, 1, 0, 0, 1, 1, 1]
Enter CRC code of 9 bits: 1
Enter CRC code of 9 bits: 0
Enter CRC code of 9 bits: 1
Enter CRC code of 9 bits: 1
Enter CRC code of 9 bits: 0
Enter CRC code of 9 bits: 0
Enter CRC code of 9 bits: 1
Enter CRC code of 9 bits: 1
Enter CRC code of 9 bits: 1
No Error""")