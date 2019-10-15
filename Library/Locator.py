import  json
import  jsonpath
import  os

    def  get_element_locator(locatorname):
        f=  open("C:/Users/mopawar/PycharmProjects/Creating_NewFramework/Data/EelementLocator.json")
        accessJson =  json.loads(f.read())
        getLocators =  jsonpath.jsonpath(accessJson,locatorname)
        return getLocators[0]