import pandas as pd
import numpy as py
import re

df_devices = pd.read_excel(r"D:\Data_Analytics\CPSC4820-Visualnz\Assignment1\Shows and Devices.xlsx",sheet_name='Devices')
df_response = pd.read_excel(r"D:\Data_Analytics\CPSC4820-Visualnz\Assignment1\Netflix Survey.xlsx",sheet_name='Form responses 1')




count_phone=0
count_tv=0
count_laptop=0
count_ipad=0
count_other=0
device_list = []
devices = ["Phone","TV","Laptop","iPad"]
devices_count = {"Phone"    : count_phone,
                  "TV"      : count_tv,
                  "Laptop"  : count_laptop,
                  "IPad"    : count_ipad,
                  "Other"   : count_other
                }

for ind in df_response.index:
    if df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] in devices:
        # print("xxxxxxxxxx")
        # print(df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] )
        if df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == 'TV':
            count_tv = count_tv + 1
        elif df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == 'Phone':
            count_phone = count_phone + 1
        elif df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == 'Laptop':
            count_laptop = count_laptop + 1
        elif df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == 'IPad':
            count_ipad = count_ipad + 1
    elif df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == "On my pohne":
        count_phone = count_phone + 1
    elif " & " in df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] or ", " in  df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind]:
        device_list.extend(re.split(' & |, ', df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind]))
    elif df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind] == "TVPHONEIPAD":
        device_list.extend(re.findall('|'.join(devices), df_response['How have you been watching Netflix? (Phone, TV, etc.)'][ind], re.IGNORECASE))
    else:    
        count_other = count_other + 1

for item in device_list:
    item_upper = item.upper()
    if item_upper == 'TV':
        count_tv = count_tv + 1
    elif item_upper == 'PHONE':
        count_phone = count_phone + 1
    elif item_upper == 'Laptop':
        count_laptop = count_laptop + 1
    elif item_upper == 'IPAD':
        count_ipad = count_ipad + 1
    else:
        count_other = count_other + 1

devices_count = {"Phone"    : count_phone,
                  "TV"      : count_tv,
                  "Laptop"  : count_laptop,
                  "IPad"    : count_ipad,
                  "Other"   : count_other
                }

#print(devices_count)
#print(device_list)
def get_new_df(input_df):
    device_data = [(device, count) for device, count in devices_count.items()]

    # Create the DataFrame from the list of tuples
    new_df = pd.DataFrame(device_data, columns=["Device", "Count"])
    return new_df
def get_output_schema():
  return pd.DataFrame({
    'Device' : prep_string(),
    'Count'  : prep_int()	

})