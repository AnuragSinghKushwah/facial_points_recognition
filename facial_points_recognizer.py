from imutils import face_utils
import cv2
import dlib
import glob
import os
import math
import pandas as pd
import os.path


detector = dlib.get_frontal_face_detector()  # Face detector

predictor = dlib.shape_predictor("C:/Users/Pragti/Downloads/shape_predictor_68_face_landmarks.dat")

pic_num= 1

files = glob.glob("image\\*")


dictionary={}
csv_file_array=[]
index_array=[[],[],[],[],[],[],[]]
col=[]
# Iterating throurgh file
for i in files:


    numb_fol = i.split("files")[-1].split("\\")[-1]

    frame = cv2.imread(i)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

    clahe_image = clahe.apply(gray)

    detections = detector(clahe_image, 1)  # Detect the faces in the image

    for k, d in enumerate(detections):
        # For each detected face

        shape = predictor(clahe_image, d)  # Get coordinates

        shape = face_utils.shape_to_np(shape)

        for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():

            for (x, y) in shape[i:j]:
                col = list(dictionary.keys())

                if ((i, j) == (48, 68)):
                    dictionary.setdefault("lips_cordinate_ degree", []).append(  math.degrees(math.atan(y/x)) )

                    co_ordi=(x,y)
                    index_array[0].append(co_ordi)


                elif((i, j) == (17, 22)):
                    dictionary.setdefault("left_ibrow_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[1].append(co_ordi)
                elif ((i, j) == (22, 27)):
                    dictionary.setdefault("right_ibrow_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[2].append(co_ordi)
                elif ((i, j) == (36, 42)):
                    dictionary.setdefault("left_eye_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[3].append(co_ordi)
                elif ((i, j) == ( 42,48)):
                    dictionary.setdefault("right_eye_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[4].append(co_ordi)
                elif ((i, j) == (27, 36)):
                    dictionary.setdefault("nose_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[5].append(co_ordi)
                elif ((i, j) == (0, 17)):
                    dictionary.setdefault("side_portion_ degree", []).append(math.degrees(math.atan(y / x)))
                    co_ordi = (x, y)
                    index_array[6].append(co_ordi)
                else:
                 pass
                cv2.circle(frame, (x, y), 1, (0, 255, 0), 2)

            try:
                    os.makedirs("plotimage/{}".format(numb_fol))
            except:

                    print(" ")
            # screen_res = 520, 520
            # scale_width = screen_res[0] / frame.shape[1]
            # scale_height = screen_res[1] / frame.shape[0]
            # scale = min(scale_width, scale_height)
            # window_width = int(frame.shape[1] * scale)
            # window_height = int(frame.shape[0] * scale)
            #
            # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            # cv2.resizeWindow('image', window_width, window_height)
            cv2.imshow("image", frame)
            cv2.waitKey(100)


        # csv_file_array.append("plotimage4\\%s\\%s.jpg" % (numb_fol, pic_num))
            out = cv2.resize(frame, (350, 350))
            cv2.imwrite("plotimage\\%s\\%s.jpg" %(numb_fol, pic_num ),out)
        # pic_num += 1



        csv_file_array.append("plotimage\\%s\\%s.jpg" % (numb_fol, pic_num))
        for csv_file in csv_file_array:

             file_name = csv_file.split("\\")[-1]
        if not os.path.isfile('plotimage\%s\%s.csv' % (numb_fol, file_name)):
            # print("/////////////////////////////////////////////")
            for z in range(len(col)):

                with open('plotimage\%s\%s.csv' % (numb_fol,file_name), "a")as f:
                    new= "index"+"  "+","+str(col[z])+"    "+ ","+ "    "+"co_ordinate\n"
                    f.write(new)
                    row=dictionary[col[z]]

                    if (col[z] == "lips_cordinate_ degree"):
                            ww=range(48,68)

                            for x, y in enumerate(row):
                                index = str(ww[x])
                                column = str(int(row[x]))
                                co_ordinate = str(index_array[z][x])
                                f.write(index + "      " + ' ' + column + "       " + " " + "                " + co_ordinate + '\n')

                    elif (col[z] == "left_ibrow_ degree"):
                        ww=range(17,22)

                        for x, y in enumerate(row):

                         index = str(ww[x])
                         column = str(int(row[x]))
                         co_ordinate = str(index_array[z][x])
                         f.write(index + "      " + ' ' + column + "       " + " " + "                " + co_ordinate + '\n')

                    elif (col[z] == "right_ibrow_ degree"):
                            ww=range(22,27)
                            for x, y in enumerate(row):
                                index = str(ww[x])
                                column = str(int(row[x]))
                                co_ordinate = str(index_array[z][x])
                                f.write(index + "      " + ' ' + column + "       " + " " + "                " + co_ordinate + '\n')

                    elif (col[z] == "left_eye_ degree"):
                            ww=range(36,42)
                            for x, y in enumerate(row):
                                index = str(ww[x])
                                column = str(int(row[x]))
                                co_ordinate = str(index_array[z][x])
                                f.write(index + "      " + ' ' + column + "       " + " " + "                " + co_ordinate + '\n')
                    elif(col[z] == "right_eye_ degree"):
                            ww=range(42,48)
                            for x, y in enumerate(row):
                                index = str(ww[x])
                                column = str(int(row[x]))
                                co_ordinate = str(index_array[z][x])
                                f.write(index + "     " + '  ' + column + "       " + "  " + "              " + co_ordinate + '\n')
                    elif (col[z] == "nose_ degree"):
                        ww = range(27, 36)
                        for x, y in enumerate(row):
                            index = str(ww[x])
                            column = str(int(row[x]))
                            co_ordinate = str(index_array[z][x])
                            f.write(index + "      " + ' ' + column + "             " + "  " + "      " + co_ordinate + '\n')
                    elif (col[z] == "side_portion_ degree"):
                        ww = range(0, 17)
                        for x, y in enumerate(row):
                            index = str(ww[x])
                            column = str(int(row[x]))
                            co_ordinate = str(index_array[z][x])
                            f.write(index + "      " + ' ' + column + "       " + " " + "                " + co_ordinate + '\n')
        else:
                print("already exist the csv in folder")

        del csv_file_array[:]
        dictionary.clear()
        del col[:]
        del index_array[0][:]
        del index_array[1][:]
        del index_array[2][:]
        del index_array[3][:]
        del index_array[4][:]
        del index_array[5][:]
        del index_array[6][:]
        pic_num += 1
# del csv_file_array[:]

