def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("insert a year: "))
print (is_leap_year(year))

#To add line comments, execute editor.action.addCommentLine (CTRL+K CTRL+C)
#
#To remove line comments, execute editor.action.removeCommentLine (CTRL+K CTRL+U)
# sadsad
# asd
# asdas
# ddasdas