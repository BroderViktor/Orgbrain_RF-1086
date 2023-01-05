Guide to this RF-1086 submission program
---
To use this program you need a **test user** in altinn, a premade test users can be found in this repo under the name "Test user.pdf" or at the link below:  

https://www.altinndigital.no/produkter/altinn-api-for-datasystem/tjenesteoversikt/skatteetaten---ar/nyheter/rf-1086-oppdatering-av-utgavekode-for-test/

First we need to setup the user and a corresponding system in altinn:
(The testnetwork seems to be quite buggy on some browsers, so if it doesn't work i recommend switching browser)

Go to the following link to access the testnetwork of altinn https://tt02.altinn.no. 

Then click on the "logg inn" button 
![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/dea5a14a7fb0f1072d918b38731b2eb9ca113686/pictures/login.png)

Click the bottommost login method
![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/singinmethod.png)

It request a social security number and a pin code, i recommend using the second testuser in the pdf, which has the social security number 10813049304 and the first pin code is always ajhhs. First login screen:

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/logininfo.png)

After this the login will ask for a second pin code of a certain number, these can be found at the bottom of the "test users.pdf".

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/secondcode.png)

Once you have logged on to the test network, select the top menu to log on as a user.

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/user.png)

Click on the user icon in the top right corner, and click on "Innstillinger" to access settings

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/settings.png)

Once you are on the settings page click on the bottom button, with the name "Avanserte Innstillinger".

Scroll down to the section "Innloggingsinformasjon", from here you add a special username and password which is used to login to altinn with the system, it's also important to check the bottom box, to allow systems to act on behalf of the user. If you want to use your phone to login you also add your phone number, (this is easier).

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/userloginsettings.png)

Scroll further down to the section "Registrer datasystem", to setup a system, add a name in the first box, in the second box find the Orgbrain system in the dropdown, then write a 7 letter password in the bottom two input fields.

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/systemadd.png)

Once you add the system take note of the password you set and find the system ID in the list below. Systems let you send requests to altinn.

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/systemlists.png)

Now you can use the program to interact with altinn. To use the program, first at the top of the script, enter the values you setup in altinn.

SystemUsername = ID of the created system,

SystemPassword = The password of created system,

TestuserUsername = The name of the user created in Innloggingsinformasjon,

TestuserPassword = The password,

AuthCodeType = The authorization type you want, you have to connect a phone number to use SMSPin, default is AltinnPin.

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/variableSetup.png)

Scroll to the bottom of the script, before running any other function to altinn, run sendAuthCodeToUser, this prints a code to the console which you have to use for all interaction with altinn systems. If you are using AltinnPin, it will provide a number which coresponds to a code on the testusers document. 

Use this code on all future request, example:

sendFormData(testUserUsername, testUserPassword, "codehere", 911007118)

![alt text](https://github.com/BroderViktor/Orgbrain_RF-1086/blob/6e3af14a7651ebc1d7ea6f905df5ee4d0bd62dc0/pictures/functions.png)


