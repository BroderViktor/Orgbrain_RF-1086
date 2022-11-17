import requests
from bs4 import BeautifulSoup

#Systemusername dont change unless granted new code by altinn
SystemUserName = "17472"
#SystemPassword dont change unless granted new password by altinn
SystemPassword = "passord1"

#test user
testUserSocialSecurityNumber = "brasa1"
testUserPassword = "Test123"

#This function sends an SMS authorization code from altinn to the user
#Returns a tuple with boolean if the function was a success or not, aswell as an norwegian error message
def sendAuthCodeToUser(username, userpassword):
   headers = {
   "Accept-Encoding": "gzip,deflate",
   "Content-Type" : "text/xml;charset=UTF-8",
   "SOAPAction": "http://www.altinn.no/services/Authentication/SystemAuthentication/2009/10/ISystemAuthenticationExternal/GetAuthenticationChallenge",
   "Host": "tt02.altinn.no",
   "Connection": "Keep-Alive",
   "User-Agent": "Apache-HttpClient/4.5.5 (Java/16.0.1)"
   }

   body = """
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.altinn.no/services/Authentication/SystemAuthentication/2009/10" xmlns:ns1="http://schemas.altinn.no/services/Authentication/2009/10">
      <soapenv:Header/>
      <soapenv:Body>
         <ns:GetAuthenticationChallenge>
            <ns:challengeRequest>
               <ns1:AuthMethod>SMSPin</ns1:AuthMethod>
               <ns1:SystemUserName>{SystemUserName_Str}</ns1:SystemUserName>
               <ns1:UserPassword>{UserPassword_Str}</ns1:UserPassword>
               <ns1:UserSSN>{UserSSN_Str}</ns1:UserSSN>
            </ns:challengeRequest>
         </ns:GetAuthenticationChallenge>
      </soapenv:Body>
   </soapenv:Envelope>

   """.format(
      SystemUserName_Str = SystemUserName, 
      UserSSN_Str = username, 
      UserPassword_Str = userpassword)
   #Posts soap request and stores respons
   re = requests.post("https://tt02.altinn.no/AuthenticationExternal/SystemAuthentication.svc", data=body, headers=headers)
   #Uses beautifulSoup to parse the xml return
   soup = BeautifulSoup(re.content, features="lxml")
   #Gets Status code
   responsStatus = soup.find("a:status").string
   if (responsStatus == "Ok"):
      return {True, "Success"}
   else:
      return {False, soup.find("a:message").string}

def sendAuthCodeToUser(username, userpassword, authcode, orgnumber, data):
   headers = {
      "Accept-Encoding": "gzip,deflate",
      "Content-Type" : "text/xml;charset=UTF-8",
      "SOAPAction": "http://www.altinn.no/services/Authentication/SystemAuthentication/2009/10/ISystemAuthenticationExternal/GetAuthenticationChallenge",
      "Host": "tt02.altinn.no",
      "Connection": "Keep-Alive",
      "User-Agent": "Apache-HttpClient/4.5.5 (Java/16.0.1)"
   }
 
   formData = """
   <Skjema skjemanummer="890" spesifikasjonsnummer="12144" blankettnummer="RF-1086" tittel="Aksjonærregisteroppgaven" gruppeid="2586">
      <GenerellInformasjon-grp-2587 gruppeid="2587">
         <Selskap-grp-2588 gruppeid="2588">
            <EnhetOrganisasjonsnummer-datadef-18 orid="18">911007118</EnhetOrganisasjonsnummer-datadef-18>
            <EnhetNavn-datadef-1 orid="1">SALTSTRAUMEN OG JELSA</EnhetNavn-datadef-1>
         </Selskap-grp-2588>
      </GenerellInformasjon-grp-2587>
   </Skjema>
   """.format()

   body = """
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.altinn.no/services/Intermediary/Shipment/IntermediaryInbound/2009/10">
      <soapenv:Header/>
      <soapenv:Body>
         <ns:SubmitFormTaskBasic>
            <ns:systemUserName>{SystemUserName_Str}</ns1:SystemUserName>
            <ns:systemPassword>{SystemPassword_Str}</ns:systemPassword>
            <ns:userSSN>{UserSSN_Str}</ns1:UserSSN>
            <ns:userPassword>{UserPassword_Str}</ns1:UserPassword>
            <ns:userPinCode>{UserPin_Str}</ns:userPinCode>
            <ns:authMethod>SMSPin</ns:authMethod>
            
            <ns:formTaskShipment>
               <ns:Reportee>{CompanyNumber_Str}</ns:Reportee>
               <ns:ExternalShipmentReference>{UniqueNumIdentifier}</ns:ExternalShipmentReference>
               <ns:FormTasks>
                  <ns:ServiceCode>1166</ns:ServiceCode>
                  <ns:ServiceEdition>181026</ns:ServiceEdition>
                  <ns:Forms>
                     <ns:Form>
                        <ns:Completed>false</ns:Completed>
                        <ns:DataFormatId>890</ns:DataFormatId>
                        <ns:DataFormatVersion>12144</ns:DataFormatVersion>
                        <ns:EndUserSystemReference>1</ns:EndUserSystemReference>
                        <ns:FormData>
                        <![CDATA[{formData_Str}]]>
                        </ns:FormData>
                     </ns:Form>
                  </ns:Forms>
               </ns:FormTasks>
            
               <ns:IsUserDelegationLocked>false</ns:IsUserDelegationLocked>
            </ns:formTaskShipment>
         </ns:SubmitFormTaskBasic>
      </soapenv:Body>
   </soapenv:Envelope>

   """.format(
         SystemUserName_Str = SystemUserName, 
         SystemPassword_Str = SystemPassword, 
         UserSSN_Str = username, 
         UserPassword_Str = userpassword,
         UserPin_Str = authcode,
         formData_Str = formData,
         UniqueNumIdentifier = 0,
         CompanyNumber_Str = orgnumber,
      )


   #Posts soap request and stores respons
   re = requests.post("https://tt02.altinn.no/AuthenticationExternal/SystemAuthentication.svc", data=body, headers=headers)
   #Uses beautifulSoup to parse the xml return
   soup = BeautifulSoup(re.content, features="lxml")
   #Gets Status code
   responsStatus = soup.find("a:status").string
   if (responsStatus == "Ok"):
      return {True, "Success"}
   else:
      return {False, soup.find("a:message").string}
