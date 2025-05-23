# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    if len(cc) <= 4:
        return cc
    masked_part = '#' * (len(cc) - 4)
    last_four = cc[-4:]
    return masked_part + last_four