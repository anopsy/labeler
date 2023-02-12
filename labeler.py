import shutil
import cv2
import os
directory = '/home/anopsy/data/frames'
#'C:\Users\Martha\Documents\train_data'
directoryGood = '/home/anopsy/data/frames/goodwaves'
#'C:\Users\Martha\Documents\train_data\good_waves'
directoryBad = '/home/anopsy/data/frames/badwaves'
#'C:\Users\Martha\Documents\train_data\bad_waves'
removed = '/home/anopsy/data/removed'
#'C:\Users\Martha\Documents\train_data\removed'
countgood=0
countbad=0

for filename in sorted(os.listdir(directory)):
    cv2.destroyAllWindows()
    if filename.endswith('.jpg'):
        img=cv2.imread(os.path.join(directory, filename))
        cv2.imshow(filename, img)
        key=cv2.waitKey(0)
        oldname= directory+ '/' + filename
        if key==ord('1'):
            print('good wave')
            newname= directoryGood + '/goodwave{}.jpg'.format(countgood)
            shutil.move(oldname, newname)
            countgood+=1
        elif key==ord('0'):
            print('bad wave')
            newname= directoryBad + '/badwave{}.jpg'.format(countbad)
            shutil.move(oldname, newname)
            countbad+=1
        elif key==ord('d'):
            print('removed')
            shutil.move(directory+ '/' + filename, removed + '/' + filename)
    else:
        continue
