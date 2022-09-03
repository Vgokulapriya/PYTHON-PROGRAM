# collect email from user 
# split the email using the @,the first part as the user name,the second part is saved as the domain
# split using domain..

def main():
    print("welcome to email slicer")
    print("")

    email_input = input("input your email address: ")

    (user_name, domain) =email_input.split("@")
    (domain,extension) = domain.split(".")

    print("user_name :",user_name)
    print("domain :",domain)
    print("Extension :",extension)

main()    