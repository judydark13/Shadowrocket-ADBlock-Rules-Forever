import os

conf_file = 'sr_ad_only.conf'

if os.path.exists(conf_file):
    # 读取文件内容
    with open(conf_file, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    # 处理每一行
    for line in lines:
        if "DOMAIN-SUFFIX" in line:
            # 提取域名部分
            domain_part = line.split(',')[1].strip()
            # 构造新的规则格式
            modified_lines.append(f"DOMAIN-SUFFIX,{domain_part}")

    # 保存修改后的内容
    with open('sr_ad_only_modified.conf', 'w') as file:
        file.write("\n".join(modified_lines))

    print("Modified .conf file saved as sr_ad_only_modified.conf")
else:
    print(f"{conf_file} not found.")
