from bson import Binary, ObjectId
from pymongo import MongoClient
from PIL import Image
import io


client = MongoClient('localhost', 27017)

db = client['EVkaro']

collection = db['charger']




def insertImagetoDB(testImage):
    
    testImage = 'test.jpg'
    
    
    with open(testImage, 'rb') as f:
         
          image_data = f.read()
          
    binary_data_to_be_stored_onMONGODB = io.BytesIO(image_data).read()
    
    charger_document = {
    "name": "momo Charger",
    "id": 36,
    "price": 39.99,
    "type": "USB-C",
    "userwhocanbuyittype": ["Android", "iPhone"],
    "image": binary_data_to_be_stored_onMONGODB 
                      }
     
    result = db.charger.insert_one(charger_document)
    
    print(result)





def calulateSizeoftheDocumentandImage():
    
    document = collection.find_one({"_id": ObjectId("65c6351098af8ea2adcd0078")})  # change it with a real id from your database once you add a document

    document_size_bytes = len(document)

    attribute_size_bytes = 0
    if "image" in document:
        attribute_size_bytes = len(Binary(document["image"]))

    return {
        "document_size_bytes": document_size_bytes,
        "attribute_size_bytes": attribute_size_bytes
    }






def displayImagebackfromBinary():
    
    document_id = ObjectId("65c6351098af8ea2adcd0078")    # change it with a real id from your database once you add a document

    document = collection.find_one({"_id": document_id})
    
    if document is None:
        print("Document not found.")
        return
    
    binary_image_data = document["image"]

    image = Image.open(io.BytesIO(binary_image_data))

    image.save("restored_image.jpg")  
    
    



insertImagetoDB()

print(calulateSizeoftheDocumentandImage())


# uncomment it when you want to display the image back from the binary form when it is returned from mongo database

# displayImagebackfromBinary()   











    