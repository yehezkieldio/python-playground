kata_extreme = ["bunuh", "babi", "bangsat", "bajingan", "anjing", "kontol", "memek", "tai", "goblok", "tolol", "idiot", "bego", "bodoh"]

def censor_filter_word(token):
    for kata in kata_extreme:
        if kata in token.lower():
            token = token.replace(kata, kata[0] + "*" * (len(kata)-2) + kata[-1])
            return token
    return token

print("TEST CASE 1: ", censor_filter_word("Dia telah membunuh bayi yang sedang bermain dengan kakaknya.."))
