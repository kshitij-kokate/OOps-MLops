class chatbook:
    def __init__(self):
        self.username = ''
        self.password =''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook how would you like to proceed ? 
                           1.press 1 to signup
                           2.press 2 to signin
                           3.press 3 to write a post 
                           4.press 4 to message a friend  
                           5.press any other to exit    
                                                    """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()
    
    def signup(self):
        email= input("enter ur email here")
        password= input("setup ur password  here")
        self.username = email
        self.password =password
        print("you hav signed up success")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password=='':
            print("you hav not signed up yet")
        else:
            uname = input("enter your password :  ")
            pwd = input ("enter password here :  ")
            if self.username==uname and self.password==pwd:
                print("you have logged in successfully")
                self.loggedin=True
            else:
                print("please input correct credentials")
        print('\n')
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt=input("   enter your post ")
        else:
            print("you hav not logged in yet")
         
        print('\n')
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt=input("   your msg ")
            frnd=input("  whom to send ")
            print(f"msg sent {frnd}")
        else:
            print("you hav not logged in yet")
        
        print('\n')
        self.menu()






obj = chatbook()