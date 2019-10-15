*** Settings ***
Documentation     A test suite with a single test for Robotcorder - Chrome Web Store
Library           Selenium2Library    timeout=10

*** Variables ***
${BROWSER}    chrome
${SLEEP}    3
${IssueID}  AAQF-13166
*** Test Cases ***
RobotCoderTest
    Open Browser    https://jira.jnj.com/login.jsp    ${BROWSER}
    Input Text    //input[@name="os_username"]    Mpawar5
    Click Element    //div[@class="field-group"]
    Input Text    //input[@name="os_password"]    Greenday@1
#    Click Element    xpath=(//div[@class="field-group"])[2]
    Click Element    //input[@name="login"]
    Input Text    //input[@name="searchString"]    AAQF-13815
    