def print_number_args_qword(num):
    if num % 8 != 0:
        print("Number of bytes not rounded to QWORD!")
        return 
    size = int(num/8)
    for i in range(0, size):
        print("     __int64 member%d;" % (8*i))
       
def main():
    num = int(input("Insert the number of bytes to print: "))
    print("struct Test {")
    print_number_args_qword(num)
    print("};")
	
if __name__ == "__main__":
	main()
    
