# import re

# def detect_file_language(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     if re.search(r'#include', content):
#         return 'C'
#     elif re.search(r'def', content):
#         return 'Python'
#     else:
#         return 'Unknown'

# def count_data_structure_operations(file_path, language):
#     with open(file_path, 'r') as file:
#         content = file.read()

#     operations = {
#         'initialization': 0,
#         'push': 0,
#         'pop': 0
#     }
#     data_structure = 'Stack'
#     if language == 'Python':
#         operations['initialization'] = len(re.findall(r'stack', content))
#         operations['push'] = len(re.findall(r'push', content))
#         operations['pop'] = len(re.findall(r'pop', content))
#         if len(re.findall(r'append', content)) > 0:
#             data_structure = 'Array'
#             operations['push'] = len(re.findall(r'append', content))


#     return operations,data_structure

# file_path = 'samplepy.py'
# language = detect_file_language(file_path)


# operations,ds = count_data_structure_operations(file_path, language)

# print(f'Language: {language}')
# print(f'Data Structure: {ds}')
# print(f'Initialization count: {operations["initialization"]}')
# print(f'Push count: {operations["push"]}')
# print(f'Pop count: {operations["pop"]}')

import re

def analyze_code(file_path):
    with open(file_path, 'r') as file:
        code_content = file.read()

    # Determine the file type based on the extension and keywords
    if file_path.lower().endswith('.py') or 'def ' in code_content:
        language = 'Python'
        stack_pattern = re.compile(r'\b(stack)\b')
        array_pattern = re.compile(r'\b(array)\b')
    elif file_path.lower().endswith('.c') or 'int main(' in code_content:
        language = 'C'
        stack_pattern = re.compile(r'\b(stack)\b|\b\(void\*\)')
        array_pattern = re.compile(r'\b(array)\b|\b\[\d+\]')
    else:
        print(f"Unsupported file type for {file_path}")
        return

    # Identify stacks and arrays
    stacks = re.findall(stack_pattern, code_content)
    arrays = re.findall(array_pattern, code_content)

    # Count initializations and operations
    initialization_count = len(re.findall(r'\b(\w+)\s*=\s*\w+\(', code_content))
    push_count = len(re.findall(r'push\(', code_content))
    pop_count = len(re.findall(r'pop\(', code_content))

    # Display statistics
    print(f"File: {file_path}")
    print(f"Language: {language}")
    print(f"Stacks: {stacks}")
    print(f"Arrays: {arrays}")
    print(f"Initialization Count: {initialization_count}")
    print(f"Push Count: {push_count}")
    print(f"Pop Count: {pop_count}")

    with open('analyzed_code.txt', 'w') as file:
        file.write(str(push_count)+str(pop_count))


file_path = 'samplepy.py'
analyze_code(file_path)
