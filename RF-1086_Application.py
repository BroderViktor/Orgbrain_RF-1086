import requests
import random
from bs4 import BeautifulSoup

#Systemusername dont change unless granted new code by altinn
SystemUserName = "17472"
#SystemPassword dont change unless granted new password by altinn
SystemPassword = "passord1"

#test user
testUserSocialSecurityNumber = "brasa1"
testUserPassword = "Tæst123"

testData = {
   "ISIN": "NO1234567891",
   "Aksjeklasse": "A-aksjer",
   "Intektsår": "2022",
   "Ansvarlig_Navn": "Viktor",
   "Ansvarlig_Rolle": "Admin",
   "Ansvarlig_Epost": "viktor",
   "Ansvarlig_Tlf": "91639035",
}

UtbytteTestData = [["utbytte1", "noemer1", "tidspunkt1"], ["utbytte2", "noemer2", "tidspunkt2"]]

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
      UserPassword_Str = userpassword).encode("utf-8")
   #Posts soap request and stores respons
   re = requests.post("https://tt02.altinn.no/AuthenticationExternal/SystemAuthentication.svc", data=body, headers=headers)
   
   print(re.content)
   
   #Uses beautifulSoup to parse the xml return
   soup = BeautifulSoup(re.content, features="html.parser")
   #Gets Status code
   responsStatus = soup.find("a:status").string
   if (responsStatus == "Ok"):
      return {True, "Success"}
   else:
      return {False, soup.find("a:message").string}

def FillFormData_GenerellInformasjon(OrgNum, PostNum, Poststed, ISIN, AkjseKlasse, Intektsår, AnsvarligNavn, AnsvarligRolle, AnsvarligEpost, AnsvarligTlf):
   #Denne skulle være med men trenger vi den ??? <AksjeTypePreutfylt-datadef-24503 orid="24503"></AksjeTypePreutfylt-datadef-24503>
   
   return """
       <GenerellInformasjon-grp-2587 gruppeid="2587">
         <Selskap-grp-2588 gruppeid="2588">
            <EnhetOrganisasjonsnummer-datadef-18 orid="18">{f_OrgNumber}</EnhetOrganisasjonsnummer-datadef-18>
            <EnhetPostnummer-datadef-6673 orid="6673">{f_PostNummer}</EnhetPostnummer-datadef-6673>
            <EnhetPoststed-datadef-6674 orid="6674">{f_Poststed}</EnhetPoststed-datadef-6674>
            <EnhetISINNummer-datadef-17513 orid="17513">{f_ISIN}</EnhetISINNummer-datadef-17513>
            <AksjeType-datadef-17659 orid="17659">{f_AkjseKlasse}</AksjeType-datadef-17659>
            <Inntektsar-datadef-692 orid="692">{f_Intektsår}</Inntektsar-datadef-692>
            <AksjonarregisteroppgaveHovedskjemaInnsendingsmate-datadef-34855 orid="34855">{WHAT}</AksjonarregisteroppgaveHovedskjemaInnsendingsmate-datadef-34855>
         </Selskap-grp-2588>
         <Kontaktperson-grp-3442 gruppeid="3442">
               <KontaktpersonSkjemaNavn-datadef-33918 orid="33918">{f_AnsvarligNavn}</KontaktpersonSkjemaNavn-datadef-33918>
               <KontaktpersonSkjemaRolle-datadef-33915 orid="33915">{f_AnsvarligRolle}</KontaktpersonSkjemaRolle-datadef-33915>
               <KontaktpersonSkjemaEPost-datadef-30533 orid="30533">{f_AnsvarligEpost}</KontaktpersonSkjemaEPost-datadef-30533>
               <KontaktpersonSkjemaTelefonnummer-datadef-33916 orid="33916">{f_AnsvarligTlf}</KontaktpersonSkjemaTelefonnummer-datadef-33916>
         </Kontaktperson-grp-3442>
         <AnnenKontaktperson-grp-5384 gruppeid="5384">
            <KontaktpersonVirksomhetEPost-datadef-28209 orid="28209">{WHAT}</KontaktpersonVirksomhetEPost-datadef-28209>
         </AnnenKontaktperson-grp-5384>
      </GenerellInformasjon-grp-2587>
      """.format(
         f_OrgNumber = OrgNum, 
         f_PostNummer = PostNum,
         f_Poststed = Poststed,
         f_ISIN = ISIN,
         f_Intektsår = Intektsår,
         f_AkjseKlasse = AkjseKlasse,
         f_AnsvarligNavn = AnsvarligNavn,
         f_AnsvarligRolle = AnsvarligRolle,
         f_AnsvarligEpost = AnsvarligEpost,
         f_AnsvarligTlf = AnsvarligTlf,
         WHAT = "",
      )

