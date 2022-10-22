import pytesseract
import cv2
import utils
from flask_restful import Resource, reqparse
from base64 import b64decode


class Document(Resource):
    def get(self):
        arg = reqparse.RequestParser()
        arg.add_argument('document')
        data = arg.parse_args()

        # Create document .bin
        documentStr64 = data["document"]
        with open('Files/encode.bin', "wb") as file:
            file.write(bytes('{0}'.format(documentStr64), encoding='utf8'))
        file = open('Files/encode.bin', 'rb')

        # Create document image
        varByte = file.read()
        file.close()
        decode = open('Files/RG.jpg', 'wb')
        decode.write(b64decode(varByte))
        decode.close()
        path = r'C:\Users\Felipe Otto\AppData\Local\Tesseract-OCR\tesseract.exe'
        docImage = cv2.imread('Files/RG.jpg')
        pytesseract.pytesseract.tesseract_cmd = path

        # Extracting image data
        completeDocument = pytesseract.image_to_string(docImage)

        # Organizing items
        completeDocument = completeDocument.split('\n')
        nameList = []
        recordList = []


        # Cleaning list
        utils.cleanList(completeDocument)

        # Separate List
        aux = 0
        for data in completeDocument:
            supportStr = ''
            for character in data:
                if character.isalpha() or character.isspace() or character in "‘,'":
                    supportStr += character
                else:
                    supportStr += character
                    aux += 1
            if aux == 0:
                nameList.append(supportStr)
            else:
                recordList.append(supportStr)
                aux = 0

        ownerName = utils.standardizeName(str(nameList[0]).title())
        fatherName = utils.standardizeName(str(nameList[1]).title())
        motherName = utils.standardizeName(str(nameList[2]).title())
        RG = utils.findRg(recordList)
        CPF = utils.findCpf(recordList)
        birthDate = utils.findBirthDate(recordList)

        data = utils.documentData(ownerName, RG, CPF, birthDate, fatherName, motherName)

        return data