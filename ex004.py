n = input('digite algo: ')
print(type(n))
print('é alfanumérico?', n.isalnum())
print('é alfabetico?', n.isalpha())
print('é numérico?', n.isnumeric())
print('só tem espaços?', n.isspace())
print('está em letras maiúsculas?', n.isupper())
print('está em letras minúsculas?', n.islower())
print('está capitalizada?', n.istitle())