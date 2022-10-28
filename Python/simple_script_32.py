def print_number_args_dword(num):
    if num % 4 != 0:
        print("Number of bytes not rounded to DWORD!")
        return 
    size = int(num/4)
    for i in range(0, size):
        print("     DWORD member%d;" % (4*i))
       
def main():
    num = int(input("Insert the number of bytes to print: "))
    print("struct Test {")
    print_number_args_dword(num)
    print("};")
	
if __name__ == "__main__":
	main()
    
