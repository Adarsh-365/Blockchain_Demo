import hashlib

def Mine(id,data,prev_hashed_value = ""):
   
   
    id = str(id)
    i = 0
    while(True):
        nonce = str(i)
        i+=1
        md = id + nonce + data +prev_hashed_value
        
        hashed_value = hashlib.sha256(md.encode()).hexdigest()
        # print(hashed_value[0:5])
        
        if hashed_value[0:4]=="0000":
           
            # print(hashed_value)
            break
    return nonce
    