def FillFormData_Selskapsopplysninger(Akjsekapital, KapitalIAksjeklasse, Pålydende, AntallAksjerFjoråret, AntallAksjer, Overkurs):
   return """
        <Selskapsopplysninger-grp-2589 gruppeid="2589">
            <AksjekapitalForHeleSelskapet-grp-3443 gruppeid="3443">
               <Aksjekapital-datadef-87 orid="87">{f_Akjsekapital}</Aksjekapital-datadef-87>
            </AksjekapitalForHeleSelskapet-grp-3443>

            <AksjekapitalIDenneAksjeklassen-grp-3444 gruppeid="3444">
               <AksjekapitalISINAksjetype-datadef-17664 orid="17664">{f_AksjekapitalIDenneAksjeklassen}</AksjekapitalISINAksjetype-datadef-17664>
            </AksjekapitalIDenneAksjeklassen-grp-3444>

            <PalydendePerAksje-grp-3447 gruppeid="3447">
               <AksjeMvPalydende-datadef-23945 orid="23945">{f_PalydendePerAksje}</AksjeMvPalydende-datadef-23945>
            </PalydendePerAksje-grp-3447>

            <AntallAksjerIDenneAksjeklassen-grp-3445 gruppeid="3445">
               <AksjerMvAntallFjoraret-datadef-29166 orid="29166">{f_AntallAksjerFjoråret}</AksjerMvAntallFjoraret-datadef-29166>
               <AksjerMvAntall-datadef-29167 orid="29167">{f_AntallAksjer}</AksjerMvAntall-datadef-29167>
            </AntallAksjerIDenneAksjeklassen-grp-3445>

            <InnbetaltAksjekapitalIDenneAksjeklassen-grp-3446 gruppeid="3446"/>

            <InnbetaltOverkursIDenneAksjeklassen-grp-3448 gruppeid="3448">
               <AksjeOverkursISINAksjetype-datadef-17661 orid="17661">{f_Overkurs}</AksjeOverkursISINAksjetype-datadef-17661>
            </InnbetaltOverkursIDenneAksjeklassen-grp-3448>

         </Selskapsopplysninger-grp-2589>
      """.format(
         f_Akjsekapital = Akjsekapital,
         f_AksjekapitalIDenneAksjeklassen = KapitalIAksjeklasse,
         f_PalydendePerAksje = Pålydende,
         f_AntallAksjerFjoråret = AntallAksjerFjoråret,
         f_AntallAksjer = AntallAksjer,
         f_Overkurs = Overkurs,
         WHAT = "",
      )

