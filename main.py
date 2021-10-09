import csv
print("Assuming that each column refers to the same user in both test.csv and train.csv data and.......")
print("Reading the csv files..........")

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
    # for i in tmp:
        



    # #using DATA from train.csv
    # with open("train.csv") as train_file:
    #     train_reader=csv.reader(train_file)

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
                





        # print("The order in which there will be user retention is:  ")