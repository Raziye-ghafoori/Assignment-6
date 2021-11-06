bank_words=[]

def meno():
    print("wellcom to my dictionary::")
    print('1.English to persian')
    print('2.persian to English')
    print('3.Add new word')
    print('4.Exit')

def laod_data():
    print("pleas wait....")
    with open("words_bank.txt","r") as file:
        info_dic=file.read()
        words=info_dic.split("\n")

        for i in range(0,len(words),2):
            dic={"english":words[i],"persian":words[i+1]}
            bank_words.append(dic)
    print("Ok Goo!!!!")


def en2per():
    output=""
    sentence=input("enter your text:: ")
    wor_sen=sentence.split(" ")
    
    for word in wor_sen:
        for bword in bank_words:
            if bword["english"]==word:
                output += bword["persian"] + " "
                break
        else:
            output += word + " "

    print(output)

def per2en():
    output=""
    sentence=input("enter your text:: ")
    wor_sen=sentence.split(" ")
    
    for word in wor_sen:
        for bword in bank_words:
            if bword["persian"]==word:
                output += bword["english"] + " "
                break
        else:
            output += word + " "

    print(output)

def new_word():
    english=input("enter english  word::")
    persian=input("enter persian  word::")
    new_word={"english":english, "persian":persian}
    bank_words.append(new_word)
    print("Ok!!entered")

def Exit():
    with open("words_bank.txt","w") as file:
        for word in bank_words:
            file.write(word["english"])
            file.write("\n")
            file.write(word["persian"])
            file.write("\n")
            
    
    print("Good By!!")
    exit()

laod_data()
while True:
    meno()
    choice=int(input("Enter your choice::"))
    if choice==1:
        en2per()
    elif choice==2:
        per2en()
    elif choice==3:
        new_word()
    elif choice==4:
        Exit()
    

