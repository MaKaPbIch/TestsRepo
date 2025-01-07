*** Settings ***
Documentation     Example test cases using Robot Framework
Library           String
Library           Collections

*** Variables ***
${MESSAGE}        Hello, World!
@{NUMBERS}        1    2    3    4    5

*** Test Cases ***
Test String Operations
    ${upper}=    Convert To Upper Case    ${MESSAGE}
    Should Be Equal    ${upper}    HELLO, WORLD!
    
    ${lower}=    Convert To Lower Case    ${MESSAGE}
    Should Be Equal    ${lower}    hello, world!

Test List Operations
    Length Should Be    ${NUMBERS}    5
    
    ${sum}=    Evaluate    sum(${NUMBERS})
    Should Be Equal As Numbers    ${sum}    15

Test Dictionary Operations
    ${dict}=    Create Dictionary    name=John    age=30    city=New York
    Dictionary Should Contain Key    ${dict}    name
    Dictionary Should Contain Value    ${dict}    30
    
Test Conditions
    ${age}=    Set Variable    20
    Run Keyword If    ${age} >= 18    Log    Adult
    ...    ELSE    Log    Minor
