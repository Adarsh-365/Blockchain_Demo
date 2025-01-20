from django.shortcuts import render
import hashlib
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import mining

def home(request):
    print("fun")
    return render(request,"index.html")


@csrf_exempt
def hash(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        data = json.loads(request.body).get('data', '')
       
        hashed_value = hashlib.sha256(data.encode()).hexdigest() if data else ''
        return JsonResponse({'hashed_value': hashed_value})
       
    
    return render(request, 'hash.html')



@csrf_exempt
def block(request):
   
  
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        
        
        try:
          
            # Parse the incoming JSON data
            data = json.loads(request.body).get('data', '')
            id_value = json.loads(request.body).get('id', '')
            nonce_value = json.loads(request.body).get('nonce', '')
            
            Doactivity = json.loads(request.body).get('Doactivity','')
            print(Doactivity)
            if Doactivity == "Mine":
                nonce_value = mining.Mine(id_value,data)
          
            data = id_value+nonce_value+data
            hashed_value = hashlib.sha256(data.encode()).hexdigest() if data else ''
            # Your hashing logic here (replace with actual logic)
            # hashed_value = some_hashing_function(data)  # Replace with actual hashing logic

            # Return the hashed value as a JSON response
            return JsonResponse({'hashed_value': hashed_value,'nonce_val':nonce_value})
        except:
            pass
    return render(request, 'block.html')



@csrf_exempt
def blockchain(request):
    
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
            print("data")
      
            # Parse the JSON data from the request
            data = json.loads(request.body)
            #  id_list, data_list, nonce_list,prevhash_list,
            
            id_list = data['id_list']
            data_list = data['data_list']
           
           
            
            prevhash_list = data['prevhash_list']
            hashed_value_list = []
            prevhash_list_new = []
            prevhash_list_new.append("0000000000000000000000000000000000000000000000000000000000000000")
            mine = data.get('mine', 0)
            blockId = data.get('blockId',0)
            nonce_list = data['nonce_list']
            if mine == 1:
                
                id = blockId-1
                nonce_value = mining.Mine(id_list[id],data_list[id],prevhash_list[id])
                nonce_list[id]= nonce_value
            else:
                
                nonce_list = data['nonce_list']
                    
            current_hash = prevhash_list[0]
            for id in range(len(id_list)):
                input_string = f"{id_list[id]}{nonce_list[id]}{data_list[id]}{current_hash}"
                print(input_string)
                hashed_value = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
                current_hash = hashed_value
                hashed_value_list.append(hashed_value)
                prevhash_list_new.append(hashed_value)
                
            print(hashed_value_list)
            # prev_hashed_value = ""
            
            
            
            

            # Respond with the hashed value
            return JsonResponse({'hashed_value_list': hashed_value_list,"prevhash_list_new":prevhash_list_new,'nonce_list':nonce_list}, status=200)
       
    blocks = [
        {'id': 1, 'nonce': 11316, 'data': '', 'prev_hashed_value': '0000000000000000000000000000000000000000000000000000000000000000', 'hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf'},
        {'id': 2, 'nonce': 35230, 'data': '', 'prev_hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf', 'hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19'},
          {'id': 3, 'nonce': 12937, 'data': '', 'prev_hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19', 'hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf'},
        {'id': 4, 'nonce': 35990, 'data': '', 'prev_hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf', 'hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83'},
          {'id': 5, 'nonce': 56265, 'data': '', 'prev_hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83', 'hashed_value': '0000e4b9052fd8aae92a8afda42e2ea0f17972ea67cead67352e74dd6f7d217c'},
        
        # Add more blocks as needed
    ]
    return render(request, 'blockchain.html',{'blocks': blocks})

def distributed(request):
   
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
           
      
            # Parse the JSON data from the request
            data = json.loads(request.body)
            #  id_list, data_list, nonce_list,prevhash_list,
            
            id_list = data['id_be_list']
            # print(id_list)
            data_list = data['data_list']
           
           
            
            prevhash_list = data['prevhash_list']
            hashed_value_list = []
            prevhash_list_new = []
            prevhash_list_new.append("0000000000000000000000000000000000000000000000000000000000000000")
            mine = data.get('mine', 0)
            blockId = data.get('blockId',0)
            print(blockId)
            nonce_list = data['nonce_list']
            if mine == 1:
                
                id = blockId-1
                nonce_value = mining.Mine(id_list[id],data_list[id],prevhash_list[id])
                nonce_list[id]= nonce_value
            else:
                
                nonce_list = data['nonce_list']
                    
          
            for id in range(len(id_list)):
                if id==0 or id==5 or id==10:
                    current_hash = "0000000000000000000000000000000000000000000000000000000000000000"
               
                input_string = f"{id_list[id]}{nonce_list[id]}{data_list[id]}{current_hash}"
                # print(input_string)
                hashed_value = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
                current_hash = hashed_value
                hashed_value_list.append(hashed_value)
                prevhash_list_new.append(hashed_value)
                
            # print(hashed_value_list)
            # prev_hashed_value = ""
            
            
            
            

            # Respond with the hashed value
            return JsonResponse({'hashed_value_list': hashed_value_list,"prevhash_list_new":prevhash_list_new,'nonce_list':nonce_list}, status=200)
    
    
    
    
    blocks1 = [
        {'id': 1, 'nonce': 11316, 'data': '', 'prev_hashed_value': '0000000000000000000000000000000000000000000000000000000000000000', 'hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf'},
        {'id': 2, 'nonce': 35230, 'data': '', 'prev_hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf', 'hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19'},
        {'id': 3, 'nonce': 12937, 'data': '', 'prev_hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19', 'hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf'},
        {'id': 4, 'nonce': 35990, 'data': '', 'prev_hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf', 'hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83'},
        {'id': 5, 'nonce': 56265, 'data': '', 'prev_hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83', 'hashed_value': '0000e4b9052fd8aae92a8afda42e2ea0f17972ea67cead67352e74dd6f7d217c'},
     ]
    blocks2 = [{'id': 6, 'nonce': 11316, 'data': '', 'prev_hashed_value': '0000000000000000000000000000000000000000000000000000000000000000', 'hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf'},
        {'id': 7, 'nonce': 35230, 'data': '', 'prev_hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf', 'hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19'},
        {'id': 8, 'nonce': 12937, 'data': '', 'prev_hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19', 'hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf'},
        {'id': 9, 'nonce': 35990, 'data': '', 'prev_hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf', 'hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83'},
        {'id': 10, 'nonce': 56265, 'data': '', 'prev_hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83', 'hashed_value': '0000e4b9052fd8aae92a8afda42e2ea0f17972ea67cead67352e74dd6f7d217c'},
    ]
    blocks3 =[{'id': 11, 'nonce': 11316, 'data': '', 'prev_hashed_value': '0000000000000000000000000000000000000000000000000000000000000000', 'hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf'},
         {'id': 12, 'nonce': 35230, 'data': '', 'prev_hashed_value': '000015783b764259d382017d91a36d206d0600e2cbb3567748f46a33fe9297cf', 'hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19'},
         {'id': 13, 'nonce': 12937, 'data': '', 'prev_hashed_value': '000012fa9b916eb9078f8d98a7864e697ae83ed54f5146bd84452cdafd043c19', 'hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf'},
         {'id': 14, 'nonce': 35990, 'data': '', 'prev_hashed_value': '0000b9015ce2a08b61216ba5a0778545bf4ddd7ceb7bbd85dd8062b29a9140bf', 'hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83'},
         {'id': 15, 'nonce': 56265, 'data': '', 'prev_hashed_value': '0000ae8bbc96cf89c68be6e10a865cc47c6c48a9ebec3c6cad729646cefaef83', 'hashed_value': '0000e4b9052fd8aae92a8afda42e2ea0f17972ea67cead67352e74dd6f7d217c'},
        ]
    return render(request, 'distributed.html',{'blocks1': blocks1,'blocks2': blocks2,'blocks3': blocks3})





import hashlib
from django.shortcuts import render

def generate_block_data(block_id, nonce, transactions, prev_hash):
    """
    Generate block data including a hash based on its content.
    """
    # Convert transactions to a string representation for hashing
    tx_string = "".join([f"{tx['from']}->{tx['to']}:{tx['value']}" for tx in transactions])
    
    # Combine block details for hashing
    content = f"{block_id}{nonce}{tx_string}{prev_hash}"
    hashed_value = hashlib.sha256(content.encode()).hexdigest()
    
    return {
        "block_id": block_id,
        "nonce": nonce,
        "transactions": transactions,
        "prev_hash": prev_hash,
        "hash": hashed_value,
    }

def tokens(request):
    """
    View to render token.html with blockchain data.
    """
    # Example transactions for each block
    transactions_list = [
        [
            {"value": "25.00", "from": "Darcy", "to": "Bingley"},
            {"value": "4.27", "from": "Elizabeth", "to": "Jane"},
            {"value": "19.22", "from": "Wickham", "to": "Lydia"},
            {"value": "106.44", "from": "Lady Catherine de Bourgh", "to": "Collins"},
            {"value": "6.42", "from": "Charlotte", "to": "Elizabeth"},
        ],
        [
            {"value": "15.75", "from": "Alice", "to": "Bob"},
            {"value": "3.50", "from": "Charlie", "to": "Daisy"},
        ],
        [
            {"value": "50.00", "from": "Eve", "to": "Frank"},
            {"value": "5.25", "from": "Grace", "to": "Heidi"},
        ],
    ]

    # Initial values
    blocks = []
    prev_hash = "0000000000000000000000000000000000000000000000000000000000000000"

    # Generate blockchain data
    for i, transactions in enumerate(transactions_list, start=1):
        block_data = generate_block_data(block_id=i, nonce=100000 + i, transactions=transactions, prev_hash=prev_hash)
        blocks.append(block_data)
        prev_hash = block_data["hash"]  # Update the previous hash for the next block

    # Render the template with the blocks
    return render(request, "tokens.html", {"blocks": blocks})



def coinbase(request):
    return render(request, 'coinbase.html')


def keys(request):
    return render(request, 'public-private-keys/keys.html')

def signature(request):
    return render(request, 'public-private-keys/signature.html')

def transactions(request):
    return render(request, 'public-private-keys/transactions.html')

def blockchainpub(request):
    return render(request, 'public-private-keys/blockchainpub.html')