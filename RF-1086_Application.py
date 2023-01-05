
import requests
import random
import bs4

# Systemusername
SystemUserName = "19215"
# SystemPassword 
SystemPassword = "systempassord1"

#Testuser username
testUserUsername = "testbruker424"
#testuser Password
testUserPassword = "testpassord1"

#Which type of login to use, either phone(SMSPin) or letter(AltinnPin)
AuthCodeType = "AltinnPin"
#AuthCodeType = "SMSPin"

UtbytteTestData = [["utbytte1", "noemer1", "tidspunkt1"],
                   ["utbytte2", "noemer2", "tidspunkt2"]]


def FillFormData_GenerellInformasjon(OrgNum, PostNum, Poststed, ISIN, AksjeKlasse, Inntektsår, AnsvarligNavn, AnsvarligRolle, AnsvarligEpost, AnsvarligTlf):
   # Denne skulle være med men trenger vi den? <AksjeTypePreutfylt-datadef-24503 orid="24503"></AksjeTypePreutfylt-datadef-24503>
   
   return """
       <GenerellInformasjon-grp-2587 gruppeid="2587">
         <Selskap-grp-2588 gruppeid="2588">
            <EnhetOrganisasjonsnummer-datadef-18 orid="18">{f_OrgNumber}</EnhetOrganisasjonsnummer-datadef-18>
            <EnhetPostnummer-datadef-6673 orid="6673">{f_PostNummer}</EnhetPostnummer-datadef-6673>
            <EnhetPoststed-datadef-6674 orid="6674">{f_Poststed}</EnhetPoststed-datadef-6674>
            <EnhetISINNummer-datadef-17513 orid="17513">{f_ISIN}</EnhetISINNummer-datadef-17513>
            <AksjeType-datadef-17659 orid="17659">{f_AksjeKlasse}</AksjeType-datadef-17659>
            <Inntektsar-datadef-692 orid="692">{f_Inntektsår}</Inntektsar-datadef-692>
            <AksjonarregisteroppgaveHovedskjemaInnsendingsmate-datadef-34855 orid="34855">{UkjentFelt}</AksjonarregisteroppgaveHovedskjemaInnsendingsmate-datadef-34855>
         </Selskap-grp-2588>
         <Kontaktperson-grp-3442 gruppeid="3442">
               <KontaktpersonSkjemaNavn-datadef-33918 orid="33918">{f_AnsvarligNavn}</KontaktpersonSkjemaNavn-datadef-33918>
               <KontaktpersonSkjemaRolle-datadef-33915 orid="33915">{f_AnsvarligRolle}</KontaktpersonSkjemaRolle-datadef-33915>
               <KontaktpersonSkjemaEPost-datadef-30533 orid="30533">{f_AnsvarligEpost}</KontaktpersonSkjemaEPost-datadef-30533>
               <KontaktpersonSkjemaTelefonnummer-datadef-33916 orid="33916">{f_AnsvarligTlf}</KontaktpersonSkjemaTelefonnummer-datadef-33916>
         </Kontaktperson-grp-3442>
         <AnnenKontaktperson-grp-5384 gruppeid="5384">
            <KontaktpersonVirksomhetEPost-datadef-28209 orid="28209">{UkjentFelt}</KontaktpersonVirksomhetEPost-datadef-28209>
         </AnnenKontaktperson-grp-5384>
      </GenerellInformasjon-grp-2587>
      """.format(
         f_OrgNumber = OrgNum, 
         f_PostNummer = PostNum,
         f_Poststed = Poststed,
         f_ISIN = ISIN,
         f_Inntektsår = Inntektsår,
         f_AksjeKlasse = AksjeKlasse,
         f_AnsvarligNavn = AnsvarligNavn,
         f_AnsvarligRolle = AnsvarligRolle,
         f_AnsvarligEpost = AnsvarligEpost,
         f_AnsvarligTlf = AnsvarligTlf,
         UkjentFelt = "",
      )


def FillFormData_Selskapsopplysninger(Aksjekapital, KapitalIAksjeklasse, Pålydende, AntallAksjerFjoråret, AntallAksjer, InnbetaltAksjekapital, Overkurs):
   return """
        <Selskapsopplysninger-grp-2589 gruppeid="2589">
            <AksjekapitalForHeleSelskapet-grp-3443 gruppeid="3443">
               <AksjekapitalFjoraret-datadef-7129 orid="7129">{f_Aksjekapital}</AksjekapitalFjoraret-datadef-7129>
               <Aksjekapital-datadef-87 orid="87">{f_Aksjekapital}</Aksjekapital-datadef-87>
            </AksjekapitalForHeleSelskapet-grp-3443>

            <AksjekapitalIDenneAksjeklassen-grp-3444 gruppeid="3444">
               <AksjekapitalISINAksjetypeFjoraret-datadef-17663 orid="17663">{f_AksjekapitalIDenneAksjeklassen}</AksjekapitalISINAksjetypeFjoraret-datadef-17663>
               <AksjekapitalISINAksjetype-datadef-17664 orid="17664">{f_AksjekapitalIDenneAksjeklassen}</AksjekapitalISINAksjetype-datadef-17664>
            </AksjekapitalIDenneAksjeklassen-grp-3444>

            <PalydendePerAksje-grp-3447 gruppeid="3447">
               <AksjeMvPalydendeFjoraret-datadef-23944 orid="23944">{f_PalydendePerAksje}</AksjeMvPalydendeFjoraret-datadef-23944>
               <AksjeMvPalydende-datadef-23945 orid="23945">{f_PalydendePerAksje}</AksjeMvPalydende-datadef-23945>
            </PalydendePerAksje-grp-3447>

            <AntallAksjerIDenneAksjeklassen-grp-3445 gruppeid="3445">
               <AksjerMvAntallFjoraret-datadef-29166 orid="29166">{f_AntallAksjerFjoråret}</AksjerMvAntallFjoraret-datadef-29166>
               <AksjerMvAntall-datadef-29167 orid="29167">{f_AntallAksjer}</AksjerMvAntall-datadef-29167>
            </AntallAksjerIDenneAksjeklassen-grp-3445>


            <InnbetaltAksjekapitalIDenneAksjeklassen-grp-3446 gruppeid="3446">
               <AksjekapitalInnbetaltFjoraret-datadef-8020 orid="8020">{f_InnbetaltAksjekapital}</AksjekapitalInnbetaltFjoraret-datadef-8020>
               <AksjekapitalInnbetalt-datadef-5867 orid="5867">{f_InnbetaltAksjekapital}</AksjekapitalInnbetalt-datadef-5867>
            </InnbetaltAksjekapitalIDenneAksjeklassen-grp-3446>

            <InnbetaltOverkursIDenneAksjeklassen-grp-3448 gruppeid="3448">
               <AksjeOverkursISINAksjetypeFjoraret-datadef-17662 orid="17662">{f_Overkurs}</AksjeOverkursISINAksjetypeFjoraret-datadef-17662>
               <AksjeOverkursISINAksjetype-datadef-17661 orid="17661">{f_Overkurs}</AksjeOverkursISINAksjetype-datadef-17661>
            </InnbetaltOverkursIDenneAksjeklassen-grp-3448>

         </Selskapsopplysninger-grp-2589>
      """.format(
         f_Aksjekapital = Aksjekapital,
         f_AksjekapitalIDenneAksjeklassen = KapitalIAksjeklasse,
         f_PalydendePerAksje = Pålydende,
         f_AntallAksjerFjoråret = AntallAksjerFjoråret,
         f_AntallAksjer = AntallAksjer,
         f_InnbetaltAksjekapital = InnbetaltAksjekapital,
         f_Overkurs = Overkurs,
         UkjentFelt = "",
      )


