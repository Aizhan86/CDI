from pages.fis.fis_page import FisPage
from pages.way4.way4_page import Way4Page
from pages.credilogic.credi_page import CredilogicPage


class TestFis:
    fis_page = FisPage()

    def test_fis_ResponseIIN(self):
        self.fis_page.check_ResponseIINAbsent()

    def test_fis_ResponseErrorStatusMessage(self):
        self.fis_page.check_ResponseErrorStatusMessage()

    def test_fis_ResponseErrorText(self):
        self.fis_page.check_ResponseErrorText()

    def test_fis_ResponseFailedField(self):
        self.fis_page.check_ResponseFailedField()

    def test_fis_ResponseStatusCode(self):
        self.fis_page.check_ResponseStatusCode()

    def test_fis_ResponseID(self):
        self.fis_page.check_ResponseID()

    def test_fis_ResponseIIN(self):
        self.fis_page.check_ResponseIIN()

    def test_fis_ResponseSuccessStatusMessage(self):
        self.fis_page.check_ResponseSuccessStatusMessage()

    def test_fis_ResponseDate(self):
        self.fis_page.check_ResponseDate()

    def test_fis_PreviousLastName(self):
        self.fis_page.check_PreviousLastName()

    def test_fis_LastName(self):
        self.fis_page.check_LastName()

    def test_fis_FirstName(self):
        self.fis_page.check_FirstName()

    def test_fis_Patronymic(self):
        self.fis_page.check_Patronymic()

    def test_fis_IIN(self):
        self.fis_page.check_IIN()

    def test_fis_Gender(self):
        self.fis_page.check_Gender()

    def test_fis_PlaceOfBirth(self):
        self.fis_page.check_PlaceOfBirth()

    def test_fis_DateOfBirth(self):
        self.fis_page.check_DateOfBirth()

    def test_fis_MobilePhoneNumber(self):
        self.fis_page.check_MobilePhoneNumber()

    def test_fis_DateOfDeath(self):
        self.fis_page.check_DateOfDeath()

    def test_fis_ResidenceCountry(self):
        self.fis_page.check_ResidenceCountry()

    def test_fis_Residence(self):
        self.fis_page.check_Residence()

    def test_fis_Education(self):
        self.fis_page.check_Education()

    def test_fis_SecretCode(self):
        self.fis_page.check_SecretCode()

    def test_fis_Email(self):
        self.fis_page.check_Email()

    def test_fis_MaritalStatus(self):
        self.fis_page.check_MaritalStatus()

    def test_fis_Citizenship(self):
        self.fis_page.check_Citizenship()

    def test_fis_DocumentId(self):
        self.fis_page.check_DocumentId()

    def test_fis_DocumentType(self):
        self.fis_page.check_DocumentType()

    def test_fis_DocumentNumber(self):
        self.fis_page.check_DocumentNumber()

    def test_fis_IssuingAuthority(self):
        self.fis_page.check_IssuingAuthority()

    def test_fis_DateOfIssue(self):
        self.fis_page.check_DateOfIssue()

    def test_fis_ExpirationDate(self):
        self.fis_page.check_ExpirationDate()

    def test_fis_RegAddressId(self):
        self.fis_page.check_RegAddressId()

    def test_fis_RegAddressType(self):
        self.fis_page.check_RegAddressType()

    def test_fis_RegAddress(self):
        self.fis_page.check_RegAddress()

    def test_fis_RegRegion(self):
        self.fis_page.check_RegRegion()

    def test_fis_RegDistrict(self):
        self.fis_page.check_RegDistrict()

    def test_fis_RegCity(self):
        self.fis_page.check_RegCity()

    def test_fis_RegStreetType(self):
        self.fis_page.check_RegStreetType()

    def test_fis_RegStreet(self):
        self.fis_page.check_RegStreet()

    def test_fis_RegHouseNumber(self):
        self.fis_page.check_RegHouseNumber()

    def test_fis_RegApartment(self):
        self.fis_page.check_RegApartment()

    def test_fis_FactAddressId(self):
        self.fis_page.check_FactAddressId()

    def test_fis_FactAddressType(self):
        self.fis_page.check_FactAddressType()

    def test_fis_FactAddress(self):
        self.fis_page.check_FactAddress()

    def test_fis_FactRegion(self):
        self.fis_page.check_FactRegion()

    def test_fis_FactDistrict(self):
        self.fis_page.check_FactDistrict()

    def test_fis_FactCity(self):
        self.fis_page.check_FactCity()

    def test_fis_FactStreetType(self):
        self.fis_page.check_FactStreetType()

    def test_fis_FactStreet(self):
        self.fis_page.check_FactStreet()

    def test_fis_FactHouseNumber(self):
        self.fis_page.check_FactHouseNumber()

    def test_fis_FactApartment(self):
        self.fis_page.check_FactApartment()

    def test_fis_ContactPersonId(self):
        self.fis_page.check_ContactPersonId()

    def test_fis_ContactPerson(self):
        self.fis_page.check_ContactPerson()

    def test_fis_RelationshipType(self):
        self.fis_page.check_RelationshipType()

    def test_fis_ContactPersonPhoneNumber(self):
        self.fis_page.check_ContactPersonPhoneNumber()

    def test_fis_EmploymentDetailsId(self):
        self.fis_page.check_EmploymentDetailsId()

    def test_fis_Organization(self):
        self.fis_page.check_Organization()

    def test_fis_BusinessArea(self):
        self.fis_page.check_BusinessArea()

    def test_fis_BIN(self):
        self.fis_page.check_BIN()

    def test_fis_Occupation(self):
        self.fis_page.check_Occupation()

class TestCredilogic:
    credi_page = CredilogicPage()

    def test_credi_ResponseStatusCode(self):
        self.credi_page.check_ResponseStatusCode()

    def test_credi_IIN(self):
        self.credi_page.check_IIN()

    def test_credi_ClientType(self):
        self.credi_page.check_ClientType()

    def test_credi_Email(self):
        self.credi_page.check_Email()

    def test_credi_AccessCode(self):
        self.credi_page.check_AccessCode()

    def test_credi_LastName(self):
        self.credi_page.check_LastName()

    def test_credi_FirstName(self):
        self.credi_page.check_FirstName()

    def test_credi_Patronymic(self):
        self.credi_page.check_Patronymic()

    def test_credi_MaidenName(self):
        self.credi_page.check_MaidenName()

    def test_credi_Gender(self):
        self.credi_page.check_Gender()

    def test_credi_PlaceOfBirth(self):
        self.credi_page.check_PlaceOfBirth()

    def test_credi_DateOfBirth(self):
        self.credi_page.check_DateOfBirth()

    def test_credi_DateOfDeath(self):
        self.credi_page.check_DateOfDeath()

    def test_credi_DateOfDeathComment(self):
        self.credi_page.check_DateOfDeathComment()

    def test_credi_iinField(self):
        self.credi_page.check_iinField()

    def test_credi_DocumentType(self):
        self.credi_page.check_DocumentType()

    def test_credi_DocumentNumber(self):
        self.credi_page.check_DocumentNumber()

    def test_credi_ExpirationDate(self):
        self.credi_page.check_ExpirationDate()

    def test_credi_DateOfIssue(self):
        self.credi_page.check_DateOfIssue()

    def test_credi_IssuingAuthority(self):
        self.credi_page.check_IssuingAuthority()

    def test_credi_ResidenceCountry(self):
        self.credi_page.check_ResidenceCountry()

    def test_credi_HomePhoneNumber(self):
        self.credi_page.check_HomePhoneNumber()

    def test_credi_MobilePhoneNumber(self):
        self.credi_page.check_MobilePhoneNumber()

    def test_credi_WorkPhoneNumber(self):
        self.credi_page.check_WorkPhoneNumber()

    def test_credi_FactRegionCode(self):
        self.credi_page.check_FactRegionCode()

    def test_credi_FactDistrictCode(self):
        self.credi_page.check_FactDistrictCode()

    def test_credi_FactCityCode(self):
        self.credi_page.check_FactCityCode()

    def test_credi_FactStreet(self):
        self.credi_page.check_FactStreet()

    def test_credi_FactStreetType(self):
        self.credi_page.check_FactStreetType()

    def test_credi_FactHouseNumber(self):
        self.credi_page.check_FactHouseNumber()

    def test_credi_FactApartment(self):
        self.credi_page.check_FactApartment()

    def test_credi_FactPostalCode(self):
        self.credi_page.check_FactPostalCode()

    def test_credi_FactSinceDate(self):
        self.credi_page.check_FactSinceDate()

    def test_credi_FactTypeOfResidence(self):
        self.credi_page.check_FactTypeOfResidence()

    def test_credi_RegRegionCode(self):
        self.credi_page.check_RegRegionCode()

    def test_credi_RegDistrictCode(self):
        self.credi_page.check_RegDistrictCode()

    def test_credi_RegCityCode(self):
        self.credi_page.check_RegCityCode()

    def test_credi_RegStreet(self):
        self.credi_page.check_RegStreet()

    def test_credi_RegStreetType(self):
        self.credi_page.check_RegStreetType()

    def test_credi_RegHouseNumber(self):
        self.credi_page.check_RegHouseNumber()

    def test_credi_RegApartment(self):
        self.credi_page.check_RegApartment()

    def test_credi_RegPostalCode(self):
        self.credi_page.check_RegPostalCode()

    def test_credi_RegSinceDate(self):
        self.credi_page.check_RegSinceDate()

    def test_credi_RegTypeOfResidence(self):
        self.credi_page.check_RegTypeOfResidence()

    def test_credi_WorkRegionCode(self):
        self.credi_page.check_WorkRegionCode()

    def test_credi_WorkDistrictCode(self):
        self.credi_page.check_WorkDistrictCode()

    def test_credi_WorkCityCode(self):
        self.credi_page.check_WorkCityCode()

    def test_credi_WorkStreet(self):
        self.credi_page.check_WorkStreet()

    def test_credi_WorkStreetType(self):
        self.credi_page.check_WorkStreetType()

    def test_credi_WorkHouseNumber(self):
        self.credi_page.check_WorkHouseNumber()

    def test_credi_WorkApartment(self):
        self.credi_page.check_WorkApartment()

    def test_credi_WorkPostalCode(self):
        self.credi_page.check_WorkPostalCode()

    def test_credi_WorkSinceDate(self):
        self.credi_page.check_WorkSinceDate()

    def test_credi_WorkTypeOfResidence(self):
        self.credi_page.check_WorkTypeOfResidence()

    def test_credi_MaritalStatus(self):
        self.credi_page.check_MaritalStatus()

    def test_credi_NumberOfChildren(self):
        self.credi_page.check_NumberOfChildren()

    def test_credi_NumberOfDependents(self):
        self.credi_page.check_NumberOfDependents()

    def test_credi_NumberOfFamilyMembers(self):
        self.credi_page.check_NumberOfFamilyMembers()

    def test_credi_Education(self):
        self.credi_page.check_Education()

    def test_credi_ContactPersonName(self):
        self.credi_page.check_ContactPersonName()

    def test_credi_ContactRelationshipType(self):
        self.credi_page.check_ContactRelationshipType()

    def test_credi_ContactPersonPhone(self):
        self.credi_page.check_ContactPersonPhone()

    def test_credi_ContactPersonMobilePhone(self):
        self.credi_page.check_ContactPersonMobilePhone()

    def test_credi_ContactPersonName2(self):
        self.credi_page.check_ContactPersonName2()

    def test_credi_ContactRelationshipType2(self):
        self.credi_page.check_ContactRelationshipType2()

    def test_credi_ContactPersonPhone2(self):
        self.credi_page.check_ContactPersonPhone2()

    def test_credi_ContactPersonMobilePhone2(self):
        self.credi_page.check_ContactPersonMobilePhone2()

    def test_credi_ContactPersonName3(self):
        self.credi_page.check_ContactPersonName3()

    def test_credi_ContactRelationshipType3(self):
        self.credi_page.check_ContactRelationshipType3()

    def test_credi_ContactPersonPhone3(self):
        self.credi_page.check_ContactPersonPhone3()

    def test_credi_ContactPersonMobilePhone3(self):
        self.credi_page.check_ContactPersonMobilePhone3()

    def test_credi_EmploymentType(self):
        self.credi_page.check_EmploymentType()

    def test_credi_EmployerName(self):
        self.credi_page.check_EmployerName()

    def test_credi_ActivitySphere(self):
        self.credi_page.check_ActivitySphere()

    def test_credi_Occupation(self):
        self.credi_page.check_Occupation()

    def test_credi_EconomicSector(self):
        self.credi_page.check_EconomicSector()

    def test_credi_ContractType(self):
        self.credi_page.check_ContractType()

    def test_credi_ContractStart(self):
        self.credi_page.check_ContractStart()

    def test_credi_BankruptcyStatus(self):
        self.credi_page.check_BankruptcyStatus()

    def test_credi_BankruptcyStatusDate(self):
        self.credi_page.check_BankruptcyStatusDate()

class TestWay4:
    way4_page = Way4Page()

    def test_way4_ResponseStatusCode(self):
        self.way4_page.check_ResponseStatusCode()

    def test_way4_ResponseIIN(self):
        self.way4_page.check_ResponseIIN()

    def test_way4_ResponseStatusMessage(self):
        self.way4_page.check_ResponseStatusMessage()

    def test_way4_ResponseDate(self):
        self.way4_page.check_ResponseDate()