import os
import glob

# 指定資料夾路徑
folder_path = 'C:/Users/a1999/Desktop/實驗/SA'

# 檢索資料夾中的所有圖片文件
image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + \
              glob.glob(os.path.join(folder_path, '*.jpeg')) + \
              glob.glob(os.path.join(folder_path, '*.png')) + \
              glob.glob(os.path.join(folder_path, '*.gif'))

# 刪除每個圖片文件
for image_file in image_files:
    os.remove(image_file)
# import os
# import glob

# def delete_images_in_folder(folder_path):
#     # 檢索資料夾中的所有圖片文件
#     image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + \
#                   glob.glob(os.path.join(folder_path, '*.jpeg')) + \
#                   glob.glob(os.path.join(folder_path, '*.png')) + \
#                   glob.glob(os.path.join(folder_path, '*.gif'))

#     # 刪除每個圖片文件
#     for image_file in image_files:
#         os.remove(image_file)

#     # 遞迴遍歷子資料夾
#     for root, dirs, files in os.walk(folder_path):
#         for dir in dirs:
#             delete_images_in_folder(os.path.join(root, dir))

# # 指定主資料夾路徑
# main_folder_path = '/path/to/main_folder'

# # 刪除主資料夾及其子資料夾中的圖片
# delete_images_in_folder(main_folder_path)