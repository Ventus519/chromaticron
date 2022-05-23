def savingData():

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from tabulate import tabulate
    import experimental
    import random

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("Downloads/leaderboardreplit-5d64a6579d9e.json", scope)

    googleSheet = gspread.authorize(credentials)

    index = 0
    sheetOne = googleSheet.open("exportingData").get_worksheet(index)

    userName = experimental.userText

    sheetOne.append_row([userName])

    index = 1
    sheetOne = googleSheet.open("exportingData").get_worksheet(index)

    leaderBoard = []
    for i in range (2, 7, 1):
        leaderBoard.append(sheetOne.row_values(i))
  
    headers = sheetOne.row_values(1)
    print(tabulate(leaderBoard, headers, tablefmt = "fancy"))
    return userName
