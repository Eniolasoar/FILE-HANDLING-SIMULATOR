print("Welcome to Python File Handling Simulator( Using Access Modes)")
print("Choose what operation you would like to perform")
print("1. Writing(w)")
print("2. Appending(a)")
print("3. Reading(r)")
print("4. Read and Write(r+)")
print("5. Write and Read(w+)")
print("6. Append and Read(a+)")
print("7. Creation(x)")

try:
    user_response = int(input("Enter response here:"))
    if user_response == 1:
        print("1. Using write to create a file")
        print("2. Using write to overwrite an existing file ")
        user_response2 = int(input("Choose an action to simulate:"))
        if user_response2 == 1:
            file = open("myfile2.txt", "w")
            user_write = input("Input words to add:");
            file.write(user_write)
            file.close()

        elif user_response2 == 2:
            file = open("myfile.txt", "w")
            user_write2 = input("Input words to add:");
            file.write(user_write2)
            file.close()

    elif user_response==2:
        file=open("myfile.txt","a")
        user_append=input("Input words to add:")
        file.write(user_append)
        file.close()

    elif user_response==3:
        file=open("myfile.txt","r")
        print(file.read())
        file.close()

    elif user_response==4:
        file=open("myfile.txt","r+")
        print(file.read())
        user_write3 = input("Input words to add:");
        file.write(user_write3)
        file.close()

    elif user_response==5:
        file=open("myfile.txt","w+")
        user_write4 = input("Input words to add:");
        file.write(user_write4)
        print(file.read())
        file.close()

    elif user_response==6:
        file=open("myfile.txt","a+")
        user_write5 = input("Input words to add:");
        file.write(user_write5)
        fileContent=file.read()
        print(fileContent)
        file.close()

    elif user_response==7:
        user_response3=input("Enter file name to create:")
        file=open(user_response3,"x")
        print("File created")
        file.close()


except:
    print("Please enter a number")
