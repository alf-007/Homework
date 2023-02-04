#homework_2
#version_2

property_transfer_xml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';
//urn:multiCall/sessionId['?']</con:targetPath>"""

property_transfer_xml_1 = property_transfer_xml.split('con:targetType')
property_transfer_xml_2 = property_transfer_xml_1[1].strip('</>')


print(property_transfer_xml_2)