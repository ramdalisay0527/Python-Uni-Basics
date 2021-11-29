baseprice = float(input("what is the baseprice?"))
weight = float(input("what is the weight?"))
distance = float(input("what is the distance?"))
if distance < 250:
    discount = 0
elif 250 <= distance < 500:
    discount = .1
elif 500 <= distance < 1000:
    discount = .15
elif 1000 <= distance < 2000:
    discount = .2
elif 2000 <= distance < 3000:
    discount =.35
elif distance >= 3000:
    discount = .5


cost = baseprice * weight * distance * (1-discount)
print("The Shipping Cost is", cost)