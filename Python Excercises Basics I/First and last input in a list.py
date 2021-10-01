color_list = ["red","blue","yellow","green"]

print(color_list[0])
print(color_list[3])


exam_st_date = (11, 12, 2021)

print("The examination will start at : ", exam_st_date[0],exam_st_date[1],exam_st_date[2])

a = int(input("Enter a number here: "))

n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )

print (n1+n2+n3)