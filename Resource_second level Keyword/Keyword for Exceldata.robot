*** Settings ***

#Library     SeleniumLibrary
Library     ../Library/ExcelExtract.py


*** Keywords ***

Read number of rows in give Excel
    [Arguments]  ${Sheetname}
    ${rows}=     find max rows   ${Sheetname}
    [Return]     ${rows}

Read cell data
    [Arguments]  ${Sheetname}   ${Row}  ${Column}
    ${Cell_data}=  find cell data   ${Sheetname}   ${Row}  ${Column}
    [Return]  ${Cell_data}