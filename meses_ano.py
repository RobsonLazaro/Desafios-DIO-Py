
month = int(input())

MESES_DO_ANO = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

if month in MESES_DO_ANO.keys():
    print(MESES_DO_ANO[month].title())
