email=input("Enter your Email:") #g@g.in ,# 

k,j,d=0,0,0

#1. condition length of email

if len(email)>=6: 

    #2. condition for first character must be alphabet

    if email[0].isalpha(): 

        #3. condition for presence '@'  $ count '@' must be one in email

        if ("@" in email) and (email.count("@")==1):

            #4. condition for which positon . dot is required(using negative index in string)


            if (email[-4]==".") ^ (email[-3]=="."):

                #5. using loop iteration for checking space is awailable

                for i in email:
                    if i==i.isspace():
                        k=1

                    # using loop to checking in email for any upper case of alphabet
                    elif i.isalpha():
                        if i==i.upper(): # w--W
                            j=1
                    # using loop to checking any digit is present in email

                    elif i.isdigit():
                        continue
                    # using loop with conditional statement for checking in email "_"(underscore), .(dot) and "@" is awailable loop should continue.


                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                  
                  print("Wrong Email recheck your email maybe space,any upper alphabet ")   
                else:
                    print("Sir, you entered a right Email thank you")    

            else:
                print("Wrong Email .(dot) is not present at right position")
        else:
            print("Wrong Email symbol @ must present and should not more than one")
    else:
        print("Wrong Email first character must be alphabet ")
else:
    print("Wrong Email at least 6 character required e.g: a@gmail.com ")