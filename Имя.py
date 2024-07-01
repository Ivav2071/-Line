def sub1(string):
    list_sub = []
    sub2 = ""
    for i in string:
        if i not in sub2:
            sub2 += i
            if sub2 not in list_sub:
                list_sub.append(sub2)
    print(max(list_sub, key=len))

sub1("sssssss")
sub1("abcdefab")
sub1("abcabcbb")






#sssssss -> s

#abcdefab -> abcdef

#abcabcbb -> abc