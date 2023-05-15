def func( *args_list ):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans

func("python","is","a","awesome","language")
