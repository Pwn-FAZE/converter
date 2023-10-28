def bin_to_c_array(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    c_array = "unsigned char data[] = {"
    for byte in data:
        c_array += str(byte) + ", "
    c_array = c_array[:-2] + "};"
    return c_array

file_path = input("请输入bin文件路径：")
c_array = bin_to_c_array(file_path)

with open("shellcode.c", "w") as f:
    f.write(c_array)

print("已生成名为shellcode的C语言数组文件。")
