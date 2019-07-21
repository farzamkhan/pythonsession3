s = "lorem ipsum is simply dummy text of the printing and typesetting industry. \
Lorem ipsum \nhas been the industry's standard dummy text ever since the 1500s.\
when an unknown\nprinter took a gallery of type and scrambled it to make a \
type specimen book. It has survived not only five centuries, but also \
the leap into electronic typesetting,\nremaining essentially unchanged."

if s.find("printing") != -1 :
    new_s = s.replace("printing", "publishing")
else:
    new_s = s
print(new_s)
print("\n", "\n", "=============================")

string_list  = s.split()
new_string_list = []
for i in range (0, len(string_list)):
    word = string_list[i]
    temp_list = []
    
    if word[0] == "l":
        temp_list = list(word)
        temp_list[0] = "L"
        word = ''.join(temp_list)
        new_string_list.append(word)
    else:
        new_string_list.append(word)

new_string = ' '.join(new_string_list)
print(new_string)
print("\n", "\n", "=============================")
counter_list = new_string.split()
more_than_6 = []
for i in range (0, len(counter_list)):
    if len(counter_list[i]) > 6 :
        more_than_6.append(counter_list[i])
print("Big Words List Is :")
print(more_than_6)

