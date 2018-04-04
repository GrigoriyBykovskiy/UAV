#!programm searching intersection point for 2 lines (defined by 2 points)
import numpy as np
def intersection_point(line1=([],[]),line2=([],[])):
    dot_1,dot_2=line1
    dot_3,dot_4=line2
    slope_of_line_1=(dot_2[1]-dot_1[1])/(dot_2[0]-dot_1[0])
    slope_of_line_2=(dot_4[1]-dot_3[1])/(dot_4[0]-dot_3[0])
    free_coefficient_of_line_1=dot_1[1]-slope_of_line_1*dot_1[0]
    free_coefficient_of_line_2=dot_3[1]-slope_of_line_2*dot_3[0]
    coefficients_for_lines=np.array([[-slope_of_line_1,1.], [-slope_of_line_2,1.]])
    free_coefficients_for_lines=np.array([free_coefficient_of_line_1,free_coefficient_of_line_2])
    intersection_point=np.linalg.solve(coefficients_for_lines, free_coefficients_for_lines)
    return(intersection_point)
def main():
    while(True):
        dot_1_1=input("Write x and y coordinates of dot_1 line_1:")
        dot_1_1=list(float(item) for item in dot_1_1.split())
        dot_1_2=input("Write x and y coordinates of dot_2 line_1:")
        dot_1_2=list(float(item) for item in dot_1_2.split())
        line_1=list()
        line_1.append(dot_1_1)
        line_1.append(dot_1_2)
        line_1=tuple(line_1)
        dot_2_1=input("Write x and y coordinates of dot_1 line_2:")
        dot_2_1=list(float(item) for item in dot_2_1.split())
        dot_2_2=input("Write x and y coordinates of dot_2 line_2:")
        dot_2_2=list(float(item) for item in dot_2_2.split())
        line_2=list()
        line_2.append(dot_2_1)
        line_2.append(dot_2_2)
        line_2=tuple(line_2)
        print("Intersection point of lines is:",intersection_point(line_1,line_2))
        ex_or_re=input("Exit -- e Repeat -- r\n")
        if (ex_or_re=='e'): 
            break
if __name__ == "__main__":
    main()
