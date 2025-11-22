import random,  os

user_int = ["Technology & Programming" ,"Gaming & Game Dev","Art & Design"]

# print("i will do it insha allah")

def path(name):
    
    file_path = name + ".txt"
    
    ct_path = os.path.join("asset","question", file_path)

    if not os.path.exists(ct_path):
        print("not found",ct_path)
    return ct_path

def extract_block(data):
    
    block = []
    current = []
    
    for line in data:
            
        line = line.strip()
        if not line:
            continue
        
        if line.endswith("?"):
            # if current:
            #     block.append(current)
            current = [line[2:].strip()]

        if line.startswith(("A)", "B)", "C)", "D)")):
            options = line[2:].replace("correct", "").strip()
            if current:
                current.append(options)
            
        if len(current) == 5:
            block.append(current)
            current = []
            
    return block

def game_loop():
    
    while True:    
        random.shuffle(user_int)
        file_path = path(user_int[0])
        
        with open(file_path,"r") as f :
            data = f.readlines()

        random.shuffle(data)
        blocks = extract_block(data)
            
        asked_file = "asset/question/asked_question.txt"
        random.shuffle(blocks)

        with open(asked_file, "r") as f:
            asked = f.read()     
            
        for block in blocks:
            b = str(block)
            if b not in asked:
                with open(asked_file, "a") as f:
                    f.write(b + "\n") 
                    
                    # print("New question stored.", block)
                    
                    return block


print(game_loop())
