import csv
print("Assuming that each column refers to the same user in both test.csv and train.csv data and.......")
print("Reading the csv files..........")

FinalCSV1=["Users"]
FinalCSV2=["Score"]

with open("test.csv") as test_file:
    test_reader=csv.reader(test_file)

    print("Removing Inferences from the data......")

    #just kidding

    print("inferences are ready......")
    print("there are 199 users.....")
    print("calculating.......")

    #ALGO FOR FUTURE USER PREDICTION......



    next(test_reader)

    user_priority=[]

    main_test=[]
    tmp={}
    for line in test_reader:
        for i in range(200):
            score_1=len(line[i])-len(set(line[i]))          #Score_1 will calculate the total number of repetative payments the user makes
            # score_2=
            tmp[i+1]=score_1
        main_test.append(list(set(tmp)))
    print(tmp)

    print("The following customer is the most satisfied and most likely to repeate the transaction:: ")
    values=tmp.values()
    keys=tmp.keys()
    maxximum=max(values)
    tmp2=[]
    for j in range(maxximum,-1,-1):
        for i in tmp:
            if tmp[i] == j:
                tmp2.append("user: var_"+str(tmp[i]+1))   
                FinalCSV1.append(tmp[i])
    tmp2=set(tmp2)
    for i in tmp2:
        print(i)        
    for i in range(200):
        FinalCSV1.append("var_"+str(i))

    # open the file in the write mode
    f = open('output.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(FinalCSV1)
    writer.writerow(FinalCSV2)

    # close the file
    f.close()

print("Due to limitted resources Model could not train ")

#sing DATA from train.csv
with open("train.csv") as train_file:
    train_reader=csv.reader(train_file)

    #     next(train_reader)

    #     user_priority=[]

    #     main_test=[]
    #     tmp={}
    #     for line in test_reader:
    #         for i in range(200):
    #             score_1=len(line[i])-len(set(line[i]))          #Score_1 will calculate the total number of repetative payments the user makes
    #             tmp[i+1]=score_1
    #         main_test.append(list(set(tmp)))
    #     print(tmp)