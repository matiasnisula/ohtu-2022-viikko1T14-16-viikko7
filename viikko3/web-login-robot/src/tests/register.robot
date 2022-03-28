*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  abc
    Set Password  abc12345
    Set Password Confirmation  abc12345
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  abc1234567
    Set Password Confirmation  abc1234567
    Submit Credentials
    Register Should Fail With Message  Username min length: 3, only characters a-z allowed

Register With Valid Username And Too Short Password
    Set Username  abcd
    Set Password  abc123
    Set Password Confirmation  abc123
    Submit Credentials
    Register Should Fail With Message  Password min length: 8, must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  abc
    Set Password  12345abc
    Set Password Confirmation  12345ab
    Submit Credentials
    Register Should Fail With Message  Password doesnt match with password confirmation

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open
    
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