def FillFormData_Utbytte(UtbytteData):


   def FormData_UtbytteHendelse(Utbytte, Hendelse, Tidpunkt):
       return """
         <UtdeltSkatterettsligUtbytteILopetAvInntektsaret-grp-3451 gruppeid="3451">
            <AksjeUtbyttePerAksje-datadef-23946 orid="23946">{f_UtbyttePerAksje}</AksjeUtbyttePerAksje-datadef-23946>
            <AksjeUtbytteHendelsestype-datadef-36564 orid="36564">{f_Hendelse}</AksjeUtbytteHendelsestype-datadef-36564>
            <AksjeUtbytteTidspunkt-datadef-17667 orid="17667">{f_Tidspunkt}</AksjeUtbytteTidspunkt-datadef-17667>
         </UtdeltSkatterettsligUtbytteILopetAvInntektsaret-grp-3451>
      """.format(
         f_UtbyttePerAksje = Utbytte,
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


def FillFormData_UtstedelseAvAksjerIfmStiftelseNyemisjonMv(AntallNyutstedteAksjer, AntallEtter, Hendelse, Tidspunkt,  Pålydende, Overkurs, EgneAksjerOverført):

   return """
         <UtstedelseAvAksjerIfmStiftelseNyemisjonMv-grp-3452 gruppeid="3452">
            <AntallNyutstedteAksjer-grp-3453 gruppeid="3453">
               <AksjerNyutstedteStiftelseMvAntall-datadef-17668 orid="17668">{f_AntallNyutstedteAksjer}</AksjerNyutstedteStiftelseMvAntall-datadef-17668>
               <AksjerStiftelseMvAntall-datadef-17669 orid="17669">{f_AntallEtter}</AksjerStiftelseMvAntall-datadef-17669>
               <AksjerNyutstedteStiftelseMvType-datadef-17670 orid="17670">{f_Hendelse}</AksjerNyutstedteStiftelseMvType-datadef-17670>
               <AksjerNyutstedteStiftelseMvTidspunkt-datadef-17671 orid="17671">{f_Tidspunkt}</AksjerNyutstedteStiftelseMvTidspunkt-datadef-17671>
               <AksjerNyutstedteStiftelseMvPalydende-datadef-23947 orid="23947">{f_Pålydende}</AksjerNyutstedteStiftelseMvPalydende-datadef-23947>
               <AksjerNyutstedteStiftelseMvOverkurs-datadef-23948 orid="23948">{f_Overkurs}</AksjerNyutstedteStiftelseMvOverkurs-datadef-23948>
               <AksjerNyutstedteStiftelseMvOverfortEgneAntall-datadef-17674 orid="17674">{f_EgneAksjerOverført}</AksjerNyutstedteStiftelseMvOverfortEgneAntall-datadef-17674>
            </AntallNyutstedteAksjer-grp-3453>
         </UtstedelseAvAksjerIfmStiftelseNyemisjonMv-grp-3452>
      """.format(
         f_AntallNyutstedteAksjer = AntallNyutstedteAksjer,
         f_AntallEtter = AntallEtter,
         f_Hendelse = Hendelse,
         f_Tidspunkt = Tidspunkt,
         f_Pålydende = Pålydende,
         f_Overkurs = Overkurs,
         f_EgneAksjerOverført = EgneAksjerOverført,
      )


def FillFormData_UtstedelseAvAksjerIfmFondsemisjonSplittMv(Antall, AntallEtter, Hendelsestype, Tidspunkt, PålydendePerUtstedtAksje, OverdragendeOrgISIN, Pålydende, EgneAksjerOverført, OverdragendeOrgNum, OverdragendeOrgAksjeklasse):

   return """
         <UtstedelseAvAksjerIfmFondsemisjonSplittMv-grp-3454 gruppeid="3454">
            <NyutstedteAksjerOmfordeling-grp-3455 gruppeid="3455">
               <AksjerNyutstedteFondsemisjonMvAntall-datadef-17677 orid="17677">{f_Antall}</AksjerNyutstedteFondsemisjonMvAntall-datadef-17677>
               <AksjerNyutstedteFondsemisjonMvAntallEtter-datadef-17678 orid="17678">{f_AntallEtter}</AksjerNyutstedteFondsemisjonMvAntallEtter-datadef-17678>
               <AksjerNyutstedteFondsemisjonMvType-datadef-17679 orid="17679">{f_Hendelsestype}</AksjerNyutstedteFondsemisjonMvType-datadef-17679>
               <AksjerNyutstedteFondsemisjonMvTidspunkt-datadef-17680 orid="17680">{f_Tidspunkt}</AksjerNyutstedteFondsemisjonMvTidspunkt-datadef-17680>
               <AksjerNyutstedteFondsemisjonMvPalydende-datadef-23949 orid="23949">{f_PålydendePerUtstedtAksje}</AksjerNyutstedteFondsemisjonMvPalydende-datadef-23949>
               <AksjerNyutstedteFondsemisjonMvEgneOverfortAntall-datadef-17682 orid="17682">{f_EgneAksjerOverført}</AksjerNyutstedteFondsemisjonMvEgneOverfortAntall-datadef-17682>
               <EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683 orid="17683">{f_OverdragendeOrgNum}</EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683>
               <AksjerNyutstedteFondsemisjonMvISIN-datadef-17684 orid="17684">{f_OverdragendeOrgISIN}</AksjerNyutstedteFondsemisjonMvISIN-datadef-17684>
               <AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905 orid="19905">{f_OverdragendeOrgAksjeklasse}</AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905>
               <AksjerNyutstedteFondsemisjonMvInnlosteAntall-datadef-17685 orid="17685">{UkjentFelt}</AksjerNyutstedteFondsemisjonMvInnlosteAntall-datadef-17685>
               <AksjerNyutstedteFondsemisjonMvInnlostPalydende-datadef-23950 orid="23950">{f_Pålydende}</AksjerNyutstedteFondsemisjonMvInnlostPalydende-datadef-23950>
               <EnhetOvertakendeKonsernfusjonKonsernfisjonOrganisasjonnummer-datadef-17687 orid="17687">{UkjentFelt}</EnhetOvertakendeKonsernfusjonKonsernfisjonOrganisasjonnummer-datadef-17687>
            </NyutstedteAksjerOmfordeling-grp-3455>
         </UtstedelseAvAksjerIfmFondsemisjonSplittMv-grp-3454>
      """.format(
         f_Antall = Antall,
         f_AntallEtter = AntallEtter,
         f_Hendelsestype = Hendelsestype,
         f_Tidspunkt = Tidspunkt,
         f_PålydendePerUtstedtAksje = PålydendePerUtstedtAksje,
         f_OverdragendeOrgISIN = OverdragendeOrgISIN,
         f_Pålydende = Pålydende,
         f_EgneAksjerOverført = EgneAksjerOverført,
         f_OverdragendeOrgNum = OverdragendeOrgNum,
         f_OverdragendeOrgAksjeklasse = OverdragendeOrgAksjeklasse,
         UkjentFelt = "vet ikke",
      )


def FillFormData_SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv(Antall, AntallEtter, PålydendePerAksje, HendelsesType, Tidspunkt, InnbetaltOverkurs, Vederlag):

   return """
      <SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv-grp-3456 gruppeid="3456">
         <SlettedeAksjerAvgang-grp-3457 gruppeid="3457">
            <AksjerSlettedeLikvidasjonMvAntall-datadef-17688 orid="17688">{f_Antall}</AksjerSlettedeLikvidasjonMvAntall-datadef-17688>
            <AksjerLividasjonMvAntall-datadef-17689 orid="17689">{f_AntallEtter}</AksjerLividasjonMvAntall-datadef-17689>
            <AksjerSlettedeLikvidasjonMvPalydende-datadef-23951 orid="23951">{f_PålydendePerAksje}</AksjerSlettedeLikvidasjonMvPalydende-datadef-23951>
            <AksjerSlettedeLikvidasjonMvType-datadef-17691 orid="17691">{f_HendelsesType}</AksjerSlettedeLikvidasjonMvType-datadef-17691>
            <AksjerSlettedeLividasjonMvTidspunkt-datadef-17692 orid="17692">{f_Tidspunkt}</AksjerSlettedeLividasjonMvTidspunkt-datadef-17692>
            <AksjerSlettedeLikvidasjonMvInnbetaltOverkurs-datadef-28212 orid="28212">{f_InnbetaltOverkurs}</AksjerSlettedeLikvidasjonMvInnbetaltOverkurs-datadef-28212>
            <AksjerSlettedeLikvidasjonMvVederlag-datadef-17770 orid="17770">{f_Vederlag}</AksjerSlettedeLikvidasjonMvVederlag-datadef-17770>
         </SlettedeAksjerAvgang-grp-3457>
      </SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv-grp-3456>
      """.format(
         f_Antall = Antall,
         f_AntallEtter = AntallEtter,
         f_PålydendePerAksje = PålydendePerAksje,
         f_HendelsesType = HendelsesType,
         f_Tidspunkt = Tidspunkt,
         f_InnbetaltOverkurs = InnbetaltOverkurs,
         f_Vederlag = Vederlag,
         UkjentFelt = "vet ikke",
      )


def FillFormData_SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon(
   Antall, AntallEtter, Hendelse, Tidspunkt, Pålydende,
   PålydendeEtterSpleis, OvertakendeSelskapOrgNum, OvertakendeDatterSelskapISIN,
   OvertakendeSelskapAksjeklasse, Vederlagsaksjer, PålydendePerVederlagsaksjer,
   Vederlagsaksjer2, OvertakendeSelskapOrgNr, OvertakendeMorSelskapISIN,
   OvertakendeAksjetype, OvertakendePalydende):

   return """
      <SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon-grp-3458 gruppeid="3458">
         <SlettedeAksjerOmfordeling-grp-3459 gruppeid="3459">
            <AksjerSlettedeSpleisMvAntall-datadef-17693 orid="17693">{f_Antall}</AksjerSlettedeSpleisMvAntall-datadef-17693>
            <AksjerSpleisAntall-datadef-17694 orid="17694">{f_AntallEtter}</AksjerSpleisAntall-datadef-17694>
            <AksjerSlettedeSpleisMvType-datadef-17695 orid="17695">{f_Hendelse}</AksjerSlettedeSpleisMvType-datadef-17695>
            <AksjerSlettedeSpleisMvTidspunkt-datadef-17696 orid="17696">{f_Tidspunkt}</AksjerSlettedeSpleisMvTidspunkt-datadef-17696>
            <AksjerSlettedeFisjonPalydende-datadef-23952 orid="23952">{f_Pålydende}</AksjerSlettedeFisjonPalydende-datadef-23952>
            <AksjerSlettedeSpleisPalydende-datadef-23953 orid="23953">{f_PålydendeEtterSpleis}</AksjerSlettedeSpleisPalydende-datadef-23953>
            <EnhetSlettedeSpleisMvDatterselskaovertakendeOrganisasjonsnumm-datadef-20373 orid="20373">{f_OvertakendeSelskapOrgNum}</EnhetSlettedeSpleisMvDatterselskaovertakendeOrganisasjonsnumm-datadef-20373>
            <AksjerSlettedeSpleisMvDatterselskapOvertakendeISINType-datadef-20374 orid="20374">{f_OvertakendeDatterSelskapISIN}</AksjerSlettedeSpleisMvDatterselskapOvertakendeISINType-datadef-20374>
            <AksjerSlettedeSpleisMvDatterselskapOvertakendeAksjetype-datadef-20375 orid="20375">{f_OvertakendeSelskapAksjeklasse}</AksjerSlettedeSpleisMvDatterselskapOvertakendeAksjetype-datadef-20375>
            <AksjerSlettedeSpleisMvOvertakendeAntall-datadef-17701 orid="17701">{f_Vederlagsaksjer}</AksjerSlettedeSpleisMvOvertakendeAntall-datadef-17701>
            <AksjerSlettedeSpleisMvOvertakendePalydende-datadef-23954 orid="23954">{f_PålydendePerVederlagsaksjer}</AksjerSlettedeSpleisMvOvertakendePalydende-datadef-23954>
            <EnhetSlettedeSpleisMvMorselskapOvertakendeOrganisasjonsnumm-datadef-17703 orid="17703">{f_OvertakendeSelskapOrgNr}</EnhetSlettedeSpleisMvMorselskapOvertakendeOrganisasjonsnumm-datadef-17703>
            <AksjerSlettedeSpleisMvMorselskapOvertakendeISINType-datadef-17704 orid="17704">{f_OvertakendeMorSelskapISIN}</AksjerSlettedeSpleisMvMorselskapOvertakendeISINType-datadef-17704>
            <AksjerSlettedeSpleisMvMorselskapOvertakendeAksjetype-datadef-19907 orid="19907">{f_OvertakendeAksjetype}</AksjerSlettedeSpleisMvMorselskapOvertakendeAksjetype-datadef-19907>
            <AksjerSlettedeSpleisMvMorselskapOvertakendeAntall-datadef-17705 orid="17705">{f_Vederlagsaksjer2}</AksjerSlettedeSpleisMvMorselskapOvertakendeAntall-datadef-17705>
            <AksjerSlettedeSpleisMvMorselskapOvertakendePalydende-datadef-23955 orid="23955">{f_OvertakendePalydende}</AksjerSlettedeSpleisMvMorselskapOvertakendePalydende-datadef-23955>
         </SlettedeAksjerOmfordeling-grp-3459>
      </SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon-grp-3458>
      """.format(
         f_Antall = Antall,
         f_AntallEtter = AntallEtter,
         f_Hendelse = Hendelse,
         f_Tidspunkt = Tidspunkt,
         f_Pålydende = Pålydende,
         f_PålydendeEtterSpleis = PålydendeEtterSpleis,
         f_OvertakendeSelskapOrgNum = OvertakendeSelskapOrgNum,
         f_OvertakendeDatterSelskapISIN = OvertakendeDatterSelskapISIN,
         f_OvertakendeSelskapAksjeklasse = OvertakendeSelskapAksjeklasse,
         f_Vederlagsaksjer = Vederlagsaksjer,
         f_PålydendePerVederlagsaksjer = PålydendePerVederlagsaksjer,
         f_Vederlagsaksjer2 = Vederlagsaksjer2,
         f_OvertakendeSelskapOrgNr = OvertakendeSelskapOrgNr,
         f_OvertakendeMorSelskapISIN = OvertakendeMorSelskapISIN,
         f_OvertakendeAksjetype = OvertakendeAksjetype,
         f_OvertakendePalydende = OvertakendePalydende,
         UkjentFelt = "vet ikke",
      )


def FillFormData_NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene(NedsettelseInnbetaltOverkurs, Tidspunkt):

   return """
      <NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene-grp-3461 gruppeid="3461">
         <AksjerOverkursNedsettelse-datadef-17707 orid="17707">{f_NedsettelseInnbetaltOverkurs}</AksjerOverkursNedsettelse-datadef-17707>
         <AksjerOverkursNedsettelseTidspunkt-datadef-17708 orid="17708">{f_Tidspunkt}</AksjerOverkursNedsettelseTidspunkt-datadef-17708>

      </NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene-grp-3461>
      """.format(
         f_NedsettelseInnbetaltOverkurs = NedsettelseInnbetaltOverkurs,
         f_Tidspunkt = "Tidspunkt",
         UkjentFelt = "vet ikke",
      )


def FillFormData_ForhoyelseAvAKVedOkningAvPalydende3462(Forhøyelse, PålydenePerAksjeFør, PålydenePerAksjeEtter, Tidspunkt):

   return """
      <ForhoyelseAvAKVedOkningAvPalydende-grp-3462 gruppeid="3462">
         <AksjekapitalForhoyelseFondsemisjon-datadef-17709 orid="17709">{f_Forhøyelse}</AksjekapitalForhoyelseFondsemisjon-datadef-17709>
         <AksjeFondsemisjonPalydendeForhoyelse-datadef-23956 orid="23956">{f_PålydenePerAksjeFør}</AksjeFondsemisjonPalydendeForhoyelse-datadef-23956>
         <AksjePalydendeEtterFondsemisjon-datadef-23957 orid="23957">{f_PålydenePerAksjeEtter}</AksjePalydendeEtterFondsemisjon-datadef-23957>
         <AksjeFondsemisjonTidspunkt-datadef-17712 orid="17712">{f_Tidspunkt}</AksjeFondsemisjonTidspunkt-datadef-17712>

      </ForhoyelseAvAKVedOkningAvPalydende-grp-3462>
      """.format(
         f_Forhøyelse = Forhøyelse,
         f_PålydenePerAksjeFør = PålydenePerAksjeFør,
         f_PålydenePerAksjeEtter = PålydenePerAksjeEtter,
         f_Tidspunkt = Tidspunkt,
         UkjentFelt = "vet ikke",
      )


def FillFormData_ForhoyelseAvAKVedOkningAvPalydende3463(ForhøyelseAvAksjeKapital, ØkningIPålydende, PålydendeEtter, HendelsesType, Tidspunkt, ForhøyelseAvOverkurs, OrgNummer, ISIN, Aksjeklasse):

   return """
      <ForhoyelseAvAKVedOkningAvPalydende-grp-3463 gruppeid="3463">
         <AksjekapitalNyemisjonForhoyelse-datadef-17713 orid="17713">{f_ForhøyelseAvAksjeKapital}</AksjekapitalNyemisjonForhoyelse-datadef-17713>
         <AksjeNyemisjonPalydendeForhoyelse-datadef-23958 orid="23958">{f_ØkningIPålydende}</AksjeNyemisjonPalydendeForhoyelse-datadef-23958>
         <AksjePalydendeEtterNyemisjon-datadef-23959 orid="23959">{f_PålydendeEtter}</AksjePalydendeEtterNyemisjon-datadef-23959>
         <AksjekapitalForhoyelsePalydendeHendelsestype-datadef-28268 orid="28268">{f_HendelsesType}</AksjekapitalForhoyelsePalydendeHendelsestype-datadef-28268>
         <AksjeNyemisjonTidspunkt-datadef-17716 orid="17716">{f_Tidspunkt}</AksjeNyemisjonTidspunkt-datadef-17716>
         <AksjeOverkursForhoyelse-datadef-22071 orid="22071">{f_ForhøyelseAvOverkurs}</AksjeOverkursForhoyelse-datadef-22071>
         <EnhetOverdragendeNyemisjonMvOrganisasjonsnummer-datadef-28213 orid="28213">{f_OrgNummer}</EnhetOverdragendeNyemisjonMvOrganisasjonsnummer-datadef-28213>
         <AksjerNyutstedteNyemisjonMvISIN-datadef-28214 orid="28214">{f_ISIN}</AksjerNyutstedteNyemisjonMvISIN-datadef-28214>
         <AksjerNyutstedteNyemisjonMvAksjetype-datadef-28215 orid="28215">{f_Aksjeklasse}</AksjerNyutstedteNyemisjonMvAksjetype-datadef-28215>
      </ForhoyelseAvAKVedOkningAvPalydende-grp-3463>
      """.format(
         f_ForhøyelseAvAksjeKapital = ForhøyelseAvAksjeKapital,
         f_ØkningIPålydende = ØkningIPålydende,
         f_PålydendeEtter = PålydendeEtter,
         f_Tidspunkt = Tidspunkt,
         f_HendelsesType = HendelsesType,
         f_ForhøyelseAvOverkurs = ForhøyelseAvOverkurs,
         f_OrgNummer = OrgNummer,
         f_ISIN = ISIN,
         f_Aksjeklasse = Aksjeklasse,
         UkjentFelt = "vet ikke",
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
         UkjentFelt = "vet ikke",
      )


def FillFormData_NedsettelseAKVedReduksjonAvPalydende(NedsettelseAvAksjekaptial, ReduksjonAvPålydendePerAksje, PålydendeEtter, Tidspunkt):

   return """
      <NedsettelseAKVedReduksjonAvPalydende-grp-3465 gruppeid="3465">
         <AksjekapitalUtbetalingNedsettelse-datadef-17722 orid="17722">{f_NedsettelseAvAksjekaptial}</AksjekapitalUtbetalingNedsettelse-datadef-17722>
         <AksjePalydendeNedsettelseUtbetaling-datadef-23962 orid="23962">{f_ReduksjonAvPålydendePerAksje}</AksjePalydendeNedsettelseUtbetaling-datadef-23962>
         <AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963 orid="23963">{f_PålydendeEtter}</AksjePalydendeEtterNedsettelseUtbetaling-datadef-23963>
         <AksjeNedsettelseTidspunkt-datadef-17725 orid="17725">{f_Tidspunkt}</AksjeNedsettelseTidspunkt-datadef-17725>
      </NedsettelseAKVedReduksjonAvPalydende-grp-3465>
      """.format(
         f_NedsettelseAvAksjekaptial = NedsettelseAvAksjekaptial,
         f_ReduksjonAvPålydendePerAksje = ReduksjonAvPålydendePerAksje,
         f_PålydendeEtter = PålydendeEtter,
         f_Tidspunkt = Tidspunkt,
         UkjentFelt = "vet ikke",
      )


def FillFormData_NedsettelseAvAKVedReduksjonUtfisjonering(ReduksjonAvPålydendePerAksje, HendelsesType, OvertakendeMorselskapsISIN, PålydendePerVederlagsaksje):

   return """
      <NedsettelseAvAKVedReduksjonUtfisjonering-grp-3466 gruppeid="3466">
         <AksjePalydendeNedsettelseUtfisjonering-datadef-23964 orid="23964">{f_ReduksjonAvPålydendePerAksje}</AksjePalydendeNedsettelseUtfisjonering-datadef-23964>
         <AksjeUtfisjoneringHendelsestype-datadef-37825 orid="37825">{f_HendelsesType}</AksjeUtfisjoneringHendelsestype-datadef-37825>
         <EnhetISINOvertakendeMorselskap-datadef-17735 orid="17735">{f_OvertakendeMorselskapsISIN}</EnhetISINOvertakendeMorselskap-datadef-17735>
         <AksjerMorselskapOvertakendeVederlagPalydende-datadef-23967 orid="23967">{f_PålydendePerVederlagsaksje}</AksjerMorselskapOvertakendeVederlagPalydende-datadef-23967>
      </NedsettelseAvAKVedReduksjonUtfisjonering-grp-3466>
      """.format(
         f_ReduksjonAvPålydendePerAksje = ReduksjonAvPålydendePerAksje,
         f_HendelsesType = HendelsesType,
         f_OvertakendeMorselskapsISIN = OvertakendeMorselskapsISIN,
         f_PålydendePerVederlagsaksje = PålydendePerVederlagsaksje,
         UkjentFelt = "vet ikke",
      )


def FillFormData_SelskapsOgAksjonaropplysninger(OrgNummer,Inntektsår,Innsendingsmåte,Aksjonæridentifikasjon,UtenlandskAkjsonærIdentifikasjon,AkjsonærNavn,AksjonærPoststed,AksjonærLandkode):
   return """
      <SelskapsOgAksjonaropplysninger-grp-3987 gruppeid="3987">
         <Selskapsidentifikasjon-grp-3986 gruppeid="3986">
            <EnhetOrganisasjonsnummer-datadef-18 orid="18">{f_OrgNummer}</EnhetOrganisasjonsnummer-datadef-18>
            <Inntektsar-datadef-692 orid="692">{f_Inntektsår}</Inntektsar-datadef-692>
            <AksjonarregisteroppgaveUnderskjemaInnsendingsmate-datadef-34856 orid="34856">{f_Innsendingsmåte}</AksjonarregisteroppgaveUnderskjemaInnsendingsmate-datadef-34856>
         </Selskapsidentifikasjon-grp-3986>
         <NorskUtenlandskAksjonar-grp-3988 gruppeid="3988">
            <AksjonarFodselsnummer-datadef-1156 orid="1156">{f_Aksjonæridentifikasjon}</AksjonarFodselsnummer-datadef-1156>
            <AksjonarUtenlandskIdenifikasjonsnummer-datadef-26626 orid="26626">{f_UtenlandskAkjsonærIdentifikasjon}</AksjonarUtenlandskIdenifikasjonsnummer-datadef-26626>
            <AksjonarNavn-datadef-1153 orid="1153">{f_AkjsonærNavn}</AksjonarNavn-datadef-1153>
            <AksjonarPoststed-datadef-7599 orid="7599">{f_AksjonærPoststed}</AksjonarPoststed-datadef-7599>
            <AksjonarLandkode-datadef-17740 orid="17740">{f_AksjonærLandkode}</AksjonarLandkode-datadef-17740>
         </NorskUtenlandskAksjonar-grp-3988>
      </SelskapsOgAksjonaropplysninger-grp-3987>
   """.format(
      f_OrgNummer = OrgNummer,
      f_Inntektsår = Inntektsår,
      f_Innsendingsmåte = Innsendingsmåte,
      f_Aksjonæridentifikasjon = Aksjonæridentifikasjon,
      f_UtenlandskAkjsonærIdentifikasjon = UtenlandskAkjsonærIdentifikasjon,
      f_AkjsonærNavn = AkjsonærNavn,
      f_AksjonærPoststed = AksjonærPoststed,
      f_AksjonærLandkode = AksjonærLandkode,
   )


def FillFormData_AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit( AntallAkjserPerAksjonærFjoråret,AntallAkjserPerAksjonær,UtdeltUtbytte,AntallAkjser,Tidspunkt,Kildeskatt,Transaksjonstype,Beløp,TidspunktTilbakeBetaling):
   return """
      <AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit-grp-3990 gruppeid="3990">
         <AntallAksjerPerAksjonar-grp-3989 gruppeid="3989">
            <AksjerAntallFjoraret-datadef-29168 orid="29168">{f_AntallAkjserPerAksjonærFjoråret}</AksjerAntallFjoraret-datadef-29168>
            <AksjonarAksjerAntall-datadef-17741 orid="17741">{f_AntallAkjserPerAksjonær}</AksjonarAksjerAntall-datadef-17741>
         </AntallAksjerPerAksjonar-grp-3989>
         <UtdeltUtbyttePerAksjonar-grp-3991 gruppeid="3991">
            <Aksjeutbytte-datadef-29169 orid="29169">{f_UtdeltUtbytte}</Aksjeutbytte-datadef-29169>
            <AksjerUtbytteAntall-datadef-17742 orid="17742">{f_AntallAkjser}</AksjerUtbytteAntall-datadef-17742>
            <AksjerUtbytteTidspunkt-datadef-17769 orid="17769">{f_Tidspunkt}</AksjerUtbytteTidspunkt-datadef-17769>
            <Kildeskatt-datadef-17743 orid="17743">{f_Kildeskatt}</Kildeskatt-datadef-17743>
         </UtdeltUtbyttePerAksjonar-grp-3991>
    
         <TilbakebetalingAvTidligereInnbetaltKapital-grp-7633 gruppeid="7633">
            <TilbakebetalingAvTidligereInnbetaltKapital-grp-7865 gruppeid="7865">
               <KapitalTidligereInnbetaltTilbakebetaling-datadef-30396 orid="30396">{f_Beløp}</KapitalTidligereInnbetaltTilbakebetaling-datadef-30396>
               <KapitalTidligereInnbetaltTilbakebetaltHendelsestype-datadef-36658 orid="36658">{f_Transaksjonstype}</KapitalTidligereInnbetaltTilbakebetaltHendelsestype-datadef-36658>
               <KapitalTidligereInnbetaltTilbakebetalingDato-datadef-30397 orid="30397">{f_TidspunktTilbakeBetaling}</KapitalTidligereInnbetaltTilbakebetalingDato-datadef-30397>
            </TilbakebetalingAvTidligereInnbetaltKapital-grp-7865>
         </TilbakebetalingAvTidligereInnbetaltKapital-grp-7633>
      </AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit-grp-3990>
   """.format(
      f_AntallAkjserPerAksjonærFjoråret = AntallAkjserPerAksjonærFjoråret,
      f_AntallAkjserPerAksjonær = AntallAkjserPerAksjonær,
      f_UtdeltUtbytte = UtdeltUtbytte,
      f_AntallAkjser = AntallAkjser,
      f_Tidspunkt = Tidspunkt,
      f_Kildeskatt = Kildeskatt,
      f_Transaksjonstype = Transaksjonstype,
      f_Beløp = Beløp,
      f_TidspunktTilbakeBetaling = TidspunktTilbakeBetaling,
   )


def FillFormData_Transaksjoner(TransaksjonType,AvgiversFødselsNummer,AvgiversOrganisasjonsNum):
   return """
      <Transaksjoner-grp-3992 gruppeid="3992">
         <KjopArvGaveStiftelseNyemisjonMv-grp-3993 gruppeid="3993">
            <AntallAksjerITilgang-grp-3998 gruppeid="3998">
               <AksjeErvervType-datadef-17745 orid="17745">{f_TransaksjonType}</AksjeErvervType-datadef-17745>
               <AksjonarTidligereFodselsnummer-datadef-26530 orid="26530">{f_AvgiversFødselsNummer}</AksjonarTidligereFodselsnummer-datadef-26530>
               <AksjonarTidligereOrganisasjonsnummer-datadef-26531 orid="26531">{f_AvgiversOrganisasjonsNum}</AksjonarTidligereOrganisasjonsnummer-datadef-26531>
            </AntallAksjerITilgang-grp-3998>
         </KjopArvGaveStiftelseNyemisjonMv-grp-3993>
      </Transaksjoner-grp-3992>
   """.format(
      f_TransaksjonType = TransaksjonType,
      f_AvgiversFødselsNummer = AvgiversFødselsNummer,
      f_AvgiversOrganisasjonsNum = AvgiversOrganisasjonsNum,
   )


def FillFormData_FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv(AntallAkjserITilgang,TransaksjonsType,Tidspunkt, OverdragendeOrgNum, OverdragendeISIN, OverdragendeAksjeKlasse, PålydendePerAksje):
   return """
      <FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv-grp-3994 gruppeid="3994">
         <AntallAksjerITilgangIfmOmfordeling-grp-3999 gruppeid="3999">
            <AksjerTilgangFondsemisjonMvAntall-datadef-17748 orid="17748">{f_AntallAkjserITilgang}</AksjerTilgangFondsemisjonMvAntall-datadef-17748>
            <AksjerTilgangFondsemisjonMvType-datadef-17749 orid="17749">{f_TransaksjonsType}</AksjerTilgangFondsemisjonMvType-datadef-17749>
            <AksjerTilgangFondsemisjonMvTidspunkt-datadef-17750 orid="17750">{f_Tidspunkt}</AksjerTilgangFondsemisjonMvTidspunkt-datadef-17750>
            <EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683 orid="17683">{f_OverdragendeOrgNum}</EnhetOverdragendeFondsemisjonMvOrganisasjonsnummer-datadef-17683>
            <AksjerNyutstedteFondsemisjonMvISIN-datadef-17684 orid="17684">{f_OverdragendeISIN}</AksjerNyutstedteFondsemisjonMvISIN-datadef-17684>
            <AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905 orid="19905">{f_OverdragendeAksjeKlasse}</AksjerNyutstedteFondsemisjonMvAksjetype-datadef-19905>
            <AksjerFondsemisjonPalydende-datadef-23968 orid="23968">{f_PålydendePerAksje}</AksjerFondsemisjonPalydende-datadef-23968>
         </AntallAksjerITilgangIfmOmfordeling-grp-3999>
      </FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv-grp-3994>
   """.format(
      f_AntallAkjserITilgang = AntallAkjserITilgang,
      f_TransaksjonsType = TransaksjonsType,
      f_Tidspunkt = Tidspunkt,
      f_OverdragendeOrgNum = OverdragendeOrgNum,
      f_OverdragendeISIN = OverdragendeISIN,
      f_OverdragendeAksjeKlasse = OverdragendeAksjeKlasse,
      f_PålydendePerAksje = PålydendePerAksje,
   )


def FillFormData_SalgArvGaveLikvidasjonPartiellLikvidasjonMv(AntallAksjerIAvgang,TotaltVederlag):
   return """
      <SalgArvGaveLikvidasjonPartiellLikvidasjonMv-grp-3995 gruppeid="3995">
         <AksjerIAvgang-grp-4002 gruppeid="4002">
            <AksjerArvMvOmsattAntall-datadef-17752 orid="17752">{f_AntallAksjerIAvgang}</AksjerArvMvOmsattAntall-datadef-17752>
            <AksjerArvMvOmsatt-datadef-17755 orid="17755">{f_TotaltVederlag}</AksjerArvMvOmsatt-datadef-17755>
         </AksjerIAvgang-grp-4002>
      </SalgArvGaveLikvidasjonPartiellLikvidasjonMv-grp-3995>
   """.format(
      f_AntallAksjerIAvgang = AntallAksjerIAvgang,
      f_TotaltVederlag = TotaltVederlag,
   )
   

def FillFormData_SpleisSkattefriFusjonOgSkattefriFisjon(AntallAksjerIAvgang,Transaksjonstype, OvertakendeOrgNum, OvertakendeISIN, OvertakendeAksjeKlasse, OvertakendePålydendePerAksje):
   return """
      <SpleisSkattefriFusjonOgSkattefriFisjon-grp-3996 gruppeid="3996">
         <AntallAksjerIAvgangVedOmfordeling-grp-4003 gruppeid="4003">
            <AksjerSpleisMvAvgangAntall-datadef-24007 orid="24007">{f_AntallAksjerIAvgang}</AksjerSpleisMvAvgangAntall-datadef-24007>
            <AksjerSpleisMvType-datadef-17758 orid="17758">{f_Transaksjonstype}</AksjerSpleisMvType-datadef-17758>
            <EnhetOvertakendeFisjonOrganisasjonsnummer-datadef-17699 orid="17699">{f_OvertakendeOrgNum}</EnhetOvertakendeFisjonOrganisasjonsnummer-datadef-17699>
            <AksjerSpleisMvOvetakendeISIN-datadef-17700 orid="17700">{f_OvertakendeISIN}</AksjerSpleisMvOvetakendeISIN-datadef-17700>
            <AksjerSpleisMvOvertakendeAksjetype-datadef-19906 orid="19906">{f_OvertakendeAksjeKlasse}</AksjerSpleisMvOvertakendeAksjetype-datadef-19906>
            <AksjerSpleisMvPalydende-datadef-23969 orid="23969">{f_OvertakendePålydendePerAksje}</AksjerSpleisMvPalydende-datadef-23969>
         </AntallAksjerIAvgangVedOmfordeling-grp-4003>
      </SpleisSkattefriFusjonOgSkattefriFisjon-grp-3996>
   """.format(
      f_AntallAksjerIAvgang = AntallAksjerIAvgang,
      f_Transaksjonstype = Transaksjonstype,
      f_OvertakendeOrgNum = OvertakendeOrgNum,
      f_OvertakendeISIN = OvertakendeISIN,
      f_OvertakendeAksjeKlasse = OvertakendeAksjeKlasse,
      f_OvertakendePålydendePerAksje = OvertakendePålydendePerAksje,
   )
   

def FillFormData_EndringerIAksjekapitalOgOverkurs(
   NedsettelseAvFondsemittertAksjekapital, ReduksjonAvPålydendePerAksje,
   OverkursTilbakeBetaling, TilbakeBetalingTidspunkt, ForhøyelseAvOverkurs,
   ØkningAvPålydendePerAksje, TransaksjonsType, TidspunktAksjeNyemisjon, OverdragendeISIN,
   ReduksjonAvAksjekapital, TidspunktAksjekapitalReduksjon, OvertakendeSelskapOrgNum,
   OvertakendeSelskapISIN, OvertakendeSelskapAksjeklasse,):
   return """
      <EndringerIAksjekapitalOgOverkurs-grp-3997 gruppeid="3997">

         <TilbakebetaltInnbetaltOgFondsemittertAKVedReduksjonAvPalydende-grp-4000 gruppeid="4000">
            <AksjePalydendeRedusert-datadef-23970 orid="23970">{f_NedsettelseAvFondsemittertAksjekapital}</AksjePalydendeRedusert-datadef-23970>
            <AksjekapitalNedsettelse-datadef-17764 orid="17764">{f_ReduksjonAvPålydendePerAksje}</AksjekapitalNedsettelse-datadef-17764>
         </TilbakebetaltInnbetaltOgFondsemittertAKVedReduksjonAvPalydende-grp-4000>

         <TilbakebetaltTidligereInnbetaltOverkursForAksjen-grp-4001 gruppeid="4001">
            <OverkursTilbakebetalt-datadef-17765 orid="17765">{f_OverkursTilbakeBetaling}</OverkursTilbakebetalt-datadef-17765>
            <OverkursTilbakebetaltTidspunkt-datadef-17766 orid="17766">{f_TilbakeBetalingTidspunkt}</OverkursTilbakebetaltTidspunkt-datadef-17766>
         </TilbakebetaltTidligereInnbetaltOverkursForAksjen-grp-4001>
        
         <ForhoyelseAvInnbetaltAksjekapitalVedOkning-grp-4987 gruppeid="4987">
            <AksjeOverkursForhoyelseAksjonar-datadef-22076 orid="22076">{f_ForhøyelseAvOverkurs}</AksjeOverkursForhoyelseAksjonar-datadef-22076>
            <AksjeNyemisjonPalydendeForhoyelseAksjonar-datadef-23971 orid="23971">{f_ØkningAvPålydendePerAksje}</AksjeNyemisjonPalydendeForhoyelseAksjonar-datadef-23971>
            <AksjekapitalNyemisjonForhoyelsePalydendeTransaksjonstype-datadef-28267 orid="28267">{f_TransaksjonsType}</AksjekapitalNyemisjonForhoyelsePalydendeTransaksjonstype-datadef-28267>
            <AksjeNyemisjonTidspunktAksjonar-datadef-22075 orid="22075">{f_TidspunktAksjeNyemisjon}</AksjeNyemisjonTidspunktAksjonar-datadef-22075>
            <AksjerNyutstedteNyemisjonMvISINAksjonar-datadef-28217 orid="28217">{f_OverdragendeISIN}</AksjerNyutstedteNyemisjonMvISINAksjonar-datadef-28217>
         </ForhoyelseAvInnbetaltAksjekapitalVedOkning-grp-4987>

         <ReduksjonInnbetaltAksjekapital-grp-9857 gruppeid="9857">
            <AksjekapitalReduksjon-datadef-37826 orid="37826">{f_ReduksjonAvAksjekapital}</AksjekapitalReduksjon-datadef-37826>
            <AksjekapitalReduksjonTidspunkt-datadef-37828 orid="37828">{f_TidspunktAksjekapitalReduksjon}</AksjekapitalReduksjonTidspunkt-datadef-37828>
            <EnhetOverdragendeKapitalreduksjonOrganisasjonsnummer-datadef-37829 orid="37829">{f_OvertakendeSelskapOrgNum}</EnhetOverdragendeKapitalreduksjonOrganisasjonsnummer-datadef-37829>
            <AksjerReduksjonISIN-datadef-37830 orid="37830">{f_OvertakendeSelskapISIN}</AksjerReduksjonISIN-datadef-37830>
            <AksjerReduksjonAksjeklasse-datadef-37831 orid="37831">{f_OvertakendeSelskapAksjeklasse}</AksjerReduksjonAksjeklasse-datadef-37831>
         </ReduksjonInnbetaltAksjekapital-grp-9857>
      </EndringerIAksjekapitalOgOverkurs-grp-3997>
   """.format(
      f_NedsettelseAvFondsemittertAksjekapital = NedsettelseAvFondsemittertAksjekapital,
      f_ReduksjonAvPålydendePerAksje = ReduksjonAvPålydendePerAksje,
      f_OverkursTilbakeBetaling = OverkursTilbakeBetaling,
      f_TilbakeBetalingTidspunkt = TilbakeBetalingTidspunkt,
      f_ForhøyelseAvOverkurs = ForhøyelseAvOverkurs,
      f_ØkningAvPålydendePerAksje = ØkningAvPålydendePerAksje,
      f_TransaksjonsType = TransaksjonsType,
      f_TidspunktAksjeNyemisjon = TidspunktAksjeNyemisjon,
      f_OverdragendeISIN = OverdragendeISIN,
      f_ReduksjonAvAksjekapital = ReduksjonAvAksjekapital,
      f_TidspunktAksjekapitalReduksjon = TidspunktAksjekapitalReduksjon,
      f_OvertakendeSelskapOrgNum = OvertakendeSelskapOrgNum,
      f_OvertakendeSelskapISIN = OvertakendeSelskapISIN,
      f_OvertakendeSelskapAksjeklasse = OvertakendeSelskapAksjeklasse,
   )


def FillFormData_UnderSkjema():
   return """
      <ns:Forms>
         <ns:Form>
            <ns:Completed>0</ns:Completed>
            <ns:DataFormatId>923</ns:DataFormatId>
            <ns:DataFormatVersion>12232</ns:DataFormatVersion>
            <ns:EndUserSystemReference>2</ns:EndUserSystemReference>
            <ns:ParentReference>0</ns:ParentReference>
            <ns:FormData><![CDATA[
               <Skjema xmlns:brreg="http://www.brreg.no/or" xsi:noNamespaceSchemaLocation="schema.xsd" skjemanummer="923" spesifikasjonsnummer="12232" blankettnummer="RF-1086-U" tittel="Aksjonærregisteroppgaven - underskjema" gruppeid="3983" etatid="NoAgency" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                  
                  {SelskapsOgAksjonaropplysninger}

                  {AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit}

                  {Transaksjoner}

                  {FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv}

                  {SalgArvGaveLikvidasjonPartiellLikvidasjonMv}

                  {SpleisSkattefriFusjonOgSkattefriFisjon}

                  {EndringerIAksjekapitalOgOverkurs}
                 
               </Skjema>
            ]]></ns:FormData>
         </ns:Form>
      </ns:Forms>
   """.format(
      SelskapsOgAksjonaropplysninger = FillFormData_SelskapsOgAksjonaropplysninger("OrgNum", "Inntektsår", "Innsendingsmåte", "AksjonærIdentifikasjon", "UtenlandskIdent", "Navn", "Poststed", "Landkode"),
      AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit = FillFormData_AntallAksjerUtbytteOgTilbakebetalingAvTidligereInnbetaltKapit("AntallAksjerFør", "AntallAksjerNå", "UtdeltUtbytte", "AntallAksjer", "Tidspunkt", "KildeSkatt", "Transaksjonstype", "beløp", "Tidspunkt"),
      Transaksjoner = FillFormData_Transaksjoner("Transaksjonstype", "Fødselsnumr", "OrgNum"),
      FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv = FillFormData_FondsemisjonSplittSkattefriFusjonFisjonSammenslaingDelingAv("AntallAksjerITilgang", "Transaksjonstype", "Tidspunkt", "OrgNum", "ISIN", "Aksjeklasse", "Pålydende"),
      SalgArvGaveLikvidasjonPartiellLikvidasjonMv = FillFormData_SalgArvGaveLikvidasjonPartiellLikvidasjonMv("AntallAksjerIAvgang", "TotaltVederlag"),
      SpleisSkattefriFusjonOgSkattefriFisjon = FillFormData_SpleisSkattefriFusjonOgSkattefriFisjon("AntallAksjerIAvgang", "TransaksionsType", "OrgNum", "OvertakendeISIN", "Aksjeklasse", "Pålydende"),
      EndringerIAksjekapitalOgOverkurs = FillFormData_EndringerIAksjekapitalOgOverkurs("NedsetteleAvAksjeKapital", "ReduksjonAvPålydende", "OverkurstilbakeBetaling", "TilbakeBetalingTidspunkt", "ForhøyelseAvOverkurs", "ØkningAvPålydende", "TransaksjonsType", "TidspunktAksjeNyem", "OverdragendeISIN", "ReduksjonAvAksjekapital", "TidspunktAksjekapitalReduksjon", "OvertakendeSelskapOrgNum", "ISIN", "Aksjeklasse"),
   )



   return """

      """.format(

         UkjentFelt = "vet ikke",
      )


def sendFormData(username, userpassword, authcode, authType, orgnumber):
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
            <ns:authMethod>{f_PinType}</ns:authMethod>
            
            <ns:formTaskShipment>
               <ns:Reportee>{CompanyNumber_Str}</ns:Reportee>
               <ns:ExternalShipmentReference>{UniqueNumIdentifier}</ns:ExternalShipmentReference>
                <ns:FormTasks>

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

                        {f_NedsettelseAvAKVedReduksjonUtfisjonering} 
                        
                     </EndringerIAksjekapitalOgOverkurs-grp-3460>

                     </Skjema>
                     ]]></ns:FormData>
                  </ns:Form>
               </ns:Forms>
               {f_UnderSkjema}
            </ns:FormTasks>
            <ns:IsUserDelegationLocked>false</ns:IsUserDelegationLocked>
            </ns:formTaskShipment>
         </ns:SubmitFormTaskBasic>
      </soapenv:Body>
   </soapenv:Envelope>

   """.format(
         f_PinType = authType,
         SystemUserName_Str = SystemUserName, 
         SystemPassword_Str = SystemPassword, 
         UserSSN_Str = username, 
         UserPassword_Str = userpassword,
         UserPin_Str = authcode,
         UniqueNumIdentifier = random.randint(0,100000),
         CompanyNumber_Str = orgnumber,
         #f_GenerellInformasjon = FillFormData_GenerellInformasjon("OrgNum", "PostNum", "Poststed", "ISIN", "Aksjeklasse", "År", "AnsvarligNavn", "Rolle", "Epost", "TlfNr"),
         f_GenerellInformasjon = FillFormData_GenerellInformasjon("911007118", "0571", "0571", "47ISINNUMMER", "03", "2022", "Viktor", "Admin", "Viktor@gmail.com", "91339542"),
         #f_Selskapsopplysninger = FillFormData_Selskapsopplysninger("AksjeKapital", "KapitalIAksjeKlasse", "Pålydende", "AntallAksjerFjoråret", "AntallAksjer", "InnbetaltAksjekapital" , "Overkurs"),
         f_Selskapsopplysninger = FillFormData_Selskapsopplysninger("1000000", "750000", "1000", "750", "750", "100000" , "250000"),
         f_Utbytte = FillFormData_Utbytte(UtbytteTestData),
         f_UtstedelseAvAksjerIfmStiftelseNyemisjonMv = FillFormData_UtstedelseAvAksjerIfmStiftelseNyemisjonMv("Antall", "AntallEtter", "Hendelse", "Tidspunkt", "Pålydende", "Overkurs", "EgneAksjerOverført"),
         f_UtstedelseAvAksjerIfmFondsemisjonSplittMv = FillFormData_UtstedelseAvAksjerIfmFondsemisjonSplittMv("10", "22", "Splitt", "121212", "PålydendePerAkjse", "", "800", "123", "12", "A-Aksjer"),
         f_SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv = FillFormData_SlettingAvAksjerIfmLikvidasjonPartiellLikvidasjonMv("Antall", "AntallEtter", "PålydendePerAkjse", "Hendelse", "Tidspunkt", "Overkurs", "Vederlag"),
         f_SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon = FillFormData_SlettingAvAksjerIfmSpleisSkattefriFusjonFisjon("Antall", "antallEtter", "Hendelse", "Tidspunkt", "Pålydende", "PålydendeEtterSpleis", "OvertakendeSelskapOrgnum", "OvertakendeSelskapISIN", "Aksjeklasse", "Vederlagsaksjer", "PålydendeperVederlagsaksjer", "Vederlagsaksjer", "OrgNr", "morSelskapISIN", "AksjeType", "Pålydende"),
         f_NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene = FillFormData_NedsettelseAvInnbetaltOverkursMedTilbakebetalingTilAksjonarene("Nedsettelse", "Tidspunkt"),
         f_ForhoyelseAvAKVedOkningAvPalydende3462 = FillFormData_ForhoyelseAvAKVedOkningAvPalydende3462("Forhøyelse", "PålydendeFør", "NedsettelseOverkurs", "Tidspunkt"),
         f_ForhoyelseAvAKVedOkningAvPalydende3463 = FillFormData_ForhoyelseAvAKVedOkningAvPalydende3463("Forhøyelse", "ØkningPålydeende", "PålydendeEtter", "Hendelse", "Tidspunkt", "ForhøyelseOverkurs", "OrgNr", "ISIN", "AksjeKlasse"),
         f_NedsettelseAvInnbetaltOgFondsemittertAK = FillFormData_NedsettelseAvInnbetaltOgFondsemittertAK("NedsettelseAvInnbetalt", "RedukasjonAvPålydende", "PålydendeEtter", "Tidspunkt", "NedsettelseAvFondsemittert"),
         f_NedsettelseAKVedReduksjonAvPalydende = FillFormData_NedsettelseAKVedReduksjonAvPalydende("NedsettelseAvAksjeKapital", "ReduksjonAvPålydendePerAksje", "Etter", "Tidspunkt"),
         f_NedsettelseAvAKVedReduksjonUtfisjonering = FillFormData_NedsettelseAvAKVedReduksjonUtfisjonering("ReduksjonAvPålydendePerAksje", "Hendelse", "OvertakendeMorISIN", "PålydendePerVederlagsAksje"),
         f_UnderSkjema = FillFormData_UnderSkjema(),
      ).encode("utf-8")

   # Posts SOAP request and stores response
   re = requests.post("https://tt02.altinn.no/IntermediaryExternal/IntermediaryInboundBasic.svc", data=body, headers=headers)

   # Uses beautifulSoup to parse the xml return
   soup = bs4.BeautifulSoup(re.content, features="html.parser")

   if (re.status_code == 200):
      #status message
      msg = soup.find("receipttext").string
      if (soup.find("receiptstatuscode").string == "Ok"):
         #Success
         return [True, msg]
      else:
         #Error on form submission
         return [False, msg]

   else:
      #Get error msg
      responsStatus = soup.find("altinnerrormessage").string
      return [False, responsStatus]


def GetArchivedForms(username, userpassword, authcode, authType, orgnumber):
   headers = {
      "Vary": "Accept-Encoding",
      "Accept-Encoding": "gzip,deflate",
      "Content-Type" : "text/xml; charset=utf-8",
      "SOAPAction": "http://www.altinn.no/services/ServiceEngine/ReporteeElementList/2009/10/IReporteeElementListExternalBasic/GetReporteeElementListBasicV2",
      "Host": "tt02.altinn.no",
      "Connection": "Keep-Alive",
      "User-Agent": "Apache-HttpClient/4.5.5 (Java/16.0.1)"
   }
   
   body = """
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.altinn.no/services/ServiceEngine/ReporteeElementList/2009/10" xmlns:ns1="http://schemas.altinn.no/services/Archive/ReporteeArchive/2009/10" xmlns:arr="http://schemas.microsoft.com/2003/10/Serialization/Arrays">
      <soapenv:Header/>
      <soapenv:Body>
         <ns:GetReporteeElementListBasicV2>
            <ns:systemUserName>{SystemUserName_Str}</ns:systemUserName>
            <ns:systemPassword>{SystemPassword_Str}</ns:systemPassword>
            <ns:userSSN>{UserSSN_Str}</ns:userSSN>
            <ns:userPassword>{UserPassword_Str}</ns:userPassword>
            <ns:userPinCode>{UserPin_Str}</ns:userPinCode>
            <ns:authMethod>{f_PinType}</ns:authMethod>
            <ns:searchBE>
               <ns1:FromDate>{f_DateStart}</ns1:FromDate>
               <ns1:Reportee>{f_OrgNumber}</ns1:Reportee>
               <ns1:SentAndArchived>1</ns1:SentAndArchived>
               <ns1:ToDate>{f_DateEnd}</ns1:ToDate>
            </ns:searchBE>
            <ns:languageID>1033</ns:languageID>
         </ns:GetReporteeElementListBasicV2>
      </soapenv:Body>
   </soapenv:Envelope>
   """.format(
      f_PinType = authType,
      SystemUserName_Str = SystemUserName, 
      SystemPassword_Str = SystemPassword, 
      UserSSN_Str = username, 
      UserPassword_Str = userpassword,
      UserPin_Str = authcode,
      f_DateStart = "1999-12-22",
      f_DateEnd = "2222-12-22",
      f_OrgNumber = orgnumber,

   ).encode("utf-8")

   re = requests.post("https://tt02.altinn.no/ServiceEngineExternal/ReporteeElementListExternalBasic.svc", data=body, headers=headers)
   
   print(re.content)

   # Uses beautifulSoup to parse the xml return
   soup = bs4.BeautifulSoup(re.content, features="html.parser")

   #Error handling
   if (re.status_code == 200):
      if (soup.find("a:reporteeelementbev2") != None):
         # Gets the id of the document
         responsStatus = soup.find("a:sereporteeelementid").string
         return [True, responsStatus]

      if (soup.find("a:reporteeelementbev2") != None):
         # Gets the id of the document
         return [False, "Did not find any previous submissions"]
   else:
      #Get error msg
      responsStatus = soup.find("altinnerrormessage").string
      return [False, responsStatus]


def GetFormData(username, userpassword, authcode, authType, elementID):
   headers = {
      "Vary": "Accept-Encoding",
      "Accept-Encoding": "gzip,deflate",
      "Content-Type" : "text/xml; charset=utf-8",
      "SOAPAction": "http://www.altinn.no/services/ServiceEngine/ReporteeElementList/2009/10/IReporteeElementListExternalBasic/GetFormSetDataBasic",
      "Host": "tt02.altinn.no",
      "Connection": "Keep-Alive",
      "User-Agent": "Apache-HttpClient/4.5.5 (Java/16.0.1)"
   }

   body = """
      <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.altinn.no/services/ServiceEngine/ReporteeElementList/2009/10">
         <soapenv:Header/>
         <soapenv:Body>
            <ns:GetFormSetDataBasic>
            <ns:systemUserName>{SystemUserName_Str}</ns:systemUserName>
            <ns:systemPassword>{SystemPassword_Str}</ns:systemPassword>
            <ns:userSSN>{UserSSN_Str}</ns:userSSN>
            <ns:userPassword>{UserPassword_Str}</ns:userPassword>
            <ns:userPinCode>{UserPin_Str}</ns:userPinCode>
            <ns:authMethod>{f_PinType}</ns:authMethod>
            <ns:reporteeElementID>{elementID_Str}</ns:reporteeElementID>
            <ns:languageID>1033</ns:languageID>
            </ns:GetFormSetDataBasic>
         </soapenv:Body>
      </soapenv:Envelope>
   """.format(
      f_PinType = authType,
      SystemUserName_Str = SystemUserName,
      SystemPassword_Str = SystemPassword,
      UserSSN_Str = username,
      UserPassword_Str = userpassword,
      UserPin_Str = authcode,
      elementID_Str = elementID,
   ).encode("utf-8")

   re = requests.post("https://tt02.altinn.no/ServiceEngineExternal/ReporteeElementListExternalBasic.svc", data=body, headers=headers)
   
   #the return data is formated weirdly, so this is a janky solution to that
   response = re.content.replace(b"&lt;", b"<").replace(b"&gt;", b">")

   # Uses beautifulSoup to parse the xml return
   soup = bs4.BeautifulSoup(response, features="html.parser")
   # Gets the id of the document
   
   #Error handling
   if (re.status_code == 200):
      return [True, "responsStatus"]
   else:
      #Get error msg
      responsStatus = soup.find("altinnerrormessage").string
      return [False, responsStatus]

# This function sends an SMS authorization code from altinn to the user
# Returns a tuple with boolean if the function was a success or not, as well as an error message (in Norwegian)
def sendAuthCodeToUser(username, userpassword, authType):
   headers = {
      "Accept-Encoding": "gzip,deflate",
      "Content-Type": "text/xml;charset=UTF-8",
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
               <ns1:AuthMethod>{f_PinType}</ns1:AuthMethod>
               <ns1:SystemUserName>{SystemUserName_Str}</ns1:SystemUserName>
               <ns1:UserPassword>{UserPassword_Str}</ns1:UserPassword>
               <ns1:UserSSN>{UserSSN_Str}</ns1:UserSSN>
            </ns:challengeRequest>
         </ns:GetAuthenticationChallenge>
      </soapenv:Body>
   </soapenv:Envelope>

   """.format(
      f_PinType = authType,
      SystemUserName_Str = SystemUserName, 
      UserSSN_Str = username, 
      UserPassword_Str = userpassword).encode("utf-8")
   # Posts SOAP request and stores response
   re = requests.post("https://tt02.altinn.no/AuthenticationExternal/SystemAuthentication.svc", data=body, headers=headers)
   
   # Uses beautifulSoup to parse the xml return
   soup = bs4.BeautifulSoup(re.content, features="html.parser")
   
   # Gets Status code to check if the request is valid
   if (re.status_code == 200):
      #if the request is valid but contains wrong info
      if (soup.find("a:status").string == "Ok"):
         return {True, soup.find("a:message").string}
      else: 
         return {False, soup.find("a:message").string}
   else:
      return {False, soup.find("a:altinnerrormessage").string}


#Get Authorization code, 
# if you are using SMSPin it will provide a code to use in future request, 
# if you are using AltinnPin, it will provide a number which coresponds to a code on the testusers document.
print(sendAuthCodeToUser(testUserUsername, testUserPassword, AuthCodeType))

#Make new form in altinn, this makes a form filled out with dummy data
#print(sendFormData(testUserUsername, testUserPassword, "codehere", 911007118))

#GetPreviouslySubmittedForms
#print(GetArchivedForms(testUserUsername, testUserPassword, "codehere", 213688812))

#Get data of a prevousily submitted form
#print(GetFormData(testUserUsername, testUserPassword, "codehere", 17158613))