def FillFormData_Utbytte(UtbytteData):


   def FormData_UtbytteHendelse(Utbytte, Hendelse, Tidpunkt):
       return """
         <UtdeltSkatterettsligUtbytteILopetAvInntektsaret-grp-3451 gruppeid="3451">
            <AksjeUtbyttePerAksje-datadef-23946 orid="23946">{f_UtbyttePerAkjse}</AksjeUtbyttePerAksje-datadef-23946>
            <AksjeUtbytteHendelsestype-datadef-36564 orid="36564">{f_Hendelse}</AksjeUtbytteHendelsestype-datadef-36564>
            <AksjeUtbytteTidspunkt-datadef-17667 orid="17667">{f_Tidspunkt}</AksjeUtbytteTidspunkt-datadef-17667>
         </UtdeltSkatterettsligUtbytteILopetAvInntektsaret-grp-3451>
      """.format(
         f_UtbyttePerAkjse = Utbytte,
         f_Hendelse = Hendelse,
         f_Tidspunkt = Tidpunkt,
      )
     
   data = ""
   for item in UtbytteData:
      data += FormData_UtbytteHendelse(item[0], item[1], item[2])

   return """
         <Utbytte-grp-3449 gruppeid="3449">
            {f_UtbytteHendelser}
         </Utbytte-grp-3449>
      """.format(
         f_UtbytteHendelser = data,
      )

def FillFormData_UtstedelseAvAksjerIfmStiftelseNyemisjonMv(AntallNyutstedteAkjser, Tidspunkt, Pålydende, Overkurs, EgneAksjerOverført):

   return """
         <UtstedelseAvAksjerIfmStiftelseNyemisjonMv-grp-3452 gruppeid="3452">
            <AntallNyutstedteAksjer-grp-3453 gruppeid="3453">
               <AksjerNyutstedteStiftelseMvAntall-datadef-17668 orid="17668">{f_AntallNyutstedteAkjser}</AksjerNyutstedteStiftelseMvAntall-datadef-17668>
               <AksjerNyutstedteStiftelseMvTidspunkt-datadef-17671 orid="17671">{f_Tidspunkt}</AksjerNyutstedteStiftelseMvTidspunkt-datadef-17671>
               <AksjerNyutstedteStiftelseMvPalydende-datadef-23947 orid="23947">{f_Pålydende}</AksjerNyutstedteStiftelseMvPalydende-datadef-23947>
               <AksjerNyutstedteStiftelseMvOverkurs-datadef-23948 orid="23948">{f_Overkurs}</AksjerNyutstedteStiftelseMvOverkurs-datadef-23948>
               <AksjerNyutstedteStiftelseMvOverfortEgneAntall-datadef-17674 orid="17674">{f_EgneAksjerOverført}</AksjerNyutstedteStiftelseMvOverfortEgneAntall-datadef-17674>
            </AntallNyutstedteAksjer-grp-3453>
         </UtstedelseAvAksjerIfmStiftelseNyemisjonMv-grp-3452>
      """.format(
         f_AntallNyutstedteAkjser = AntallNyutstedteAkjser,
         f_Tidspunkt = Tidspunkt,
         f_Pålydende = Pålydende,
         f_Overkurs = Overkurs,
         f_EgneAksjerOverført = EgneAksjerOverført,
      )

