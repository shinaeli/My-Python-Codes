import math


def show_primes(limit):

    for count in range(2, limit+1):
        if count % 2 == 0:
            continue
        else:
            half = math.floor(count / 2)
            divider = 2
            while divider <= half:
                if count % divider == 0:
                    continue
                else:
                    print(count)
                    break
                divider += 1
            # if
        # num = 2
        # while num <= count:
        #     if count % num != 0:
        #         print(count)
        #     else:
        #         break
        #     num += 1


show_primes(20)
