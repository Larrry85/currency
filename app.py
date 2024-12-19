while True: # Loop continues until user enters 0
    print("ACME(tm) US DOLLAR EXCHANGE RATE APP")
    print("1) LOAD currency exchange rate data from a file")
    print("2) USE AVERAGE exchange rate")
    print("3) USE HIGHEST exchange rate")
    print("4) USE LOWEST exchange rate")
    print("5) CONVERT USD TO EUR")
    print("6) CONVERT USD TO AUD")
    print("7) CONVERT USD TO GBP")
    print("0) QUIT program")
    ans = input("Choose what to do: ")    
#####################################################################
    def function_load(): # when user entered 1 this function was called
        
        rivit = [] # list to put all rows of data worth info
        rivit2 =[] # all rows, even empty ones

        filename = input("Give name of the data file: ") # user enters name of the file
        with open(filename, "r") as readfile:
            header = readfile.readline()            # ignores header
            for item in readfile:
                rivit2.append(item) # push data in rivit 2 list = all days, even the empty ones   
                if len(item) > 14: # ignores all data below 14 characters = not enough data
                    rivit.append(item) # puts data in rivit list, no empty days                                   

            daysall =(len(rivit2)) # days is how many rows/days are left
            dayseka = float(daysall) # days in float type
            firstday = (rivit2[0]) # first row/day of data
            firstday2 = firstday.split(";")
            ekapaiva = firstday2[0]   # first date
            lastday = rivit2[len(rivit2)-1] # last row/day of data
            lastday2 = lastday.split(";")
            vikapaiva = lastday2[0]   # last date
            days =(len(rivit)) # days is how many rows/days are left
            daysf = float(days) # days in float type

        eurot = []
        aussit = [] # lists to collect different currency
        britit = []
        number = int(len(rivit)) # length of file / rows
        
        for rivi in rivit:
                yksirivi = rivi.split("\t")  # Change the delimiter to tab
                print(yksirivi)  # Add this line to print the contents of yksirivi
                try:
                    rivintoka = float(yksirivi[1])  # index number 1 is euros
                    eurot.append(rivintoka)
                    rivinkolmas = float(yksirivi[2])  # index number 2 is aussit
                    aussit.append(rivinkolmas)
                    rivinneljas = float(yksirivi[3])  # index number 3 is britit
                    britit.append(rivinneljas)
                except ValueError:
                    print(f"Skipping invalid data: {yksirivi}")

        i = -1
        while i < number: # loop goes through every index/ row of file
            rivi = rivit[i]            
            rivi = rivi.strip() # strips off useless marks in the file
            yksirivi = rivi.split("\t") # splits data from ;
            try:
                rivintoka = float(yksirivi[1])  # index number 1 is euros
                eurot.append(rivintoka)  # puts all euros in list
                rivinkolmas = float(yksirivi[2])
                aussit.append(rivinkolmas)
                rivinneljas = float(yksirivi[3])
                britit.append(rivinneljas)
            except ValueError:
                print(f"Skipping invalid data: {yksirivi}")
            i += 1          # loop continues, index number rises
        eurot.pop(0)# for some reason there was one extra number in the beginning
        aussit.pop(0)
        britit.pop(0)

        yka = 0
        for item1 in eurot: # goes through euro list
            yka += float(item1) # string to float            
        yka = yka / daysf # sum / length
        ymax = max(eurot) # largest number from list
        ymin = min(eurot) # smallest number from list

        zka = 0
        for item2 in aussit: # goes through aud list
            zka += float(item2)
        zka = zka / daysf
        zmax = max(aussit)
        zmin = min(aussit)

        qka = 0
        for item3 in britit: # goes through gbp list
            qka += float(item3)
        qka = qka / daysf    
        qmax = max(britit)
        qmin = min(britit)
      
        print("Data loaded successfully!")
        print("Currency exchange data is from", daysall, "days between", ekapaiva, "and", vikapaiva + ".")
        print("")
        vastaus =[yka, zka, qka, ymax, zmax, qmax, ymin, zmin, qmin] # needed data

        tulokset = []   # data gets put in tulokset list
        tulokset.append(vastaus[0]) # eur ave
        tulokset.append(vastaus[1]) # aud ave
        tulokset.append(vastaus[2]) # gbp ave
        tulokset.append(vastaus[3]) # eur max
        tulokset.append(vastaus[4]) # aud max
        tulokset.append(vastaus[5]) # gbp max
        tulokset.append(vastaus[6]) # eur min
        tulokset.append(vastaus[7]) # aud min
        tulokset.append(vastaus[8]) # gbp min

        ea = "eurave" # data gets pulled from tulokset list
        one = float(tulokset[0]) # float type data
        eh = "eurhigh"
        two = float(tulokset[3])
        el = "eurlow"
        three = float(tulokset[6])
        aa = "ausave"
        four = float(tulokset[1])
        ah = "aushigh"
        five = float(tulokset[4])
        al = "auslow"
        six = float(tulokset[7])
        ba = "briave"
        seven = float(tulokset[2])
        bh = "brihigh"
        eight = float(tulokset[5])
        bl = "brilow"
        nine = float(tulokset[8])
    
        euros = [one, two, three] # euro list
        audit = [four, five, six] # aussi list
        bri = [seven, eight, nine] # britti list
        ratet = {ea : one, eh : two, el : three, aa : four, ah : five, al : six, ba : seven, bh : eight, bl : nine} ##  data organised in pairs

        kaikki = [] # all arrays in list
        ratevalueave = [] # average currency data list
        ratevalueave.append(ratet[ea]) # average data gets put in average currency list
        ratevalueave.append(ratet[aa])
        ratevalueave.append(ratet[ba])
        kaikki.append(ratevalueave)
        ratevaluehigh = [] # high currency data list
        ratevaluehigh.append(ratet[eh])# high data gets put in high currency list
        ratevaluehigh.append(ratet[ah])
        ratevaluehigh.append(ratet[bh])
        kaikki.append(ratevaluehigh)
        ratevaluelow = []    # low currency data list
        ratevaluelow.append(ratet[el])# low data gets put in low currency list
        ratevaluelow.append(ratet[al])
        ratevaluelow.append(ratet[bl])
        kaikki.append(ratevaluelow)
        value = kaikki[0]
        return ratevalueave, ratevaluehigh, ratevaluelow, euros, audit, bri, kaikki, value   

    if ans == "1": # if user enters 1...

        juttu = function_load() #...this function is called
