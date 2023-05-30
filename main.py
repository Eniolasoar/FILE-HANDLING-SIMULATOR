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
        print("\nWriting is the process of adding content to a file.It operates in two forms:")
        print("\t1. Using write to create a file")
        print("\t2. Using write to overwrite an existing file \n")
        user_response2 = int(input("Choose an action to simulate:"))
        if user_response2 == 1:
            print("\nNote first that you are trying to write to 'myfile2.txt' which doesn't exist.Therefore,it is being created")
            file = open("myfile2.txt", "w")
            user_write = input("\nInput words to add:")
            file.write(user_write)
            print("Check the file created(myfile2.txt) and the content you added")
            file.close()

        elif user_response2 == 2:
            print("First check the file content in the directory(myfile.txt)")
            user_check = input("File checked?")
            if user_check == "yes":
                file = open("myfile.txt", "w")
                user_write2 = input("Input words to add:")
                file.write(user_write2)
                print("Now check the file.Notice that the previous file was deleted and the "
                      "only content there is the one you just wrote")
                file.close()



    elif user_response == 2:
        print(
            "Appending is for adding content to an existing file content.Unlike writing,it never overwrites an existing file content")
        print("Below is a demonstration:")
        print("First check the content of myfile.txt")
        user_check2 = input("File checked?")
        if user_check2 == "yes":
            file = open("myfile.txt", "a")
            user_append = input("Input words to add:")
            file.write(user_append)
            print("Check the file again.You would notice the words was added to the end of the last file content")
            print("Try running the write operation to see the differences between writing and appending")
            file.close()

    elif user_response == 3:
        print("Reading is another way of saying you would like to see the content of the file")
        print("Below is the content of myfile.txt")
        file = open("myfile.txt", "r")
        print(file.read())
        file.close()

    elif user_response == 4:
        print("The read and write mode helps you to first see the content of your file first before overwriting"
              "it with a new data")
        file = open("myfile.txt", "r+")
        print(file.read())
        print("ABOVE IS THE CONTENT OF THE FILE BEFORE USING THE WRITE OPERATION")
        user_write3 = input("Input words to add:")
        file.write(user_write3)
        print(" THE NEW FILE CONTENT:")
        print("Notice that the old content in the file was overwritten with the new one")
        file.close()

    elif user_response == 5:
        print("The w+ allows you to overwrite an existing file and then see the content of the file")
        print("First check the content of the myfile.txt in your directory")
        file = open("myfile.txt", "w+")
        user_write4 = input("Input words to add:")
        file.write(user_write4)
        print("Notice that the existing file content was deleted.Below is the new file content:")
        print(file.read())
        file.close()

    elif user_response == 6:
        print("The a+ is similar to the w+ only that it doesn't overwrite the existing file")
        file = open("myfile.txt", "a+")
        user_write5 = input("Input words to add:")
        file.write(user_write5)
        fileContent = file.read()
        print(fileContent)
        file.close()

    elif user_response == 7:
        user_response3 = input("Enter file name to create:")
        file = open(user_response3, "x")
        print("File created")
        file.close()

    while True:
        user_response4 = input("\nWOULD YOU LIKE TO TEST RUN ANOTHER FILE HANDLING OPERATION(yes/no):")
        response_convert=user_response4.lower()
        if response_convert == "yes":
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
                    print("Writing is the process of adding content to a file.It operates in two forms:")
                    print("1. Using write to create a file")
                    print("2. Using write to overwrite an existing file ")
                    user_response2 = int(input("Choose an action to simulate:"))
                    if user_response2 == 1:
                        file = open("myfile2.txt", "w")
                        user_write = input("Input words to add:")
                        file.write(user_write)
                        print("Check the file created and the content you added")
                        file.close()

                    elif user_response2 == 2:
                        print("First check the file content in the directory(myfile.txt)")
                        user_check = input("File checked?")
                        if user_check == "yes":
                            file = open("myfile.txt", "w")
                            user_write2 = input("Input words to add:")
                            file.write(user_write2)
                            print("Now check the file.Notice that the previous file was deleted and the "
                                  "only content there is the one you just wrote")
                            file.close()



                elif user_response == 2:
                    print(
                        "Appending is for adding content to an existing file content.Unlike writing,it never overwrites an existing file content")
                    print("Below is a demonstration:")
                    print("First check the content of myfile.txt")
                    user_check2 = input("File checked?")
                    if user_check2 == "yes":
                        file = open("myfile.txt", "a")
                        user_append = input("Input words to add:")
                        file.write(user_append)
                        print(
                            "Check the file again.You would notice the words was added to the end of the last file content")
                        print("Try running the write operation to see the differences between writing and appending")
                        file.close()

                elif user_response == 3:
                    print("Reading is another way of saying you would like to see the content of the file")
                    print("Below is the content of myfile.txt")
                    file = open("myfile.txt", "r")
                    print(file.read())
                    file.close()

                elif user_response == 4:
                    print(
                        "The read and write mode helps you to first see the content of your file first before overwriting"
                        "it with a new data")
                    file = open("myfile.txt", "r+")
                    print(file.read())
                    print("ABOVE IS THE CONTENT OF THE FILE BEFORE USING THE WRITE OPERATION")
                    user_write3 = input("Input words to add:")
                    file.write(user_write3)
                    print(" THE NEW FILE CONTENT:")
                    print("Notice that the old content in the file was overwritten with the new one")
                    file.close()

                elif user_response == 5:
                    print("The w+ allows you to overwrite an existing file and then see the content of the file")
                    print("First check the content of the myfile.txt in your directory")
                    file = open("myfile.txt", "w+")
                    user_write4 = input("Input words to add:")
                    file.write(user_write4)
                    print("Notice that the existing file content was deleted.Below is the new file content:")
                    print(file.read())
                    file.close()

                elif user_response == 6:
                    print("The a+ is similar to the w+ only that it doesn't overwrite the existing file")
                    file = open("myfile.txt", "a+")
                    user_write5 = input("Input words to add:")
                    file.write(user_write5)
                    fileContent = file.read()
                    print(fileContent)
                    file.close()

                elif user_response == 7:
                    user_response3 = input("Enter file name to create:")
                    file = open(user_response3, "x")
                    print("File created")
                    file.close()

            except:
                print("Please follow the necessary instruction")

        else:
            print("Thank you for utilising the simulator")
            exit()


except:
    print("Please follow the necessary instruction")
