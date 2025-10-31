import da

while True:
    text = input('da > ')
    if text == 'exit':
        break
    else:
        result, error = da.run('<stdin>', text)
        if error: print(error.as_string())
        else: print(result)