def FillFormData_UtstedelseAvAksjerIfmFondsemisjonSplittMv(Antall, AntallEtter, Hendelsestype, Tidspunkt, OverdragendeOrgISIN, Pålydende, EgneAksjerOverført, OverdragendeOrgNum, OverdragendeOrgAkjseklasse):

   return """
         <UtstedelseAvAksjerIfmFondsemisjonSplittMv-grp-3454 gruppeid="3454">
            <NyutstedteAksjerOmfordeling-grp-3455 gruppeid="3455">
               <AksjerNyutstedteFondsemisjonMvAntall-datadef-17677 orid="17677">{f_Antall}</AksjerNyutstedteFondsemisjonMvAntall-datadef-17677>
               <AksjerNyutstedteFondsemisjonMvAntallEtter-datadef-17678 orid="17678">{f_AntallEtter}</AksjerNyutstedteFondsemisjonMvAntallEtter-datadef-17678>
               <AksjerNyutstedteFondsemisjonMvType-datadef-17679 orid="17679">{f_Hendelsestype}</AksjerNyutstedteFondsemisjonMvType-datadef-17679>
               <AksjerNyutstedteFondsemisjonMvTidspunkt-datadef-17680 orid="17680">{f_Tidspunkt}</AksjerNyutstedteFondsemisjonMvTidspunkt-datadef-17680>
               <AksjerNyutstedteFondsemisjonMvEgneOverfortAntall-datadef-17682 orid="17682">{f_EgneAksjerOverført}</AksjerNyutstedteFondsemisjonMvEgneOverfortAntall-datadef-17682>
               <EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683 orid="17683">{f_OverdragendeOrgNum}</EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683>
               <AksjerNyutstedteFondsemisjonMvISIN-datadef-17684 orid="17684">{WHAT}</AksjerNyutstedteFondsemisjonMvISIN-datadef-17684>
               <AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905 orid="19905">{f_OverdragendeOrgAkjseklasse}</AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905>
               <AksjerNyutstedteFondsemisjonMvInnlosteAntall-datadef-17685 orid="17685">{f_OverdragendeOrgISIN}</AksjerNyutstedteFondsemisjonMvInnlosteAntall-datadef-17685>
               <AksjerNyutstedteFondsemisjonMvInnlostPalydende-datadef-23950 orid="23950">{f_Pålydende}</AksjerNyutstedteFondsemisjonMvInnlostPalydende-datadef-23950>
               <EnhetOvertakendeKonsernfusjonKonsernfisjonOrganisasjonnummer-datadef-17687 orid="17687">{WHAT}</EnhetOvertakendeKonsernfusjonKonsernfisjonOrganisasjonnummer-datadef-17687>
            </NyutstedteAksjerOmfordeling-grp-3455>
         </UtstedelseAvAksjerIfmFondsemisjonSplittMv-grp-3454>
      """.format(
         f_Antall = Antall,
         f_AntallEtter = AntallEtter,
         f_Hendelsestype = Hendelsestype,
         f_Tidspunkt = Tidspunkt,
         f_OverdragendeOrgISIN = OverdragendeOrgISIN,
         f_Pålydende = Pålydende,
         f_EgneAksjerOverført = EgneAksjerOverført,
         f_OverdragendeOrgNum = OverdragendeOrgNum,
         f_OverdragendeOrgAkjseklasse = OverdragendeOrgAkjseklasse,
         WHAT = "vet ikke",
      )

def FillFormData_SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv(Antall,HendelsesType,Tidspunkt,InnbetaltOverkurs,Vederlag):

   return """
      <SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv-grp-3456 gruppeid="3456">
         <SlettedeAksjerAvgang-grp-3457 gruppeid="3457">
            <AksjerSlettedeLikvidasjonMvAntall-datadef-17688 orid="17688">{f_Antall}</AksjerSlettedeLikvidasjonMvAntall-datadef-17688>
            <AksjerSlettedeLikvidasjonMvType-datadef-17691 orid="17691">{f_HendelsesType}</AksjerSlettedeLikvidasjonMvType-datadef-17691>
            <AksjerSlettedeLividasjonMvTidspunkt-datadef-17692 orid="17692">{f_Tidspunkt}</AksjerSlettedeLividasjonMvTidspunkt-datadef-17692>
            <AksjerSlettedeLikvidasjonMvInnbetaltOverkurs-datadef-28212 orid="28212">{f_InnbetaltOverkurs}</AksjerSlettedeLikvidasjonMvInnbetaltOverkurs-datadef-28212>
            <AksjerSlettedeLikvidasjonMvVederlag-datadef-17770 orid="17770">{f_Vederlag}</AksjerSlettedeLikvidasjonMvVederlag-datadef-17770>
         </SlettedeAksjerAvgang-grp-3457>
      </SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv-grp-3456>
      """.format(
         f_Antall = Antall,
         f_HendelsesType = HendelsesType,
         f_Tidspunkt = Tidspunkt,
         f_InnbetaltOverkurs = InnbetaltOverkurs,
         f_Vederlag = Vederlag,
         WHAT = "vet ikke",
      )

