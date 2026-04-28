from pprint import pprint

import xmltodict


# with open("../xmlfile.xml", "r") as file:
#     xml_string = file.read()
#     print(xml_string)

xml_string = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:myg="http://www.mygemini.com/schemas/mygemini"
                  xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soapenv:Header>
        <wsse:Security>
            <wsse:UsernameToken>
                <wsse:Username>******</wsse:Username>
                <wsse:Password>******</wsse:Password>
                <wsse:Nonce>******</wsse:Nonce>
            </wsse:UsernameToken>
        </wsse:Security>
    </soapenv:Header>
    <soapenv:Body>
        <myg:GetAccountMovementsRequestIo>
            <myg:accountMovementFilterIo>
                <myg:pager>
                    <myg:pageIndex>0</myg:pageIndex>
                    <myg:pageSize>700</myg:pageSize>
                </myg:pager>
                <myg:accountNumber>GE16TB7739436090000001</myg:accountNumber>
                <myg:accountCurrencyCode>GEL</myg:accountCurrencyCode>
                <myg:periodFrom>2025-03-19T00:00:00</myg:periodFrom>
                <myg:periodTo>2025-03-20T23:00:00</myg:periodTo>
            </myg:accountMovementFilterIo>
        </myg:GetAccountMovementsRequestIo>
    </soapenv:Body>
</soapenv:Envelope>"""



converted_xml: dict = xmltodict.parse(xml_string)


converted_xml['soapenv:Envelope']['soapenv:Body']['myg:GetAccountMovementsRequestIo']['myg:accountMovementFilterIo']['myg:accountCurrencyCode'] = "EUR"

pprint(converted_xml, indent=4)

edited_xml: str = xmltodict.unparse(converted_xml)



with open("edited_xml.xml", "w") as file:
    file.write(edited_xml)

