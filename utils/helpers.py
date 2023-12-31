import json
import sys


def read_json(file_name, local=False, custom_path=''):
    """
    :param finle_name: filename
    :return: data
    """
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    try:
        f = open(base + file_name + '.json')
        data = json.load(f)
        f.close()
    except Exception as e:
        print(e)
        data = []

    return data


def save_json(data, name, local=False, custom_path=''):
    if custom_path:
        base = custom_path
    else:
        if local:
            base = 'C:/Users/Administrator/Desktop/'
        else:
            base = 'database/'
    jsonString = json.dumps(data)
    jsonFile = open(base + name + '.json', "w")
    jsonFile.write(jsonString)
    jsonFile.close()


def round_any(d, rounded_values=4):
    if type(d) == dict:
        for key in d:
            d[key] = round_any(d[key], rounded_values)
    elif type(d) in [list, set, tuple]:
        for i in range(len(d)):
            d[i] = round_any(d[i], rounded_values)
    else:
        try:
            d = rounded(d, rounded_values=rounded_values)
        except:
            pass
    return d


def rounded(number, n=0, rounded_values=2):
    if number is None:
        return None
    if abs(number) >= 1 or n > 10:
        return round(number / (10 ** n), rounded_values + n)
    else:
        return rounded(number * 10, n + 1, rounded_values)


def list_flatter(listi):
    result = []
    for el in listi:
        if type(el) == list:
            for e in el:
                result.append(e)
        else:
            result.append(el)
    return result


def set_env():
    if sys.platform == 'win32':
        env = 'local'
    else:
        env = 'prod'
    return env

def chunkify(big_list, chunk_size):
    chunks = [big_list[x:x + chunk_size] for x in range(0, len(big_list), chunk_size)]
    return chunks


def cross_matching(pattern_list, strings_list):
    findings = []
    for s in strings_list:
        for p in pattern_list:
            if p == s:
                findings.append(True)
            else:
                findings.append(False)
    if findings.count(True) == len(strings_list) and findings.count(True) == len(pattern_list):
        found = True
    else:
        found = False
    return found


def open_html(file_path=""):
    html_content = None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except Exception as e:
        pass
        # print(f'Error: reading  html file:')
        # print(e)
        # print(file_path)
    return html_content

def save_html(html_content, file_path=""):
    # file_path = f"database/hr_html/{file_name}.html"
    try:
        with open(file_path, 'wb') as file:
            file.write(html_content)
            # print(f'HTML content saved to {file_path}')
    except Exception as e:
        print(f'Error: save html file: {e}')