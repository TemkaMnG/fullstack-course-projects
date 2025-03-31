# Week_ Project_1

Header = "Hello World!"                                         # sain uu delhii utga onooh heseg
print(Header)                                                   # onooson utgiig hewleh heseg

your_name = input("Enter your name: ")                          # hereglegch ner oruulah heseg
print("Hello, " + your_name + "!")                              # Hereglegchiin neriig mendchilgeetei hewleh heseg

age = input("Enter your age: ")                                 # nas oruulah heseg
print("Та " + age + " - настай байна.")                         # hereglegchiin nasiig hewleh

age = int(age)                                                  # toon utga / hereglegchiin nasiig awah heseg /
if age > 100:                                                   # shalgah heseg / hereglegchiin nas 100 aas ih bol /
    print(f"Та аль хэдийн 100 нас хүрсэн байна.")               # hereglegchiin nas 100 aas ih bol hewlene
elif age == 100:                                                # hereglegchiin nas 100 tai tentsvv ved /
    print(f"Та яг 100 нас хүрсэн байна.")                       # hereglegchiin nas 100 tai tentsvv ved hewlene
elif age < 100:                                                 # hereglegchiin nas 100 aas baga baiwal /
    print(f"{100 - age} + жилийн дараа 100 нас хүрэх болно.")   # hereglegchiin nas 100 aas baga baiwak hewlene

