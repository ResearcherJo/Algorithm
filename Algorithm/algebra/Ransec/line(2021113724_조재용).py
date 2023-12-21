import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import svd

print("Matplotlib Version : 3.8.2")
print("numpy Version : 1.26.2")

def total_least_squares_fit(x, y):
    # 데이터의 중심을 원점으로 이동
    x_mean, y_mean = np.mean(x), np.mean(y)
    centered_points = np.column_stack((x - x_mean, y - y_mean))
    
    # 데이터 행렬 만들기
    A = centered_points.T
    
    # SVD (Singular Value Decomposition)를 사용하여 A 행렬 분해
    _, _, Vt = svd(A)
    
    # TLS 해 계산
    m_tls, b_tls = -Vt[0, 1] / Vt[0, 0], y_mean - (-Vt[0, 1] / Vt[0, 0]) * x_mean
    
    return m_tls, b_tls

def ransac_fit(x, y, out, d,n):
    def find_line(x1, y1, x2, y2):
        # 두 점을 지나는 직선의 방정식 찾기: y = mx + b
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m, b

    def count_points_on_line(x, y, m, b, out):
        # 주어진 직선에서 out만큼 떨어진 공간에 속하는 점들의 개수 계산
        distances = np.abs(y - (m * x + b))
        count = np.sum(distances <= out)
        return count

    best_m, best_b, best_count = None, None, 0

    for _ in range(n):  # 적절한 반복 횟수 선택
        # 서로 다른 두 점 선택
        idx1, idx2 = np.random.choice(len(x), size=2, replace=False)
        x1, y1, x2, y2 = x[idx1], y[idx1], x[idx2], y[idx2]

        # 두 점을 지나는 직선의 방정식 찾기
        m, b = find_line(x1, y1, x2, y2)

        # 직선에서 out만큼 떨어진 공간에 속하는 점들의 개수 계산
        count = count_points_on_line(x, y, m, b, out)

        # 현재 직선이 더 많은 점들을 포함하면 업데이트
        if count > best_count:
            best_m, best_b, best_count = m, b, count

        # 임계값 이상인 경우 종료
        if best_count >= d:
            break

    return best_m, best_b

# txt 파일의 절대 경로 / 상대경로로 할때 안되었습니다.
file_path = 'Algorithm/algebra/Ransec/line_fit_sample_data_with_delimiter_comma.txt'

matrix = []

with open(file_path, 'r') as file:
    for line in file:
        row = [float(value) for value in line.strip().split(',')]
        matrix.append(row)

#좌표 추출
x = [point[0] for point in matrix]
y = [point[1] for point in matrix]

m_tls, b_tls = total_least_squares_fit(x,y)
m_ransac, b_ransac = ransac_fit(np.array(x),np.array(y),0.01,98,1000)

plt.scatter(x, y, label='Data Points', color ='black')
plt.plot(x, m_tls * np.array(x) + b_tls, color='red', label='Total Least Squares Fit')
plt.plot(x, np.polyval([m_ransac, b_ransac], x), color='yellow', label='RANSAC Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

