def extract_num_from_str(text):
    result=""
    check="0123456789"
    for x in text:
        if x in check:
            result+=x

    return result

print(extract_num_from_str("Born in february "))