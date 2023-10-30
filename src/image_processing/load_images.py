#!/bin/python3

import os
import face_recognition as fc

class FaceData:
    def __init__(self, img_dir_name):
        self.__img_dir_name__ = img_dir_name
        self.faces = self.__get_faces__()
        self.face_names = self.__get_face_names__()
        self.face_encodings = self.__get_face_encodings__()

    def __get_faces__(self):
        os.chdir(self.__img_dir_name__)
        cwd = os.getcwd()
        faces = []
        for r, d, face_files in os.walk(cwd):
            faces = face_files
        return faces

    def __get_face_names__(self):
        face_names = []
        for face in self.faces:
            dot_index = face.index(".")
            face_name = face[:dot_index]
            face_names.append(face_name)
        return face_names

    def __get_face_encodings__(self):
        face_encodings = []
        for face in self.faces:
            try:
                loaded_face = fc.load_image_file(face)
                loaded_face_encoding = fc.face_encodings(loaded_face)[0]
                face_encodings.append(loaded_face_encoding)
            except Exception as err:
                print(f"idk check ur file :'{face}'")
                # print("Here is ur error bro",err)
        return face_encodings

    def get_faces_data(self):
        data = self.face_names, self.faces, self.face_encodings
        return data
