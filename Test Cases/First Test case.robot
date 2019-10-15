*** Settings ***
#This test case is created to pull element locater from json fie
Library     Collections
Library     SeleniumLibrary
Library     ../Library/Locator.py


*** Variables ***

${browser}  Chrome
${URL}      https://jira.jnj.com/login.jsp

*** Test Cases ***

Firt test case to import json file
    [Tags]  abcd
     open Browser   ${URL}  ${browser}
     sleep  5s
     ${Username} =  Locator Name     Login_Page.User_name_name
     input text     name:${Username}  Mpawar5
     input text     xpath://input[@type='password']  Greenday@1
     click button   xpath://input[@name='login']
     close Browser


*** Keywords ***
Locator Name
   [Arguments]   ${JsonPath}
   ${result}=  get_element_locator      ${JsonPath}
   [return]   $(result}