#Chicken Count in Indonesia
#README : Don't delete the code, see the different of looping with the title of triple hash (#)
#           if wanna choose one, just block the code until the last point, and press ctrl + /
# AUTHOR : Ananda Fikri - clone writer
#
#
#
# # #FOR LOOPING

# count = int(input("banyak anak ayam: " ))
# for i in reversed(range(-1,count-1)):
#     j = i+2
#     i+=1
#     # print(j)
#     if i == 0 and j == 1:
#         i = "sudahlah habis"
#         print("tekotekotekoooteeek... anak ayam turun" ,j,"mati satu,", i)
#     else:
#         print("tekotekotekoooteeek... anak ayam turun" ,j,"mati satu, tinggallah", i)

# = final point of For Loop - left it in hash comment ==

# # #WHILE LOOPING

count = int(input("banyak anak ayam: "))
left = count
i = 0
while count >= 0:
    # print(count)
    count-=1
    left = count+1
    if left > 0:
        if count == 0 and left == 1:
            print("tekotekotekoooteeek... anak ayam turun" ,left,"mati satu, sudahlah habis")
        else:
            print("tekotekotekoooteeek... anak ayam turun" ,left,"mati satu, tinggallah", count)

# = final point of For Loop - left it in hash comment ==

#don't delete it
print()
print("<"*20, "https://github/clonewriter", ">"*20)