# Rail fence implementation in python
def RailFence(text, key): 
    rail = [['\n' for i in range(len(text))] for j in range(key)] 
    down = False 
    row, col = 0,0
    
    for i in range(len(text)): 
        if(row==0)or(row==key-1):
            down = not down
        rail[row][col] = text[i]
        col += 1 
        if down: 
            row += 1 
        else:
            row -= 1 
    encrypt = [] 
    for i in range(key):
        for j in range(len(text)): 
            if rail[i][j] != '\n':
                encrypt.append(rail[i][j]) 
    return("".join(encrypt)) 

def main():
    print("-- Rail Fence Cipher (Encryption) --") 
    text = input("Enter the plain text: ") 
    key = int(input("Enter the key value: ")) 
    print("Encrypted text: ", RailFence(text, key))

main()