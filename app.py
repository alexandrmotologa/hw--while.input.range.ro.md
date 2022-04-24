while True:
    try:
        start_n = int(input("Write a start number: "))
        end_n = int(input("Write an end number: "))
        if start_n < end_n:
            for i in range(start_n, end_n+1):
                print(i)
        elif start_n > end_n:
            for i in range(start_n, end_n-1, -1):
                print(i)
        else:
            print("Value Error")
    except:
        print("Value Error")