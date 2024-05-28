import rtx_api_3_5 as rtx_api

while True:
    user_input = input("$ ")
    response = rtx_api.send_message(user_input)
    print(response)
    if "```python" in response:
        pycase = response[response.find("```python") + len("```python"):]
        response = pycase[:pycase.rfind("```") - len("```")]
    if "<br>" in response:
        response = response[:response.find("<br>")]
    if "ip_address" in response:
        response = response.replace("ip_address", "hostname")
    print(response)
    exec(response)
