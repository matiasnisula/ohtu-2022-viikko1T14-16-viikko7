*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User kalle 1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User kalle 1234
    Create User kalle 123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...