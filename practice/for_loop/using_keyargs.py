def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key, value])
    return ans
object = function(First = "Python", Second = "Java", Third = "C++")

print(object)


