hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))


def computepay(h, r):
    if h <= 40:
        return h * r
    elif h > 40:
        p = h * r
        rh = (h - 40) * (r * 0.5)
        fp = p + rh
        return fp


p = computepay(hrs, rate)
print("Pay", p)
