message= " $6<&1#><*\x1a!$2\x22\x1a,\x1a- $7!\x1a<*0\x1a),. !\x1a=*78"
flag = ""
for char in message:
    flag += chr(ord(char) ^ ord("E"))
print flag

# It was pretty obvious that the message was probably the flag, so I tried xor-ing
# each character by the characters that the flag probably begins with. (easyctf{)
# In the end, it was clear that the key was "E" repeated over and over again.
# XOR each character by "E" to reverse the xor.
# Print that stuff out and you get the flag:

# easyctf{yo_dawg_i_heard_you_liked_xor}
