print("*" * 40)
print("\033[4;37;40mConfederação Nacional de Natação\033[m")
print("*" * 40)

idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("\033[1;30;46mCATEGORIA MIRIM\033[m")
elif idade <= 14:
    print("\033[1;30;43mCATEGORIA INFANTIL\033[m")
elif idade <= 19:
    print("\033[1;30;45mCATEGORIA JUNIOR\033[m")
elif idade == 20:
    print("\033[1;30;40mCATEGORIA SENIOR\033[m")
else:
    print("\033[1;30;41mCATEGORIA MASTER\033[m")
