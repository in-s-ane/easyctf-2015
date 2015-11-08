import string
# f = open("knownplaintext2.in", "r").read()

# in
# out

"]tE\x0b]h-@k-%LU%Q"
"Q%UL%-k-h]E]t\x0b@"

"^y,tO0UO2xl'x#Mi.p=6}#(+g,1\x0bw' "
" 'w\x0b1,g+(#}6=p.M#x'lx2U0O,^ytOi"

">~h \tP;~y=7h3nW/A=XB:O"
"OB:XA/n3hW=7y=~P\th~> ;"

"!K.]_a=)t?qTIs\x0b!iB%]$xn\x0b5A"
"A5\x0bx]$%iB!s\x0bnITqt=)a]_.!K?"

"94*L.\x0b\t&E@0Tr9"
"9rT@&E0\t\x0b.*94L"

f = "e AwDqH(:aw=7(Am?'t;Hsm|U~Hbv'"

out = ""
if f[0] == "e":
    dec = f[2:]
    for i in range(0, len(dec), 4)[::-1]:
        special = ""
        normal = ""
        section = dec[i:i+4][::-1]
        print section
        for char in section:
            if char not in string.ascii_letters + string.digits:
                special += char
            else:
                normal += char

        out += special + normal
elif f[0] == "d":
    pass

print out
print "====="
print "'vb~|UHmsHt?';mA(=aw7:(HDAwq"

# f = open("knownplaintext2.out", "w").write(out)