def FillFormData_SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon(Antall,OvertakendeDatterSelskapISIN,OvertakendeSelskapOrgNmr, OvertakendeMorSelskapISIN, OvertakendeAksjetype,OvertakendePalydende):

   return """
      <SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon-grp-3458 gruppeid="3458">
         <SlettedeAksjerOmfordeling-grp-3459 gruppeid="3459">
            <AksjerSlettedeSpleisMvDatterselskapOvertakendeISINType-datadef-20374 orid="20374">{f_OvertakendeDatterSelskapISIN}</AksjerSlettedeSpleisMvDatterselskapOvertakendeISINType-datadef-20374>
            <EnhetSlettedeSpleisMvMorselskapOvertakendeOrganisasjonsnumm-datadef-17703 orid="17703">{f_OvertakendeSelskapOrgNmr}</EnhetSlettedeSpleisMvMorselskapOvertakendeOrganisasjonsnumm-datadef-17703>
            <AksjerSlettedeSpleisMvMorselskapOvertakendeISINType-datadef-17704 orid="17704">{f_OvertakendeMorSelskapISIN}</AksjerSlettedeSpleisMvMorselskapOvertakendeISINType-datadef-17704>
            <AksjerSlettedeSpleisMvMorselskapOvertakendeAksjetype-datadef-19907 orid="19907">{f_OvertakendeAksjetype}</AksjerSlettedeSpleisMvMorselskapOvertakendeAksjetype-datadef-19907>
            <AksjerSlettedeSpleisMvMorselskapOvertakendePalydende-datadef-23955 orid="23955">{f_OvertakendePalydende}</AksjerSlettedeSpleisMvMorselskapOvertakendePalydende-datadef-23955>
         </SlettedeAksjerOmfordeling-grp-3459>
      </SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon-grp-3458>
      """.format(
         f_Antall = Antall,
         f_OvertakendeDatterSelskapISIN = OvertakendeDatterSelskapISIN,
         f_OvertakendeSelskapOrgNmr = OvertakendeSelskapOrgNmr,
         f_OvertakendeMorSelskapISIN = OvertakendeMorSelskapISIN,
         f_OvertakendeAksjetype = OvertakendeAksjetype,
         f_OvertakendePalydende = OvertakendePalydende,
         WHAT = "vet ikke",
      )

def FillFormData_NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene(NedsettelseInnbetaltOverkurs, Tidspunkt):

   return """
      <NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene-grp-3461 gruppeid="3461">
         <AksjerOverkursNedsettelse-datadef-17707 orid="17707">{f_NedsettelseInnbetaltOverkurs}</AksjerOverkursNedsettelse-datadef-17707>
         <AksjerOverkursNedsettelseTidspunkt-datadef-17708 orid="17708">{f_Tidspunkt}</AksjerOverkursNedsettelse-datadef-17708>
      </NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene-grp-3461>
      """.format(
         f_NedsettelseInnbetaltOverkurs = NedsettelseInnbetaltOverkurs,
         f_Tidspunkt = Tidspunkt,
         WHAT = "vet ikke",
      )

def FillFormData_ForhoyelseAvAKVedOkningAvPalydende3462(PålydenePerAkjseFør, NedsettelseInnbetaltOverkurs, Tidspunkt):

   return """
      <ForhoyelseAvAKVedOkningAvPalydende-grp-3462 gruppeid="3462">
         <AksjeFondsemisjonPalydendeForhoyelse-datadef-23956 orid="23956">{f_PålydenePerAkjseFør}</AksjePalydendeEtterFondsemisjon-datadef-23956>
         <AksjePalydendeEtterFondsemisjon-datadef-23957 orid="23957">{f_PålydenePerAkjseEtter}</AksjePalydendeEtterFondsemisjon-datadef-23957>
         <AksjeFondsemisjonTidspunkt-datadef-17712 orid="17712">{f_Tidspunkt}</AksjeFondsemisjonTidspunkt-datadef-17712>
      </ForhoyelseAvAKVedOkningAvPalydende-grp-3462>
      """.format(
         f_PålydenePerAkjseFør = PålydenePerAkjseFør,
         f_NedsettelseInnbetaltOverkurs = NedsettelseInnbetaltOverkurs,
         f_Tidspunkt = Tidspunkt,
         WHAT = "vet ikke",
      )

