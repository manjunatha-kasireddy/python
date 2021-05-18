
def sleepin(weekday, vacation):
   
   if not weekday or vacation:
      print("True")
   else:
      print("False")


sleepin(True, True)


# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are
# on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
