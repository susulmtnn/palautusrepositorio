*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Suvi
    Set Password  suvion123
    Set Reconfirm Password  suvion123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sw
    Set Password  123456
    Set Reconfirm Password  123456
    Submit Credentials
    Register Should Fail With Message  The minimum length for a username is 3

Register With Valid Username And Too Short Password
    Set Username  seija
    Set Password  123456
    Set Reconfirm Password  123456
    Submit Credentials
    Register Should Fail With Message  Minimum password length is 8


Register With Valid Username And Invalid Password
    Set Username  suvisuvi
    Set Password  suvionsuvi
    Set Reconfirm Password  suvionsuvi
    Submit Credentials
    Register Should Fail With Message  Password cannot only contain characters

Register With Nonmatching Password And Password Confirmation
    Set Username  marsumarsu
    Set Password  marsumarsu22
    Set Reconfirm Password  suvionsuvi12
    Submit Credentials
    Register Should Fail With Message  Passwords do not match


Register With Username That Is Already In Use
    Set Username  suvi
    Set Password  suvion1234
    Set Reconfirm Password  suvion1234
    Submit Credentials
    Register Should Fail With Message  User already exists

Login After Successful Registration
    Set Username  Suvi
    Set Password  suvion123
    Set Reconfirm Password  suvion123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page 
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  Suvi
    Set Password  suvion123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  marsu
    Set Password  marsu
    Set Reconfirm Password  marsu
    Submit Credentials
    Register Should Fail With Message  Minimum password length is 8
    Click Link  Login 
    Login Page Should Be Open
    Set Username  marsu
    Set Password  marsu
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Reconfirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
    
Login Should Succeed
    Main Page Should Be Open

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  suvi  kalle123
    Go To Register Page