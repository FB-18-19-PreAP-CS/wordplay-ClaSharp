def palin():
    for i in range(100000):
        num = str(i).zfill(6)
        if num[2:] == num[5:1:-1]:
            print(num)
    
if __name__ == "__main__":
    palin()