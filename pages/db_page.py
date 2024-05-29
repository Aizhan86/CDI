import json
import requests
import os
import pyodbc
import psycopg2
import cx_Oracle
class BasePage(object):
    def __init__(self):
        super().__init__()  # Call superclass __init__ method
        # self.config()
        # self.execute_query()
        # self.get_id()
        # self.get_fis_client_data()
        # self.get_credi_client_data()

    def execute_query(self, driver, conn_info, sql_query):
        if driver == "mssql":
            conn = pyodbc.connect(conn_info)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            columns = [column[0] for column in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return data
        elif driver == "postgres":
            conn = psycopg2.connect(**conn_info)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            columns = [desc[0] for desc in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return data
        elif driver == "oracle":
            conn = cx_Oracle.connect(conn_info)
            cursor = conn.cursor()
            cursor.execute(sql_query)
            columns = [desc[0] for desc in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return data
        else:
            raise ValueError("Unsupported driver")


    def config(self, conf):
        # Определяем путь к файлу database_config.json
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        json_file_path = os.path.join(parent_dir, 'database_config.json')

        # Чтение данных из JSON файла
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        config = data[f'{conf}']
        return config

    # Загрузка информации о базах данных из JSON-файла
    # with open("../database_config.json") as f:
    #     config = json.load(f)

    # Для MS SQL Server
    # mssql_conn_string = 'DRIVER={SQL Server};SERVER=server_name;DATABASE=database_name;UID=username;PWD=password'
    # mssql_sql_query = 'SELECT * FROM your_table'
    # mssql_data = execute_query("mssql", mssql_conn_string, mssql_sql_query)

    # Для FIS
    def get_id(self, id, document_type):
        fis_id_query = f"SELECT get_client_id('{id}', '{document_type}');"
        fis_id_data = self.execute_query("postgres", self.config("fisDB"), fis_id_query)
        client_id_data = fis_id_data[0]['get_client_id'][0]
        return client_id_data

    def print(self):
        fis_id_data = self.get_id(866936)
        print(fis_id_data)

    def get_fis_client_data(self, id, document_type):
        fis_client_query = f"SELECT * FROM get_client_data('{id}', '{document_type}')"
        fis_client_data = self.execute_query("postgres", self.config("fisDB"), fis_client_query)
        client_data_list = fis_client_data[0]['get_client_data']
        client_data = {}
        for data in client_data_list:
            client_data.update(data)
        return client_data


    # client_data = get_client_data(866936)
    # print(client_data)

    # Для Credilogic
    def get_credi_client_data(self, id):
        cl_query = f"""
            select 
        ap.customer_id, 
        ap.iin, 
        ap.client_type_id,
        ap.access_code, 
        ap.email, 
        ap.surname, 
        ap.firstname, 
        ap.patronymic,
        ap.birth_full_name,
        ap.sex_id,
        ap.placebirth,
        ap.birth_date,
        ap.date_of_death,
        ap.date_of_death_comment,
        aid.type,
        aid.nr,
        aid.issue_date,
        aid.expiration_date,
        aid.issuer,
        aid.country_of_residence,
        addr_dp.PHONE_NUMBER as home_phone,
        addr_mp.PHONE_NUMBER as mobile_phone,
        addr_wp.PHONE_NUMBER as work_phone,
        addr_fact.region_id as fact_region_id, 
        addr_fact.district_id as fact_district_id, 
        addr_fact.city_id as fact_city_id, 
        addr_fact.street as fact_street, 
        addr_fact.street_type as fact_street_type, 
        addr_fact.building as fact_building, 
        addr_fact.appartment as fact_appartment, 
        addr_fact.postal_code as fact_postal_code, 
        addr_fact.since as fact_since, 
        addr_fact.residence_type as fact_residence_type,
        addr_reg.region_id as reg_region_id, 
        addr_reg.district_id as reg_district_id, 
        addr_reg.city_id as reg_city_id, 
        addr_reg.street as reg_street, 
        addr_reg.street_type as reg_street_type, 
        addr_reg.building as reg_building, 
        addr_reg.appartment as reg_appartment, 
        addr_reg.postal_code as reg_postal_code, 
        addr_reg.since as reg_since, 
        addr_reg.residence_type as reg_residence_type,
        addr_work.region_id as work_region_id, 
        addr_work.district_id as work_district_id, 
        addr_work.city_id as work_city_id, 
        addr_work.street as work_street, 
        addr_work.street_type as work_street_type, 
        addr_work.building as work_building, 
        addr_work.appartment as work_appartment, 
        addr_work.postal_code as work_postal_code, 
        addr_work.since as work_since, 
        addr_work.residence_type as work_residence_type,
        ap.maritalstatus_id,
        ap.nb_children,
        ap.nb_of_dependents,
        ap.nb_of_family_members,
        ap.education_id,
        ap.contact_fullname,
        ap.contact_relationship,
        addr_cp1.PHONE_NUMBER as contact_phone,
        addr_mp1.PHONE_NUMBER as contact_mobile_phone,
        ap.contact_fullname2,
        ap.contact_relationship2,
        addr_cp2.PHONE_NUMBER as contact_phone2,
        addr_mp2.PHONE_NUMBER as contact_mobile_phone2,
        ap.contact_fullname3,
        ap.contact_relationship3,
        addr_cp3.PHONE_NUMBER as contact_phone3,
        addr_mp3.PHONE_NUMBER as contact_mobile_phone3,
        ap.employment_status_code,
        ap.employer_name,
        ap.employer_activity_code,
        ap.occupation_code,
        ap.economic_sector,
        ap.employment_contract_type,
        ap.employment_contract_start,
        ap.bankruptcy_status,
        ap.bankruptcy_status_date
         
        from credilogic.ath_person ap
        
        left join credilogic.ath_id_documents aid on ap.customer_id = aid.id_documents_id
        
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE mphone on mphone.CUSTOMER_ID = ap.CUSTOMER_ID and mphone.ADDRESS_USE_TYPE='CUST_MOBILE_PHONE'
        left join CREDILOGIC.ATH_ADDRESS addr_mp on addr_mp.ADDRESS_ID = mphone.ADDRESS_ID
         
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE dphone on dphone.CUSTOMER_ID = ap.CUSTOMER_ID and dphone.ADDRESS_USE_TYPE='CUST_HOME_PHONE'
        left join CREDILOGIC.ATH_ADDRESS addr_dp on addr_dp.ADDRESS_ID = dphone.ADDRESS_ID
         
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE wphone on wphone.CUSTOMER_ID = ap.CUSTOMER_ID and wphone.ADDRESS_USE_TYPE='CUST_WORK_PHONE'
        left join CREDILOGIC.ATH_ADDRESS addr_wp on addr_wp.ADDRESS_ID = wphone.ADDRESS_ID
        
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE faddrs on faddrs.CUSTOMER_ID = ap.CUSTOMER_ID and faddrs.ADDRESS_USE_TYPE='CUST_LIVING_ADDRESS'
        left join CREDILOGIC.ATH_ADDRESS addr_fact on addr_fact.ADDRESS_ID = faddrs.ADDRESS_ID
         
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE raddrs on raddrs.CUSTOMER_ID = ap.CUSTOMER_ID and raddrs.ADDRESS_USE_TYPE='CUST_REGISTRATIONAL_ADDRESS'
        left join CREDILOGIC.ATH_ADDRESS addr_reg on addr_reg.ADDRESS_ID = raddrs.ADDRESS_ID
         
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE waddrs on waddrs.CUSTOMER_ID = ap.CUSTOMER_ID and waddrs.ADDRESS_USE_TYPE='CUST_WORK_ADDRESS'
        join CREDILOGIC.ATH_ADDRESS addr_work on addr_work.ADDRESS_ID = waddrs.ADDRESS_ID
        
        
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE cphone1 on cphone1.CUSTOMER_ID = ap.CUSTOMER_ID and cphone1.ADDRESS_USE_TYPE='CUST_CONTACT_PHONE'
        left join CREDILOGIC.ATH_ADDRESS addr_cp1 on addr_cp1.ADDRESS_ID = cphone1.ADDRESS_ID
          
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE mphone1 on mphone1.CUSTOMER_ID = ap.CUSTOMER_ID and mphone1.ADDRESS_USE_TYPE='CUST_CONTACT_MOBILE_PHONE'
        left join CREDILOGIC.ATH_ADDRESS addr_mp1 on addr_mp1.ADDRESS_ID = mphone1.ADDRESS_ID
        
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE cphone2 on cphone2.CUSTOMER_ID = ap.CUSTOMER_ID and cphone2.ADDRESS_USE_TYPE='CUST_CONTACT_PHONE_2'
        left join CREDILOGIC.ATH_ADDRESS addr_cp2 on addr_cp2.ADDRESS_ID = cphone2.ADDRESS_ID
          
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE mphone2 on mphone2.CUSTOMER_ID = ap.CUSTOMER_ID and mphone2.ADDRESS_USE_TYPE='CUST_CONTACT_MOBILE_PHONE_2'
        left join CREDILOGIC.ATH_ADDRESS addr_mp2 on addr_mp2.ADDRESS_ID = mphone2.ADDRESS_ID
        
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE cphone3 on cphone3.CUSTOMER_ID = ap.CUSTOMER_ID and cphone3.ADDRESS_USE_TYPE='CUST_CONTACT_PHONE_3'
        left join CREDILOGIC.ATH_ADDRESS addr_cp3 on addr_cp3.ADDRESS_ID = cphone3.ADDRESS_ID
          
        left join CREDILOGIC.ATH_CUSTOMER_ADDRESS_USE mphone3 on mphone3.CUSTOMER_ID = ap.CUSTOMER_ID and mphone3.ADDRESS_USE_TYPE='CUST_CONTACT_MOBILE_PHONE_3'
        left join CREDILOGIC.ATH_ADDRESS addr_mp3 on addr_mp3.ADDRESS_ID = mphone3.ADDRESS_ID 
        
        where ap.customer_id = '{id}' 
        """

        cl_data = self.execute_query("oracle", self.config("credilogicDB"), cl_query)
        return cl_data


    # def print(self):
    #     credi_client_data = self.get_credi_client_data(943670256)
    #     print(credi_client_data)





    # Для RSBank
    def get_rs_client_data(self, id, address_type):
        rs_query = f"""
        select dp.t_partyid, 
do.t_code as iin, 
dd.t_ismale, 
dd.t_name1, 
dd.t_name2, 
dd.t_name3, 
dd.t_birsplase, 
dc.t_value, 
dd.t_born, 
dd.t_death, 
dp.t_nrcountry,
nvl(uc.t_code, null) as codeword, 
dp.t_notresident, 
dp.t_branch, 
dp.t_legalform, 
zz.t_paperkind, 
zz.t_paperseries, 
zz.t_papernumber, 
zz.t_paperissuer, 
zz.t_paperissueddate, 
zz.t_validtodate, 
da.t_type as addresstype, 
da.t_country, 
da.t_okato, 
da.t_regionnum, 
da.t_coderegion, 
da.t_region, 
da.t_codeprovince, 
da.t_province, 
da.t_codedistrict, 
da.t_district, 
da.t_codeplace, 
da.t_place, 
da.t_codestreet, 
da.t_street, 
da.t_house, 
da.t_flat, 
da.t_postindex, 
da.t_adress,
dc.t_contacttype
from dpersn_dbt dd, dparty_dbt dp, dpersnidc_dbt zz, dadress_dbt da, dcontact_dbt dc, dobjcode_dbt do, usr_code_word_dbt uc
where dp.t_partyid = dd.T_PERSONID 
and dp.t_partyid = zz.T_PERSONID 
and dp.t_partyid = da.t_partyid 
and dp.t_partyid = dc.t_partyid
and dp.t_partyid = do.t_objectid
and dp.t_partyid = uc.t_partyid
and do.t_codekind = 16 
and dp.t_partyid = '{id}'
and da.t_type = '{address_type}'
        """
        rs_data = self.execute_query("oracle", self.config("rsDB"), rs_query)
        return rs_data

    def print(self):
        rs_client_data = self.get_rs_client_data(943670256, 2)
        print(rs_client_data)
    # # Выводим результаты
    # # print("MS SQL Server data:")
    # # for row in mssql_data:
    # #     print(row)
    #
    # print("FIS data:")
    # for row in fis_client_data:
    #     print(row)
    #
    # print("Credilogic data:")
    # for row in cl_data:
    #     print(row)
    #
    # print("RSBank data:")
    # for row in rs_data:
    #     print(row)