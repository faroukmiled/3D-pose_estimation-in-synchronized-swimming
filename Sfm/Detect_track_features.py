# visualize features in red with centroid in green
from create_centroid_subtracted_matrix import get_centroids,load_json
import cv2
cross_size=3
dict=load_json()
n_frames=10
centroids=get_centroids(dict)
for i in range(n_frames):
        img=cv2.imread("./images/img"+str(i)+".jpg")
        for m in range(len(dict[str(i)])):
            x,y=list(dict[str(i)][m].values())[0][0],list(dict[str(i)][m].values())[0][1]
            cv2.line(img, (x-cross_size, y), (x+cross_size, y), (0, 0, 255), thickness=2)
            cv2.line(img, (x, y-cross_size), (x, y+cross_size), (0, 0, 255), thickness=2)

        # Display the result
        x,y=centroids[i]
        cv2.line(img, (x-cross_size, y), (x+cross_size, y), (0, 255, 0), thickness=2)
        cv2.line(img, (x, y-cross_size), (x, y+cross_size), (0, 255, 0), thickness=2)

        cv2.imshow('Image with features', img)
        cv2.imwrite("./img_features/features_img+centroid"+str(i)+".jpg",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
