# Unofficial Creditsafe Connect API Documentation
-- generated from `https://raw.githubusercontent.com/creditsafe/connect-docs/master/cs_connectv1-15.json`
Last Updated: 09th July 2024

## Introduction
Creditsafe Connect is a REST API that provides access to the Creditsafe Global Company Database. The API enables you to:
- Control your master data
- Utilize up-to-date Business and Director information
- Enhance onboarding and qualification processes
- Receive alerts when customer's and supplier's Credit Report changes

## Quick Start Guide
1. Activate your account using the instructions in your Welcome Email
2. By default, you'll be set up on the Sandbox environment
3. Construct an `/authenticate` POST request with your username & password
4. Use the returned `authentication token` in the `Authorization` header for all subsequent calls

## Environments
- Production: `https://connect.creditsafe.com/v1`
- Sandbox: `https://connect.sandbox.creditsafe.com/v1`

## API Details
- API Version: 1.10.4
- Package Version: 1.0.0
- Generated using: Swagger Codegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pycsapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pycsapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

## How to use

This guide demonstrates how to connect, authenticate, and make API calls to search for companies and retrieve credit reports using the `pycsapi` library.

### Prerequisites

Make sure you have the `pycsapi` library installed. If not, you can install it using:
```bash
python setup.py install
```

---

### Step 1: Set Up Configuration

Set up the configuration with the API endpoint and your credentials.

```python
from pycsapi import Configuration

# Configure the API host and your credentials
configuration = Configuration()
configuration.host = "https://connect.sandbox.creditsafe.com/v1"
configuration.username = "your_username"  # Replace with your username
configuration.password = "your_password"  # Replace with your password
```

---

### Step 2: Authenticate and Retrieve Access Token

Use the `AuthenticationApi` to authenticate and get an access token.

```python
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint

# Authenticate and retrieve the token
try:
    api_instance = pycsapi.AuthenticationApi(pycsapi.ApiClient(configuration))
    body = pycsapi.ConnectAuthenticationAuthRequest(
        username=configuration.username,
        password=configuration.password
    )
    api_response = api_instance.authenticate(body=body)
    pprint(api_response)
    
    # Set the API key (token) for subsequent requests
    configuration.api_key["accessToken"] = api_response.token
    configuration.api_key_prefix["accessToken"] = "Bearer"
except ApiException as e:
    print(f"Exception when calling AuthenticationApi->authenticate: {e}\n")
```


### Step 3: Perform a Company Search

Use the `CompaniesApi` to search for companies by VAT number and country code.

```python
try:
    # Create an instance of the Companies API
    companies_api = pycsapi.CompaniesApi(pycsapi.ApiClient(configuration))
    
    # Search for a company
    companies = companies_api.company_search(
        countries="IT",  # Country code
        vat_no="example_vat_number"  # Replace with actual VAT number
    )
    print("Company Search Result:")
    pprint(companies)
except ApiException as e:
    print(f"Exception when calling CompaniesApi: {e}\n")
```


### Step 4: Retrieve a Company Credit Report

Once a company is found, you can fetch its credit report using the company ID.

```python
try:
    # Check if companies are found and retrieve the first one
    if companies and "companies" in companies:
        company = companies["companies"][0]
        company_id = company["id"]
        
        # Get the credit report for the company
        credit_report = companies_api.company_credit_report(company_id)
        print("Credit Report:")
        pprint(credit_report)
    else:
        print("No companies found for the given VAT number.")
except ApiException as e:
    print(f"Exception when calling CompaniesApi: {e}\n")
```

## Documentation for API Endpoints

