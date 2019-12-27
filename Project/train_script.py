import face_recognition
import os
import json



def trained():
	path = 'training_samples/'
	overall_encodings ={}
	submitted = False
	if "Thumbs.db" in os.listdir(path):
		os.remove(path + "Thumbs.db")
	allFiles = os.listdir(path)
	# print(allFiles)
	for image in allFiles: 
		print(image)
		train_image = face_recognition.load_image_file(path + image)
		train_image_encoding = face_recognition.face_encodings(train_image)[0]
		known_face_encodings = train_image_encoding  
		known_face_names = image
		overall_encodings[known_face_names] = known_face_encodings
	return overall_encodings

