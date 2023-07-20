
fruits=['mango','apple','sapota']
order='yes'
while order=='yes':
    if order=='yes':
        print(fruits)
        user=input('please tell order sir/madam:')
        if user in fruits:
            print("i want {}".format(user))
            user=input("how many juices do you want:")
        else:
            print("sorry it's not available")
        order=input('any other order sir/madam:')
    else:
        pass
print("thank you for visiting")
