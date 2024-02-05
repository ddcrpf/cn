print("""import time 


def leaky_baucket():
    bucketsize = int(input("Enter bucket Size:"))
    outgoing = int(input("Enter outgoing rate:"))
    n = int(input("Enter the number of inputs: "))
    
    
    store = 0
    
    while n!=0:
        incoming = int(input("Incoming size is: "))
        print("Bucket buffer size is {} out of {}". format(store, bucketsize))
        
        
        if incoming<= (bucketsize- store):
            store += incoming
            print("Bucket buffer size is {} out of {}". format(store, bucketsize))
            
        else: 
            print("Packet loss : {}".format(incoming - (bucketsize - store)))
            store = bucketsize
            print("Bucket size is {} out of {}".format(store, bucketsize))
            
        store -= outgoing
        print("After outgoing: {} packets left out of {} in buffer ".format(store, bucketsize))
        
        n-=1
        time.sleep(3)

if __name__ == "__main__":
    leaky_baucket()
    
    

output -- 
    
Enter bucket Size:300
Enter outgoing rate:50
Enter the number of inputs: 2
Incoming size is: 200
Bucket buffer size is 0 out of 300
Bucket buffer size is 200 out of 300
After outgoing: 150 packets left out of 300 in buffer 
Incoming size is: 200
Bucket buffer size is 150 out of 300
Packet loss : 50
Bucket size is 300 out of 300
After outgoing: 250 packets left out of 300 in buffer 
    """)