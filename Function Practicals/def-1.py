def shutdown(user):
    if user=='yes':
        print("Shutdown Sucessfully!")
    elif user=='no':
        print("Shoutdown abort!!!!")
    else:
        print("Invaild input")
user=input("Enter yes or no:")
shutdown(user)