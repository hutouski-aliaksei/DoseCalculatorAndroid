# Dose Calculator for Android

The Dose Calculator is a software for calculation of DER form different gamma and neutron radiation sources. This software is developed using Python 3.11.11, QML 6.8.1 and SQLite3.

[Desktop version GitHub](https://github.com/hutouski-aliaksei/DoseCalculatorModern)

The Dose Calculator has two different modes, there are:
1.	DER calculation with known source, distance and shielding.
2.	Distance calculation with known DER, source and shielding.

Kerma calculated from photons flux using ICRP PUBLICATION 119, Annex I.
For kerma-to-dose conversion used standard ISO 4037-3:2019, Table 14.
Neutron fluence-to-dose coefficients from ISO 8529-1:2001, Table 1.
For attenuation calculations used data from NIST (https://www.nist.gov/pml/x-ray-mass-attenuation-coefficients).
 
## 1.	DER calculation

![Screenshot_20241222_202919_DoseCalculator](https://github.com/user-attachments/assets/aac59901-82ff-4684-a4d8-793c6daa976b)

***

  1.	You can choose an existing source from “Source catalogue”. All source parameters will be automatically filled in corresponding fields: half-life, production date, original activity. Current activity for current date will be also calculated.
  2.	It is also possible to fill all fields manually, except half-life, it loads from database in correspondence with the source chosen.
  3.	All changes in source parameters will entail recalculation of current activity.
  4.	In the list Material you can chose shielding material. If there is no any shielding you should select Air. Air shielding applied automatically, distance for air shield is calculated as difference between distance to the source and thickness of the shield.
  5.	In the Thickness field it is possible to enter the thickness of the shield in centimeters.
  6.	Field Distance is for the distance from the source in centimeters.
  7.	Using list Dose type you can choose ambient (H*) or personal (Hp10) dose rate.
  8.	All changes in Shield parameters section will entail to recalculation of DER and Flux.
  9.	There are data about calculated DER and Flux in the right top corner of the software.
  10.	In the right bottom corner, there are data about gamma lines, yields, DERs and fluxes of corresponding lines.
 
## 2.	Distance calculation with known DER

  1.	For distance calculation you need at first to fill all data about the source.
  2.	Then enter desired DER in µSv/h in the field Desired DER. You must enter the value slowly, number by number, because calculation may take some time. Calculation process is accompanied by animation.
  3.	After calculation is finished necessary distance will be shown in the field Distance in centimeters.
 
