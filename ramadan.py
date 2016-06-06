def replace_line(line_num): #function to increasee number of sala every enter
    lines = open("sala.txt", 'r').readlines()
    lines[line_num] = str( int(lines[line_num]) +1 )+"\n"
    out = open("sala.txt", 'w')
    out.writelines(lines)
    out.close()

import datetime
milady_day = datetime.datetime.now().day # get milady day
if milady_day >=6 : # conver to hijri (valid only for 2016)
    hijri_day = milady_day - 5
else:
    hijri_day = milady_day + 25

print ( hijri_day , " days have passed from ramadan , keep on")

print ("what sala have you  prayed in mosque today ?\nfor:\n")
print ( "Fajr\t Enter\t=>\t 1 ")
print ( "Zohr\t Enter\t=>\t 2 ")
print ( "Asr\t Enter\t=>\t 3 ")
print ( "Maghrb\t Enter\t=>\t 4 ")
print ( "Eshaa\t Enter\t=>\t 5 \t(including taraweeh)\n")
print ( "To Exit Enter\t=>\t 0 ")


while True :
    try:
        sala_num=int(input("Enter number of sala : "))
        if sala_num == 0 :
            print ("barak allah fek , see you  tomorrow in shaa Alla ")
            break
        else:replace_line(sala_num-1)
    except:
        print ("Please enter numercal value in the range")
        continue

if hijri_day == 1 : # calculate number of sala times at the last day of the mounth
    read_file = open("sala.txt", "r")
    fajr=int(read_file.readline())
    zohr=int(read_file.readline())
    asr=int(read_file.readline())
    maghrb=int(read_file.readline())
    eshaa=int(read_file.readline())

    print("happy fest :D")
    print("you have prayed : \n")
    print("{} sala of Fajr   with percentage of {}%".format(fajr,int(fajr/30*100,) )) # print number of sala and percentage
    print("{} sala of Zohr   with percentage of {}%".format(zohr,int(zohr/30*100) ))
    print("{} sala of Asr    with percentage of {}%".format(asr,int(asr/30*100) ))
    print("{} sala of Maghrb with percentage of {}%".format(maghrb,int(maghrb/30*100) ))
    print("{} sala of Eshaa  with percentage of {}%\t(including taraweeh)\n".format(eshaa,int(eshaa/30*100) ))
    total = (fajr+zohr+asr+maghrb+eshaa)
    print("total = {} sala with percentage of {} %".format(total,int(total/150*100)))


    result_file = open("1437_result.txt", "w")

    result_file.write("you have prayed :\n")
    result_file.write("{} sala of Fajr   with percentage of  {}%\n".format(fajr,int(fajr/30*100,) ))
    result_file.write("{} sala of Zohr   with percentage of  {}%\n".format(zohr,int(zohr/30*100) ))
    result_file.write("{} sala of Asr    with percentage of  {}%\n".format(asr,int(asr/30*100) ))
    result_file.write("{} sala of Maghrb with percentage of  {}%\n".format(maghrb,int(maghrb/30*100) ))
    result_file.write("{} sala of Eshaa  with percentage of  {}%\n\n".format(eshaa,int(eshaa/30*100) ))
    result_file.write("total = {} sala with percentage of {} %\n\n".format(total,int(total/150*100)))
    result_file.write("قال صلى الله عليه وسلم: بشِّر المشَّائين إلى المساجد في الظلم بالنور التام يوم القيامة. رواه الترمذي وابن ماجه بسند صحيح")

    result_file.close()

    read_file.close()
quit()
