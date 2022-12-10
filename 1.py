# Typeface-Test
from scipy.ndimage import label
import numpy


def find_region_bounding_boxes(matrix):
    matrix=numpy.array(matrix)
    labels,num_labels=label(matrix)
    indices=[(labels==i).nonzero() for i in range(1,num_labels+1)]
    bounding_boxes=[]
    for region in indices:
        xs=region[0]
        ys=region[1]
        min_x=min(xs)
        max_x=max(xs)
        min_y=min(ys)
        max_y=max(ys)
        center_x=(min_x+max_x)/2
        center_y=(min_y+max_y)/2
        width=max_y-min_y+1
        height=max_x-min_x+1
        bounding_boxes.append([center_x,center_y,width,height])
    return bounding_boxes



