import csv
import random
import smtplib

PASSWORD = "your password"
MY_EMAIL = "xxxxx@gmail.com"

boys = []
girls = []
all_names = []
emails_dict = {}
with open("Data.csv") as data:
    data_csv = csv.reader(data)
    for row in data_csv:
        if row[2].strip() == 'b':
            boys.append(row[0].strip())
        else:
            girls.append(row[0].strip())

        emails_dict[row[0]] = row[3]

girls_choose_from = girls.copy()
boys_choose_from = boys.copy()
all_names = boys + girls
random.shuffle(all_names)

res = {}
for key in all_names:
    if key in boys and girls_choose_from != []:
        random_choice_name = random.choice(girls_choose_from)
        index = girls_choose_from.index(random_choice_name)
        girls_choose_from.pop(index)
        res[key] = random_choice_name
    elif key in girls and boys_choose_from != []:
        random_choice_name = random.choice(boys_choose_from)
        index = boys_choose_from.index(random_choice_name)
        boys_choose_from.pop(index)
        res[key] = random_choice_name
    elif key in boys and girls_choose_from == []:
        random_choice_name = random.choice(boys_choose_from)
        index = boys_choose_from.index(random_choice_name)
        boys_choose_from.pop(index)
        res[key] = random_choice_name
    elif key in girls and boys_choose_from == []:
        random_choice_name = random.choice(girls_choose_from)
        index = girls_choose_from.index(random_choice_name)
        girls_choose_from.pop(index)
        res[key] = random_choice_name

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)

    for key in all_names:
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=emails_dict[key],
            msg=f"""Subject: SECRET SANTAA \n\n 
                            It's been a great year with you and everyone else around , we made memories.....happy and sad ones , we have been through it all together. 
                            This year is coming to an end BUT DON'T YOU DARE think our memories will. 
                            So congrats to all of us it's finally the end of the year but the beginning of a new year of us together.
                            Let the Christmas games begin 
                            Did you hear the jingling bells ? Did you see the one horse open sleigh ? Did you know you're the secret santa ? 
                            HoHoHo

                            Dear secret santa ({key}):
                                We would like to announce that your lucky victim is {res[key]}"""
        )
    ## this to send the result dict to your email
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject: SECRET SANTAA \n\n {res}"
    )