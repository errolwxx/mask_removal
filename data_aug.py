import face_recognition
from PIL import Image
import os

# delCount, prcsCount = 0

root = './test/'
path2Knowns = './knowns/'
names = os.listdir(root)
# names.remove("Brad Pitt")


for name in names:
    delCount = 0
    prcsCount = 0
    srcLoaded = face_recognition.load_image_file('{}{}.jpg'.format(path2Knowns, name))
    srcEncoding = [face_recognition.face_encodings(srcLoaded)[0]]
    for img in os.listdir(root + name):
        path = '{}{}/{}'.format(root, name, img)
        try:
            imgLoaded = face_recognition.load_image_file(path)
            # locations = face_recognition.face_locations(img)
            imgEncodings = face_recognition.face_encodings(imgLoaded)
            # print(path)
        except Exception:
            # print(path)
            os.remove(path)
            delCount += 1
            continue
        # for loc in locations:


        for i, ec in enumerate(imgEncodings):
            if face_recognition.compare_faces(srcEncoding, ec)[0]:
                top, right, bottom, left = face_recognition.face_locations(imgLoaded)[i]
                face = Image.fromarray(imgLoaded[top:bottom, left:right])
                face.save('{}{}/{}'.format(root, name, img))
                prcsCount += 1
                print("{} deleted out of {} processed ({})".format(delCount, prcsCount, name))
                break
            else:
                continue
