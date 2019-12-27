import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import os
from train_script import trained
import json
import time

known_face_encodings = []
known_face_names = []

with open("scanned.json",'w',encoding = 'utf-8') as scanned_file:
	json.dump([],scanned_file)


for key, value in trained().items():
	known_face_encodings.append(value)
	known_face_names.append(key)

print('Learned encoding for', len(known_face_encodings), 'images.')


def tested(test_image,known_face_encodings,known_face_names):
	path = 'test/'
	unknown_image = face_recognition.load_image_file(path + test_image)
	face_locations = face_recognition.face_locations(unknown_image)
	face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

	for  face_encoding in  face_encodings:
	    # See if the face is a match for the known face(s)
	    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
	    name = "Unknown"

	    # Or instead, use the known face with the smallest distance to the new face
	    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
	    best_match_index = np.argmin(face_distances)
	    # print(matches,best_match_index)
	    if matches[best_match_index]:
	        prediction = known_face_names[best_match_index]
	        # print("Pred",prediction)
	    else:
	    	print("dont match")
	    	prediction = "Unknown.jpg"

	return prediction.split('.')[0]



imagePath = 'test/'

