import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import svd

print("Matplotlib Version : 3.8.2")
print("numpy Version : 1.26.2")

def total_least_squares_fit_plane(x, y, z):
    # 데이터의 중심을 원점으로 이동
    x_mean, y_mean, z_mean = np.mean(x), np.mean(y), np.mean(z)
    centered_points = np.column_stack((x - x_mean, y - y_mean, z - z_mean))
    
    # 데이터 행렬 만들기
    A = centered_points.T
    
    # SVD (Singular Value Decomposition)를 사용하여 A 행렬 분해
    _, _, Vt = svd(A)
    
    # TLS 해 계산
    m_tls, n_tls, d_tls = -Vt[0, 2] / Vt[0, 0], -Vt[1, 2] / Vt[1, 1], z_mean - (-Vt[0, 2] / Vt[0, 0]) * x_mean - (-Vt[1, 2] / Vt[1, 1]) * y_mean
    
    return m_tls, n_tls, d_tls


def ransac_fit_plane(x, y, z, out, d, n):
    def find_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3):
        # 세 점을 지나는 평면의 방정식 찾기: ax + by + cz + d = 0
        # 여기서 a, b, c는 평면의 법선 벡터이다.
        v1 = np.array([x2 - x1, y2 - y1, z2 - z1])
        v2 = np.array([x3 - x1, y3 - y1, z3 - z1])
        normal_vector = np.cross(v1, v2)
        a, b, c = normal_vector
        d = -(a * x1 + b * y1 + c * z1)
        return a, b, c, d

    def count_points_on_plane(x, y, z, a, b, c, d, out):
        # 주어진 평면에서 out만큼 떨어진 공간에 속하는 점들의 개수 계산
        distances = np.abs(a * x + b * y + c * z + d) / np.sqrt(a**2 + b**2 + c**2)
        count = np.sum(distances <= out)
        return count

    best_a, best_b, best_c, best_d, best_count = None, None, None, None, 0

    for _ in range(n):
        # 서로 다른 세 점 선택
        idx1, idx2, idx3 = np.random.choice(len(x), size=3, replace=False)
        x1, y1, z1, x2, y2, z2, x3, y3, z3 = x[idx1], y[idx1], z[idx1], x[idx2], y[idx2], z[idx2], x[idx3], y[idx3], z[idx3]

        # 세 점을 지나는 평면의 방정식 찾기
        a, b, c, d = find_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3)

        # 평면에서 out만큼 떨어진 공간에 속하는 점들의 개수 계산
        count = count_points_on_plane(x, y, z, a, b, c, d, out)

        # 현재 평면이 더 많은 점들을 포함하면 업데이트
        if count > best_count:
            best_a, best_b, best_c, best_d, best_count = a, b, c, d, count

        # 임계값 이상인 경우 종료
        if best_count >= d:
            break

    return best_a, best_b, best_c, best_d

# txt 파일의 절대 경로 / 상대경로로 할때 안되었습니다.
file_path = 'Algorithm/algebra/Ransec/plane_fit_sample_data_with_delimiter_comma.txt'

matrix = []

with open(file_path, 'r') as file:
    for line in file:
        row = [float(value) for value in line.strip().split(',')]
        matrix.append(row)

#좌표 추출
x = [point[0] for point in matrix]
y = [point[1] for point in matrix]
z = [point[2] for point in matrix]

m_tls, n_tls, d_tls = total_least_squares_fit_plane(x,y,z)
a_ransac, b_ransac, c_ransac, d_ransac = ransac_fit_plane(np.array(x),np.array(y),np.array(z),0.01,98,1000)

#시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, label='Data Points', color='black')

# 평면 시각화(TLS)
x_range = np.linspace(min(x), max(x), 100)
y_range = np.linspace(min(y), max(y), 100)
x_plane, y_plane = np.meshgrid(x_range, y_range)
z_plane = m_tls * x_plane + n_tls * y_plane + d_tls
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5, color='blue', label='TLS Plane Fit')

# 평면 시각화(Ransac)
x_range = np.linspace(min(x), max(x), 100)
y_range = np.linspace(min(y), max(y), 100)
x_plane, y_plane = np.meshgrid(x_range, y_range)
z_plane = -(a_ransac * x_plane + b_ransac * y_plane + d_ransac) / c_ransac
ax.plot_surface(x_plane, y_plane, z_plane, alpha=0.5, color='red', label='RANSAC Plane Fit')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()