All URIs are relative to *https://connect.creditsafe.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**authenticate**](docs/AuthenticationApi.md#authenticate) | **POST** /authenticate | Authenticate
*BankMatchApi* | [**bank_match**](docs/BankMatchApi.md#bank_match) | **GET** /localSolutions/GB/bankmatch | Bank Match
*BankVerificationApi* | [**bank_verification_get_history_by_id**](docs/BankVerificationApi.md#bank_verification_get_history_by_id) | **GET** /localSolutions/GB/bankVerification/history/{id} | Returns Request History By ID
*BankVerificationApi* | [**bank_verification_get_history_list**](docs/BankVerificationApi.md#bank_verification_get_history_list) | **GET** /localSolutions/GB/bankVerification/history | Requests Search History
*BankVerificationApi* | [**bank_verification_search**](docs/BankVerificationApi.md#bank_verification_search) | **POST** /localSolutions/GB/bankVerification/search | Single Request
*BankVerificationApi* | [**bank_verification_update_history**](docs/BankVerificationApi.md#bank_verification_update_history) | **PATCH** /localSolutions/GB/bankVerification/history/{id}/reference | Update CustomerReference by HistoryId
*BankVerificationApi* | [**bank_verification_validate**](docs/BankVerificationApi.md#bank_verification_validate) | **POST** /localSolutions/GB/bankVerification/validate/{id} | Validate Bank Verification Request
*CompaniesApi* | [**company_credit_report**](docs/CompaniesApi.md#company_credit_report) | **GET** /companies/{connectId} | Company Credit Report
*CompaniesApi* | [**company_search**](docs/CompaniesApi.md#company_search) | **GET** /companies | Company Search
*CompaniesApi* | [**company_search_criteria**](docs/CompaniesApi.md#company_search_criteria) | **GET** /companies/searchcriteria | Company Search Criteria
*CompaniesApi* | [**confidence_match_search**](docs/CompaniesApi.md#confidence_match_search) | **GET** /companies/match | Confidence Match Search
*ConsumersApi* | [**consumer_report**](docs/ConsumersApi.md#consumer_report) | **GET** /consumers | Consumer Report
*ConsumersApi* | [**consumer_search_criteria**](docs/ConsumersApi.md#consumer_search_criteria) | **GET** /consumers/searchcriteria | Consumer Search Criteria
*DCCreateAndViewAllJobsApi* | [**create_job**](docs/DCCreateAndViewAllJobsApi.md#create_job) | **POST** /dataCleaning/jobs | Create Job Request
*DCCreateAndViewAllJobsApi* | [**get_all_jobs**](docs/DCCreateAndViewAllJobsApi.md#get_all_jobs) | **GET** /dataCleaning/jobs | Returns all Data Cleaning Jobs
*DCIndividualJobManagementApi* | [**archive_job**](docs/DCIndividualJobManagementApi.md#archive_job) | **POST** /dataCleaning/jobs/{id}/archive | Archive Job by id
*DCIndividualJobManagementApi* | [**data_cleaning_job_enrich**](docs/DCIndividualJobManagementApi.md#data_cleaning_job_enrich) | **POST** /dataCleaning/jobs/{id}/enrich | Start Enrichment Request
*DCIndividualJobManagementApi* | [**get_job_by_id_number**](docs/DCIndividualJobManagementApi.md#get_job_by_id_number) | **GET** /dataCleaning/jobs/{id} | Returns Job by {id} number
*DCIndividualJobManagementApi* | [**job_file_upload_with_id**](docs/DCIndividualJobManagementApi.md#job_file_upload_with_id) | **POST** /dataCleaning/jobs/{id}/upload | Upload a Job File with an {id}
*DCIndividualJobManagementApi* | [**job_update_mappings**](docs/DCIndividualJobManagementApi.md#job_update_mappings) | **PUT** /dataCleaning/jobs/{id}/mappings | Update Mappings Request
*DCIndividualJobManagementApi* | [**returns_enriched_job_file**](docs/DCIndividualJobManagementApi.md#returns_enriched_job_file) | **GET** /dataCleaning/jobs/{id}/enrichedFile | Returns Enriched Job File
*DCIndividualJobManagementApi* | [**submit_job_request**](docs/DCIndividualJobManagementApi.md#submit_job_request) | **POST** /dataCleaning/jobs/{id}/submit | Submit Job Request
*DCIndividualJobManagementApi* | [**update_job_enrichments**](docs/DCIndividualJobManagementApi.md#update_job_enrichments) | **PUT** /dataCleaning/jobs/{id}/enrichments | Update Enrichments Request
*DecisionLogsApi* | [**decision_history**](docs/DecisionLogsApi.md#decision_history) | **GET** /decisionEngine/usageLog | Decision History
*DecisionLogsApi* | [**get_decision_log**](docs/DecisionLogsApi.md#get_decision_log) | **GET** /decisionEngine/usageLog/{decisionLogId} | Get Decision Log
*DecisionLogsApi* | [**update_decision_log**](docs/DecisionLogsApi.md#update_decision_log) | **PATCH** /decisionEngine/usageLog/{decisionLogId} | Update Decision Log
*DecisionOutcomeApi* | [**decision_outcome**](docs/DecisionOutcomeApi.md#decision_outcome) | **GET** /decisionEngine/decisionOutcome/{guid} | Return Decision Outcome
*DecisionOutcomeApi* | [**update_decision_engine_decision_outcome_details**](docs/DecisionOutcomeApi.md#update_decision_engine_decision_outcome_details) | **PATCH** /decisionEngine/decisionOutcome/{guid} | Update Decision Outcome
*DecisionTreesApi* | [**decision_trees**](docs/DecisionTreesApi.md#decision_trees) | **GET** /decisionEngine/GUID | Decision Trees
*DecisionTreesApi* | [**user_data_fields**](docs/DecisionTreesApi.md#user_data_fields) | **GET** /decisionEngine/{provenirId}/userDataFields | User Data Fields
*FRBankMatchApi* | [**fr_bankmatch**](docs/FRBankMatchApi.md#fr_bankmatch) | **GET** /localSolutions/FR/bankmatch | Bank Match
*FRBankMatchApi* | [**fr_bankmatch_status**](docs/FRBankMatchApi.md#fr_bankmatch_status) | **GET** /localSolutions/FR/bankmatch/audition | Bank Match Status
*FinanceAgreementsApi* | [**finance_agreements**](docs/FinanceAgreementsApi.md#finance_agreements) | **GET** /localSolutions/GB/CCDS/{companyId} | Finance Agreements
*FreshInvestigationsApi* | [**comments_for_fresh_investigation_order_id**](docs/FreshInvestigationsApi.md#comments_for_fresh_investigation_order_id) | **POST** /freshinvestigations/{orderId}/comments | Comments for fresh investigation orderId
*FreshInvestigationsApi* | [**create_fresh_investigation**](docs/FreshInvestigationsApi.md#create_fresh_investigation) | **POST** /freshinvestigations | Create Fresh Investigation
*FreshInvestigationsApi* | [**delete_fresh_investigations**](docs/FreshInvestigationsApi.md#delete_fresh_investigations) | **DELETE** /freshinvestigations/{orderId} | Delete Fresh Investigations
*FreshInvestigationsApi* | [**get_attachment_for_the_given_fresh_investigation_attachment_id**](docs/FreshInvestigationsApi.md#get_attachment_for_the_given_fresh_investigation_attachment_id) | **GET** /freshinvestigations/{orderId}/attachments/{id} | Get attachment for the given fresh investigation attachment Id
*FreshInvestigationsApi* | [**get_attachments_for_the_given_fresh_investigation_order_id**](docs/FreshInvestigationsApi.md#get_attachments_for_the_given_fresh_investigation_order_id) | **GET** /freshinvestigations/{orderId}/attachments | Get attachments for the given fresh investigation orderId
*FreshInvestigationsApi* | [**get_fresh_investigations**](docs/FreshInvestigationsApi.md#get_fresh_investigations) | **GET** /freshinvestigations | Get Fresh Investigations
*FreshInvestigationsApi* | [**retrieve_comments_of_specified_fresh_investigation_report**](docs/FreshInvestigationsApi.md#retrieve_comments_of_specified_fresh_investigation_report) | **GET** /freshinvestigations/{orderId}/comments | Retrieve comments of specified FreshInvestigation Report
*FreshInvestigationsApi* | [**retrieve_fresh_investigation_order**](docs/FreshInvestigationsApi.md#retrieve_fresh_investigation_order) | **GET** /freshinvestigations/{orderId} | Retrieve FreshInvestigation Order
*FreshInvestigationsApi* | [**retrieve_fresh_investigation_report_content**](docs/FreshInvestigationsApi.md#retrieve_fresh_investigation_report_content) | **GET** /freshinvestigations/{orderId}/report | Retrieve FreshInvestigation Report Content
*FreshInvestigationsApi* | [**update_fresh_investigation_report_content**](docs/FreshInvestigationsApi.md#update_fresh_investigation_report_content) | **PATCH** /freshinvestigations/{orderId} | Update FreshInvestigation Report Content
*FreshInvestigationsApi* | [**upload_attachments_for_fresh_investigation_order_id**](docs/FreshInvestigationsApi.md#upload_attachments_for_fresh_investigation_order_id) | **POST** /freshinvestigations/{orderId}/attachments | Upload attachments for fresh investigation orderId
*GBConsumersAndAMLApi* | [**local_solutions_gb_identitysearch_history_get**](docs/GBConsumersAndAMLApi.md#local_solutions_gb_identitysearch_history_get) | **GET** /localSolutions/GB/identitysearch/history | Gets a list of identitysearch history items
*GBConsumersAndAMLApi* | [**local_solutions_gb_identitysearch_searchreasons_get**](docs/GBConsumersAndAMLApi.md#local_solutions_gb_identitysearch_searchreasons_get) | **GET** /localSolutions/GB/identitysearch/searchreasons | Gets identitysearch Reasons.
*GBConsumersAndAMLApi* | [**resolves_a_picklist_against_a_given_unique_id**](docs/GBConsumersAndAMLApi.md#resolves_a_picklist_against_a_given_unique_id) | **PUT** /localSolutions/GB/identitysearch | Resolves a picklist against a given UniqueId
*GBConsumersAndAMLApi* | [**retrieves_a_prior_identity_search_result**](docs/GBConsumersAndAMLApi.md#retrieves_a_prior_identity_search_result) | **GET** /localSolutions/GB/identitysearch/history/{uniqueId} | Retrieves a prior identitysearch result.
*GBConsumersAndAMLApi* | [**retrieves_a_prior_identity_searchs_input**](docs/GBConsumersAndAMLApi.md#retrieves_a_prior_identity_searchs_input) | **GET** /localSolutions/GB/identitysearch/history/{uniqueId}/input | Retrieves a prior identitysearch&#x27;s input
*GBConsumersAndAMLApi* | [**revalidate_a_given_identitysearch_with_additional_documents**](docs/GBConsumersAndAMLApi.md#revalidate_a_given_identitysearch_with_additional_documents) | **PUT** /localSolutions/GB/identitysearch/revalidation/{uniqueId} | Revalidate a given identitysearch with additional documents
*GBConsumersAndAMLApi* | [**sets_the_reference_for_an_existing_history_item**](docs/GBConsumersAndAMLApi.md#sets_the_reference_for_an_existing_history_item) | **PUT** /localSolutions/GB/identitysearch/history/{uniqueId}/reference | Sets the reference for an existing history item
*GBConsumersAndAMLApi* | [**submits_agb_consumer_or_aml_search**](docs/GBConsumersAndAMLApi.md#submits_agb_consumer_or_aml_search) | **POST** /localSolutions/GB/identitysearch | Submits a GB Consumer or AML Search
*GMCreateAndViewAllPortfoliosApi* | [**create_monitoring_portfolio**](docs/GMCreateAndViewAllPortfoliosApi.md#create_monitoring_portfolio) | **POST** /monitoring/portfolios | Create Monitoring Portfolio
*GMCreateAndViewAllPortfoliosApi* | [**list_all_portfolios**](docs/GMCreateAndViewAllPortfoliosApi.md#list_all_portfolios) | **GET** /monitoring/portfolios | List All Portfolios
*GMEventRulesAndNotificationsApi* | [**all_event_rules**](docs/GMEventRulesAndNotificationsApi.md#all_event_rules) | **GET** /monitoring/eventRules | All EventRules
*GMEventRulesAndNotificationsApi* | [**all_notification_events**](docs/GMEventRulesAndNotificationsApi.md#all_notification_events) | **GET** /monitoring/notificationEvents | All Notification Events
*GMEventRulesAndNotificationsApi* | [**filtered_event_rules**](docs/GMEventRulesAndNotificationsApi.md#filtered_event_rules) | **GET** /monitoring/eventRules/{countryCode} | Filtered EventRules
*GMEventRulesAndNotificationsApi* | [**list_company_events**](docs/GMEventRulesAndNotificationsApi.md#list_company_events) | **GET** /monitoring/companies/{id}/events | List Company Events
*GMImportingPortfoliosApi* | [**import_a_portfolio_file**](docs/GMImportingPortfoliosApi.md#import_a_portfolio_file) | **POST** /monitoring/portfolios/{portfolioId}/import | Import A Portfolio File
*GMImportingPortfoliosApi* | [**sync_a_portfolio_file**](docs/GMImportingPortfoliosApi.md#sync_a_portfolio_file) | **POST** /monitoring/portfolios/{portfolioId}/sync | Sync A Portfolio File
*GMIndividualPortfolioManagementApi* | [**add_company_to_portfolio**](docs/GMIndividualPortfolioManagementApi.md#add_company_to_portfolio) | **POST** /monitoring/portfolios/{portfolioId}/companies | Add Company To Portfolio
*GMIndividualPortfolioManagementApi* | [**clear_companies_from_portfolio**](docs/GMIndividualPortfolioManagementApi.md#clear_companies_from_portfolio) | **PATCH** /monitoring/portfolios/{portfolioId}/companies/clear | Clear Companies From Portfolio
*GMIndividualPortfolioManagementApi* | [**delete_company_from_portfolio**](docs/GMIndividualPortfolioManagementApi.md#delete_company_from_portfolio) | **DELETE** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Delete Company From Portfolio
*GMIndividualPortfolioManagementApi* | [**get_company_details_from_a_portfolio**](docs/GMIndividualPortfolioManagementApi.md#get_company_details_from_a_portfolio) | **GET** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Get Company Details From A Portfolio
*GMIndividualPortfolioManagementApi* | [**list_companies_in_a_portfolio**](docs/GMIndividualPortfolioManagementApi.md#list_companies_in_a_portfolio) | **GET** /monitoring/portfolios/{portfolioId}/companies | List Companies In A Portfolio
*GMIndividualPortfolioManagementApi* | [**list_company_specific_notification_events**](docs/GMIndividualPortfolioManagementApi.md#list_company_specific_notification_events) | **GET** /monitoring/portfolios/{portfolioId}/companies/{companyId}/notificationEvents | List Company Specific NotificationEvents
*GMIndividualPortfolioManagementApi* | [**list_countries_of_monitored_companies**](docs/GMIndividualPortfolioManagementApi.md#list_countries_of_monitored_companies) | **GET** /monitoring/portfolios/{portfolioId}/countries | List Countries of Monitored Companies
*GMIndividualPortfolioManagementApi* | [**list_portfolio_event_rules**](docs/GMIndividualPortfolioManagementApi.md#list_portfolio_event_rules) | **GET** /monitoring/portfolios/{portfolioId}/eventRules | List Portfolio Event Rules
*GMIndividualPortfolioManagementApi* | [**list_portfolio_event_rules_by_country**](docs/GMIndividualPortfolioManagementApi.md#list_portfolio_event_rules_by_country) | **GET** /monitoring/portfolios/{portfolioId}/eventRules/{countryCode} | List Portfolio Event Rules By Country
*GMIndividualPortfolioManagementApi* | [**list_portfolio_notifications**](docs/GMIndividualPortfolioManagementApi.md#list_portfolio_notifications) | **GET** /monitoring/portfolios/{portfolioId}/notificationEvents | List Portfolio Notifications
*GMIndividualPortfolioManagementApi* | [**portfolio_risk_summary**](docs/GMIndividualPortfolioManagementApi.md#portfolio_risk_summary) | **GET** /monitoring/portfolios/{portfolioId}/riskSummary | Portfolio Risk Summary
*GMIndividualPortfolioManagementApi* | [**set_portfolio_default_rules**](docs/GMIndividualPortfolioManagementApi.md#set_portfolio_default_rules) | **PUT** /monitoring/portfolios/{portfolioId}/eventRules/setDefault | Set Portfolio Default Rules
*GMIndividualPortfolioManagementApi* | [**update_company_details_in_portfolio**](docs/GMIndividualPortfolioManagementApi.md#update_company_details_in_portfolio) | **PATCH** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Update Company Details In Portfolio
*GMIndividualPortfolioManagementApi* | [**update_event_rules**](docs/GMIndividualPortfolioManagementApi.md#update_event_rules) | **PUT** /monitoring/portfolios/{portfolioId}/eventRules/{countryCode} | Update EventRules
*GMUserDetailsApi* | [**monitoring_user_details**](docs/GMUserDetailsApi.md#monitoring_user_details) | **GET** /monitoring/user/details | Monitoring User Details
*GMUserManagementOfPortfoliosApi* | [**copy_companies_between_portfolios**](docs/GMUserManagementOfPortfoliosApi.md#copy_companies_between_portfolios) | **POST** /monitoring/portfolios/{portfolioId}/companies/copy | Copy Companies Between Portfolios
*GMUserManagementOfPortfoliosApi* | [**delete_portfolio**](docs/GMUserManagementOfPortfoliosApi.md#delete_portfolio) | **DELETE** /monitoring/portfolios/{portfolioId} | Delete Portfolio
*GMUserManagementOfPortfoliosApi* | [**move_companies_between_portfolios**](docs/GMUserManagementOfPortfoliosApi.md#move_companies_between_portfolios) | **POST** /monitoring/portfolios/{portfolioId}/companies/remove | Move Companies Between Portfolios
*GMUserManagementOfPortfoliosApi* | [**portfolio_user_permissions**](docs/GMUserManagementOfPortfoliosApi.md#portfolio_user_permissions) | **GET** /monitoring/portfolios/{portfolioId}/sharingPermissions | Portfolio User Permissions
*GMUserManagementOfPortfoliosApi* | [**retrieve_portfolio_by_id**](docs/GMUserManagementOfPortfoliosApi.md#retrieve_portfolio_by_id) | **GET** /monitoring/portfolios/{portfolioId} | Retrieve Portfolio By Id
*GMUserManagementOfPortfoliosApi* | [**share_portfolio_with_users**](docs/GMUserManagementOfPortfoliosApi.md#share_portfolio_with_users) | **PATCH** /monitoring/portfolios/{portfolioId}/sharingPermissions | Share Portfolio With Users
*GMUserManagementOfPortfoliosApi* | [**update_portfolio_details**](docs/GMUserManagementOfPortfoliosApi.md#update_portfolio_details) | **PATCH** /monitoring/portfolios/{portfolioId} | Update Portfolio Details
*ImagesApi* | [**company_image**](docs/ImagesApi.md#company_image) | **GET** /images/{imageId} | Company Image
*ImagesApi* | [**company_image_documents**](docs/ImagesApi.md#company_image_documents) | **GET** /images/companies | Company Image Documents
*ImagesApi* | [**image_document_category_types**](docs/ImagesApi.md#image_document_category_types) | **GET** /images/companies/types | Image Document Category Types
*InstanceManagementApi* | [**instance_configuration**](docs/InstanceManagementApi.md#instance_configuration) | **GET** /decisionEngine/instance/{guid} | Instance Configuration
*InstanceManagementApi* | [**return_all_instances**](docs/InstanceManagementApi.md#return_all_instances) | **GET** /decisionEngine/instances | Return All Available Instances
*InstanceManagementApi* | [**update_instance_configuration**](docs/InstanceManagementApi.md#update_instance_configuration) | **PUT** /decisionEngine/instance/{guid} | Update Instance Configuration
*KYCAMLBulkScreeningApi* | [**compliancepostkycsearchesbulkbyprofileid**](docs/KYCAMLBulkScreeningApi.md#compliancepostkycsearchesbulkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/searches/bulk | Perform Bulk AML Screening
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_create_schedule**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_create_schedule) | **POST** /compliance/kyc-protect/schedules | Add Search To AML Monitoring
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_delete_schedules**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_delete_schedules) | **DELETE** /compliance/kyc-protect/schedules | Delete Searches From AML Monitoring
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_delete_schedules_by_schedule_id**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_delete_schedules_by_schedule_id) | **DELETE** /compliance/kyc-protect/schedules/{scheduleId} | Delete A Search From AML Monitoring
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_get_schedules**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_get_schedules) | **GET** /compliance/kyc-protect/schedules | Return All Ordered Schedules
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_get_schedules_aml_alerts**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_get_schedules_aml_alerts) | **GET** /compliance/kyc-protect/schedules/amlAlerts | Return All Hits For A Schedule By Created Date
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_put_schedules**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_put_schedules) | **PUT** /compliance/kyc-protect/schedules | Update Schedules
*KYCAMLMonitoringManagementApi* | [**k_yc_protect_put_schedules_by_schedule_id**](docs/KYCAMLMonitoringManagementApi.md#k_yc_protect_put_schedules_by_schedule_id) | **PUT** /compliance/kyc-protect/schedules/{scheduleId} | Update A Schedule In Monitoring
*KYCAMLMonitoringManagementApi* | [**kycprotectgetschedulesbyscheduleid**](docs/KYCAMLMonitoringManagementApi.md#kycprotectgetschedulesbyscheduleid) | **GET** /compliance/kyc-protect/schedules/{scheduleId} | Returns A Schedule
*KYCAMLScreeningBusinessesApi* | [**get_kyc_search_business_by_search_id**](docs/KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_by_search_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId} | Return Business AML Search By Search Id
*KYCAMLScreeningBusinessesApi* | [**get_kyc_search_business_hits_by_search_id**](docs/KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_hits_by_search_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId}/hits | Return Business AML Search Hits
*KYCAMLScreeningBusinessesApi* | [**get_kyc_search_business_hits_by_search_id_and_hit_id**](docs/KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_hits_by_search_id_and_hit_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId} | Return Full AML Search Hit Information By SearchId And HitId
*KYCAMLScreeningBusinessesApi* | [**k_yc_search_business**](docs/KYCAMLScreeningBusinessesApi.md#k_yc_search_business) | **POST** /compliance/kyc-protect/searches/businesses | Performs An AML Search For A Business And Saves The Results To The Database
*KYCAMLScreeningBusinessesApi* | [**k_yc_search_business_get**](docs/KYCAMLScreeningBusinessesApi.md#k_yc_search_business_get) | **GET** /compliance/kyc-protect/searches/businesses | Returns Business AML Searches
*KYCAMLScreeningBusinessesApi* | [**k_yc_search_business_put**](docs/KYCAMLScreeningBusinessesApi.md#k_yc_search_business_put) | **PUT** /compliance/kyc-protect/searches/businesses | Update Business AML Searches
*KYCAMLScreeningBusinessesApi* | [**put_kyc_search_business_by_search_id**](docs/KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_by_search_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId} | Update A Business AML Search By Search Id
*KYCAMLScreeningBusinessesApi* | [**put_kyc_search_business_by_search_id_and_hit_id**](docs/KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_by_search_id_and_hit_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId} | Update A Single Business Hit
*KYCAMLScreeningBusinessesApi* | [**put_kyc_search_business_hits_by_search_id**](docs/KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_hits_by_search_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId}/hits | Update Batch Of Business AML Search Hits
*KYCAMLScreeningIndividualsApi* | [**compliance_kyc_protect_create_individuals_search**](docs/KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_create_individuals_search) | **POST** /compliance/kyc-protect/searches/individuals | Performs An AML Search For An Individual And Saves The Results To The Database
*KYCAMLScreeningIndividualsApi* | [**compliance_kyc_protect_get_individuals_search**](docs/KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_get_individuals_search) | **GET** /compliance/kyc-protect/searches/individuals | Returns Individual AML Searches
*KYCAMLScreeningIndividualsApi* | [**compliance_kyc_protect_update_individuals_search**](docs/KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_update_individuals_search) | **PUT** /compliance/kyc-protect/searches/individuals | Update Individual AML Searches
*KYCAMLScreeningIndividualsApi* | [**gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id**](docs/KYCAMLScreeningIndividualsApi.md#gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id) | **GET** /compliance/kyc-protect/searches/individuals/{searchId} | Return Individual AML Search By Search Id
*KYCAMLScreeningIndividualsApi* | [**gets_the_individual_search_hits**](docs/KYCAMLScreeningIndividualsApi.md#gets_the_individual_search_hits) | **GET** /compliance/kyc-protect/searches/individuals/{searchId}/hits | Returns Individual AML Search Hits
*KYCAMLScreeningIndividualsApi* | [**returns_full_profile_information_of_a_individual_hit_by_hit_id**](docs/KYCAMLScreeningIndividualsApi.md#returns_full_profile_information_of_a_individual_hit_by_hit_id) | **GET** /compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId} | Return Full AML Search Hit Information By SearchId And HitId
*KYCAMLScreeningIndividualsApi* | [**update_single_individual_hit**](docs/KYCAMLScreeningIndividualsApi.md#update_single_individual_hit) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId} | Update A Single Individual Hit
*KYCAMLScreeningIndividualsApi* | [**updates_a_batch_of_individual_hits**](docs/KYCAMLScreeningIndividualsApi.md#updates_a_batch_of_individual_hits) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId}/hits | Updates A Batch Of individual AML search Hits
*KYCAMLScreeningIndividualsApi* | [**updates_an_individual_search**](docs/KYCAMLScreeningIndividualsApi.md#updates_an_individual_search) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId} | Updates An Individual AML Search By SearchID
*KYCAMLScreeningProfileManagementApi* | [**delete_kyc_profile_searches_by_profile_id**](docs/KYCAMLScreeningProfileManagementApi.md#delete_kyc_profile_searches_by_profile_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/searches/link | Deletes AML searches linked to a profile
*KYCAMLScreeningProfileManagementApi* | [**getkychitsofthesearcheslinkedtoprofile**](docs/KYCAMLScreeningProfileManagementApi.md#getkychitsofthesearcheslinkedtoprofile) | **GET** /compliance/kyc-protect/profiles/{profileId}/hits | Return All Hits Of Searches Linked To A Profile
*KYCAMLScreeningProfileManagementApi* | [**k_yc_protect_adds_a_search_to_the_given_profile**](docs/KYCAMLScreeningProfileManagementApi.md#k_yc_protect_adds_a_search_to_the_given_profile) | **POST** /compliance/kyc-protect/profiles/{profileId}/searches/link | Adds AML Searches To The Given Profile
*KYCAMLScreeningProfileManagementApi* | [**k_yc_protect_get_aml_alerts_by_profile_id**](docs/KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_aml_alerts_by_profile_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/amlAlerts | Return All Hits Linked To The Profile
*KYCAMLScreeningProfileManagementApi* | [**k_yc_protect_get_profile_schedules**](docs/KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_profile_schedules) | **GET** /compliance/kyc-protect/profiles/{profileId}/schedules | Return All Schedules By ProfileId And Modified Date
*KYCAMLScreeningProfileManagementApi* | [**k_yc_protect_get_profile_schedules_by_schedule_id**](docs/KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_profile_schedules_by_schedule_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/schedules/{scheduleId} | Return Schedule By ProfileId And ScheduleId
*KYCAMLScreeningProfileManagementApi* | [**k_yc_protect_get_s_list_of_searches_on_the_given_profile**](docs/KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_s_list_of_searches_on_the_given_profile) | **GET** /compliance/kyc-protect/profiles/{profileId}/searches | Return List Of AML Searches On The Given Profile
*KYCAdministratorResourcesApi* | [**k_yc_protect_get_profile_document_types**](docs/KYCAdministratorResourcesApi.md#k_yc_protect_get_profile_document_types) | **GET** /compliance/kyc-protect/profiles/document-types | Return Profile Document Types
*KYCAdministratorResourcesApi* | [**protect_get_kyc_profile_types**](docs/KYCAdministratorResourcesApi.md#protect_get_kyc_profile_types) | **GET** /compliance/kyc-protect/profiles/types | Return Profile Types
*KYCAdministratorResourcesApi* | [**protect_get_lookup_country_codes**](docs/KYCAdministratorResourcesApi.md#protect_get_lookup_country_codes) | **GET** /compliance/kyc-protect/lookup/countryCodes | Return Accepted Country Codes
*KYCAdministratorResourcesApi* | [**protect_get_lookup_currency_codes**](docs/KYCAdministratorResourcesApi.md#protect_get_lookup_currency_codes) | **GET** /compliance/kyc-protect/lookup/currencyCodes | Returns Accepted Currency Codes
*KYCAsyncAMLApi* | [**compliancegetkycasyncamljobs**](docs/KYCAsyncAMLApi.md#compliancegetkycasyncamljobs) | **GET** /compliance/kyc-protect/asyncAmlJobs | Return All Async AML Jobs
*KYCAsyncAMLApi* | [**compliancegetkycasyncamljobsjobid**](docs/KYCAsyncAMLApi.md#compliancegetkycasyncamljobsjobid) | **GET** /compliance/kyc-protect/asyncAmlJobs/{jobId} | Return Async AML Jobs By Id
*KYCAsyncAMLApi* | [**compliancegetkycasyncamljobsjobidcriteria**](docs/KYCAsyncAMLApi.md#compliancegetkycasyncamljobsjobidcriteria) | **GET** /compliance/kyc-protect/asyncAmlJobs/{jobId}/criteria | Return Async Job Criteria By Id
*KYCAuditApi* | [**compliance_get_kyc_audits**](docs/KYCAuditApi.md#compliance_get_kyc_audits) | **GET** /compliance/kyc-protect/audits | Return Audit Trail
*KYCBatchUploadsApi* | [**compliance_get_kyc_batch_upload_by_upload_id**](docs/KYCBatchUploadsApi.md#compliance_get_kyc_batch_upload_by_upload_id) | **GET** /compliance/kyc-protect/batchUploads/{uploadId} | Return Batch Upload File Details
*KYCBatchUploadsApi* | [**compliance_get_kyc_batch_uploads**](docs/KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads) | **GET** /compliance/kyc-protect/batchUploads | Return A List Of Requested Uploads
*KYCBatchUploadsApi* | [**compliance_get_kyc_batch_uploads_download_errors_by_upload_id**](docs/KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_download_errors_by_upload_id) | **GET** /compliance/kyc-protect/batchUploads/{uploadId}/errors/download | Download Batch Upload Error File
*KYCBatchUploadsApi* | [**compliance_get_kyc_batch_uploads_retry_by_upload_id**](docs/KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_retry_by_upload_id) | **PUT** /compliance/kyc-protect/batchUploads/{uploadId}/retry | Retry Previous Upload
*KYCBatchUploadsApi* | [**compliance_get_kyc_batch_uploads_template**](docs/KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_template) | **GET** /compliance/kyc-protect/batchUploads/template | Return Template For Batch Upload
*KYCBatchUploadsApi* | [**compliance_post_kyc_batch_uploads**](docs/KYCBatchUploadsApi.md#compliance_post_kyc_batch_uploads) | **POST** /compliance/kyc-protect/batchUploads | Request Batch Upload
*KYCGlobalMonitoringApi* | [**compliance_delete_kyc_monitoring_profiles**](docs/KYCGlobalMonitoringApi.md#compliance_delete_kyc_monitoring_profiles) | **DELETE** /compliance/kyc-protect/kycMonitoring/profiles | Delete Profiles From Monitoring
*KYCGlobalMonitoringApi* | [**compliance_post_kyc_monitoring_profiles_bulk**](docs/KYCGlobalMonitoringApi.md#compliance_post_kyc_monitoring_profiles_bulk) | **POST** /compliance/kyc-protect/kycMonitoring/profiles/bulk | Add Profiles To Monitoring
*KYCGlobalMonitoringApi* | [**compliance_protect_get_lookup_monitoring_country_codes**](docs/KYCGlobalMonitoringApi.md#compliance_protect_get_lookup_monitoring_country_codes) | **GET** /compliance/kyc-protect/lookup/kycMonitoring/countryCodes | Returns Available Country Codes
*KYCGlobalMonitoringApi* | [**compliancegetkycmonitoringindividualprofilealertsbyalertid**](docs/KYCGlobalMonitoringApi.md#compliancegetkycmonitoringindividualprofilealertsbyalertid) | **GET** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId} | Return Alert By Alert Id And ProfileId
*KYCGlobalMonitoringApi* | [**compliancegetkycmonitoringprofilealertsbyprofileid**](docs/KYCGlobalMonitoringApi.md#compliancegetkycmonitoringprofilealertsbyprofileid) | **GET** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts | Return List Of Alerts By Profile
*KYCGlobalMonitoringApi* | [**complianceputkycmonitoringindividualprofilealertsbyalertid**](docs/KYCGlobalMonitoringApi.md#complianceputkycmonitoringindividualprofilealertsbyalertid) | **PUT** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId} | Update Status of Alert By Profile Id And Alert Id
*KYCProfileBusinessIndividualDetailsApi* | [**k_yc_protect_creates_an_address_for_the_user**](docs/KYCProfileBusinessIndividualDetailsApi.md#k_yc_protect_creates_an_address_for_the_user) | **POST** /compliance/kyc-protect/profiles/{profileId}/details/addresses | Creates An Address For Profile
*KYCProfileBusinessIndividualDetailsApi* | [**k_yc_protect_gets_list_of_addresses**](docs/KYCProfileBusinessIndividualDetailsApi.md#k_yc_protect_gets_list_of_addresses) | **GET** /compliance/kyc-protect/profiles/{profileId}/details/addresses | Return Lists Of Addresses
*KYCProfileBusinessIndividualDetailsApi* | [**protect_deletekyc_profile_address_details_by_profile_id_and_address_id**](docs/KYCProfileBusinessIndividualDetailsApi.md#protect_deletekyc_profile_address_details_by_profile_id_and_address_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Delete Profile Address Details By Profile Id And Address Id
*KYCProfileBusinessIndividualDetailsApi* | [**protect_getkyc_profile_address_details_by_profile_id_and_address_id**](docs/KYCProfileBusinessIndividualDetailsApi.md#protect_getkyc_profile_address_details_by_profile_id_and_address_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Return Profile Address Details By Profile And Address Id
*KYCProfileBusinessIndividualDetailsApi* | [**protect_getkyc_profile_details**](docs/KYCProfileBusinessIndividualDetailsApi.md#protect_getkyc_profile_details) | **GET** /compliance/kyc-protect/profiles/{profileId}/details | Return Profile Details
*KYCProfileBusinessIndividualDetailsApi* | [**protect_putkyc_profile_address_details_by_profile_id_and_address_id**](docs/KYCProfileBusinessIndividualDetailsApi.md#protect_putkyc_profile_address_details_by_profile_id_and_address_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Update Profile Address Details By Profile Id And Address Id
*KYCProfileBusinessIndividualDetailsApi* | [**protect_putkyc_profile_details**](docs/KYCProfileBusinessIndividualDetailsApi.md#protect_putkyc_profile_details) | **PUT** /compliance/kyc-protect/profiles/{profileId}/details | Update Profile Details
*KYCProfileKeyPartiesApi* | [**compliancedeletekyckeypartiesbyprofileid**](docs/KYCProfileKeyPartiesApi.md#compliancedeletekyckeypartiesbyprofileid) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties | Delete a batch of key parties
*KYCProfileKeyPartiesApi* | [**compliancedeletekyckeypartiessearches**](docs/KYCProfileKeyPartiesApi.md#compliancedeletekyckeypartiessearches) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches | Deletes A Batch Of Key Party Searches
*KYCProfileKeyPartiesApi* | [**compliancegetkyckeypartiesbyprofileid**](docs/KYCProfileKeyPartiesApi.md#compliancegetkyckeypartiesbyprofileid) | **GET** /compliance/kyc-protect/profiles/{profileId}/keyparties | Return All Key Party Records Linked To A Profile
*KYCProfileKeyPartiesApi* | [**compliancegetkyckeypartiessearches**](docs/KYCProfileKeyPartiesApi.md#compliancegetkyckeypartiessearches) | **GET** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches | Return All Key Party Searches
*KYCProfileKeyPartiesApi* | [**compliancepostkyckeypartiesbyprofileid**](docs/KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiesbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties | Creates A Key Party Folder Linked To The Profile Id
*KYCProfileKeyPartiesApi* | [**compliancepostkyckeypartiessearchesbulkbyprofileid**](docs/KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiessearchesbulkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches/bulk | Request Multiple Searches Linked To A Key Party Asynchronously
*KYCProfileKeyPartiesApi* | [**compliancepostkyckeypartiessearcheslinkbyprofileid**](docs/KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiessearcheslinkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches/link | Links Searches To Key Parties
*KYCProfileKeyPartiesApi* | [**complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid**](docs/KYCProfileKeyPartiesApi.md#complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId} | Deletes a Key PArty By Key Party Id
*KYCProfileKeyPartiesApi* | [**complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid**](docs/KYCProfileKeyPartiesApi.md#complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid) | **PUT** /compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId} | Updates The Key Party By Profile Id and Key Party Id
*KYCProfileKeyPartiesApi* | [**complianceputkyckeypartiesbyprofileid**](docs/KYCProfileKeyPartiesApi.md#complianceputkyckeypartiesbyprofileid) | **PUT** /compliance/kyc-protect/profiles/{profileId}/keyparties | Update A Batch Of Key Parties
*KYCProfileManagementApi* | [**compliance_protect_delete_kyc_profiles**](docs/KYCProfileManagementApi.md#compliance_protect_delete_kyc_profiles) | **DELETE** /compliance/kyc-protect/profiles | Delete All Profiles
*KYCProfileManagementApi* | [**compliance_protect_get_kyc_profiles**](docs/KYCProfileManagementApi.md#compliance_protect_get_kyc_profiles) | **GET** /compliance/kyc-protect/profiles | Return Created Profiles
*KYCProfileManagementApi* | [**k_yc_protect_assigns_list_of_profiles_to_user**](docs/KYCProfileManagementApi.md#k_yc_protect_assigns_list_of_profiles_to_user) | **PUT** /compliance/kyc-protect/profiles/assign/bulk | Assigns A List Of Profiles To User
*KYCProfileManagementApi* | [**k_yc_protect_create_profile**](docs/KYCProfileManagementApi.md#k_yc_protect_create_profile) | **POST** /compliance/kyc-protect/profiles | Create Profile
*KYCProfileManagementApi* | [**protect_assign_profiles**](docs/KYCProfileManagementApi.md#protect_assign_profiles) | **PUT** /compliance/kyc-protect/profiles/assign | Assign Profile To User
*KYCProfileManagementApi* | [**protect_delete_kyc_profiles_by_id**](docs/KYCProfileManagementApi.md#protect_delete_kyc_profiles_by_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId} | Delete Profile By Profile Id
*KYCProfileManagementApi* | [**protect_get_kyc_profiles_by_profile_id**](docs/KYCProfileManagementApi.md#protect_get_kyc_profiles_by_profile_id) | **GET** /compliance/kyc-protect/profiles/{profileId} | Return Profile By Profile Id
*KYCProfileUpdatesApi* | [**k_yc_protect_add_an_attachment_to_the_given_profile**](docs/KYCProfileUpdatesApi.md#k_yc_protect_add_an_attachment_to_the_given_profile) | **POST** /compliance/kyc-protect/profiles/{profileId}/attachments | Add An Attachment To The Given Profile
*KYCProfileUpdatesApi* | [**k_yc_protect_get_list_of_attachments_on_the_given_profile**](docs/KYCProfileUpdatesApi.md#k_yc_protect_get_list_of_attachments_on_the_given_profile) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments | Return List Of Attachments On The Given Profile
*KYCProfileUpdatesApi* | [**protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id**](docs/KYCProfileUpdatesApi.md#protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Delete Attachment By Profile And Attachment Id
*KYCProfileUpdatesApi* | [**protect_deletekyc_profile_id_by_note_id**](docs/KYCProfileUpdatesApi.md#protect_deletekyc_profile_id_by_note_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Deletes Profile Note By Note Id
*KYCProfileUpdatesApi* | [**protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id**](docs/KYCProfileUpdatesApi.md#protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}/download | Download Profile Attachment By Profile And Attachment Id
*KYCProfileUpdatesApi* | [**protect_getkyc_profile_attachment_by_profile_id_and_attachment_id**](docs/KYCProfileUpdatesApi.md#protect_getkyc_profile_attachment_by_profile_id_and_attachment_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Return A Profile Attachment By Profile And Attachment Id
*KYCProfileUpdatesApi* | [**protect_getkyc_profile_notes**](docs/KYCProfileUpdatesApi.md#protect_getkyc_profile_notes) | **GET** /compliance/kyc-protect/profiles/{profileId}/notes | Return Profile Notes
*KYCProfileUpdatesApi* | [**protect_getkyc_profile_notes_by_note_id**](docs/KYCProfileUpdatesApi.md#protect_getkyc_profile_notes_by_note_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Return Profile Notes By Note Id
*KYCProfileUpdatesApi* | [**protect_postkyc_profile_notes**](docs/KYCProfileUpdatesApi.md#protect_postkyc_profile_notes) | **POST** /compliance/kyc-protect/profiles/{profileId}/notes | Create Profile Note
*KYCProfileUpdatesApi* | [**protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id**](docs/KYCProfileUpdatesApi.md#protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Update Profile Attachment By Profile And Attachment Id
*KYCProfileUpdatesApi* | [**protect_update_kyc_profile_notes_by_note_id**](docs/KYCProfileUpdatesApi.md#protect_update_kyc_profile_notes_by_note_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Update Profile Note By Note Id
*KYCProfileUpdatesApi* | [**protect_updates_kyc_profile_by_id**](docs/KYCProfileUpdatesApi.md#protect_updates_kyc_profile_by_id) | **PUT** /compliance/kyc-protect/profiles/{profileId} | Update Profile By Profile Id
*LandRegistryApi* | [**gb_land_registry**](docs/LandRegistryApi.md#gb_land_registry) | **GET** /localSolutions/GB/landRegistry/{companyId} | GB Land Registry
*MiscApi* | [**custom_report_parameters**](docs/MiscApi.md#custom_report_parameters) | **GET** /reportcustomdata/{country} | Custom Report Parameters
*MiscApi* | [**report_schema**](docs/MiscApi.md#report_schema) | **GET** /companies/schema/{countryCode} | Report Schema
*NLKVKApi* | [**extract_nl_kvk_number**](docs/NLKVKApi.md#extract_nl_kvk_number) | **GET** /localSolutions/NL/extract/{kvkNumber} | Return NL Extract
*PeopleDirectorsApi* | [**director_report**](docs/PeopleDirectorsApi.md#director_report) | **GET** /people/{peopleId} | Director Report
*PeopleDirectorsApi* | [**director_s_search**](docs/PeopleDirectorsApi.md#director_s_search) | **GET** /people | Director Search
*PeopleDirectorsApi* | [**people_director_search_criteria**](docs/PeopleDirectorsApi.md#people_director_search_criteria) | **GET** /people/searchcriteria | People/Director Search Criteria
*ProtectAuditApi* | [**export_audit_log_file**](docs/ProtectAuditApi.md#export_audit_log_file) | **POST** /protect/audits | Export Audit Log File
*ProtectAuditApi* | [**retrieve_protect_audit_log**](docs/ProtectAuditApi.md#retrieve_protect_audit_log) | **GET** /protect/audits | Retrieve Protect Audit Log
*ProtectBatchUploadsApi* | [**batch_upload_file**](docs/ProtectBatchUploadsApi.md#batch_upload_file) | **POST** /protect/batchUploads | Batch Upload File
*ProtectBatchUploadsApi* | [**returns_batch_upload_by_id**](docs/ProtectBatchUploadsApi.md#returns_batch_upload_by_id) | **GET** /protect/batchUploads/{batchUploadId} | Returns Batch Uploads by ID
*ProtectBatchUploadsApi* | [**returns_batch_uploads**](docs/ProtectBatchUploadsApi.md#returns_batch_uploads) | **GET** /protect/batchUploads | Returns Batch Uploads
*ProtectBatchUploadsApi* | [**returns_error_file_link**](docs/ProtectBatchUploadsApi.md#returns_error_file_link) | **GET** /protect/batchUploads/{batchUploadId}/errorFile | Returns Error File Link
*ProtectBatchUploadsApi* | [**returns_selected_template_link**](docs/ProtectBatchUploadsApi.md#returns_selected_template_link) | **GET** /protect/batchUploads/templates/{type} | Returns Selected Template Link
*ProtectIDVApi* | [**idv_search**](docs/ProtectIDVApi.md#idv_search) | **POST** /protect/idv/gdc/search | IDV Search
*ProtectIDVApi* | [**returns_idv_report**](docs/ProtectIDVApi.md#returns_idv_report) | **GET** /protect/idv/file | Returns IDV Report
*ProtectInvestigationsApi* | [**add_investigations_records**](docs/ProtectInvestigationsApi.md#add_investigations_records) | **POST** /protect/investigations/{investigationId}/records | Add Investigations Records
*ProtectInvestigationsApi* | [**assign_risk_to_investigation**](docs/ProtectInvestigationsApi.md#assign_risk_to_investigation) | **PUT** /protect/investigations/{id}/risk | Assign Risk to Investigation
*ProtectInvestigationsApi* | [**create_investigation_and_return_report_link**](docs/ProtectInvestigationsApi.md#create_investigation_and_return_report_link) | **POST** /protect/investigations/file | Create Investigation And Return Report Link
*ProtectInvestigationsApi* | [**create_investigation_note**](docs/ProtectInvestigationsApi.md#create_investigation_note) | **POST** /protect/investigations/{id}/notes | Create Investigation Note
*ProtectInvestigationsApi* | [**create_protect_investigation**](docs/ProtectInvestigationsApi.md#create_protect_investigation) | **POST** /protect/investigations | Create Protect Investigation
*ProtectInvestigationsApi* | [**create_protect_investigation_pdf**](docs/ProtectInvestigationsApi.md#create_protect_investigation_pdf) | **POST** /protect/investigations/{investigationId}/file | Create Protect Investigation PDF
*ProtectInvestigationsApi* | [**delete_investigation**](docs/ProtectInvestigationsApi.md#delete_investigation) | **DELETE** /protect/investigations/{investigationId} | Delete Investigation
*ProtectInvestigationsApi* | [**delete_investigation_records**](docs/ProtectInvestigationsApi.md#delete_investigation_records) | **DELETE** /protect/investigations/{investigationId}/records | Delete Investigation Records
*ProtectInvestigationsApi* | [**get_investigation_notes**](docs/ProtectInvestigationsApi.md#get_investigation_notes) | **GET** /protect/investigations/{id}/notes | Get Investigation Notes
*ProtectInvestigationsApi* | [**get_investigation_results_by_id**](docs/ProtectInvestigationsApi.md#get_investigation_results_by_id) | **GET** /protect/investigations/{investigationId}/results | Get Investigation Results By Id
*ProtectInvestigationsApi* | [**list_all_protect_investigations**](docs/ProtectInvestigationsApi.md#list_all_protect_investigations) | **GET** /protect/investigations | List All Protect Investigations
*ProtectInvestigationsApi* | [**return_investigations_records**](docs/ProtectInvestigationsApi.md#return_investigations_records) | **GET** /protect/investigations/{investigationId}/records | Return Investigation Records
*ProtectInvestigationsApi* | [**return_protect_investigation_by_id**](docs/ProtectInvestigationsApi.md#return_protect_investigation_by_id) | **GET** /protect/investigations/{investigationId} | Return Protect Investigation By Id
*ProtectInvestigationsApi* | [**returns_investigation_report**](docs/ProtectInvestigationsApi.md#returns_investigation_report) | **POST** /protect/investigations/{investigationId}/records/file | Returns Investigation Report
*ProtectInvestigationsApi* | [**update_investigations_records**](docs/ProtectInvestigationsApi.md#update_investigations_records) | **PUT** /protect/investigations/{investigationId}/records | Update Investigation Records
*ProtectProfileApi* | [**add_investigation_to_profile**](docs/ProtectProfileApi.md#add_investigation_to_profile) | **PUT** /protect/profiles/{profileId}/investigations/{investigationId} | Add Investigation To Profile
*ProtectProfileApi* | [**create_protect_profile**](docs/ProtectProfileApi.md#create_protect_profile) | **POST** /protect/profiles | Create Protect Profile
*ProtectProfileApi* | [**edit_protect_profile**](docs/ProtectProfileApi.md#edit_protect_profile) | **PUT** /protect/profiles/{profileId} | Edit Protect Profile
*ProtectProfileApi* | [**list_all_protect_profiles**](docs/ProtectProfileApi.md#list_all_protect_profiles) | **GET** /protect/profiles | List All Protect Profiles
*ProtectProfileApi* | [**list_investigations_in_a_profile**](docs/ProtectProfileApi.md#list_investigations_in_a_profile) | **GET** /protect/profiles/{profileId}/investigations | List Investigations In A Profile.
*ProtectProfileApi* | [**retrieve_protect_profile_by_id**](docs/ProtectProfileApi.md#retrieve_protect_profile_by_id) | **GET** /protect/profiles/{profileId} | Retrieve Protect Profile By ID
*ProtectSchedulesApi* | [**create_protect_schedule**](docs/ProtectSchedulesApi.md#create_protect_schedule) | **POST** /protect/schedules | Create Protect Schedule
*ProtectSchedulesApi* | [**deletes_schedule_from_investigation**](docs/ProtectSchedulesApi.md#deletes_schedule_from_investigation) | **DELETE** /protect/schedules/{id} | Deletes Schedule from Investigation
*ProtectSchedulesApi* | [**retrieve_schedule_by_id**](docs/ProtectSchedulesApi.md#retrieve_schedule_by_id) | **GET** /protect/schedules/{id} | Retrieve Schedule By Id
*ProtectSchedulesApi* | [**updates_schedule**](docs/ProtectSchedulesApi.md#updates_schedule) | **PUT** /protect/schedules/{id} |  Updates Schedule
*RunDecisionApi* | [**run_decision_tree**](docs/RunDecisionApi.md#run_decision_tree) | **POST** /decisionEngine/{provenirId} | Run Decision Tree
*USSearchSupportApi* | [**create_freshinvestigation_for_us_country**](docs/USSearchSupportApi.md#create_freshinvestigation_for_us_country) | **POST** /localSolutions/US/searchSupport | US Fresh Investigation Request
*UserAdministrationApi* | [**protect_get_active_customer_users**](docs/UserAdministrationApi.md#protect_get_active_customer_users) | **GET** /access/users/active | List of Active Users
*UserAdministrationApi* | [**protect_get_details_of_logged_in_user**](docs/UserAdministrationApi.md#protect_get_details_of_logged_in_user) | **GET** /access/users/me | Logged In User Details
*UserAdministrationApi* | [**subscription_details**](docs/UserAdministrationApi.md#subscription_details) | **GET** /access | Subscription Details

## Documentation For Models

 - [AMLMultiBureauSearch](docs/AMLMultiBureauSearch.md)
 - [AMLMultiBureauSearchIdAml](docs/AMLMultiBureauSearchIdAml.md)
 - [AMLSearch](docs/AMLSearch.md)
 - [AMLSearchIdAml](docs/AMLSearchIdAml.md)
 - [AddKeyPartySearchContract](docs/AddKeyPartySearchContract.md)
 - [AddSearchContract](docs/AddSearchContract.md)
 - [Address](docs/Address.md)
 - [AlertType](docs/AlertType.md)
 - [AlertsFrequency](docs/AlertsFrequency.md)
 - [AllOfConnectFootprintDataFinanceOverallAggregations](docs/AllOfConnectFootprintDataFinanceOverallAggregations.md)
 - [AllOfConnectFootprintIndicatorDataOverallAggregations](docs/AllOfConnectFootprintIndicatorDataOverallAggregations.md)
 - [AllOfConnectIndicatorDataOverallAggregations](docs/AllOfConnectIndicatorDataOverallAggregations.md)
 - [AllOfConsumerSearchCommon](docs/AllOfConsumerSearchCommon.md)
 - [AllOfConsumerSearchConsumer](docs/AllOfConsumerSearchConsumer.md)
 - [AnyOfConnectFreshInvCompletedInvestigationSectionsItems](docs/AnyOfConnectFreshInvCompletedInvestigationSectionsItems.md)
 - [AnyOfConnectMonitoringUpdateEventRulesBodyParam0](docs/AnyOfConnectMonitoringUpdateEventRulesBodyParam0.md)
 - [AnyOfConnectMonitoringUpdateEventRulesBodyParam1](docs/AnyOfConnectMonitoringUpdateEventRulesBodyParam1.md)
 - [AnyOfConnectMonitoringUpdateEventRulesBodyParam2](docs/AnyOfConnectMonitoringUpdateEventRulesBodyParam2.md)
 - [ApplicationSearchesModelsHitsEntriesDisqualifiedDirectorEntryValue](docs/ApplicationSearchesModelsHitsEntriesDisqualifiedDirectorEntryValue.md)
 - [ArrayOfConnectDataCleaningJob](docs/ArrayOfConnectDataCleaningJob.md)
 - [ArrayOfConnectDataCleaningResponse](docs/ArrayOfConnectDataCleaningResponse.md)
 - [AssignRiskToInvestigationDto](docs/AssignRiskToInvestigationDto.md)
 - [AttachmentNotFound](docs/AttachmentNotFound.md)
 - [Basic](docs/Basic.md)
 - [BasicEnrichments](docs/BasicEnrichments.md)
 - [BasicPlus](docs/BasicPlus.md)
 - [BatchUpload](docs/BatchUpload.md)
 - [BatchUploadFileType](docs/BatchUploadFileType.md)
 - [BatchUploadStatus](docs/BatchUploadStatus.md)
 - [BusinessesSearchIdBody](docs/BusinessesSearchIdBody.md)
 - [CombinedDecision](docs/CombinedDecision.md)
 - [CompliancekycprotectprofilesprofileIdkeypartiessearcheslinkItems](docs/CompliancekycprotectprofilesprofileIdkeypartiessearcheslinkItems.md)
 - [CompliancekycprotectsearchesbusinessesItems](docs/CompliancekycprotectsearchesbusinessesItems.md)
 - [ConnectAuthenticationAccessCountries](docs/ConnectAuthenticationAccessCountries.md)
 - [ConnectAuthenticationAccessCountriesCountryAccess](docs/ConnectAuthenticationAccessCountriesCountryAccess.md)
 - [ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectDirectorReports](docs/ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectDirectorReports.md)
 - [ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectMonitoring](docs/ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectMonitoring.md)
 - [ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOfflineReports](docs/ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOfflineReports.md)
 - [ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOnlineReports](docs/ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOnlineReports.md)
 - [ConnectAuthenticationAuthRequest](docs/ConnectAuthenticationAuthRequest.md)
 - [ConnectAuthenticationAuthResponse](docs/ConnectAuthenticationAuthResponse.md)
 - [ConnectAuthenticationUnauthorised](docs/ConnectAuthenticationUnauthorised.md)
 - [ConnectBankMatchAggregations](docs/ConnectBankMatchAggregations.md)
 - [ConnectBankMatchBusinessAddress](docs/ConnectBankMatchBusinessAddress.md)
 - [ConnectBankMatchData](docs/ConnectBankMatchData.md)
 - [ConnectBankMatchFacility](docs/ConnectBankMatchFacility.md)
 - [ConnectBankMatchPerOrganisationAggregation](docs/ConnectBankMatchPerOrganisationAggregation.md)
 - [ConnectBankMatchResult](docs/ConnectBankMatchResult.md)
 - [ConnectBankMatchResultBankMatchResults](docs/ConnectBankMatchResultBankMatchResults.md)
 - [ConnectBankMatchTotals](docs/ConnectBankMatchTotals.md)
 - [ConnectCcdsAggregations](docs/ConnectCcdsAggregations.md)
 - [ConnectCcdsAggregationsPerOrganisationAggregations](docs/ConnectCcdsAggregationsPerOrganisationAggregations.md)
 - [ConnectCcdsAggregationsTotalCreditCards](docs/ConnectCcdsAggregationsTotalCreditCards.md)
 - [ConnectCcdsAggregationsTotalLoans](docs/ConnectCcdsAggregationsTotalLoans.md)
 - [ConnectCcdsFacilities](docs/ConnectCcdsFacilities.md)
 - [ConnectCcdsFinancialIndicatorData](docs/ConnectCcdsFinancialIndicatorData.md)
 - [ConnectCcdsFootprintDataFinance](docs/ConnectCcdsFootprintDataFinance.md)
 - [ConnectCcdsFullHistory](docs/ConnectCcdsFullHistory.md)
 - [ConnectCcdsHistory](docs/ConnectCcdsHistory.md)
 - [ConnectCcdsIndicatorDataFinance](docs/ConnectCcdsIndicatorDataFinance.md)
 - [ConnectCcdsOverallAggregations](docs/ConnectCcdsOverallAggregations.md)
 - [ConnectCompanySearchNoResults](docs/ConnectCompanySearchNoResults.md)
 - [ConnectCompanySearchSearchCriteria](docs/ConnectCompanySearchSearchCriteria.md)
 - [ConnectConfidenceMatchMatchResults](docs/ConnectConfidenceMatchMatchResults.md)
 - [ConnectConfidenceMatchMatchResultsAddress](docs/ConnectConfidenceMatchMatchResultsAddress.md)
 - [ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan](docs/ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.md)
 - [ConnectConfidenceMatchMatchResultsMatchedCompanies](docs/ConnectConfidenceMatchMatchResultsMatchedCompanies.md)
 - [ConnectConfidenceMatchNoResults](docs/ConnectConfidenceMatchNoResults.md)
 - [ConnectCreditSafeCcdsCompany](docs/ConnectCreditSafeCcdsCompany.md)
 - [ConnectDataCleaningArchiveJobRequest](docs/ConnectDataCleaningArchiveJobRequest.md)
 - [ConnectDataCleaningArchiveResponse](docs/ConnectDataCleaningArchiveResponse.md)
 - [ConnectDataCleaningCreateJobRequest](docs/ConnectDataCleaningCreateJobRequest.md)
 - [ConnectDataCleaningEnrichRequest](docs/ConnectDataCleaningEnrichRequest.md)
 - [ConnectDataCleaningJob](docs/ConnectDataCleaningJob.md)
 - [ConnectDataCleaningJobJobEnrichmentSettings](docs/ConnectDataCleaningJobJobEnrichmentSettings.md)
 - [ConnectDataCleaningJobJobSummary](docs/ConnectDataCleaningJobJobSummary.md)
 - [ConnectDataCleaningMappingResponse](docs/ConnectDataCleaningMappingResponse.md)
 - [ConnectDataCleaningMappingResponseInner](docs/ConnectDataCleaningMappingResponseInner.md)
 - [ConnectDataCleaningResponse](docs/ConnectDataCleaningResponse.md)
 - [ConnectDataCleaningSubmitJobRequest](docs/ConnectDataCleaningSubmitJobRequest.md)
 - [ConnectDataCleaningUpdateMappingsRequest](docs/ConnectDataCleaningUpdateMappingsRequest.md)
 - [ConnectDataCleaningUploadResponse](docs/ConnectDataCleaningUploadResponse.md)
 - [ConnectDecisionEngineDecisionLogResponse](docs/ConnectDecisionEngineDecisionLogResponse.md)
 - [ConnectDecisionEngineDecisionLogResponseResponse](docs/ConnectDecisionEngineDecisionLogResponseResponse.md)
 - [ConnectDecisionEngineGUIDListResponse](docs/ConnectDecisionEngineGUIDListResponse.md)
 - [ConnectDecisionEngineGUIDListResponseGUIDList](docs/ConnectDecisionEngineGUIDListResponseGUIDList.md)
 - [ConnectDecisionEnginePatchDecisionOutcomeRequest](docs/ConnectDecisionEnginePatchDecisionOutcomeRequest.md)
 - [ConnectDecisionEnginePatchDecisionOutcomeRequestDecisionOutcomes](docs/ConnectDecisionEnginePatchDecisionOutcomeRequestDecisionOutcomes.md)
 - [ConnectDecisionEngineRunDecisionResponse](docs/ConnectDecisionEngineRunDecisionResponse.md)
 - [ConnectDecisionEngineRunDecisionResponseAudits](docs/ConnectDecisionEngineRunDecisionResponseAudits.md)
 - [ConnectDecisionEngineUpdateDecisionRequest](docs/ConnectDecisionEngineUpdateDecisionRequest.md)
 - [ConnectDecisionEngineUsageLogResponse](docs/ConnectDecisionEngineUsageLogResponse.md)
 - [ConnectDecisionEngineUsageLogResponseResponse](docs/ConnectDecisionEngineUsageLogResponseResponse.md)
 - [ConnectDecisionEngineUsageLogResponseResponseAudits](docs/ConnectDecisionEngineUsageLogResponseResponseAudits.md)
 - [ConnectDecisionEngineUsageLogResponseUsageLog](docs/ConnectDecisionEngineUsageLogResponseUsageLog.md)
 - [ConnectDecisionEngineUserDataFieldsResponse](docs/ConnectDecisionEngineUserDataFieldsResponse.md)
 - [ConnectDecisionEngineUserDataFieldsResponseDropdownDetails](docs/ConnectDecisionEngineUserDataFieldsResponseDropdownDetails.md)
 - [ConnectDecisionEngineUserDataFieldsResponseFields](docs/ConnectDecisionEngineUserDataFieldsResponseFields.md)
 - [ConnectDecisionEngineUserDataFieldsResponseValidation](docs/ConnectDecisionEngineUserDataFieldsResponseValidation.md)
 - [ConnectErrorResponsesAccessForbidden](docs/ConnectErrorResponsesAccessForbidden.md)
 - [ConnectErrorResponsesBadRequest](docs/ConnectErrorResponsesBadRequest.md)
 - [ConnectErrorResponsesInvalidToken](docs/ConnectErrorResponsesInvalidToken.md)
 - [ConnectErrorResponsesResourceNotFoundRequest](docs/ConnectErrorResponsesResourceNotFoundRequest.md)
 - [ConnectFootprintDataFinance](docs/ConnectFootprintDataFinance.md)
 - [ConnectFootprintDataFinanceCreditSafe](docs/ConnectFootprintDataFinanceCreditSafe.md)
 - [ConnectFootprintDataFinanceFootprintData](docs/ConnectFootprintDataFinanceFootprintData.md)
 - [ConnectFootprintDataFinanceFootprintDataYear](docs/ConnectFootprintDataFinanceFootprintDataYear.md)
 - [ConnectFootprintDataFinanceFootprintDataYearMonth](docs/ConnectFootprintDataFinanceFootprintDataYearMonth.md)
 - [ConnectFootprintDataFinanceIndicatorData](docs/ConnectFootprintDataFinanceIndicatorData.md)
 - [ConnectFootprintDataFinanceIndicatorDataYear](docs/ConnectFootprintDataFinanceIndicatorDataYear.md)
 - [ConnectFootprintIndicatorData](docs/ConnectFootprintIndicatorData.md)
 - [ConnectFootprintIndicatorDataFinancialIndicator](docs/ConnectFootprintIndicatorDataFinancialIndicator.md)
 - [ConnectFootprintIndicatorDataFinancialIndicatorYear](docs/ConnectFootprintIndicatorDataFinancialIndicatorYear.md)
 - [ConnectFootprintIndicatorDataFootprintData](docs/ConnectFootprintIndicatorDataFootprintData.md)
 - [ConnectFreshInvCompletedInvestigation](docs/ConnectFreshInvCompletedInvestigation.md)
 - [ConnectFreshInvCompletedInvestigationContactDetails](docs/ConnectFreshInvCompletedInvestigationContactDetails.md)
 - [ConnectFreshInvCompletedInvestigationSearchCriteria](docs/ConnectFreshInvCompletedInvestigationSearchCriteria.md)
 - [ConnectFreshInvCompletedInvestigationSearchCriteriaAddress](docs/ConnectFreshInvCompletedInvestigationSearchCriteriaAddress.md)
 - [ConnectFreshInvCompletedInvestigationStatus](docs/ConnectFreshInvCompletedInvestigationStatus.md)
 - [ConnectFreshInvCreateInvestigation](docs/ConnectFreshInvCreateInvestigation.md)
 - [ConnectFreshInvCreateInvestigationContactInfo](docs/ConnectFreshInvCreateInvestigationContactInfo.md)
 - [ConnectFreshInvCreateInvestigationContactInfoCompany](docs/ConnectFreshInvCreateInvestigationContactInfoCompany.md)
 - [ConnectFreshInvCreateInvestigationSearchCriteria](docs/ConnectFreshInvCreateInvestigationSearchCriteria.md)
 - [ConnectFreshInvCreateInvestigationSearchCriteriaAddress](docs/ConnectFreshInvCreateInvestigationSearchCriteriaAddress.md)
 - [ConnectFreshInvInvestigationCompanyData](docs/ConnectFreshInvInvestigationCompanyData.md)
 - [ConnectFreshInvInvestigationCompanyDataAddress](docs/ConnectFreshInvInvestigationCompanyDataAddress.md)
 - [ConnectFreshInvInvestigationConfirmed](docs/ConnectFreshInvInvestigationConfirmed.md)
 - [ConnectFreshInvInvestigationContactInfo](docs/ConnectFreshInvInvestigationContactInfo.md)
 - [ConnectFreshInvInvestigationContactInfoCompany](docs/ConnectFreshInvInvestigationContactInfoCompany.md)
 - [ConnectFreshInvListInvestigations](docs/ConnectFreshInvListInvestigations.md)
 - [ConnectFreshInvListInvestigationsContactDetails](docs/ConnectFreshInvListInvestigationsContactDetails.md)
 - [ConnectFreshInvListInvestigationsOrders](docs/ConnectFreshInvListInvestigationsOrders.md)
 - [ConnectFreshInvListInvestigationsSearchCriteria](docs/ConnectFreshInvListInvestigationsSearchCriteria.md)
 - [ConnectFreshInvListInvestigationsStatus](docs/ConnectFreshInvListInvestigationsStatus.md)
 - [ConnectFullFinanceData](docs/ConnectFullFinanceData.md)
 - [ConnectFullFinanceDataFinancialIndicator](docs/ConnectFullFinanceDataFinancialIndicator.md)
 - [ConnectFullFinanceDataFinancialIndicatorYear](docs/ConnectFullFinanceDataFinancialIndicatorYear.md)
 - [ConnectFullFinanceDataFootprintData](docs/ConnectFullFinanceDataFootprintData.md)
 - [ConnectFullFinanceDataFootprintDataYear](docs/ConnectFullFinanceDataFootprintDataYear.md)
 - [ConnectIdentityAMLMultiBureauSearchRequest](docs/ConnectIdentityAMLMultiBureauSearchRequest.md)
 - [ConnectIdentityAMLSearchRequest](docs/ConnectIdentityAMLSearchRequest.md)
 - [ConnectIdentityAction](docs/ConnectIdentityAction.md)
 - [ConnectIdentityAddress](docs/ConnectIdentityAddress.md)
 - [ConnectIdentityAddress1](docs/ConnectIdentityAddress1.md)
 - [ConnectIdentityAddressList](docs/ConnectIdentityAddressList.md)
 - [ConnectIdentityAmlCommonSearchCriteria](docs/ConnectIdentityAmlCommonSearchCriteria.md)
 - [ConnectIdentityAmlMultiBureauSearchCriteria](docs/ConnectIdentityAmlMultiBureauSearchCriteria.md)
 - [ConnectIdentityAmlResultCode](docs/ConnectIdentityAmlResultCode.md)
 - [ConnectIdentityAmlSearchCriteria](docs/ConnectIdentityAmlSearchCriteria.md)
 - [ConnectIdentityAmlSearchResult](docs/ConnectIdentityAmlSearchResult.md)
 - [ConnectIdentityAmlSupplierResult](docs/ConnectIdentityAmlSupplierResult.md)
 - [ConnectIdentityAmlSupplierResultResultCodes](docs/ConnectIdentityAmlSupplierResultResultCodes.md)
 - [ConnectIdentityBankAccountDetails](docs/ConnectIdentityBankAccountDetails.md)
 - [ConnectIdentityBasicResponse](docs/ConnectIdentityBasicResponse.md)
 - [ConnectIdentityBatchSearchRequest](docs/ConnectIdentityBatchSearchRequest.md)
 - [ConnectIdentityCameoResponse](docs/ConnectIdentityCameoResponse.md)
 - [ConnectIdentityCommonResult](docs/ConnectIdentityCommonResult.md)
 - [ConnectIdentityCommonSearchCriteria](docs/ConnectIdentityCommonSearchCriteria.md)
 - [ConnectIdentityConsumerCommonSearchCriteria](docs/ConnectIdentityConsumerCommonSearchCriteria.md)
 - [ConnectIdentityConsumerSearchCriteria](docs/ConnectIdentityConsumerSearchCriteria.md)
 - [ConnectIdentityConsumerSearchResult](docs/ConnectIdentityConsumerSearchResult.md)
 - [ConnectIdentityConsumerSearchResultCommon](docs/ConnectIdentityConsumerSearchResultCommon.md)
 - [ConnectIdentityConsumerSearchResultConsumerResult](docs/ConnectIdentityConsumerSearchResultConsumerResult.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddressResidents](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddressResidents.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionSocialClassComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionSocialClassComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionTenureComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionTenureComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionUnemploymentComposition](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionUnemploymentComposition.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareAccounts](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareAccounts.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHistory](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHistory.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetails](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetails.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetailsAddress](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetailsAddress.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareIndebtedness](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareIndebtedness.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSummary](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSummary.md)
 - [ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSupplierDetails](docs/ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSupplierDetails.md)
 - [ConnectIdentityConsumerSearchResultInput](docs/ConnectIdentityConsumerSearchResultInput.md)
 - [ConnectIdentityConsumerSearchResultInputCommon](docs/ConnectIdentityConsumerSearchResultInputCommon.md)
 - [ConnectIdentityConsumerSearchResultInputCommonPerson](docs/ConnectIdentityConsumerSearchResultInputCommonPerson.md)
 - [ConnectIdentityConsumerSearchResultInputCommonPersonAddresses](docs/ConnectIdentityConsumerSearchResultInputCommonPersonAddresses.md)
 - [ConnectIdentityConsumerSearchResultInputConsumer](docs/ConnectIdentityConsumerSearchResultInputConsumer.md)
 - [ConnectIdentityConsumerSearchResultInputIdAml](docs/ConnectIdentityConsumerSearchResultInputIdAml.md)
 - [ConnectIdentityCreditReport](docs/ConnectIdentityCreditReport.md)
 - [ConnectIdentityCreditScore](docs/ConnectIdentityCreditScore.md)
 - [ConnectIdentityCurrentName](docs/ConnectIdentityCurrentName.md)
 - [ConnectIdentityDateType](docs/ConnectIdentityDateType.md)
 - [ConnectIdentityDemographic](docs/ConnectIdentityDemographic.md)
 - [ConnectIdentityDemographicsNeighbourhoodDefinition](docs/ConnectIdentityDemographicsNeighbourhoodDefinition.md)
 - [ConnectIdentityDemographicsPropertyComposition](docs/ConnectIdentityDemographicsPropertyComposition.md)
 - [ConnectIdentityDemographicsShareholderComposition](docs/ConnectIdentityDemographicsShareholderComposition.md)
 - [ConnectIdentityDemographicsUnemploymentComposition](docs/ConnectIdentityDemographicsUnemploymentComposition.md)
 - [ConnectIdentityDriversLicense](docs/ConnectIdentityDriversLicense.md)
 - [ConnectIdentityElectricitySupplier](docs/ConnectIdentityElectricitySupplier.md)
 - [ConnectIdentityEuropeanIDCard](docs/ConnectIdentityEuropeanIDCard.md)
 - [ConnectIdentityGender](docs/ConnectIdentityGender.md)
 - [ConnectIdentityHistoryListResponse](docs/ConnectIdentityHistoryListResponse.md)
 - [ConnectIdentityIdAml](docs/ConnectIdentityIdAml.md)
 - [ConnectIdentityIdAmlResult](docs/ConnectIdentityIdAmlResult.md)
 - [ConnectIdentityIdentityHistoryItem](docs/ConnectIdentityIdentityHistoryItem.md)
 - [ConnectIdentityInputResponse](docs/ConnectIdentityInputResponse.md)
 - [ConnectIdentityInsolvencyRestriction](docs/ConnectIdentityInsolvencyRestriction.md)
 - [ConnectIdentityMappedDocuments](docs/ConnectIdentityMappedDocuments.md)
 - [ConnectIdentityMappedPepMatch](docs/ConnectIdentityMappedPepMatch.md)
 - [ConnectIdentityMappedResultCode](docs/ConnectIdentityMappedResultCode.md)
 - [ConnectIdentityMappedResultCodeDetails](docs/ConnectIdentityMappedResultCodeDetails.md)
 - [ConnectIdentityMappedSanctionDetail](docs/ConnectIdentityMappedSanctionDetail.md)
 - [ConnectIdentityMappedSanctionMatch](docs/ConnectIdentityMappedSanctionMatch.md)
 - [ConnectIdentityMatchValue](docs/ConnectIdentityMatchValue.md)
 - [ConnectIdentityMultiBureauAmlSearchResult](docs/ConnectIdentityMultiBureauAmlSearchResult.md)
 - [ConnectIdentityMultiBureauAmlSupplierResult](docs/ConnectIdentityMultiBureauAmlSupplierResult.md)
 - [ConnectIdentityMultiBureauAmlSupplierResultResultCodes](docs/ConnectIdentityMultiBureauAmlSupplierResultResultCodes.md)
 - [ConnectIdentityNINumber](docs/ConnectIdentityNINumber.md)
 - [ConnectIdentityName](docs/ConnectIdentityName.md)
 - [ConnectIdentityPassport](docs/ConnectIdentityPassport.md)
 - [ConnectIdentityPepDetails](docs/ConnectIdentityPepDetails.md)
 - [ConnectIdentityPepOrSanction](docs/ConnectIdentityPepOrSanction.md)
 - [ConnectIdentityPepSanctionAddress](docs/ConnectIdentityPepSanctionAddress.md)
 - [ConnectIdentityPepSanctionDate](docs/ConnectIdentityPepSanctionDate.md)
 - [ConnectIdentityPerson](docs/ConnectIdentityPerson.md)
 - [ConnectIdentityPicklist](docs/ConnectIdentityPicklist.md)
 - [ConnectIdentityPicklistInputs](docs/ConnectIdentityPicklistInputs.md)
 - [ConnectIdentityPicklistOption](docs/ConnectIdentityPicklistOption.md)
 - [ConnectIdentityProduct](docs/ConnectIdentityProduct.md)
 - [ConnectIdentityReasonCode](docs/ConnectIdentityReasonCode.md)
 - [ConnectIdentityReasonResponse](docs/ConnectIdentityReasonResponse.md)
 - [ConnectIdentityReportAddress](docs/ConnectIdentityReportAddress.md)
 - [ConnectIdentityReportAlias](docs/ConnectIdentityReportAlias.md)
 - [ConnectIdentityReportAssociate](docs/ConnectIdentityReportAssociate.md)
 - [ConnectIdentityReportCifas](docs/ConnectIdentityReportCifas.md)
 - [ConnectIdentityReportCreditSearchesAtCurrentAddress](docs/ConnectIdentityReportCreditSearchesAtCurrentAddress.md)
 - [ConnectIdentityReportDemographics](docs/ConnectIdentityReportDemographics.md)
 - [ConnectIdentityReportElectoralRollHistory](docs/ConnectIdentityReportElectoralRollHistory.md)
 - [ConnectIdentityReportHistory](docs/ConnectIdentityReportHistory.md)
 - [ConnectIdentityReportInsolvency](docs/ConnectIdentityReportInsolvency.md)
 - [ConnectIdentityReportInsolvencyAtAddress](docs/ConnectIdentityReportInsolvencyAtAddress.md)
 - [ConnectIdentityReportJudgement](docs/ConnectIdentityReportJudgement.md)
 - [ConnectIdentityReportLinks](docs/ConnectIdentityReportLinks.md)
 - [ConnectIdentityReportMatchedData](docs/ConnectIdentityReportMatchedData.md)
 - [ConnectIdentityReportNotice](docs/ConnectIdentityReportNotice.md)
 - [ConnectIdentityReportResidencyConfirmation](docs/ConnectIdentityReportResidencyConfirmation.md)
 - [ConnectIdentityReportResident](docs/ConnectIdentityReportResident.md)
 - [ConnectIdentityReportRtr](docs/ConnectIdentityReportRtr.md)
 - [ConnectIdentityReportShareAccount](docs/ConnectIdentityReportShareAccount.md)
 - [ConnectIdentityReportSummaryJudgements](docs/ConnectIdentityReportSummaryJudgements.md)
 - [ConnectIdentityReportUndeclaredAddress](docs/ConnectIdentityReportUndeclaredAddress.md)
 - [ConnectIdentityRevalidateRequest](docs/ConnectIdentityRevalidateRequest.md)
 - [ConnectIdentitySearchResult](docs/ConnectIdentitySearchResult.md)
 - [ConnectIdentitySetReasonRequest](docs/ConnectIdentitySetReasonRequest.md)
 - [ConnectIdentityShareAccountDefault](docs/ConnectIdentityShareAccountDefault.md)
 - [ConnectIdentityShareAccountDelinquency](docs/ConnectIdentityShareAccountDelinquency.md)
 - [ConnectIdentityShareAccountDetails](docs/ConnectIdentityShareAccountDetails.md)
 - [ConnectIdentityShareAccountHistory](docs/ConnectIdentityShareAccountHistory.md)
 - [ConnectIdentityShareAccountHistoryBatch](docs/ConnectIdentityShareAccountHistoryBatch.md)
 - [ConnectIdentityShareAccountHolderDetails](docs/ConnectIdentityShareAccountHolderDetails.md)
 - [ConnectIdentityShareAccountSupplierDetails](docs/ConnectIdentityShareAccountSupplierDetails.md)
 - [ConnectIdentitySummary](docs/ConnectIdentitySummary.md)
 - [ConnectIdentitySummaryAddress](docs/ConnectIdentitySummaryAddress.md)
 - [ConnectIdentitySummaryBehaviouralData](docs/ConnectIdentitySummaryBehaviouralData.md)
 - [ConnectIdentitySummaryCardData](docs/ConnectIdentitySummaryCardData.md)
 - [ConnectIdentitySummaryIch](docs/ConnectIdentitySummaryIch.md)
 - [ConnectIdentitySummaryInDebt](docs/ConnectIdentitySummaryInDebt.md)
 - [ConnectIdentitySummaryLinks](docs/ConnectIdentitySummaryLinks.md)
 - [ConnectIdentitySummaryShare](docs/ConnectIdentitySummaryShare.md)
 - [ConnectIdentitySummaryThirdParty](docs/ConnectIdentitySummaryThirdParty.md)
 - [ConnectIdentitySupplier](docs/ConnectIdentitySupplier.md)
 - [ConnectIdentitySupplierDetails](docs/ConnectIdentitySupplierDetails.md)
 - [ConnectIdentitySupplierResult](docs/ConnectIdentitySupplierResult.md)
 - [ConnectIdentityThirdPartyAlerts](docs/ConnectIdentityThirdPartyAlerts.md)
 - [ConnectIdentityTransUnionResult](docs/ConnectIdentityTransUnionResult.md)
 - [ConnectIdentityUpdateUserPackage](docs/ConnectIdentityUpdateUserPackage.md)
 - [ConnectImagesCompanyImageTypes](docs/ConnectImagesCompanyImageTypes.md)
 - [ConnectImagesCompanyImageTypesInner](docs/ConnectImagesCompanyImageTypesInner.md)
 - [ConnectImagesCompanyImages](docs/ConnectImagesCompanyImages.md)
 - [ConnectImagesCompanyImagesCompany](docs/ConnectImagesCompanyImagesCompany.md)
 - [ConnectImagesCompanyImagesData](docs/ConnectImagesCompanyImagesData.md)
 - [ConnectImagesCompanyImagesDocument](docs/ConnectImagesCompanyImagesDocument.md)
 - [ConnectImagesCompanyImagesLocalProperties](docs/ConnectImagesCompanyImagesLocalProperties.md)
 - [ConnectIndicatorData](docs/ConnectIndicatorData.md)
 - [ConnectIndicatorDataFinancialIndicator](docs/ConnectIndicatorDataFinancialIndicator.md)
 - [ConnectIndicatorDataFootprintData](docs/ConnectIndicatorDataFootprintData.md)
 - [ConnectMonitoringAddCompanyToPortfolioRequest](docs/ConnectMonitoringAddCompanyToPortfolioRequest.md)
 - [ConnectMonitoringAddCompanyToPortfolioResponse](docs/ConnectMonitoringAddCompanyToPortfolioResponse.md)
 - [ConnectMonitoringAllNotificationsEvents](docs/ConnectMonitoringAllNotificationsEvents.md)
 - [ConnectMonitoringAllNotificationsEventsData](docs/ConnectMonitoringAllNotificationsEventsData.md)
 - [ConnectMonitoringClearCompaniesRequest](docs/ConnectMonitoringClearCompaniesRequest.md)
 - [ConnectMonitoringClearCompaniesResponse](docs/ConnectMonitoringClearCompaniesResponse.md)
 - [ConnectMonitoringCompaniesInAPortfolio](docs/ConnectMonitoringCompaniesInAPortfolio.md)
 - [ConnectMonitoringCompaniesInAPortfolioData](docs/ConnectMonitoringCompaniesInAPortfolioData.md)
 - [ConnectMonitoringCompanyEvents](docs/ConnectMonitoringCompanyEvents.md)
 - [ConnectMonitoringCompanyEventsData](docs/ConnectMonitoringCompanyEventsData.md)
 - [ConnectMonitoringCompanyInfo](docs/ConnectMonitoringCompanyInfo.md)
 - [ConnectMonitoringCopyAndMoveCompaniesBodyCompanies](docs/ConnectMonitoringCopyAndMoveCompaniesBodyCompanies.md)
 - [ConnectMonitoringCopyAndMoveCompaniesRequest](docs/ConnectMonitoringCopyAndMoveCompaniesRequest.md)
 - [ConnectMonitoringCopyAndMoveCompaniesResponse](docs/ConnectMonitoringCopyAndMoveCompaniesResponse.md)
 - [ConnectMonitoringCopyAndMoveCompaniesResponseData](docs/ConnectMonitoringCopyAndMoveCompaniesResponseData.md)
 - [ConnectMonitoringCreatePortfolioRequest](docs/ConnectMonitoringCreatePortfolioRequest.md)
 - [ConnectMonitoringCreatePortfolioRequestEmails](docs/ConnectMonitoringCreatePortfolioRequestEmails.md)
 - [ConnectMonitoringCreatePortfolioResponse](docs/ConnectMonitoringCreatePortfolioResponse.md)
 - [ConnectMonitoringDeleteCompanyFromPortfolio](docs/ConnectMonitoringDeleteCompanyFromPortfolio.md)
 - [ConnectMonitoringDeletePortfolio](docs/ConnectMonitoringDeletePortfolio.md)
 - [ConnectMonitoringEventRulesResponse](docs/ConnectMonitoringEventRulesResponse.md)
 - [ConnectMonitoringEventRulesResponseInner](docs/ConnectMonitoringEventRulesResponseInner.md)
 - [ConnectMonitoringGetCompanyFromPortfolio](docs/ConnectMonitoringGetCompanyFromPortfolio.md)
 - [ConnectMonitoringGetPortfolioById](docs/ConnectMonitoringGetPortfolioById.md)
 - [ConnectMonitoringImportAndSyncPortfolioRequest](docs/ConnectMonitoringImportAndSyncPortfolioRequest.md)
 - [ConnectMonitoringImportAndSyncPortfolioResponse](docs/ConnectMonitoringImportAndSyncPortfolioResponse.md)
 - [ConnectMonitoringIsProcessedRequest](docs/ConnectMonitoringIsProcessedRequest.md)
 - [ConnectMonitoringIsProcessedResponse](docs/ConnectMonitoringIsProcessedResponse.md)
 - [ConnectMonitoringIsProcessedResponseData](docs/ConnectMonitoringIsProcessedResponseData.md)
 - [ConnectMonitoringListPortfolioEventRules](docs/ConnectMonitoringListPortfolioEventRules.md)
 - [ConnectMonitoringListPortfolioEventRulesInner](docs/ConnectMonitoringListPortfolioEventRulesInner.md)
 - [ConnectMonitoringListPortfolios](docs/ConnectMonitoringListPortfolios.md)
 - [ConnectMonitoringListPortfoliosData](docs/ConnectMonitoringListPortfoliosData.md)
 - [ConnectMonitoringListPortfoliosDataEmails](docs/ConnectMonitoringListPortfoliosDataEmails.md)
 - [ConnectMonitoringListPortfoliosDataPortfolios](docs/ConnectMonitoringListPortfoliosDataPortfolios.md)
 - [ConnectMonitoringListPortfoliosDataSharedPortfolios](docs/ConnectMonitoringListPortfoliosDataSharedPortfolios.md)
 - [ConnectMonitoringListSharingPermissions](docs/ConnectMonitoringListSharingPermissions.md)
 - [ConnectMonitoringListSharingPermissionsData](docs/ConnectMonitoringListSharingPermissionsData.md)
 - [ConnectMonitoringListSharingPermissionsDataUserPermission](docs/ConnectMonitoringListSharingPermissionsDataUserPermission.md)
 - [ConnectMonitoringMonitoredCountriesInPortfolio](docs/ConnectMonitoringMonitoredCountriesInPortfolio.md)
 - [ConnectMonitoringPaging](docs/ConnectMonitoringPaging.md)
 - [ConnectMonitoringRiskSummary](docs/ConnectMonitoringRiskSummary.md)
 - [ConnectMonitoringSharePortfolioRequest](docs/ConnectMonitoringSharePortfolioRequest.md)
 - [ConnectMonitoringSharePortfolioRequestBody](docs/ConnectMonitoringSharePortfolioRequestBody.md)
 - [ConnectMonitoringSharePortfolioRequestResponse](docs/ConnectMonitoringSharePortfolioRequestResponse.md)
 - [ConnectMonitoringSharePortfolioRequestResponseData](docs/ConnectMonitoringSharePortfolioRequestResponseData.md)
 - [ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest](docs/ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest.md)
 - [ConnectMonitoringUpdateCompanyInPortfolio](docs/ConnectMonitoringUpdateCompanyInPortfolio.md)
 - [ConnectMonitoringUpdateEventRulesBody](docs/ConnectMonitoringUpdateEventRulesBody.md)
 - [ConnectMonitoringUpdateEventRulesRequest](docs/ConnectMonitoringUpdateEventRulesRequest.md)
 - [ConnectMonitoringUpdatePortfolioRequest](docs/ConnectMonitoringUpdatePortfolioRequest.md)
 - [ConnectMonitoringUpdatePortfolioRequestEmail](docs/ConnectMonitoringUpdatePortfolioRequestEmail.md)
 - [ConnectMonitoringUserDetails](docs/ConnectMonitoringUserDetails.md)
 - [ConnectMonitoringUserDetailsInner](docs/ConnectMonitoringUserDetailsInner.md)
 - [ConnectProtectAddress](docs/ConnectProtectAddress.md)
 - [ConnectProtectAlertsFrequency](docs/ConnectProtectAlertsFrequency.md)
 - [ConnectProtectAuditDto](docs/ConnectProtectAuditDto.md)
 - [ConnectProtectAuditExportPayloadDto](docs/ConnectProtectAuditExportPayloadDto.md)
 - [ConnectProtectAuditExportRequestDto](docs/ConnectProtectAuditExportRequestDto.md)
 - [ConnectProtectAuditsExportResponseDto](docs/ConnectProtectAuditsExportResponseDto.md)
 - [ConnectProtectCreateInvestigationQueryDto](docs/ConnectProtectCreateInvestigationQueryDto.md)
 - [ConnectProtectCreateInvestigationRecordBody](docs/ConnectProtectCreateInvestigationRecordBody.md)
 - [ConnectProtectCreateProfileDto](docs/ConnectProtectCreateProfileDto.md)
 - [ConnectProtectCreateScheduleRequest](docs/ConnectProtectCreateScheduleRequest.md)
 - [ConnectProtectErrorResponsesAccessForbidden](docs/ConnectProtectErrorResponsesAccessForbidden.md)
 - [ConnectProtectGetInvestigationFileBodyDto](docs/ConnectProtectGetInvestigationFileBodyDto.md)
 - [ConnectProtectInvestigation](docs/ConnectProtectInvestigation.md)
 - [ConnectProtectInvestigationFileResponse](docs/ConnectProtectInvestigationFileResponse.md)
 - [ConnectProtectInvestigationQuery](docs/ConnectProtectInvestigationQuery.md)
 - [ConnectProtectInvestigationResponse](docs/ConnectProtectInvestigationResponse.md)
 - [ConnectProtectInvestigationType](docs/ConnectProtectInvestigationType.md)
 - [ConnectProtectListAllInvestigationsCurrentAlert](docs/ConnectProtectListAllInvestigationsCurrentAlert.md)
 - [ConnectProtectProblemDetails](docs/ConnectProtectProblemDetails.md)
 - [ConnectProtectProfile](docs/ConnectProtectProfile.md)
 - [ConnectProtectRecord](docs/ConnectProtectRecord.md)
 - [ConnectProtectSchedule](docs/ConnectProtectSchedule.md)
 - [ConnectResourceNotFoundErrorResponse](docs/ConnectResourceNotFoundErrorResponse.md)
 - [ConnectUSLocalSolutionsFreshInvCreateInvestigation](docs/ConnectUSLocalSolutionsFreshInvCreateInvestigation.md)
 - [ConnectUSLocalSolutionsFreshInvCreateInvestigationFormData](docs/ConnectUSLocalSolutionsFreshInvCreateInvestigationFormData.md)
 - [ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody](docs/ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.md)
 - [ConnectUpdateFreshInvestigation](docs/ConnectUpdateFreshInvestigation.md)
 - [ConnectUpdateFreshInvestigationPendingInfo](docs/ConnectUpdateFreshInvestigationPendingInfo.md)
 - [ConsumerCommonAddress](docs/ConsumerCommonAddress.md)
 - [ConsumerCommonCurrentAddress](docs/ConsumerCommonCurrentAddress.md)
 - [ConsumerCommonName](docs/ConsumerCommonName.md)
 - [ConsumerResultElectoralRollHistory](docs/ConsumerResultElectoralRollHistory.md)
 - [ConsumerResultHistory](docs/ConsumerResultHistory.md)
 - [ConsumerResultHistoryAddress](docs/ConsumerResultHistoryAddress.md)
 - [ConsumerResultInsolvencies](docs/ConsumerResultInsolvencies.md)
 - [ConsumerResultInsolvenciesAddress](docs/ConsumerResultInsolvenciesAddress.md)
 - [ConsumerResultInsolvenciesRestriction](docs/ConsumerResultInsolvenciesRestriction.md)
 - [ConsumerResultJudgements](docs/ConsumerResultJudgements.md)
 - [ConsumerResultJudgementsAddress](docs/ConsumerResultJudgementsAddress.md)
 - [ConsumerResultLinkAliases](docs/ConsumerResultLinkAliases.md)
 - [ConsumerResultLinkAssociates](docs/ConsumerResultLinkAssociates.md)
 - [ConsumerResultLinksUndeclaredAddresses](docs/ConsumerResultLinksUndeclaredAddresses.md)
 - [ConsumerResultLinksUndeclaredAddressesSupplierDetails](docs/ConsumerResultLinksUndeclaredAddressesSupplierDetails.md)
 - [ConsumerResultNotices](docs/ConsumerResultNotices.md)
 - [ConsumerResultReportSummary](docs/ConsumerResultReportSummary.md)
 - [ConsumerResultReportSummaryAddress](docs/ConsumerResultReportSummaryAddress.md)
 - [ConsumerResultReportSummaryCardData](docs/ConsumerResultReportSummaryCardData.md)
 - [ConsumerResultReportSummaryCreditSearchesAtCurrentAddress](docs/ConsumerResultReportSummaryCreditSearchesAtCurrentAddress.md)
 - [ConsumerResultReportSummaryImpairedCreditHistory](docs/ConsumerResultReportSummaryImpairedCreditHistory.md)
 - [ConsumerResultReportSummaryInsolvencyAtAddress](docs/ConsumerResultReportSummaryInsolvencyAtAddress.md)
 - [ConsumerResultReportSummaryJudgements](docs/ConsumerResultReportSummaryJudgements.md)
 - [ConsumerResultReportSummaryLinks](docs/ConsumerResultReportSummaryLinks.md)
 - [ConsumerResultReportSummaryMatchedData](docs/ConsumerResultReportSummaryMatchedData.md)
 - [ConsumerResultReportSummaryResidency](docs/ConsumerResultReportSummaryResidency.md)
 - [ConsumerResultReportSummaryThirdParty](docs/ConsumerResultReportSummaryThirdParty.md)
 - [ConsumerSearch](docs/ConsumerSearch.md)
 - [CountryOption](docs/CountryOption.md)
 - [CreateInvestigationNoteDto](docs/CreateInvestigationNoteDto.md)
 - [CreateInvestigationQueryDto](docs/CreateInvestigationQueryDto.md)
 - [CreateInvestigationRecordBody](docs/CreateInvestigationRecordBody.md)
 - [CreateScheduleDto](docs/CreateScheduleDto.md)
 - [CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment](docs/CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment.md)
 - [CreditsafeGlobalDataAddressCriteriaSchema](docs/CreditsafeGlobalDataAddressCriteriaSchema.md)
 - [CreditsafeGlobalDataAddressData](docs/CreditsafeGlobalDataAddressData.md)
 - [CreditsafeGlobalDataAddressDataReport](docs/CreditsafeGlobalDataAddressDataReport.md)
 - [CreditsafeGlobalDataCompany](docs/CreditsafeGlobalDataCompany.md)
 - [CreditsafeGlobalDataCompanyActivityClassification](docs/CreditsafeGlobalDataCompanyActivityClassification.md)
 - [CreditsafeGlobalDataCompanyData](docs/CreditsafeGlobalDataCompanyData.md)
 - [CreditsafeGlobalDataCompanyDataAdditionalData](docs/CreditsafeGlobalDataCompanyDataAdditionalData.md)
 - [CreditsafeGlobalDataCompanyStatus](docs/CreditsafeGlobalDataCompanyStatus.md)
 - [CreditsafeGlobalDataCompanyType](docs/CreditsafeGlobalDataCompanyType.md)
 - [CreditsafeGlobalDataCoreAttachmentBinaryAttachment](docs/CreditsafeGlobalDataCoreAttachmentBinaryAttachment.md)
 - [CreditsafeGlobalDataCoreSupplierConnectorConsumerReportResponse](docs/CreditsafeGlobalDataCoreSupplierConnectorConsumerReportResponse.md)
 - [CreditsafeGlobalDataCountriesList](docs/CreditsafeGlobalDataCountriesList.md)
 - [CreditsafeGlobalDataCountry](docs/CreditsafeGlobalDataCountry.md)
 - [CreditsafeGlobalDataCountryCode](docs/CreditsafeGlobalDataCountryCode.md)
 - [CreditsafeGlobalDataCurrency](docs/CreditsafeGlobalDataCurrency.md)
 - [CreditsafeGlobalDataCustomDataEntrySchema](docs/CreditsafeGlobalDataCustomDataEntrySchema.md)
 - [CreditsafeGlobalDataCustomDataSchema](docs/CreditsafeGlobalDataCustomDataSchema.md)
 - [CreditsafeGlobalDataDirectorSearchData](docs/CreditsafeGlobalDataDirectorSearchData.md)
 - [CreditsafeGlobalDataDirectorSearchDataCompany](docs/CreditsafeGlobalDataDirectorSearchDataCompany.md)
 - [CreditsafeGlobalDataLanguage](docs/CreditsafeGlobalDataLanguage.md)
 - [CreditsafeGlobalDataMessage](docs/CreditsafeGlobalDataMessage.md)
 - [CreditsafeGlobalDataMessageCode](docs/CreditsafeGlobalDataMessageCode.md)
 - [CreditsafeGlobalDataMessageType](docs/CreditsafeGlobalDataMessageType.md)
 - [CreditsafeGlobalDataOfficeType](docs/CreditsafeGlobalDataOfficeType.md)
 - [CreditsafeGlobalDataQueryMatchType](docs/CreditsafeGlobalDataQueryMatchType.md)
 - [CreditsafeGlobalDataReportsAdditionalData](docs/CreditsafeGlobalDataReportsAdditionalData.md)
 - [CreditsafeGlobalDataReportsAdvisor](docs/CreditsafeGlobalDataReportsAdvisor.md)
 - [CreditsafeGlobalDataReportsBalanceSheet](docs/CreditsafeGlobalDataReportsBalanceSheet.md)
 - [CreditsafeGlobalDataReportsBanker](docs/CreditsafeGlobalDataReportsBanker.md)
 - [CreditsafeGlobalDataReportsCommonRatingValue](docs/CreditsafeGlobalDataReportsCommonRatingValue.md)
 - [CreditsafeGlobalDataReportsCompanyActivity](docs/CreditsafeGlobalDataReportsCompanyActivity.md)
 - [CreditsafeGlobalDataReportsCompanyActivityList](docs/CreditsafeGlobalDataReportsCompanyActivityList.md)
 - [CreditsafeGlobalDataReportsCompanyInGroup](docs/CreditsafeGlobalDataReportsCompanyInGroup.md)
 - [CreditsafeGlobalDataReportsCompanyInGroupAdditionalData](docs/CreditsafeGlobalDataReportsCompanyInGroupAdditionalData.md)
 - [CreditsafeGlobalDataReportsCompanyReport](docs/CreditsafeGlobalDataReportsCompanyReport.md)
 - [CreditsafeGlobalDataReportsCompanyReportExtraSection](docs/CreditsafeGlobalDataReportsCompanyReportExtraSection.md)
 - [CreditsafeGlobalDataReportsCompanyReportResponse](docs/CreditsafeGlobalDataReportsCompanyReportResponse.md)
 - [CreditsafeGlobalDataReportsCompanyStatusDescription](docs/CreditsafeGlobalDataReportsCompanyStatusDescription.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation](docs/CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerCreditRating](docs/CreditsafeGlobalDataReportsConsumerConsumerCreditRating.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerCreditScore](docs/CreditsafeGlobalDataReportsConsumerConsumerCreditScore.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerDirectorship](docs/CreditsafeGlobalDataReportsConsumerConsumerDirectorship.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerIncome](docs/CreditsafeGlobalDataReportsConsumerConsumerIncome.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerInformation](docs/CreditsafeGlobalDataReportsConsumerConsumerInformation.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerInformationAdditionalData](docs/CreditsafeGlobalDataReportsConsumerConsumerInformationAdditionalData.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary](docs/CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment](docs/CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment.md)
 - [CreditsafeGlobalDataReportsConsumerConsumerReport](docs/CreditsafeGlobalDataReportsConsumerConsumerReport.md)
 - [CreditsafeGlobalDataReportsConsumerCriteriaSet](docs/CreditsafeGlobalDataReportsConsumerCriteriaSet.md)
 - [CreditsafeGlobalDataReportsCorporatePosition](docs/CreditsafeGlobalDataReportsCorporatePosition.md)
 - [CreditsafeGlobalDataReportsCorporatePositionAdditionalData](docs/CreditsafeGlobalDataReportsCorporatePositionAdditionalData.md)
 - [CreditsafeGlobalDataReportsCorporatePositionResigned](docs/CreditsafeGlobalDataReportsCorporatePositionResigned.md)
 - [CreditsafeGlobalDataReportsCreditRating](docs/CreditsafeGlobalDataReportsCreditRating.md)
 - [CreditsafeGlobalDataReportsDirector](docs/CreditsafeGlobalDataReportsDirector.md)
 - [CreditsafeGlobalDataReportsDirectorAdditionalData](docs/CreditsafeGlobalDataReportsDirectorAdditionalData.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorReport](docs/CreditsafeGlobalDataReportsDirectorsDirectorReport.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorReportResponse](docs/CreditsafeGlobalDataReportsDirectorsDirectorReportResponse.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorSummary](docs/CreditsafeGlobalDataReportsDirectorsDirectorSummary.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorship](docs/CreditsafeGlobalDataReportsDirectorsDirectorship.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData](docs/CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData.md)
 - [CreditsafeGlobalDataReportsDirectorsDirectorships](docs/CreditsafeGlobalDataReportsDirectorsDirectorships.md)
 - [CreditsafeGlobalDataReportsDirectorship](docs/CreditsafeGlobalDataReportsDirectorship.md)
 - [CreditsafeGlobalDataReportsDirectorships](docs/CreditsafeGlobalDataReportsDirectorships.md)
 - [CreditsafeGlobalDataReportsEmployeeInformation](docs/CreditsafeGlobalDataReportsEmployeeInformation.md)
 - [CreditsafeGlobalDataReportsEntity](docs/CreditsafeGlobalDataReportsEntity.md)
 - [CreditsafeGlobalDataReportsEntityFullName](docs/CreditsafeGlobalDataReportsEntityFullName.md)
 - [CreditsafeGlobalDataReportsEntityType](docs/CreditsafeGlobalDataReportsEntityType.md)
 - [CreditsafeGlobalDataReportsFinancialRatios](docs/CreditsafeGlobalDataReportsFinancialRatios.md)
 - [CreditsafeGlobalDataReportsFinancialValue1SystemDecimal](docs/CreditsafeGlobalDataReportsFinancialValue1SystemDecimal.md)
 - [CreditsafeGlobalDataReportsFinancialValue1SystemString](docs/CreditsafeGlobalDataReportsFinancialValue1SystemString.md)
 - [CreditsafeGlobalDataReportsGender](docs/CreditsafeGlobalDataReportsGender.md)
 - [CreditsafeGlobalDataReportsGlobalFinancialsGGS](docs/CreditsafeGlobalDataReportsGlobalFinancialsGGS.md)
 - [CreditsafeGlobalDataReportsIdType](docs/CreditsafeGlobalDataReportsIdType.md)
 - [CreditsafeGlobalDataReportsIndicatorIndustryComparison](docs/CreditsafeGlobalDataReportsIndicatorIndustryComparison.md)
 - [CreditsafeGlobalDataReportsIndicators](docs/CreditsafeGlobalDataReportsIndicators.md)
 - [CreditsafeGlobalDataReportsIndicatorsInner](docs/CreditsafeGlobalDataReportsIndicatorsInner.md)
 - [CreditsafeGlobalDataReportsLegalForm](docs/CreditsafeGlobalDataReportsLegalForm.md)
 - [CreditsafeGlobalDataReportsLtdCompanyBasicInformation](docs/CreditsafeGlobalDataReportsLtdCompanyBasicInformation.md)
 - [CreditsafeGlobalDataReportsLtdCompanyIdentification](docs/CreditsafeGlobalDataReportsLtdCompanyIdentification.md)
 - [CreditsafeGlobalDataReportsLtdCompanySummary](docs/CreditsafeGlobalDataReportsLtdCompanySummary.md)
 - [CreditsafeGlobalDataReportsLtdContactInformation](docs/CreditsafeGlobalDataReportsLtdContactInformation.md)
 - [CreditsafeGlobalDataReportsLtdCreditScore](docs/CreditsafeGlobalDataReportsLtdCreditScore.md)
 - [CreditsafeGlobalDataReportsLtdDirectors](docs/CreditsafeGlobalDataReportsLtdDirectors.md)
 - [CreditsafeGlobalDataReportsLtdDirectorsExtra](docs/CreditsafeGlobalDataReportsLtdDirectorsExtra.md)
 - [CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra](docs/CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra.md)
 - [CreditsafeGlobalDataReportsLtdFinancialStatement](docs/CreditsafeGlobalDataReportsLtdFinancialStatement.md)
 - [CreditsafeGlobalDataReportsLtdGroupStructure](docs/CreditsafeGlobalDataReportsLtdGroupStructure.md)
 - [CreditsafeGlobalDataReportsLtdOtherInformation](docs/CreditsafeGlobalDataReportsLtdOtherInformation.md)
 - [CreditsafeGlobalDataReportsLtdShareCapitalStructure](docs/CreditsafeGlobalDataReportsLtdShareCapitalStructure.md)
 - [CreditsafeGlobalDataReportsOtherFinancials](docs/CreditsafeGlobalDataReportsOtherFinancials.md)
 - [CreditsafeGlobalDataReportsPreviousDirector](docs/CreditsafeGlobalDataReportsPreviousDirector.md)
 - [CreditsafeGlobalDataReportsPreviousLegalForm](docs/CreditsafeGlobalDataReportsPreviousLegalForm.md)
 - [CreditsafeGlobalDataReportsPreviousName](docs/CreditsafeGlobalDataReportsPreviousName.md)
 - [CreditsafeGlobalDataReportsPreviousValue](docs/CreditsafeGlobalDataReportsPreviousValue.md)
 - [CreditsafeGlobalDataReportsProfitAndLossFigures](docs/CreditsafeGlobalDataReportsProfitAndLossFigures.md)
 - [CreditsafeGlobalDataReportsRangeDescribedValue1SystemString](docs/CreditsafeGlobalDataReportsRangeDescribedValue1SystemString.md)
 - [CreditsafeGlobalDataReportsReportAdditionalInformation](docs/CreditsafeGlobalDataReportsReportAdditionalInformation.md)
 - [CreditsafeGlobalDataReportsReportAlternateSummary](docs/CreditsafeGlobalDataReportsReportAlternateSummary.md)
 - [CreditsafeGlobalDataReportsReportNegativeInformation](docs/CreditsafeGlobalDataReportsReportNegativeInformation.md)
 - [CreditsafeGlobalDataReportsReportNegativeInformationExtra](docs/CreditsafeGlobalDataReportsReportNegativeInformationExtra.md)
 - [CreditsafeGlobalDataReportsReportPaymentData](docs/CreditsafeGlobalDataReportsReportPaymentData.md)
 - [CreditsafeGlobalDataReportsReportPaymentDataExtra](docs/CreditsafeGlobalDataReportsReportPaymentDataExtra.md)
 - [CreditsafeGlobalDataReportsReportSection](docs/CreditsafeGlobalDataReportsReportSection.md)
 - [CreditsafeGlobalDataReportsShareClass](docs/CreditsafeGlobalDataReportsShareClass.md)
 - [CreditsafeGlobalDataReportsShareClassAdditionalData](docs/CreditsafeGlobalDataReportsShareClassAdditionalData.md)
 - [CreditsafeGlobalDataReportsShareHolder](docs/CreditsafeGlobalDataReportsShareHolder.md)
 - [CreditsafeGlobalDataSearchCriteriaSchema](docs/CreditsafeGlobalDataSearchCriteriaSchema.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaBase](docs/CreditsafeGlobalDataSearchCriteriaSchemaBase.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaCountry](docs/CreditsafeGlobalDataSearchCriteriaSchemaCountry.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaCountryDirector](docs/CreditsafeGlobalDataSearchCriteriaSchemaCountryDirector.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaDirector](docs/CreditsafeGlobalDataSearchCriteriaSchemaDirector.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaQueryStringSchema](docs/CreditsafeGlobalDataSearchCriteriaSchemaQueryStringSchema.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaSet](docs/CreditsafeGlobalDataSearchCriteriaSchemaSet.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaSetDirector](docs/CreditsafeGlobalDataSearchCriteriaSchemaSetDirector.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyStatus](docs/CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyStatus.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyType](docs/CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyType.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataOfficeType](docs/CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataOfficeType.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemBoolean](docs/CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemBoolean.md)
 - [CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemString](docs/CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemString.md)
 - [CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataCompany](docs/CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataCompany.md)
 - [CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataDirectorSearchData](docs/CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataDirectorSearchData.md)
 - [CreditsafeGlobalDataServiceResponse](docs/CreditsafeGlobalDataServiceResponse.md)
 - [CreditsafeGlobalDataServiceResponse1CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse](docs/CreditsafeGlobalDataServiceResponse1CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse.md)
 - [CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse](docs/CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderAdditionalDataShareholderDetail](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderAdditionalDataShareholderDetail.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderBeneficialOwnershipReport](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderBeneficialOwnershipReport.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholder](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholder.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderAndBeneficialOwnershipReport](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderAndBeneficialOwnershipReport.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderReport](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderReport.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderStructure](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderStructure.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderSummary](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderSummary.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholding](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholding.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdingAdditionalData](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdingAdditionalData.md)
 - [CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdings](docs/CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdings.md)
 - [CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcyBankruptcyReportResponse](docs/CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcyBankruptcyReportResponse.md)
 - [CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcySearchBankruptcy](docs/CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcySearchBankruptcy.md)
 - [CreditsafeGlobalDataServicesDEDataServiceRawClientShareholdersShareholderReportResponse](docs/CreditsafeGlobalDataServicesDEDataServiceRawClientShareholdersShareholderReportResponse.md)
 - [CreditsafeLocalSolutionsGBLandRegistry](docs/CreditsafeLocalSolutionsGBLandRegistry.md)
 - [CreditsafeUSLocalFIResponse](docs/CreditsafeUSLocalFIResponse.md)
 - [CreditsafeUSLocalFIResponseFreshInvestigationRequestResult](docs/CreditsafeUSLocalFIResponseFreshInvestigationRequestResult.md)
 - [DeleteFreshInvetigationsByOrderId](docs/DeleteFreshInvetigationsByOrderId.md)
 - [DeleteKYCMonitoringProfilesResponse](docs/DeleteKYCMonitoringProfilesResponse.md)
 - [DeleteKYCMonitoringProfilesResponseFailed](docs/DeleteKYCMonitoringProfilesResponseFailed.md)
 - [DeleteKYCMonitoringProfilesResquest](docs/DeleteKYCMonitoringProfilesResquest.md)
 - [DeleteKYCProfileSearchesByProfileIdRequestBody](docs/DeleteKYCProfileSearchesByProfileIdRequestBody.md)
 - [DeleteKYCProfileSearchesByProfileIdResponse](docs/DeleteKYCProfileSearchesByProfileIdResponse.md)
 - [DeleteKYCProfileSearchesByProfileIdResponseError](docs/DeleteKYCProfileSearchesByProfileIdResponseError.md)
 - [DeleteKYCProfileSearchesByProfileIdResponseFailed](docs/DeleteKYCProfileSearchesByProfileIdResponseFailed.md)
 - [DeleteKYCProfiles](docs/DeleteKYCProfiles.md)
 - [DeleteKYCProtectSchedulesResponse](docs/DeleteKYCProtectSchedulesResponse.md)
 - [DeleteKYCProtectSchedulesResponseFailed](docs/DeleteKYCProtectSchedulesResponseFailed.md)
 - [DeleteKeyPartiesResponseByProfileId](docs/DeleteKeyPartiesResponseByProfileId.md)
 - [DeleteKeyPartiesResponseByProfileIdFailedObjectResponse](docs/DeleteKeyPartiesResponseByProfileIdFailedObjectResponse.md)
 - [DeleteKeyPartiesResponseByProfileIdFailedObjectResponseError](docs/DeleteKeyPartiesResponseByProfileIdFailedObjectResponseError.md)
 - [DeleteKeyPartyByIdNoContent](docs/DeleteKeyPartyByIdNoContent.md)
 - [DeleteKeyPartySearchContractRequest](docs/DeleteKeyPartySearchContractRequest.md)
 - [DeleteKeyPartySearchContractRequestItems](docs/DeleteKeyPartySearchContractRequestItems.md)
 - [DeleteKeyPartySearchContractResponse](docs/DeleteKeyPartySearchContractResponse.md)
 - [DeleteKeyPartySearchContractResponseError](docs/DeleteKeyPartySearchContractResponseError.md)
 - [DeleteKeyPartySearchContractResponseFailed](docs/DeleteKeyPartySearchContractResponseFailed.md)
 - [DeleteKeyPartySearchContractResponseFailedItem](docs/DeleteKeyPartySearchContractResponseFailedItem.md)
 - [DeleteRecordsDto](docs/DeleteRecordsDto.md)
 - [DetailsAddressesBody](docs/DetailsAddressesBody.md)
 - [DownloadAttachment](docs/DownloadAttachment.md)
 - [DownloadAttachmentResponse](docs/DownloadAttachmentResponse.md)
 - [FileDownloadResponse](docs/FileDownloadResponse.md)
 - [FreshInvestigationAttachmentUploadForOrderRequest](docs/FreshInvestigationAttachmentUploadForOrderRequest.md)
 - [FreshInvestigationAttachmentUploadForOrderResponse](docs/FreshInvestigationAttachmentUploadForOrderResponse.md)
 - [FreshInvestigationCommentsForOrderRequest](docs/FreshInvestigationCommentsForOrderRequest.md)
 - [FreshInvestigationCommentsForOrderResponse](docs/FreshInvestigationCommentsForOrderResponse.md)
 - [FreshInvestigationGetAttachmentsForOrderResponse](docs/FreshInvestigationGetAttachmentsForOrderResponse.md)
 - [FreshInvestigationGetAttachmentsForOrderResponseAttachments](docs/FreshInvestigationGetAttachmentsForOrderResponseAttachments.md)
 - [GBLocalSolutionBankVerificationSearchRequest](docs/GBLocalSolutionBankVerificationSearchRequest.md)
 - [GBLocalSolutionBankVerificationSearchResponse](docs/GBLocalSolutionBankVerificationSearchResponse.md)
 - [GBLocalSolutionBankVerificationSearchResponseSupplierRequestData](docs/GBLocalSolutionBankVerificationSearchResponseSupplierRequestData.md)
 - [GBLocalSolutionBankVerificationSearchResponseSupplierResponse](docs/GBLocalSolutionBankVerificationSearchResponseSupplierResponse.md)
 - [GBLocalSolutionCPHistoryRequestByIdRequest](docs/GBLocalSolutionCPHistoryRequestByIdRequest.md)
 - [GBLocalSolutionGetHistoryListResponse](docs/GBLocalSolutionGetHistoryListResponse.md)
 - [GBLocalSolutionGetHistoryRequestResponse](docs/GBLocalSolutionGetHistoryRequestResponse.md)
 - [GBLocalSolutionGetHistoryRequestResponseSupplierRequestData](docs/GBLocalSolutionGetHistoryRequestResponseSupplierRequestData.md)
 - [GBLocalSolutionGetHistoryRequestResponseSupplierResponse](docs/GBLocalSolutionGetHistoryRequestResponseSupplierResponse.md)
 - [GenderType](docs/GenderType.md)
 - [GetAuditsResponse](docs/GetAuditsResponse.md)
 - [GetAuditsResponseItems](docs/GetAuditsResponseItems.md)
 - [GetBatchUploadsDownloadErrorsByUploadIdResponse](docs/GetBatchUploadsDownloadErrorsByUploadIdResponse.md)
 - [GetBatchUploadsTemplateResponse](docs/GetBatchUploadsTemplateResponse.md)
 - [GetDecisionEngineDecisionOutcomeResponse](docs/GetDecisionEngineDecisionOutcomeResponse.md)
 - [GetDecisionEngineDecisionOutcomeResponseDecisionOutcomes](docs/GetDecisionEngineDecisionOutcomeResponseDecisionOutcomes.md)
 - [GetDecisionEngineDecisionOutcomeResponseDecisionOutcomesItems](docs/GetDecisionEngineDecisionOutcomeResponseDecisionOutcomesItems.md)
 - [GetDecisionEngineInstancesResponse](docs/GetDecisionEngineInstancesResponse.md)
 - [GetDecisionEngineInstancesResponseInstances](docs/GetDecisionEngineInstancesResponseInstances.md)
 - [GetFreshInvestigationCommentsByOrderIdResponse](docs/GetFreshInvestigationCommentsByOrderIdResponse.md)
 - [GetFreshInvestigationCommentsByOrderIdResponseComments](docs/GetFreshInvestigationCommentsByOrderIdResponseComments.md)
 - [GetIndividualSearchIdHitsResponse](docs/GetIndividualSearchIdHitsResponse.md)
 - [GetIndividualSearchIdHitsResponseItems](docs/GetIndividualSearchIdHitsResponseItems.md)
 - [GetIndividualSearchIdHitsResponseSupersededHit](docs/GetIndividualSearchIdHitsResponseSupersededHit.md)
 - [GetInvestigationFileBodyDto](docs/GetInvestigationFileBodyDto.md)
 - [GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser](docs/GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser.md)
 - [GetKYCIndividualSearchResponse](docs/GetKYCIndividualSearchResponse.md)
 - [GetKYCIndividualSearchResponseItems](docs/GetKYCIndividualSearchResponseItems.md)
 - [GetKYCProfileAttachmentDetailsByAttachmentId](docs/GetKYCProfileAttachmentDetailsByAttachmentId.md)
 - [GetKYCProfileByProfileId](docs/GetKYCProfileByProfileId.md)
 - [GetKYCProfileDetailsByProfileId](docs/GetKYCProfileDetailsByProfileId.md)
 - [GetKYCProfileDetailsByProfileIdTurnover](docs/GetKYCProfileDetailsByProfileIdTurnover.md)
 - [GetKYCProfileNotesByNoteId](docs/GetKYCProfileNotesByNoteId.md)
 - [GetKYCProfileNotesByNoteIdRequest](docs/GetKYCProfileNotesByNoteIdRequest.md)
 - [GetKYCProfileTypes](docs/GetKYCProfileTypes.md)
 - [GetKYCProfiles](docs/GetKYCProfiles.md)
 - [GetKYCProfilesItems](docs/GetKYCProfilesItems.md)
 - [GetKYCProtectProfileIdNoteIdResponse](docs/GetKYCProtectProfileIdNoteIdResponse.md)
 - [GetKYCProtectProfileIdNotesResponse](docs/GetKYCProtectProfileIdNotesResponse.md)
 - [GetKYCProtectProfileIdNotesResponseItems](docs/GetKYCProtectProfileIdNotesResponseItems.md)
 - [GetKeyPartiesResponseByProfileId](docs/GetKeyPartiesResponseByProfileId.md)
 - [GetKeyPartiesResponseByProfileIdItems](docs/GetKeyPartiesResponseByProfileIdItems.md)
 - [GetKeyPartiesResponseByProfileIdItemsAddressResponse](docs/GetKeyPartiesResponseByProfileIdItemsAddressResponse.md)
 - [GetKeyPartySearchResponse](docs/GetKeyPartySearchResponse.md)
 - [GetKycProtectAsyncAmlJobCriteriaResponse](docs/GetKycProtectAsyncAmlJobCriteriaResponse.md)
 - [GetKycProtectAsyncAmlJobItemResponse](docs/GetKycProtectAsyncAmlJobItemResponse.md)
 - [GetKycProtectAsyncAmlJobResponse](docs/GetKycProtectAsyncAmlJobResponse.md)
 - [GetKycProtectBatchUploadsByUploadIdItemResponse](docs/GetKycProtectBatchUploadsByUploadIdItemResponse.md)
 - [GetKycProtectBatchUploadsByUploadsResponse](docs/GetKycProtectBatchUploadsByUploadsResponse.md)
 - [GetProfileHitsByProfileIdResponse](docs/GetProfileHitsByProfileIdResponse.md)
 - [GetProfileHitsByProfileIdResponseItems](docs/GetProfileHitsByProfileIdResponseItems.md)
 - [GetProfileHitsByProfileIdResponseSupersededHit](docs/GetProfileHitsByProfileIdResponseSupersededHit.md)
 - [HitsHitIdBody](docs/HitsHitIdBody.md)
 - [IdEnrichmentsBody](docs/IdEnrichmentsBody.md)
 - [IdvRequestDto](docs/IdvRequestDto.md)
 - [IdvResponseDto](docs/IdvResponseDto.md)
 - [IdvSourcesDto](docs/IdvSourcesDto.md)
 - [IndividualSearchResultHitResponse](docs/IndividualSearchResultHitResponse.md)
 - [IndividualSearchResultHitResponseAmlResults](docs/IndividualSearchResultHitResponseAmlResults.md)
 - [IndividualSearchResultHitSummaryResponse](docs/IndividualSearchResultHitSummaryResponse.md)
 - [IndividualSearchUpdateHitRequest](docs/IndividualSearchUpdateHitRequest.md)
 - [IndividualsSearchResultUpdateHits](docs/IndividualsSearchResultUpdateHits.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse204](docs/InlineResponse204.md)
 - [InlineResponse404](docs/InlineResponse404.md)
 - [InlineResponse4041](docs/InlineResponse4041.md)
 - [InlineResponse409](docs/InlineResponse409.md)
 - [InternationalAgeAlgorithm](docs/InternationalAgeAlgorithm.md)
 - [InternationalAgeAlgorithmWarning](docs/InternationalAgeAlgorithmWarning.md)
 - [InternationalEnhancedPepDatabase](docs/InternationalEnhancedPepDatabase.md)
 - [InternationalEnhancedPepDatabaseDetail](docs/InternationalEnhancedPepDatabaseDetail.md)
 - [InternationalEnhancedPepDatabasePeps](docs/InternationalEnhancedPepDatabasePeps.md)
 - [InternationalSanctions](docs/InternationalSanctions.md)
 - [InternationalSanctionsDetail](docs/InternationalSanctionsDetail.md)
 - [InternationalSanctionsDetailAddresses](docs/InternationalSanctionsDetailAddresses.md)
 - [InternationalSanctionsDetailDates](docs/InternationalSanctionsDetailDates.md)
 - [InternationalSanctionsSanctions](docs/InternationalSanctionsSanctions.md)
 - [Investigation](docs/Investigation.md)
 - [InvestigationAlert](docs/InvestigationAlert.md)
 - [InvestigationAlertStatus](docs/InvestigationAlertStatus.md)
 - [InvestigationNote](docs/InvestigationNote.md)
 - [InvestigationOrderBys](docs/InvestigationOrderBys.md)
 - [InvestigationQuery](docs/InvestigationQuery.md)
 - [InvestigationRecordDto](docs/InvestigationRecordDto.md)
 - [InvestigationResponse](docs/InvestigationResponse.md)
 - [InvestigationRisk](docs/InvestigationRisk.md)
 - [InvestigationRiskResponse](docs/InvestigationRiskResponse.md)
 - [InvestigationStatus](docs/InvestigationStatus.md)
 - [InvestigationType](docs/InvestigationType.md)
 - [JobEnrichmentSettings](docs/JobEnrichmentSettings.md)
 - [JobMappingDto](docs/JobMappingDto.md)
 - [KYCBaseBusinessSearchResultHitSummaryResponse](docs/KYCBaseBusinessSearchResultHitSummaryResponse.md)
 - [KYCBusinessSearchResultHitSummaryResponse](docs/KYCBusinessSearchResultHitSummaryResponse.md)
 - [KYCGetSearchBusinessesBySearchIdHitsResponse](docs/KYCGetSearchBusinessesBySearchIdHitsResponse.md)
 - [KYCGetSearchBusinessesBySearchIdHitsResponseItems](docs/KYCGetSearchBusinessesBySearchIdHitsResponseItems.md)
 - [KYCGetSearchBusinessesBySearchIdHitsResponseSupersededHit](docs/KYCGetSearchBusinessesBySearchIdHitsResponseSupersededHit.md)
 - [KYCGetSearchBusinessesBySearchIdResponse](docs/KYCGetSearchBusinessesBySearchIdResponse.md)
 - [KYCGetSearchIndividualBySearchIdResponse](docs/KYCGetSearchIndividualBySearchIdResponse.md)
 - [KYCPUTSearchBusinessesResponse](docs/KYCPUTSearchBusinessesResponse.md)
 - [KYCPUTSearchBusinessesResponseFailed](docs/KYCPUTSearchBusinessesResponseFailed.md)
 - [KYCPUTSearchBusinessesResponseFailedItem](docs/KYCPUTSearchBusinessesResponseFailedItem.md)
 - [KYCPostIndividualSearchContract](docs/KYCPostIndividualSearchContract.md)
 - [KYCProfileIdSchedulesScheduleIdResponse](docs/KYCProfileIdSchedulesScheduleIdResponse.md)
 - [KYCProfileScheduleResponse](docs/KYCProfileScheduleResponse.md)
 - [KYCProtectBaseIndividualSearchResultHitSummaryResponse](docs/KYCProtectBaseIndividualSearchResultHitSummaryResponse.md)
 - [KYCProtectProfileDetailsNoteByNoteIdNotFound](docs/KYCProtectProfileDetailsNoteByNoteIdNotFound.md)
 - [KYCProtectScheduleHitResponse](docs/KYCProtectScheduleHitResponse.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponse](docs/KYCPutSearchBusinessesBySearchIdHitsResponse.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponseFailed](docs/KYCPutSearchBusinessesBySearchIdHitsResponseFailed.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponseFailedItem](docs/KYCPutSearchBusinessesBySearchIdHitsResponseFailedItem.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponseItems](docs/KYCPutSearchBusinessesBySearchIdHitsResponseItems.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponseSuccessful](docs/KYCPutSearchBusinessesBySearchIdHitsResponseSuccessful.md)
 - [KYCPutSearchBusinessesBySearchIdHitsResponseSupersededHit](docs/KYCPutSearchBusinessesBySearchIdHitsResponseSupersededHit.md)
 - [KYCPutSearchBusinessesBySearchIdResponse](docs/KYCPutSearchBusinessesBySearchIdResponse.md)
 - [KYCPutSearchIndividualBySearchIdResponse](docs/KYCPutSearchIndividualBySearchIdResponse.md)
 - [KeyPartyByIdReturn](docs/KeyPartyByIdReturn.md)
 - [KeyPartyByIdReturnAddress](docs/KeyPartyByIdReturnAddress.md)
 - [KycMonitoringKycAlertResponse](docs/KycMonitoringKycAlertResponse.md)
 - [KycProtectAsyncJobCriteriaResponse](docs/KycProtectAsyncJobCriteriaResponse.md)
 - [KycProtectErrorObject](docs/KycProtectErrorObject.md)
 - [KycProtectGetCustomerUsersDetailsResponse](docs/KycProtectGetCustomerUsersDetailsResponse.md)
 - [KycProtectGetCustomerUsersDetailsResponseItems](docs/KycProtectGetCustomerUsersDetailsResponseItems.md)
 - [KycProtectGetIndividualSearchItems](docs/KycProtectGetIndividualSearchItems.md)
 - [KycProtectGetMyUserDetailsResponse](docs/KycProtectGetMyUserDetailsResponse.md)
 - [KycProtectGetMyUserDetailsResponsePrimaryContact](docs/KycProtectGetMyUserDetailsResponsePrimaryContact.md)
 - [KycProtectGetSearchResponse](docs/KycProtectGetSearchResponse.md)
 - [KycProtectIndividualSearchResponse](docs/KycProtectIndividualSearchResponse.md)
 - [KycProtectPostPostIndividualSearchResponse](docs/KycProtectPostPostIndividualSearchResponse.md)
 - [KycProtectPostProfilesRequest](docs/KycProtectPostProfilesRequest.md)
 - [KycProtectPostProfilesRequestDetails](docs/KycProtectPostProfilesRequestDetails.md)
 - [KycProtectPostProfilesRequestDetailsAssetsUnderManagement](docs/KycProtectPostProfilesRequestDetailsAssetsUnderManagement.md)
 - [KycProtectPostProfilesRequestDetailsTurnover](docs/KycProtectPostProfilesRequestDetailsTurnover.md)
 - [KycProtectPostPutIndividualSearchRequest](docs/KycProtectPostPutIndividualSearchRequest.md)
 - [KycProtectProblemDetails](docs/KycProtectProblemDetails.md)
 - [KycProtectProfileAddressResponse](docs/KycProtectProfileAddressResponse.md)
 - [KycProtectProfileAssignBulkResponse](docs/KycProtectProfileAssignBulkResponse.md)
 - [KycProtectProfileAttachmentResponse](docs/KycProtectProfileAttachmentResponse.md)
 - [KycProtectProfileConflictResponse](docs/KycProtectProfileConflictResponse.md)
 - [KycProtectProfileCreatedResponse](docs/KycProtectProfileCreatedResponse.md)
 - [KycProtectProfileCreatedResponseDetails](docs/KycProtectProfileCreatedResponseDetails.md)
 - [KycProtectProfileCreatedResponseDetailsAssetsUnderManagement](docs/KycProtectProfileCreatedResponseDetailsAssetsUnderManagement.md)
 - [KycProtectProfileCreatedResponseDetailsTurnover](docs/KycProtectProfileCreatedResponseDetailsTurnover.md)
 - [KycProtectProfileDetailsResponse](docs/KycProtectProfileDetailsResponse.md)
 - [KycProtectProfileDetailsResponseTurnover](docs/KycProtectProfileDetailsResponseTurnover.md)
 - [KycProtectProfileGetAttachmentResponse](docs/KycProtectProfileGetAttachmentResponse.md)
 - [KycProtectProfileGetDetailsAddressResponse](docs/KycProtectProfileGetDetailsAddressResponse.md)
 - [KycprotectSchedulesBody](docs/KycprotectSchedulesBody.md)
 - [KycprotectSchedulesBody1](docs/KycprotectSchedulesBody1.md)
 - [LocalSolutionsFRBankMatch](docs/LocalSolutionsFRBankMatch.md)
 - [LocalSolutionsFRBankMatchEntity](docs/LocalSolutionsFRBankMatchEntity.md)
 - [LocalSolutionsFRBankMatchEntityAdditionalProperties](docs/LocalSolutionsFRBankMatchEntityAdditionalProperties.md)
 - [LocalSolutionsFRBankMatchEntityAdditionalPropertiesVatRequestInfo](docs/LocalSolutionsFRBankMatchEntityAdditionalPropertiesVatRequestInfo.md)
 - [LocalSolutionsFRBankMatchEntityCompany](docs/LocalSolutionsFRBankMatchEntityCompany.md)
 - [LocalSolutionsFRBankMatchEntityPaymentIdentity](docs/LocalSolutionsFRBankMatchEntityPaymentIdentity.md)
 - [LocalSolutionsFRBankMatchInput](docs/LocalSolutionsFRBankMatchInput.md)
 - [LocalSolutionsFRBankMatchInputCompany](docs/LocalSolutionsFRBankMatchInputCompany.md)
 - [LocalSolutionsFRBankMatchInputPaymentIdentity](docs/LocalSolutionsFRBankMatchInputPaymentIdentity.md)
 - [LocalSolutionsFRBankMatchIssuerCompany](docs/LocalSolutionsFRBankMatchIssuerCompany.md)
 - [MODEL1c736e](docs/MODEL1c736e.md)
 - [MODEL1e2683](docs/MODEL1e2683.md)
 - [MODEL1e2683Items](docs/MODEL1e2683Items.md)
 - [MODEL20274f](docs/MODEL20274f.md)
 - [MODEL28cf8d](docs/MODEL28cf8d.md)
 - [MODEL3eb319](docs/MODEL3eb319.md)
 - [MODEL3eb319Failed](docs/MODEL3eb319Failed.md)
 - [MODEL4df4ca](docs/MODEL4df4ca.md)
 - [MODEL4f561c](docs/MODEL4f561c.md)
 - [MODEL5941c0](docs/MODEL5941c0.md)
 - [MODEL5b4b1c](docs/MODEL5b4b1c.md)
 - [MODEL5bb0b0](docs/MODEL5bb0b0.md)
 - [MODEL5bdbb3](docs/MODEL5bdbb3.md)
 - [MODEL6bcc20](docs/MODEL6bcc20.md)
 - [MODEL7b2457](docs/MODEL7b2457.md)
 - [MODEL7b2457Items](docs/MODEL7b2457Items.md)
 - [MODEL7c8060](docs/MODEL7c8060.md)
 - [MODEL7fba1c](docs/MODEL7fba1c.md)
 - [MODEL8790cc](docs/MODEL8790cc.md)
 - [MODEL931a1b](docs/MODEL931a1b.md)
 - [MODELb33a65](docs/MODELb33a65.md)
 - [MODELcebf3b](docs/MODELcebf3b.md)
 - [MODELcf4983](docs/MODELcf4983.md)
 - [MODELe000b1](docs/MODELe000b1.md)
 - [MODELf6df8e](docs/MODELf6df8e.md)
 - [MODELf73bb1](docs/MODELf73bb1.md)
 - [MODELf73bb1Items](docs/MODELf73bb1Items.md)
 - [MatchRate](docs/MatchRate.md)
 - [MatchType](docs/MatchType.md)
 - [OneOfCreditsafeGlobalDataCompanyDataVatNo](docs/OneOfCreditsafeGlobalDataCompanyDataVatNo.md)
 - [OrderDirection](docs/OrderDirection.md)
 - [PostKYCKeypartiesByProfileIdAddressContractResponse](docs/PostKYCKeypartiesByProfileIdAddressContractResponse.md)
 - [PostKYCKeypartiesByProfileIdAddressRequestContractResponse](docs/PostKYCKeypartiesByProfileIdAddressRequestContractResponse.md)
 - [PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse](docs/PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.md)
 - [PostKYCKeypartiesByProfileIdFailedResponse](docs/PostKYCKeypartiesByProfileIdFailedResponse.md)
 - [PostKYCKeypartiesByProfileIdRequest](docs/PostKYCKeypartiesByProfileIdRequest.md)
 - [PostKYCKeypartiesByProfileIdRequestAddress](docs/PostKYCKeypartiesByProfileIdRequestAddress.md)
 - [PostKYCKeypartiesByProfileIdRequestItems](docs/PostKYCKeypartiesByProfileIdRequestItems.md)
 - [PostKYCKeypartiesByProfileIdResponse](docs/PostKYCKeypartiesByProfileIdResponse.md)
 - [PostKYCKeypartiesSearchesLinkByProfileIdResponse](docs/PostKYCKeypartiesSearchesLinkByProfileIdResponse.md)
 - [PostKYCKeypartiesSearchesLinkByProfileIdResponseError](docs/PostKYCKeypartiesSearchesLinkByProfileIdResponseError.md)
 - [PostKYCKeypartiesSearchesLinkByProfileIdResponseFailed](docs/PostKYCKeypartiesSearchesLinkByProfileIdResponseFailed.md)
 - [PostKYCKeypartiesSearchesLinkByProfileIdResponseFailedItem](docs/PostKYCKeypartiesSearchesLinkByProfileIdResponseFailedItem.md)
 - [PostKYCMonitoringProfilesBulkResponse](docs/PostKYCMonitoringProfilesBulkResponse.md)
 - [PostKYCMonitoringProfilesBulkResponseError](docs/PostKYCMonitoringProfilesBulkResponseError.md)
 - [PostKYCMonitoringProfilesBulkResponseFailed](docs/PostKYCMonitoringProfilesBulkResponseFailed.md)
 - [PostKYCMonitoringProfilesBulkResquest](docs/PostKYCMonitoringProfilesBulkResquest.md)
 - [PostKYCProfileNotes](docs/PostKYCProfileNotes.md)
 - [PostKYCProfileNotesRequest](docs/PostKYCProfileNotesRequest.md)
 - [PostKYCProtectSchedulesRequest](docs/PostKYCProtectSchedulesRequest.md)
 - [PostKYCProtectSchedulesResponse](docs/PostKYCProtectSchedulesResponse.md)
 - [PostKYCProtectSchedulesResponseFailed](docs/PostKYCProtectSchedulesResponseFailed.md)
 - [PostKycProtectBatchUploadsRequest](docs/PostKycProtectBatchUploadsRequest.md)
 - [PostKycProtectBatchUploadsResponse](docs/PostKycProtectBatchUploadsResponse.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ProfileIdAttachmentsBody](docs/ProfileIdAttachmentsBody.md)
 - [ProfileIdKeypartiesBody](docs/ProfileIdKeypartiesBody.md)
 - [ProtectBatchUploadsBody](docs/ProtectBatchUploadsBody.md)
 - [PutBatchUploadsRetryByIdResponse](docs/PutBatchUploadsRetryByIdResponse.md)
 - [PutIndividualSearchIdHitsByHitIdResponse](docs/PutIndividualSearchIdHitsByHitIdResponse.md)
 - [PutIndividualSearchIdHitsByHitIdResponseSupersededHit](docs/PutIndividualSearchIdHitsByHitIdResponseSupersededHit.md)
 - [PutIndividualSearchIdHitsResponse](docs/PutIndividualSearchIdHitsResponse.md)
 - [PutIndividualSearchIdHitsResponseError](docs/PutIndividualSearchIdHitsResponseError.md)
 - [PutIndividualSearchIdHitsResponseFailed](docs/PutIndividualSearchIdHitsResponseFailed.md)
 - [PutIndividualSearchIdHitsResponseFailedItem](docs/PutIndividualSearchIdHitsResponseFailedItem.md)
 - [PutIndividualSearchIdHitsResponseSuccessful](docs/PutIndividualSearchIdHitsResponseSuccessful.md)
 - [PutIndividualSearchIdHitsResponseSupersededHit](docs/PutIndividualSearchIdHitsResponseSupersededHit.md)
 - [PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser](docs/PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser.md)
 - [PutKYCIndividualSearchBySearchIdRequest](docs/PutKYCIndividualSearchBySearchIdRequest.md)
 - [PutKYCIndividualSearchRequest](docs/PutKYCIndividualSearchRequest.md)
 - [PutKYCIndividualSearchRequestItems](docs/PutKYCIndividualSearchRequestItems.md)
 - [PutKYCKeypartiesByProfileIdAddressContract](docs/PutKYCKeypartiesByProfileIdAddressContract.md)
 - [PutKYCKeypartiesByProfileIdFailedContractResponse](docs/PutKYCKeypartiesByProfileIdFailedContractResponse.md)
 - [PutKYCKeypartiesByProfileIdFailedResponse](docs/PutKYCKeypartiesByProfileIdFailedResponse.md)
 - [PutKYCKeypartiesByProfileIdRequest](docs/PutKYCKeypartiesByProfileIdRequest.md)
 - [PutKYCKeypartiesByProfileIdRequestItems](docs/PutKYCKeypartiesByProfileIdRequestItems.md)
 - [PutKYCProfileAssign](docs/PutKYCProfileAssign.md)
 - [PutKYCProfileDetailsByProfileId](docs/PutKYCProfileDetailsByProfileId.md)
 - [PutKYCProfileDetailsByProfileIdRequest](docs/PutKYCProfileDetailsByProfileIdRequest.md)
 - [PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement](docs/PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement.md)
 - [PutKYCProfileDetailsByProfileIdRequestTurnover](docs/PutKYCProfileDetailsByProfileIdRequestTurnover.md)
 - [PutKYCProfileDetailsNoteByNoteIdResponse](docs/PutKYCProfileDetailsNoteByNoteIdResponse.md)
 - [PutKYCProfileNotesByNoteId](docs/PutKYCProfileNotesByNoteId.md)
 - [PutKYCProfileNotesByNoteIdRequest](docs/PutKYCProfileNotesByNoteIdRequest.md)
 - [PutKYCProtectSchedulesResponse](docs/PutKYCProtectSchedulesResponse.md)
 - [PutKYCProtectSchedulesResponseError](docs/PutKYCProtectSchedulesResponseError.md)
 - [PutKYCProtectSchedulesResponseFailed](docs/PutKYCProtectSchedulesResponseFailed.md)
 - [PutKYCProtectSchedulesResponseFailedItem](docs/PutKYCProtectSchedulesResponseFailedItem.md)
 - [PutKYCProtectSchedulesResponseSuccessful](docs/PutKYCProtectSchedulesResponseSuccessful.md)
 - [PutKYCSearchIndividualResponse](docs/PutKYCSearchIndividualResponse.md)
 - [PutKYCSearchIndividualResponseError](docs/PutKYCSearchIndividualResponseError.md)
 - [PutKYCSearchIndividualResponseFailed](docs/PutKYCSearchIndividualResponseFailed.md)
 - [PutKYCSearchIndividualResponseFailedItem](docs/PutKYCSearchIndividualResponseFailedItem.md)
 - [PutKYCSearchIndividualResponseSuccessful](docs/PutKYCSearchIndividualResponseSuccessful.md)
 - [Record](docs/Record.md)
 - [Schedule](docs/Schedule.md)
 - [ScheduleResponse](docs/ScheduleResponse.md)
 - [ScheduleResponseItems](docs/ScheduleResponseItems.md)
 - [SearchResultHitsAddressResponse](docs/SearchResultHitsAddressResponse.md)
 - [SearchResultHitsBusinessLinkResponse](docs/SearchResultHitsBusinessLinkResponse.md)
 - [SearchResultHitsContactResponse](docs/SearchResultHitsContactResponse.md)
 - [SearchResultHitsIdentifierResponse](docs/SearchResultHitsIdentifierResponse.md)
 - [SearchResultHitsIndividualAliasResponse](docs/SearchResultHitsIndividualAliasResponse.md)
 - [SearchResultHitsIndividualLinkResponse](docs/SearchResultHitsIndividualLinkResponse.md)
 - [SearchResultHitsSourceResponse](docs/SearchResultHitsSourceResponse.md)
 - [SearchesBulkBody](docs/SearchesBulkBody.md)
 - [SearchesBulkBody1](docs/SearchesBulkBody1.md)
 - [SearchesBusinessesBody](docs/SearchesBusinessesBody.md)
 - [SearchesBusinessesBody1](docs/SearchesBusinessesBody1.md)
 - [SearchesLinkBody](docs/SearchesLinkBody.md)
 - [SearchesLinkBody1](docs/SearchesLinkBody1.md)
 - [SourceType](docs/SourceType.md)
 - [Standard](docs/Standard.md)
 - [UKBirthsRegistryDatabase](docs/UKBirthsRegistryDatabase.md)
 - [UKCreditBureau](docs/UKCreditBureau.md)
 - [UKCreditHeaderAml](docs/UKCreditHeaderAml.md)
 - [UKCreditHeaderAmlAccountsInfo](docs/UKCreditHeaderAmlAccountsInfo.md)
 - [UKDeceasedPersonDatabase](docs/UKDeceasedPersonDatabase.md)
 - [UKEditedVotersDatabase](docs/UKEditedVotersDatabase.md)
 - [UKEditedVotersDatabaseComments](docs/UKEditedVotersDatabaseComments.md)
 - [UKEditedVotersDatabaseMatch](docs/UKEditedVotersDatabaseMatch.md)
 - [UKEditedVotersDatabaseMisMatch](docs/UKEditedVotersDatabaseMisMatch.md)
 - [UKEditedVotersDatabaseWarning](docs/UKEditedVotersDatabaseWarning.md)
 - [UKLandlineTelephoneDatabase](docs/UKLandlineTelephoneDatabase.md)
 - [UKNCOA](docs/UKNCOA.md)
 - [UKNationalIdentityRegister](docs/UKNationalIdentityRegister.md)
 - [UpdateDecisionEngineInstanceRequestBody](docs/UpdateDecisionEngineInstanceRequestBody.md)
 - [UpdateDecisionEngineInstanceRequestBodyWithExample](docs/UpdateDecisionEngineInstanceRequestBodyWithExample.md)
 - [UpdateInvestigationRecordsDto](docs/UpdateInvestigationRecordsDto.md)
 - [UpdateInvestigationRequestDto](docs/UpdateInvestigationRequestDto.md)
 - [UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest](docs/UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest.md)
 - [UpdateKYCAttachmentsByAttachmentId](docs/UpdateKYCAttachmentsByAttachmentId.md)
 - [UpdateKYCAttachmentsByAttachmentIdRequest](docs/UpdateKYCAttachmentsByAttachmentIdRequest.md)
 - [UpdateKYCAttchmentsByAttachmentId](docs/UpdateKYCAttchmentsByAttachmentId.md)
 - [UpdateKYCProfileByProfileId](docs/UpdateKYCProfileByProfileId.md)
 - [UpdateKYCProfileByProfileIdRequest](docs/UpdateKYCProfileByProfileIdRequest.md)
 - [UpdateKeyPartyById](docs/UpdateKeyPartyById.md)
 - [UpdateKeyPartyByIdAddress](docs/UpdateKeyPartyByIdAddress.md)
 - [UpdateKycAlertContract](docs/UpdateKycAlertContract.md)
 - [ValidateIdBody](docs/ValidateIdBody.md)
 - [WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse](docs/WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse.md)
 - [WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse](docs/WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesCourtResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesCourtResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesDisqualifiedDirectorEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesDisqualifiedDirectorEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesEventsHitEventResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesEventsHitEventResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesPepEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesPepEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesPepEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesPepEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesPositionResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesPositionResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryResponse.md)
 - [WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryValueResponse](docs/WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryValueResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitAddressResponse](docs/WebApiModelsSearchesSearchResultHitsHitAddressResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitAmlResultsPepsResponse](docs/WebApiModelsSearchesSearchResultHitsHitAmlResultsPepsResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitAmlResultsSanctionsResponse](docs/WebApiModelsSearchesSearchResultHitsHitAmlResultsSanctionsResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse](docs/WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse](docs/WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitContactResponse](docs/WebApiModelsSearchesSearchResultHitsHitContactResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitIdentifierResponse](docs/WebApiModelsSearchesSearchResultHitsHitIdentifierResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse](docs/WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse.md)
 - [WebApiModelsSearchesSearchResultHitsHitSourceResponse](docs/WebApiModelsSearchesSearchResultHitsHitSourceResponse.md)
 - [WebApiModelsSearchesSearchResultHitsIndividualHitAmlResultsResponse](docs/WebApiModelsSearchesSearchResultHitsIndividualHitAmlResultsResponse.md)