#####################################################################
    def function_ave():
        print("Using the average currency exchange rate.")
        print("")
        kaekki = juttu[6]
        reit = kaekki[0]
        return reit  # programme uses average rate

    def function_high():
        print("Using the highest currency exchange rate.")
        print("")
        kaekki = juttu[6]
        reit = kaekki[1]
        return reit # programme uses high rate

    def function_low():
        print("Using the lowest currency exchange rate.")
        print("")
        kaekki = juttu[6]
        reit = kaekki[2]
        return reit # programme uses low rate
    
    if ans == "2": # if user enters 2
        val = function_ave() #...this function is called

    if ans == "3": # if user enters 3
        val = function_high() #...this function is called

    if ans == "4": # if user enters 4
        val = function_low() #...this function is called
#####################################################################
    def function_eur():
        maara = float(input("Give USD to convert: "))
        try: # function tries to use different value
            value = val
            numbers = maara * value[0]
        except: # if it doesn't find it, it uses average/default value
            value = juttu[7]            
            numbers = maara * value[0]  
        print(maara, "USD in EUR is", round(numbers, 2), "EUR")
        print("") 

    def function_aud():
        maara = float(input("Give USD to convert: "))
        try:
            value = val
            numbers = maara * value[1]
        except:
            value = juttu[7]            
            numbers = maara * value[1]  
        print(maara, "USD in AUD is", round(numbers, 2), "AUD")
        print("")

    def function_gbp():
        maara = float(input("Give USD to convert: "))
        try:
            value = val
            numbers = maara * value[2]
        except:
            value = juttu[7]            
            numbers = maara * value[2]  
        print(maara, "USD in GBP is", round(numbers, 2), "GBP")
        print("")
         
    if ans == "5": # if user enters 5 # user wants to convert usd to eur...
        function_eur() #...this function is called
        
    if ans == "6": # if user wants to convert usd to aud...
        function_aud() #...this function is called
        
    if ans == "7": # user wants to convert usd to gbp...
        function_gbp() #...this function is called

##################################################################### 
    def function_quit():
        return True # function rerurns true, so it breaks the loop
        
    if ans == "0":
        if function_quit: # this function is called
            break
