# day 28 database email
N = int(input())
names = []
email = []
for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1].split('@')
    names.append(firstName)
    email.append(emailID)
filter_2 = [names[i] for i in range(len(email)) if email[i][1] == 'gmail.com']
filter_2.sort()
for j in range(len(filter_2)):
    print(filter_2[j])