def FillFormData_ForhoyelseAvAKVedOkningAvPalydende3463(ForhøyelseAvAkjseKapital, ØkningIPålydenede, HendelsesType, ForhøyelseAvOverkurs,OrgNummer,ISIN,Akjseklasse):

   return """
      <ForhoyelseAvAKVedOkningAvPalydende-grp-3463 gruppeid="3463">
         <AksjekapitalNyemisjonForhoyelse-datadef-17713 orid="17713">{f_ForhøyelseAvAkjseKapital}</AksjekapitalNyemisjonForhoyelse-datadef-17713>
         <AksjeNyemisjonPalydendeForhoyelse-datadef-23958 orid="23958">{f_ØkningIPålydenede}</AksjeNyemisjonPalydendeForhoyelse-datadef-23958>
         <AksjekapitalForhoyelsePalydendeHendelsestype-datadef-28268 orid="28268">{f_HendelsesType}</AksjekapitalForhoyelsePalydendeHendelsestype-datadef-28268>
         <AksjeOverkursForhoyelse-datadef-22071 orid="22071">{f_ForhøyelseAvOverkurs}</AksjeOverkursForhoyelse-datadef-22071>
         <EnhetOverdragendeNyemisjonMvOrganisasjonsnummer-datadef-28213 orid="28213">{f_OrgNummer}</EnhetOverdragendeNyemisjonMvOrganisasjonsnummer-datadef-28213>
         <AksjerNyutstedteNyemisjonMvISIN-datadef-28214 orid="28214">{f_ISIN}</AksjerNyutstedteNyemisjonMvISIN-datadef-28214>
         <AksjerNyutstedteNyemisjonMvAksjetype-datadef-28215 orid="28215">{f_Akjseklasse}</AksjerNyutstedteNyemisjonMvAksjetype-datadef-28215>
      </ForhoyelseAvAKVedOkningAvPalydende-grp-3463>
      """.format(
         f_ForhøyelseAvAkjseKapital = ForhøyelseAvAkjseKapital,
         f_ØkningIPålydenede = ØkningIPålydenede,
         f_HendelsesType = HendelsesType,
         f_ForhøyelseAvOverkurs = ForhøyelseAvOverkurs,
         f_OrgNummer = OrgNummer,
         f_ISIN = ISIN,
         f_Akjseklasse = Akjseklasse,
         WHAT = "vet ikke",
      )

def FillFormData_NedsettelseAvInnbetaltOgFondsemittertAK(NedsettekseAvInnbetalt, ReduksjonAvPålydende, PålydendeEtter, Tidspunkt, NedsettelseAvFondsemittert):

   return """
      <NedsettelseAvInnbetaltOgFondsemittertAK-grp-3464 gruppeid="3464">
         <AksjekapitalInnbetaltNedsettelse-datadef-17717 orid="17717">{f_NedsettekseAvInnbetalt}</AksjekapitalInnbetaltNedsettelse-datadef-17717>
         <AksjePalydendeNedsettelseTapsdekning-datadef-23960 orid="23960">{f_ReduksjonAvPålydende}</AksjePalydendeNedsettelseTapsdekning-datadef-23960>
         <AksjePalydendeEtterNedsettelseTapsdekning-datadef-23961 orid="23961">{f_PålydendeEtter}</AksjePalydendeEtterNedsettelseTapsdekning-datadef-23961>
         <AksjeNedsettelseTidspunkt-datadef-17720 orid="17720">{f_Tidspunkt}</AksjeNedsettelseTidspunkt-datadef-17720>
         <AksjekapitalFondsemittertNedsettelse-datadef-17721 orid="17721">{f_NedsettelseAvFondsemittert}</AksjekapitalFondsemittertNedsettelse-datadef-17721>
      </NedsettelseAvInnbetaltOgFondsemittertAK-grp-3464>
      """.format(
         f_NedsettekseAvInnbetalt = NedsettekseAvInnbetalt,
         f_ReduksjonAvPålydende = ReduksjonAvPålydende,
         f_PålydendeEtter = PålydendeEtter,
         f_Tidspunkt = Tidspunkt,
         f_NedsettelseAvFondsemittert = NedsettelseAvFondsemittert,
         WHAT = "vet ikke",
      )

