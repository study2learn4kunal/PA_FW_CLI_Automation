#!/usr/bin/env python
# coding: utf-8

# In[10]:


input_path = 'C:\\Users\\Home\\Documents\\input_data_vsys.csv'
output_path = 'C:\\Users\\Home\\Documents\\output_data.txt'

with open(input_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Create a new text file for writing
    with open(output_path, 'w') as output_file:
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # Write header to the new text file
                # output_file.write(','.join(row) + '\n')
                line_count += 1
            else:
                for _ in range(1):
                    output_file.write(f'# Interface Config \n\n')
                    # Write repeated lines to the new text file
                    output_file.write(f'set template {row[0]} vsys {row[1]} network layer3 unit {row[2]} tag\n')
                    output_file.write(f'set template {row[0]} vsys {row[1]} network layer3 unit {row[2]} mtu\n\n')
                    output_file.write(f'# Zone Config \n\n')
                    output_file.write(f'set template {row[0]} config zone {row[3]} network layer3 unit {row[2]}\n')
                
                    # Add a space between each set of lines
                output_file.write('\n')
                
                # Increment the line count
                line_count += 1

print(f"Data written to {output_path}")


# In[ ]:




