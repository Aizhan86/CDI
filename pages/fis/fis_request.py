from pages import values

req = {"ClientId": values.fis_id,
  "PreviousLastName": values.prezhnjaja_familija,
  "LastName": values.familija,
  "FirstName": values.imja,
  "Patronymic": values.otchestvo,
  "IIN": values.iin,
  "Gender": values.fisGender,
  "PlaceOfBirth": values.gorod,
  "DateOfBirth": values.data_rozhdenija,
  "MobilePhoneNumber": values.phone,
  "DateOfDeath": values.today.strftime('%Y-%m-%d'),
  "ResidenceCountry": values.strana,
  "Residence": values.rezident,
  "Education": values.fisObrazovanie,
  "SecretCode": values.kodovoe_slovo,
  "Email": values.email,
  "MaritalStatus": values.fisSemejnoe_polozhenie,
  "Citizenship": values.strana,
 "Documents": [{
      "DocumentId": values.document_id,
      "DocumentType": values.fisTipDokumenta,
      "DocumentNumber": values.nomer,
      "IssuingAuthority": values.fisOrganVydachi,
      "DateOfIssue": values.data_vydachi,
      "ExpirationDate": values.srok_dejstvija.strftime('%Y-%m-%d')
    }
], "Addresses": [{
      "AddressId": values.fact_address_id,
      "AddressType": "фактический_адрес",
      "Address": values.nazvanie_strany,
      "Region": values.nazvanie_regiona,
      "District": values.rajon_oblasti,
      "City": values.gorod,
      "StreetType": values.tip_ulicy,
      "Street": values.ulica,
      "HouseNumber": values.nomer_doma,
      "Apartment": values.nomer_kvartiry
      },
{
      "AddressId": values.reg_address_id,
      "AddressType": "адрес_регистрации",
      "Address": values.nazvanie_strany,
      "Region": values.fisNazvanie_regiona,
      "District": values.rajon_oblasti,
      "City": values.gorod,
      "StreetType": values.tip_ulicy,
      "Street": values.ulica,
      "HouseNumber": values.nomer_doma,
      "Apartment": values.nomer_kvartiry
}], "ContactPersons": [{
      "ContactPersonId": values.contact_id,
      "ContactPerson": values.kontaktnoe_lico1,
      "RelationshipType": values.tip_otnoshenija,
      "ContactPersonPhoneNumber": values.contact_person1_mphone
    }
], "EmploymentDetails": {
    "EmploymentDetailsId": values.employment_id,
    "Organization": values.naimenovanie_rabotodatelja,
    "BusinessArea": values.sfera_dejatelnosti,
    "BIN": values.bin_organizacii,
    "Occupation": values.rod_zanjatosti
  }
}


failed_req = {"ClientId": '',
  "PreviousLastName": values.prezhnjaja_familija,
  "LastName": '',
  "FirstName": '',
  "Patronymic": values.otchestvo,
  "IIN": '',
  "Gender": '',
  "PlaceOfBirth": '',
  "DateOfBirth": '',
  "MobilePhoneNumber": values.phone,
  "DateOfDeath": values.today.strftime('%Y-%m-%d'),
  "ResidenceCountry": '',
  "Residence": '',
  "Education": '',
  "SecretCode": values.kodovoe_slovo,
  "Email": values.email,
  "MaritalStatus": '',
  "Citizenship": '',
 "Documents": [{
      "DocumentId": '',
      "DocumentType": values.fisTipDokumenta,
      "DocumentNumber": values.nomer,
      "IssuingAuthority": values.fisOrganVydachi,
      "DateOfIssue": values.data_vydachi,
      "ExpirationDate": values.srok_dejstvija.strftime('%Y-%m-%d')
    }
], "Addresses": [{
      "AddressId": '',
      "AddressType": "фактический_адрес",
      "Address": values.nazvanie_strany,
      "Region": values.nazvanie_regiona,
      "District": values.rajon_oblasti,
      "City": values.gorod,
      "StreetType": values.tip_ulicy,
      "Street": values.ulica,
      "HouseNumber": values.nomer_doma,
      "Apartment": values.nomer_kvartiry
      },
{
      "AddressId": '',
      "AddressType": "адрес_регистрации",
      "Address": values.nazvanie_strany,
      "Region": values.fisNazvanie_regiona,
      "District": values.rajon_oblasti,
      "City": values.gorod,
      "StreetType": values.tip_ulicy,
      "Street": values.ulica,
      "HouseNumber": values.nomer_doma,
      "Apartment": values.nomer_kvartiry
}], "ContactPersons": [{
      "ContactPersonId": '',
      "ContactPerson": values.kontaktnoe_lico1,
      "RelationshipType": values.tip_otnoshenija,
      "ContactPersonPhoneNumber": values.contact_person1_mphone
    }
], "EmploymentDetails": {
    "EmploymentDetailsId": '',
    "Organization": values.naimenovanie_rabotodatelja,
    "BusinessArea": values.sfera_dejatelnosti,
    "BIN": values.bin_organizacii,
    "Occupation": values.rod_zanjatosti
  }
}
