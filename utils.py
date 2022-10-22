
def cleanList(completeDocument):
    for itemList in completeDocument:
        if len(itemList) == 0:
            completeDocument.remove('')

def findRg(completeDocument):
    for itemList in completeDocument:
        itemList = itemList.split(' ')
        for setList in itemList:
            if len(setList) == 12 and setList[-2] == '-':
                RG = setList
                return RG

def findCpf(completeDocument):
    for itemList in completeDocument:
        itemList = itemList.split(' ')
        for setList in itemList:
            if len(setList) == 12 and setList[-3] == '/':
                CPF = setList.replace('/', '')
                CPF = '{}.{}.{}-{}'.format(CPF[:3], CPF[3:6], CPF[6:9], CPF[9:])
                return CPF

def findBirthDate(completeDocument):
    import datetime
    for itemList in completeDocument:
        itemList = itemList.split(' ')
        for setList in itemList:
            if len(setList) == 10:
                supportDate = setList
                if supportDate[2] == '/' and supportDate[5] == '/':
                    birthDate = supportDate[6:]
                    actualDate = datetime.datetime.now()
                    support = actualDate.date()
                    actualYear = int(support.strftime("%Y"))
                    if actualYear - int(birthDate) >= 18:
                        birthDate = supportDate
                        break
    return birthDate

def standardizeName(name):
    supportName = ''
    for character in name:
        if character.isalpha() or character == " ":
            supportName += character
    return supportName

def documentData(ownerName, RG, CPF, birthDate, fatherName, motherName):
    data = {
        "Nome": ownerName,
        "RG": RG,
        "CPF": CPF,
        "Data Nascimento": birthDate,
        "Nome Pai": fatherName,
        "Nome Mae": motherName
        }
    return data