def FillFormData_NedsettelseAKVedReduksjonAvPalydende():

   return """
      <NedsettelseAKVedReduksjonAvPalydende-grp-3465 gruppeid="3465">
         <AksjekapitalUtbetalingNedsettelse-datadef-17722 orid="17722">-295749.765094196</AksjekapitalUtbetalingNedsettelse-datadef-17722>
         <AksjePalydendeNedsettelseUtbetaling-datadef-23962 orid="23962">-4051799.7650942</AksjePalydendeNedsettelseUtbetaling-datadef-23962>
         <AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963 orid="23963">1663570.2349058</AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963>
      </NedsettelseAKVedReduksjonAvPalydende-grp-3465>
      """.format(

         WHAT = "vet ikke",
      )

def FillFormData_():

   return """

      """.format(

         WHAT = "vet ikke",
      )

def FillFormData_():

   return """

      """.format(

         WHAT = "vet ikke",
      )

def sendFormData(username, userpassword, authcode, orgnumber, data):
   headers = {
      "Vary": "Accept-Encoding",
      "Accept-Encoding": "gzip,deflate",
      "Content-Type" : "text/xml; charset=utf-8",
      "SOAPAction": "http://www.altinn.no/services/Intermediary/Shipment/IntermediaryInbound/2009/10/IIntermediaryInboundExternalBasic/SubmitFormTaskBasic",
      "Host": "tt02.altinn.no",
      "Connection": "Keep-Alive",
      "User-Agent": "Apache-HttpClient/4.5.5 (Java/16.0.1)"
   }

   body = """
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.altinn.no/services/Intermediary/Shipment/IntermediaryInbound/2009/10">
      <soapenv:Header/>
      <soapenv:Body>
         <ns:SubmitFormTaskBasic>
            <ns:systemUserName>{SystemUserName_Str}</ns:systemUserName>
            <ns:systemPassword>{SystemPassword_Str}</ns:systemPassword>
            <ns:userSSN>{UserSSN_Str}</ns:userSSN>
            <ns:userPassword>{UserPassword_Str}</ns:userPassword>
            <ns:userPinCode>{UserPin_Str}</ns:userPinCode>
            <ns:authMethod>SMSPin</ns:authMethod>
            
            <ns:formTaskShipment>
               <ns:Reportee>{CompanyNumber_Str}</ns:Reportee>
               <ns:ExternalShipmentReference>{UniqueNumIdentifier}</ns:ExternalShipmentReference>
                <ns:FormTasks>
                <!--<ns:ServiceCode>1166</ns:ServiceCode>
               <ns:ServiceEdition>181026</ns:ServiceEdition>
-->
               <ns:ServiceCode>1051</ns:ServiceCode>
               <ns:ServiceEdition>201010</ns:ServiceEdition>
               <ns:Forms>
                  <ns:Form>
                     <ns:Completed>0</ns:Completed>
                     <ns:DataFormatId>890</ns:DataFormatId>
                     <ns:DataFormatVersion>12144</ns:DataFormatVersion>
                     <ns:EndUserSystemReference>1</ns:EndUserSystemReference>
                     <ns:ParentReference>0</ns:ParentReference>
                     <ns:FormData><![CDATA[
                     <Skjema xmlns:brreg="http://www.brreg.no/or" xsi:noNamespaceSchemaLocation="schema.xsd" skjemanummer="890" spesifikasjonsnummer="12144" blankettnummer="RF-1086" tittel="Aksjonærregisteroppgaven" gruppeid="2586" etatid="NoAgency" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                     
                     {f_GenerellInformasjon}

                     {f_Selskapsopplysninger}

                     {f_Utbytte}

                     {f_UtstedelseAvAksjerIfmStiftelseNyemisjonMv}

                     {f_UtstedelseAvAksjerIfmFondsemisjonSplittMv}

                     {f_SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv}

                     {f_SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon}
                  
                     <EndringerIAksjekapitalOgOverkurs-grp-3460 gruppeid="3460">
                        
                        {f_NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene}

                        {f_ForhoyelseAvAKVedOkningAvPalydende3462}

                        {f_ForhoyelseAvAKVedOkningAvPalydende3463} 

                        {f_NedsettelseAvInnbetaltOgFondsemittertAK} 

                        {f_NedsettelseAKVedReduksjonAvPalydende} 
                        
                        
                        <NedsettelseAKVedReduksjonAvPalydende-grp-3465 gruppeid="3465">
                           <AksjekapitalUtbetalingNedsettelse-datadef-17722 orid="17722">-295749.765094196</AksjekapitalUtbetalingNedsettelse-datadef-17722>
                           <AksjePalydendeNedsettelseUtbetaling-datadef-23962 orid="23962">-4051799.7650942</AksjePalydendeNedsettelseUtbetaling-datadef-23962>
                           <AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963 orid="23963">1663570.2349058</AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963>
                        </NedsettelseAKVedReduksjonAvPalydende-grp-3465>
                        
                        <NedsettelseAvAKVedReduksjonUtfisjonering-grp-3466 gruppeid="3466">
                           <AksjePalydendeNedsettelseUtfisjonering-datadef-23964 orid="23964">-349509.765094196</AksjePalydendeNedsettelseUtfisjonering-datadef-23964>
                           <AksjeUtfisjoneringHendelsestype-datadef-37825 orid="37825">string</AksjeUtfisjoneringHendelsestype-datadef-37825>
                           <EnhetISINOvertakendeMorselskap-datadef-17735 orid="17735">string</EnhetISINOvertakendeMorselskap-datadef-17735>
                           <AksjerMorselskapOvertakendeVederlagPalydende-datadef-23967 orid="23967">1298100.2349058</AksjerMorselskapOvertakendeVederlagPalydende-datadef-23967>
                        </NedsettelseAvAKVedReduksjonUtfisjonering-grp-3466>
                     </EndringerIAksjekapitalOgOverkurs-grp-3460>
                     </Skjema>
                     ]]></ns:FormData>
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
         UniqueNumIdentifier = random.randint(0,100000),
         CompanyNumber_Str = orgnumber,
         f_GenerellInformasjon = FillFormData_GenerellInformasjon("911","911","92","","A-Akjse","2022","vikt","rolle","vik@gm","911"),
         f_Selskapsopplysninger = FillFormData_Selskapsopplysninger("1000","190","10","19","19",""),
         f_Utbytte = FillFormData_Utbytte(UtbytteTestData),
         f_UtstedelseAvAksjerIfmStiftelseNyemisjonMv = FillFormData_UtstedelseAvAksjerIfmStiftelseNyemisjonMv("10", "121212", "800", "123", "12"),
         f_UtstedelseAvAksjerIfmFondsemisjonSplittMv = FillFormData_UtstedelseAvAksjerIfmFondsemisjonSplittMv("10", "22", "Splitt", "121212", "", "800", "123", "12", "A-Aksjer"),
      ).encode("utf-8")
   #print(body)
   #print("\n\n\n\n\n")
   #Posts soap request and stores respons
   re = requests.post("https://tt02.altinn.no/IntermediaryExternal/IntermediaryInboundBasic.svc", data=body, headers=headers)
   print(re.encoding)
   #Uses beautifulSoup to parse the xml return
   #soup = BeautifulSoup(re.content)
   #Gets Status code
   #responsStatus = soup.find("ReceiptText")
   if (False):
      return {True, "Success"}
   else:
      print(re.content)
      #return {False, soup.find("a:message").string}

sendFormData(testUserSocialSecurityNumber, testUserPassword, "tue4u", 911007118, testData)

#sendAuthCodeToUser(testUserSocialSecurityNumber, testUserPassword)