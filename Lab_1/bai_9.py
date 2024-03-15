#Nhập tọa độ đỉnh: 
Mx, My = map(float, input("Nhập vào tọa độ đỉnh M(x,y): ").split())
Nx, Ny = map(float, input("Nhập vào tọa độ đỉnh N(x,y): ").split())
Px, Py = map(float, input("Nhập vào tọa độ đỉnh P(x,y): ").split())
Qx, Qy = map(float, input("Nhập vào tọa độ đỉnh Q(x,y): ").split())

#Tính toán tọa độ trung điểm mỗi cạnh:
MN = (Mx+Nx)/2, (My+Ny)/2
NP = (Nx+Px)/2, (Ny+Py)/2
PQ = (Px+Qx)/2, (Py+Qy)/2
QM = (Qx+Mx)/2, (Qy+My)/2

#In ra trung điểm mỗi cạnh:
print("Trung điểm cạnh MN là:", MN)
print("Trung điểm cạnh NP là:", NP)
print("Trung điểm cạnh PQ là:", PQ)
print("Trung điểm cạnh QM là:", QM)
