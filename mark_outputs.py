import os,cv2
import sys
import pickle
classes=["b",'basophil','eosinophil','giant_platelet','ig','lymphocyte','monocyte','neutrophil','notawbc','nrbc','platelet_clump']
p=pickle.load(open(sys.argv[1]))
file_names=[]
for line in open(sys.argv[2]):
    file_names.append(line.strip())

for i in xrange(len(p[0])):
    img=cv2.imread(file_names[i])
    for c in xrange(len(p)):
        for predictions in xrange(len(p[c][i])):
            if p[c][i][predictions][4] > 0.5:
                cv2.rectangle(img,(p[c][i][predictions][0],p[c][i][predictions][1]),(p[c][i][predictions][2],p[c][i][predictions][3]),(0,255,0),3)
                cv2.putText(img,classes[c],(p[c][i][predictions][2],p[c][i][predictions][3]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA)
    file_name=file_names[i].strip().split("/")[-1]
    cv2.imwrite(os.path.join(sys.argv[3],file_name),img)
