import time
import requests
from pages.fis import fis_request
from pages.db_page import BasePage
from pages import values
import json
from datetime import datetime
from pages import config

class FisPage(BasePage):

    print('fis_request:')
    print(fis_request.req)

    # test 'failed field'
    response_err = requests.put(url=config.url_fis, json=fis_request.failed_req, verify=False)
    response_err_dict = json.loads(response_err.text)
    print("response " + str(response_err.status_code) + " : " + response_err.text)

    def check_ResponseIINAbsent(self):
        assert self.response_err_dict['iin'] == '', "IIN field failed in response"

    def check_ResponseErrorStatusMessage(self):
        assert self.response_err_dict['status'] == "error", f"Error status message has not received: {self.response_err_dict['status']}"

    def check_ResponseErrorText(self):
        assert self.response_err_dict['error_text'] == "not valid JSON", f"Error text incorrect: {self.response_err_dict['error_text']}"

    def check_ResponseFailedField(self):
        mandatory_fields = ['ClientId', 'LastName', 'FirstName', 'IIN', 'Gender', 'PlaceOfBirth', 'DateOfBirth', 'ResidenceCountry', 'Residence', 'Education', 'MaritalStatus', 'Citizenship', 'EmploymentDetailsId', 'DocumentId', 'ContactPersonId', 'AddressId', 'AddressId']
        assert sorted(self.response_err_dict['failed_fields'].strip('[]').split(',')) == sorted(mandatory_fields), f"List of failed fields differs from the list of mandatory fields: {self.response_err_dict['failed_fields'].strip('[]').split(',')}"

    #success case
    response = requests.put(url=url, json=fis_request.req, verify=False)
    response_dict = json.loads(response.text)
    print("response " + str(response.status_code) + " : " + response.text)
    def check_ResponseStatusCode(self):
        assert self.response.status_code == 200, f"Response error status code received: {self.response.status_code}"

    def check_ResponseID(self):
        assert self.response_dict['id'] == fis_request.req['ClientId'], f"Invalid ClientId: {self.response_dict['id']}"

    def check_ResponseIIN(self):
        assert self.response_dict['iin'] == fis_request.req['IIN'], f"Invalid IIN: {self.response_dict['iin']}"

    def check_ResponseSuccessStatusMessage(self):
        assert self.response_dict['status'] == "success", f"Error status message received: {self.response_dict['status']}"

    def check_ResponseDate(self):
        response_date = datetime.strptime(self.response_dict['date_time'], '%d.%m.%Y %H:%M:%S').strftime('%Y-%m-%d')
        assert response_date == values.today.strftime('%Y-%m-%d'), f"Invalid Response Date: {response_date}"

    time.sleep(10)

    db_page = BasePage()
    client_data_list = db_page.get_fis_client_data(values.fis_id, values.fisTipDokumenta)
    
    def check_PreviousLastName(self):
        assert fis_request.req['PreviousLastName'] == self.client_data_list['prezhnjaja_familija'], 'PreviousLastName has not changed'
    def check_LastName(self):
        assert fis_request.req['LastName'] == self.client_data_list['familija'], 'LastName has not changed'
    def check_FirstName(self):
        assert fis_request.req['FirstName'] == self.client_data_list['imja'], 'FirstName has not changed'
    def check_Patronymic(self):
        assert fis_request.req['Patronymic'] == self.client_data_list['otchestvo'], 'Patronymic has not changed'
    def check_IIN(self):
        assert fis_request.req['IIN'] == self.client_data_list['iin'], 'IIN has not changed'
    def check_Gender(self):
        assert fis_request.req['Gender'] == self.client_data_list['pol'], 'Gender has not changed'
    def check_PlaceOfBirth(self):
        assert fis_request.req['PlaceOfBirth'] == self.client_data_list['mesto_rozhdenija'], 'PlaceOfBirth has not changed'
    def check_DateOfBirth(self):
        assert fis_request.req['DateOfBirth'] == self.client_data_list['data_rozhdenija'], 'DateOfBirth has not changed'
    def check_MobilePhoneNumber(self):
        assert fis_request.req['MobilePhoneNumber'] == self.client_data_list['phone'], 'MobilePhoneNumber has not changed'
    def check_DateOfDeath(self):
        assert fis_request.req['DateOfDeath'] == self.client_data_list['data_smerti'], 'DateOfDeath has not changed'
    def check_ResidenceCountry(self):
        assert fis_request.req['ResidenceCountry'] == self.client_data_list['strana_rezidentstva'], 'ResidenceCountry has not changed'
    def check_Residence(self):
        assert str(fis_request.req['Residence']) == str(self.client_data_list['rezident']), 'Residence has not changed'
    def check_Education(self):
        assert fis_request.req['Education'] == self.client_data_list['obrazovanie'], 'Education has not changed'
    def check_SecretCode(self):
        assert fis_request.req['SecretCode'] == self.client_data_list['kodovoe_slovo'], 'SecretCode has not changed'
    def check_Email(self):
        assert fis_request.req['Email'] == self.client_data_list['email'], 'Email has not changed'
    def check_MaritalStatus(self):
        assert fis_request.req['MaritalStatus'] == self.client_data_list['semejnoe_polozhenie'], 'MaritalStatus has not changed'
    def check_Citizenship(self):
        assert fis_request.req['Citizenship'] == self.client_data_list['strana_rezidentstva'], 'Citizenship has not changed'
    def check_DocumentId(self):
        assert fis_request.req['Documents'][0]['DocumentId'] == self.client_data_list['document_id'], 'DocumentId has not changed'
    def check_DocumentType(self):
        assert fis_request.req['Documents'][0]['DocumentType'] == self.client_data_list['tip_dokumenta'], 'DocumentType has not changed'
    def check_DocumentNumber(self):
        assert fis_request.req['Documents'][0]['DocumentNumber'] == self.client_data_list['nomer'], 'DocumentNumber has not changed'
    def check_IssuingAuthority(self):
        assert fis_request.req['Documents'][0]['IssuingAuthority'] == self.client_data_list['organ_vydachi'], 'IssuingAuthority has not changed'
    def check_DateOfIssue(self):
        assert fis_request.req['Documents'][0]['DateOfIssue'] == self.client_data_list['data_vydachi'], 'DateOfIssue has not changed'
    def check_ExpirationDate(self):
        assert fis_request.req['Documents'][0]['ExpirationDate'] == self.client_data_list['srok_dejstvija'], 'ExpirationDate has not changed'
    def check_RegAddressId(self):
        assert fis_request.req['Addresses'][1]['AddressId'] == self.client_data_list['reg_address_id'], 'RegAddressId has not changed'
    def check_RegAddressType(self):
        assert fis_request.req['Addresses'][1]['AddressType'] == self.client_data_list['reg_tip_adresa'], 'RegAddressType has not changed'
    def check_RegAddress(self):
        assert fis_request.req['Addresses'][1]['Address'] == self.client_data_list['reg_nazvanie_strany'], 'RegAddress has not changed'
    def check_RegRegion(self):
        assert fis_request.req['Addresses'][1]['Region'] == self.client_data_list['reg_nazvanie_regiona'], 'RegRegion has not changed'
    def check_RegDistrict(self):
        assert fis_request.req['Addresses'][1]['District'] == self.client_data_list['reg_rajon_oblasti'], 'RegDistrict has not changed'
    def check_RegCity(self):
        assert fis_request.req['Addresses'][1]['City'] == self.client_data_list['reg_gorod'], 'RegCity has not changed'
    def check_RegStreetType(self):
        assert fis_request.req['Addresses'][1]['StreetType'] == self.client_data_list['reg_tip_ulicy'], 'RegStreetType has not changed'
    def check_RegStreet(self):
        assert fis_request.req['Addresses'][1]['Street'] == self.client_data_list['reg_ulica'], 'RegStreet has not changed'
    def check_RegHouseNumber(self):
        assert fis_request.req['Addresses'][1]['HouseNumber'] == self.client_data_list['reg_nomer_doma'], 'RegHouseNumber has not changed'
    def check_RegApartment(self):
        assert fis_request.req['Addresses'][1]['Apartment'] == self.client_data_list['reg_nomer_kvartiry'], 'RegApartment has not changed'
    def check_FactAddressId(self):
        assert fis_request.req['Addresses'][0]['AddressId'] == self.client_data_list['fact_address_id'], 'FactAddressId has not changed'
    def check_FactAddressType(self):
        assert fis_request.req['Addresses'][0]['AddressType'] == self.client_data_list['fact_tip_adresa'], 'FactAddressType has not changed'
    def check_FactAddress(self):
        assert fis_request.req['Addresses'][0]['Address'] == self.client_data_list['fact_nazvanie_strany'], 'FactAddress has not changed'
    def check_FactRegion(self):
        assert fis_request.req['Addresses'][0]['Region'] == self.client_data_list['fact_nazvanie_regiona'], 'FactRegion has not changed'
    def check_FactDistrict(self):
        assert fis_request.req['Addresses'][0]['District'] == self.client_data_list['fact_rajon_oblasti'], 'FactDistrict has not changed'
    def check_FactCity(self):
        assert fis_request.req['Addresses'][0]['City'] == self.client_data_list['fact_gorod'], 'FactCity has not changed'
    def check_FactStreetType(self):
        assert fis_request.req['Addresses'][0]['StreetType'] == self.client_data_list['fact_tip_ulicy'], 'FactStreetType has not changed'
    def check_FactStreet(self):
        assert fis_request.req['Addresses'][0]['Street'] == self.client_data_list['fact_ulica'], 'FactStreet has not changed'
    def check_FactHouseNumber(self):
        assert fis_request.req['Addresses'][0]['HouseNumber'] == self.client_data_list['fact_nomer_doma'], 'FactHouseNumber has not changed'
    def check_FactApartment(self):
        assert fis_request.req['Addresses'][0]['Apartment'] == self.client_data_list['fact_nomer_kvartiry'], 'FactApartment has not changed'
    def check_ContactPersonId(self):
        assert fis_request.req['ContactPersons'][0]['ContactPersonId'] == self.client_data_list['contact_id'], 'ContactPersonId has not changed'
    def check_ContactPerson(self):
        assert fis_request.req['ContactPersons'][0]['ContactPerson'] == self.client_data_list['kontaktnoe_lico'], 'ContactPerson has not changed'
    def check_RelationshipType(self):
        assert fis_request.req['ContactPersons'][0]['RelationshipType'] == self.client_data_list['tip_otnoshenija'], 'RelationshipType has not changed'
    def check_ContactPersonPhoneNumber(self):
        assert fis_request.req['ContactPersons'][0]['ContactPersonPhoneNumber'] == self.client_data_list['contact_person_phone'], 'ContactPersonPhoneNumber has not changed'
    def check_EmploymentDetailsId(self):
        assert fis_request.req['EmploymentDetails']['EmploymentDetailsId'] == self.client_data_list['employment_id'], 'EmploymentDetailsId has not changed'
    def check_Organization(self):
        assert fis_request.req['EmploymentDetails']['Organization'] == self.client_data_list['naimenovanie_rabotodatelja'], 'Organization has not changed'
    def check_BusinessArea(self):
        assert fis_request.req['EmploymentDetails']['BusinessArea'] == self.client_data_list['sfera_dejatelnosti'], 'BusinessArea has not changed'
    def check_BIN(self):
        assert fis_request.req['EmploymentDetails']['BIN'] == self.client_data_list['bin_organizacii'], 'BIN has not changed'
    def check_Occupation(self):
        assert fis_request.req['EmploymentDetails']['Occupation'] == self.client_data_list['rod_zanjatosti'], 'Occupation has not changed'

print('Residence:')
print(fis_request.req['Residence'])
print(str(FisPage().client_data_list['rezident']))


