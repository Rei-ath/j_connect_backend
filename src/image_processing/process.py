import face_recognition as fc
import numpy as np
from load_images import FaceData
import os
import time


script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, '..', '..', 'images')

known_face_names, faces, known_face_encodings = FaceData(
    images_dir).get_faces_data()

def process_main(frame):
    try:
        frame_np = np.array(frame)
        find = False
        rgb_frame = np.ascontiguousarray(frame_np[:, :, ::-1])
        face_locations = fc.face_locations(rgb_frame)
        face_encodings = fc.face_encodings(rgb_frame, face_locations)
        for (t, r, b, l), face_encoding in zip(
            face_locations, face_encodings
        ):
            matches = fc.compare_faces(known_face_encodings, face_encoding)
            face_distances = fc.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                find = True
            elif True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                find = True
            else:
                name = "who tf is this"
                find = False
        return find, name
    except Exception as err:
        print(err)

if __name__ == '__main__':
    from PIL import Image
    image = Image.open(
        os.path.join(images_dir,"devansu.jpeg"))
    loop_start = time.time()
    for i in range(100):
        start = time.time()
        found, name = process_main(image)
        end = time.time()
        print(f"Executed in process_main(image) in > {(end-start)* 10**3 } ms <")
        if found:
            print(f"found : {name}\nstatus : {found}")
        else:
            print(f"didnt found : {name}\nstatus : {found}")
    loop_end = time.time()
    print(f"Executed loop for 100 in >>>>{(loop_end-loop_start)* 10**3 } ms <<<<")
