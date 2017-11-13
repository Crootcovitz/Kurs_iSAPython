string_wejsciowy = 'Ala ma kota, kot ma Ale'

string_wyjsciowy = string_wejsciowy[0] + \
                 chr(ord(string_wejsciowy[0]) + 49) + \
                 string_wejsciowy[-1] + \
                 string_wejsciowy[7] + \
                 string_wejsciowy[3] + \
                 chr(ord(string_wejsciowy[0]) + 54) + \
                 string_wejsciowy[8] + \
                 string_wejsciowy[1] + \
                 chr(ord(string_wejsciowy[0]) + 40) + \
                 string_wejsciowy[3] + \
                 chr(ord(string_wejsciowy[0]) + 47) + \
                 chr(ord(string_wejsciowy[0]) + 50) + \
                 chr(ord(string_wejsciowy[0]) + 56) + \
                 string_wejsciowy[11] + \
                 string_wejsciowy[3] + \
                 string_wejsciowy[2] + \
                 string_wejsciowy[3] + \
                 chr(ord(string_wejsciowy[0]) + 45) + \
                 string_wejsciowy[2] + \
                 chr(ord(string_wejsciowy[0]) + 41) + \
                 chr(ord(string_wejsciowy[2]) + 1) + \
                 string_wejsciowy[2] + \
                 chr(ord(string_wejsciowy[0]) + 49) + \
                 chr(ord(string_wejsciowy[2]) + 3) + \
                 chr(ord(string_wejsciowy[0]) + 57) + \
                 chr(ord(string_wejsciowy[0]) + 40) + \
                 string_wejsciowy[-1] + \
                 chr(ord(string_wejsciowy[0]) + 41) + \
                 string_wejsciowy[3] + \
                 chr(ord(string_wejsciowy[2]) + 1) + \
                 string_wejsciowy[7:9][::-1] + \
                 chr(ord(string_wejsciowy[0]) + 50) + \
                 string_wejsciowy[-1] + \
                 chr(ord(string_wejsciowy[0]) + 49) + \
                 chr(ord(string_wejsciowy[0]) + 56)

print(string_wyjsciowy)
