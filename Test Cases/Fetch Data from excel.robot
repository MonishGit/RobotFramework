*** Settings ***

Library      SeleniumLibrary
Resource     ../Resource_second level Keyword/Keyword for Exceldata.robot


*** Variables ***

*** Test Cases ***

First test case which will Featch excel data using resource and python file
    [tags]  abcde

    [Documentation]  this test is important for data parameterization
    ${rows}=  Read number of rows in give Excel   Test3
    ${Cell_data}=  Read cell data   Test3   1   1
    Log to console  ${Cell_data}
    Log to console  ${rows}


*** Keywords ***