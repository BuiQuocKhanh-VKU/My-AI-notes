# numPy: Numerical Python
# xử lý các mảng (arrays) đa chiều và thực hiện các phép toán số học với mảng.
print("#### NumPy ####")
import numpy as np
# Create a NumPy array
arr = np.array([1,2,3,4,5])
print("arr:", arr)

arr2D = np.array(([1,2,3],[4,5,6]))
print("arr2D:", arr2D)

arrSum = np.sum(arr)
print("Sum of arr: ", arrSum)

arr_mean = np.mean(arr)
print("GTri trung binh: ", arr_mean)  

# Pandas: Thư viện mạnh mẽ để xử lý dữ liệu dạng bảng (DataFrame).
print("#### Pandas ####")
import pandas as pd

# Create a DataFrame
data = {
    "name" : ['Khanh', 'Hanh', 'Hieu'], 
    "age" : [20, 21, 22],
    "city" : ['Da Nang', 'Hue', 'Quang Tri']    
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)


print("Name column:\n", df['name'])  # In ra cột 'name'

filtered_df = df[df['age'] > 21]
print("filtered:\n", filtered_df) 

avg_age = df['age'].mean()
print("Average age:", avg_age)  # Tính trung bình tuổi
