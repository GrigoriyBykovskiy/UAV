#! Programm find distance from camera to dot
import numpy
import cv2
def main():
    know_widht=20.0/2.54
    know_distance=40.0/2.54
    image_paths=["1-+5.0.bmp","1-+10.0.bmp","1-+15.0.bmp"]
    for i in range(3):
        image=cv2.imread(image_paths[i])
        pixel_widht=find_marker(image)
        focal_lenght=(know_distance*pixel_widht[1][0])/know_widht
        distance=distance_to_camera(know_widht,focal_lenght,pixel_widht[1][0])
        print(distance*2.54)
def find_marker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    (_,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key = cv2.contourArea)
    return cv2.minAreaRect(c)
def distance_to_camera(know_widht,focal_lenght,pixel_widht):
    return (know_widht*focal_lenght)/pixel_widht
main()