# coding: utf-8

# flake8: noqa
"""
    Creditsafe Connect

     Last Updated: 09th July 2024<br>  # Introduction   Creditsafe Connect is a REST API that provides access to the <a href=\"https://www.creditsafe.com/gb/en/more/about/our-data.html\" target=\"_blank\">Creditsafe Global Company Database.</a> This allows you to: <ul><li>Control your master data</li><li>Utilize up-to-date Business and Director information, enhancing your onboarding and qualification processes</li><li>Receive alerts when your customer's and supplier's Credit Report changes</li></ul><br>Check the status of Creditsafe Services <a href=\"https://status.creditsafe.com/\" target=\"_blank\">HERE</a>     ## Customer Feedback  Use the buttons below to let us know what you think of this documentation. Please leave comments in your feedback for the author to consider for future versions.<br><br><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f49570f5&embed_data=dGVtcGVyYXR1cmVfaWQ9MSZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"> <img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/gold.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=601a6fd1&embed_data=dGVtcGVyYXR1cmVfaWQ9MiZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/green.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f1f7701c&embed_data=dGVtcGVyYXR1cmVfaWQ9MyZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/amber.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=73951e8b&embed_data=dGVtcGVyYXR1cmVfaWQ9NCZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/red.png\" /></a> <br><br> Selecting one of the buttons above will open a new tab to the feedback portal.   ## Quick Start  To start your Creditsafe Connect API integration you will need to have activated your account and set a password by following the instructions in your Welcome Email. If you have not received a Welcome Email please contact your Creditsafe Account Manager.</br></br>By default, you will have been setup on our Sandbox environment.</br></br>  Using a REST API client construct an `/authenticate` POST request and enter your username & password (case-sensitive) into the POST body. A successful response will return an  `authentication token`.</br></br>  Use the `authentication token` in an `Authorization` header on all other Creditsafe Connect calls as proof of your authenticity.   ## Environments  Production Environment baseurl: <code> https://connect.creditsafe.com/v1 </code> </br> Sandbox Test Environment baseurl:  <code>https://connect.sandbox.creditsafe.com/v1</code>    ## Resources   | Item | Description | |----------------|----------------| | <a href=\"https://connect-portal.creditsafe.com\" target=\"_blank\"> A Front End Demo Site</a> | Opens a friendly UI to test the Connect API | | <a href=\"https://creditsafe.github.io/connect-docs/cs_connectv1-15.html\" target=\"_blank\"> Open API Spec </a>  | This will allow you to view the documentation in the swagger portal - this will be discontinued | <a href=\"https://help.creditsafeuk.com/en/support/solutions\" target=\"_blank\"> Help Articles</a> | Opens the Help Hub with a list of common questions and answers | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000053487-connect-api-data-dictionaries\" target=\"_blank\"> Data Dictionaries </a> | The connect documentation shows the general use case, the data dictionaries include the additional specific data that is returned by individual countries | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054765-connect-api-data-availability-per-country\" target=\"_blank\"> Data Availability per Country </a> | The Data Matrix is a document that outlines all the fields that are available in the company report for an online territory | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054656-connect-api-feature-availability-per-country\" target=\"_blank\"> Creditsafe Online Country Feature Availability</a> | This matrix displays what features are available with the online Creditsafe Countries and the partner network | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a> | The document identifies the templates available for specific parts of the Company Credit Report, avoiding the need to order the full report object in one API call. | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000081984-connect-api-server-response-codes\" target=\"_blank\"> Connect API Response Codes </a> | Opens up a basic table of response codes, provides a link to a more detailed response code list |   <br>    ## Versioning and Changes    ### Non-Breaking Changes   Non-breaking changes will generally include additive functions or bug fixes. It is crucial for the integration of the code to be done in such a way that it does not depend on the sequence in which items are returned. This ensures that updates can be applied seamlessly without affecting the existing functionality.    ### Breaking Changes   Breaking changes refer to any modifications to the API's functionality that could disrupt the current contract of the API. Such changes necessitate communication with stakeholders and will lead to a major version number update, indicating the significant nature of these changes.   # noqa: E501

    OpenAPI spec version: 1.10.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from pycsapi.models.aml_multi_bureau_search import AMLMultiBureauSearch
from pycsapi.models.aml_multi_bureau_search_id_aml import AMLMultiBureauSearchIdAml
from pycsapi.models.aml_search import AMLSearch
from pycsapi.models.aml_search_id_aml import AMLSearchIdAml
from pycsapi.models.add_key_party_search_contract import AddKeyPartySearchContract
from pycsapi.models.add_search_contract import AddSearchContract
from pycsapi.models.address import Address
from pycsapi.models.alert_type import AlertType
from pycsapi.models.alerts_frequency import AlertsFrequency
from pycsapi.models.all_of_connect_footprint_data_finance_overall_aggregations import (
    AllOfConnectFootprintDataFinanceOverallAggregations,
)
from pycsapi.models.all_of_connect_footprint_indicator_data_overall_aggregations import (
    AllOfConnectFootprintIndicatorDataOverallAggregations,
)
from pycsapi.models.all_of_connect_indicator_data_overall_aggregations import (
    AllOfConnectIndicatorDataOverallAggregations,
)
from pycsapi.models.all_of_consumer_search_common import AllOfConsumerSearchCommon
from pycsapi.models.all_of_consumer_search_consumer import AllOfConsumerSearchConsumer
from pycsapi.models.any_of_connect_fresh_inv_completed_investigation_sections_items import (
    AnyOfConnectFreshInvCompletedInvestigationSectionsItems,
)
from pycsapi.models.any_of_connect_monitoring_update_event_rules_body_param0 import (
    AnyOfConnectMonitoringUpdateEventRulesBodyParam0,
)
from pycsapi.models.any_of_connect_monitoring_update_event_rules_body_param1 import (
    AnyOfConnectMonitoringUpdateEventRulesBodyParam1,
)
from pycsapi.models.any_of_connect_monitoring_update_event_rules_body_param2 import (
    AnyOfConnectMonitoringUpdateEventRulesBodyParam2,
)
from pycsapi.models.application_searches_models_hits_entries_disqualified_director_entry_value import (
    ApplicationSearchesModelsHitsEntriesDisqualifiedDirectorEntryValue,
)
from pycsapi.models.array_of_connect_data_cleaning_job import (
    ArrayOfConnectDataCleaningJob,
)
from pycsapi.models.array_of_connect_data_cleaning_response import (
    ArrayOfConnectDataCleaningResponse,
)
from pycsapi.models.assign_risk_to_investigation_dto import AssignRiskToInvestigationDto
from pycsapi.models.attachment_not_found import AttachmentNotFound
from pycsapi.models.basic import Basic
from pycsapi.models.basic_enrichments import BasicEnrichments
from pycsapi.models.basic_plus import BasicPlus
from pycsapi.models.batch_upload import BatchUpload
from pycsapi.models.batch_upload_file_type import BatchUploadFileType
from pycsapi.models.batch_upload_status import BatchUploadStatus
from pycsapi.models.businesses_search_id_body import BusinessesSearchIdBody
from pycsapi.models.combined_decision import CombinedDecision
from pycsapi.models.compliancekycprotectprofilesprofile_idkeypartiessearcheslink_items import (
    CompliancekycprotectprofilesprofileIdkeypartiessearcheslinkItems,
)
from pycsapi.models.compliancekycprotectsearchesbusinesses_items import (
    CompliancekycprotectsearchesbusinessesItems,
)
from pycsapi.models.connect_authentication_access_countries import (
    ConnectAuthenticationAccessCountries,
)
from pycsapi.models.connect_authentication_access_countries_country_access import (
    ConnectAuthenticationAccessCountriesCountryAccess,
)
from pycsapi.models.connect_authentication_access_countries_country_access_creditsafe_connect_director_reports import (
    ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectDirectorReports,
)
from pycsapi.models.connect_authentication_access_countries_country_access_creditsafe_connect_monitoring import (
    ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectMonitoring,
)
from pycsapi.models.connect_authentication_access_countries_country_access_creditsafe_connect_offline_reports import (
    ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOfflineReports,
)
from pycsapi.models.connect_authentication_access_countries_country_access_creditsafe_connect_online_reports import (
    ConnectAuthenticationAccessCountriesCountryAccessCreditsafeConnectOnlineReports,
)
from pycsapi.models.connect_authentication_auth_request import (
    ConnectAuthenticationAuthRequest,
)
from pycsapi.models.connect_authentication_auth_response import (
    ConnectAuthenticationAuthResponse,
)
from pycsapi.models.connect_authentication_unauthorised import (
    ConnectAuthenticationUnauthorised,
)
from pycsapi.models.connect_bank_match_aggregations import ConnectBankMatchAggregations
from pycsapi.models.connect_bank_match_business_address import (
    ConnectBankMatchBusinessAddress,
)
from pycsapi.models.connect_bank_match_data import ConnectBankMatchData
from pycsapi.models.connect_bank_match_facility import ConnectBankMatchFacility
from pycsapi.models.connect_bank_match_per_organisation_aggregation import (
    ConnectBankMatchPerOrganisationAggregation,
)
from pycsapi.models.connect_bank_match_result import ConnectBankMatchResult
from pycsapi.models.connect_bank_match_result_bank_match_results import (
    ConnectBankMatchResultBankMatchResults,
)
from pycsapi.models.connect_bank_match_totals import ConnectBankMatchTotals
from pycsapi.models.connect_ccds_aggregations import ConnectCcdsAggregations
from pycsapi.models.connect_ccds_aggregations_per_organisation_aggregations import (
    ConnectCcdsAggregationsPerOrganisationAggregations,
)
from pycsapi.models.connect_ccds_aggregations_total_credit_cards import (
    ConnectCcdsAggregationsTotalCreditCards,
)
from pycsapi.models.connect_ccds_aggregations_total_loans import (
    ConnectCcdsAggregationsTotalLoans,
)
from pycsapi.models.connect_ccds_facilities import ConnectCcdsFacilities
from pycsapi.models.connect_ccds_financial_indicator_data import (
    ConnectCcdsFinancialIndicatorData,
)
from pycsapi.models.connect_ccds_footprint_data_finance import (
    ConnectCcdsFootprintDataFinance,
)
from pycsapi.models.connect_ccds_full_history import ConnectCcdsFullHistory
from pycsapi.models.connect_ccds_history import ConnectCcdsHistory
from pycsapi.models.connect_ccds_indicator_data_finance import (
    ConnectCcdsIndicatorDataFinance,
)
from pycsapi.models.connect_ccds_overall_aggregations import (
    ConnectCcdsOverallAggregations,
)
from pycsapi.models.connect_company_search_no_results import (
    ConnectCompanySearchNoResults,
)
from pycsapi.models.connect_company_search_search_criteria import (
    ConnectCompanySearchSearchCriteria,
)
from pycsapi.models.connect_confidence_match_match_results import (
    ConnectConfidenceMatchMatchResults,
)
from pycsapi.models.connect_confidence_match_match_results_address import (
    ConnectConfidenceMatchMatchResultsAddress,
)
from pycsapi.models.connect_confidence_match_match_results_match_score_explain_plan import (
    ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan,
)
from pycsapi.models.connect_confidence_match_match_results_matched_companies import (
    ConnectConfidenceMatchMatchResultsMatchedCompanies,
)
from pycsapi.models.connect_confidence_match_no_results import (
    ConnectConfidenceMatchNoResults,
)
from pycsapi.models.connect_credit_safe_ccds_company import ConnectCreditSafeCcdsCompany
from pycsapi.models.connect_data_cleaning_archive_job_request import (
    ConnectDataCleaningArchiveJobRequest,
)
from pycsapi.models.connect_data_cleaning_archive_response import (
    ConnectDataCleaningArchiveResponse,
)
from pycsapi.models.connect_data_cleaning_create_job_request import (
    ConnectDataCleaningCreateJobRequest,
)
from pycsapi.models.connect_data_cleaning_enrich_request import (
    ConnectDataCleaningEnrichRequest,
)
from pycsapi.models.connect_data_cleaning_job import ConnectDataCleaningJob
from pycsapi.models.connect_data_cleaning_job_job_enrichment_settings import (
    ConnectDataCleaningJobJobEnrichmentSettings,
)
from pycsapi.models.connect_data_cleaning_job_job_summary import (
    ConnectDataCleaningJobJobSummary,
)
from pycsapi.models.connect_data_cleaning_mapping_response import (
    ConnectDataCleaningMappingResponse,
)
from pycsapi.models.connect_data_cleaning_mapping_response_inner import (
    ConnectDataCleaningMappingResponseInner,
)
from pycsapi.models.connect_data_cleaning_response import ConnectDataCleaningResponse
from pycsapi.models.connect_data_cleaning_submit_job_request import (
    ConnectDataCleaningSubmitJobRequest,
)
from pycsapi.models.connect_data_cleaning_update_mappings_request import (
    ConnectDataCleaningUpdateMappingsRequest,
)
from pycsapi.models.connect_data_cleaning_upload_response import (
    ConnectDataCleaningUploadResponse,
)
from pycsapi.models.connect_decision_engine_decision_log_response import (
    ConnectDecisionEngineDecisionLogResponse,
)
from pycsapi.models.connect_decision_engine_decision_log_response_response import (
    ConnectDecisionEngineDecisionLogResponseResponse,
)
from pycsapi.models.connect_decision_engine_guid_list_response import (
    ConnectDecisionEngineGUIDListResponse,
)
from pycsapi.models.connect_decision_engine_guid_list_response_guid_list import (
    ConnectDecisionEngineGUIDListResponseGUIDList,
)
from pycsapi.models.connect_decision_engine_patch_decision_outcome_request import (
    ConnectDecisionEnginePatchDecisionOutcomeRequest,
)
from pycsapi.models.connect_decision_engine_patch_decision_outcome_request_decision_outcomes import (
    ConnectDecisionEnginePatchDecisionOutcomeRequestDecisionOutcomes,
)
from pycsapi.models.connect_decision_engine_run_decision_response import (
    ConnectDecisionEngineRunDecisionResponse,
)
from pycsapi.models.connect_decision_engine_run_decision_response_audits import (
    ConnectDecisionEngineRunDecisionResponseAudits,
)
from pycsapi.models.connect_decision_engine_update_decision_request import (
    ConnectDecisionEngineUpdateDecisionRequest,
)
from pycsapi.models.connect_decision_engine_usage_log_response import (
    ConnectDecisionEngineUsageLogResponse,
)
from pycsapi.models.connect_decision_engine_usage_log_response_response import (
    ConnectDecisionEngineUsageLogResponseResponse,
)
from pycsapi.models.connect_decision_engine_usage_log_response_response_audits import (
    ConnectDecisionEngineUsageLogResponseResponseAudits,
)
from pycsapi.models.connect_decision_engine_usage_log_response_usage_log import (
    ConnectDecisionEngineUsageLogResponseUsageLog,
)
from pycsapi.models.connect_decision_engine_user_data_fields_response import (
    ConnectDecisionEngineUserDataFieldsResponse,
)
from pycsapi.models.connect_decision_engine_user_data_fields_response_dropdown_details import (
    ConnectDecisionEngineUserDataFieldsResponseDropdownDetails,
)
from pycsapi.models.connect_decision_engine_user_data_fields_response_fields import (
    ConnectDecisionEngineUserDataFieldsResponseFields,
)
from pycsapi.models.connect_decision_engine_user_data_fields_response_validation import (
    ConnectDecisionEngineUserDataFieldsResponseValidation,
)
from pycsapi.models.connect_error_responses_access_forbidden import (
    ConnectErrorResponsesAccessForbidden,
)
from pycsapi.models.connect_error_responses_bad_request import (
    ConnectErrorResponsesBadRequest,
)
from pycsapi.models.connect_error_responses_invalid_token import (
    ConnectErrorResponsesInvalidToken,
)
from pycsapi.models.connect_error_responses_resource_not_found_request import (
    ConnectErrorResponsesResourceNotFoundRequest,
)
from pycsapi.models.connect_footprint_data_finance import ConnectFootprintDataFinance
from pycsapi.models.connect_footprint_data_finance_credit_safe import (
    ConnectFootprintDataFinanceCreditSafe,
)
from pycsapi.models.connect_footprint_data_finance_footprint_data import (
    ConnectFootprintDataFinanceFootprintData,
)
from pycsapi.models.connect_footprint_data_finance_footprint_data_year import (
    ConnectFootprintDataFinanceFootprintDataYear,
)
from pycsapi.models.connect_footprint_data_finance_footprint_data_year_month import (
    ConnectFootprintDataFinanceFootprintDataYearMonth,
)
from pycsapi.models.connect_footprint_data_finance_indicator_data import (
    ConnectFootprintDataFinanceIndicatorData,
)
from pycsapi.models.connect_footprint_data_finance_indicator_data_year import (
    ConnectFootprintDataFinanceIndicatorDataYear,
)
from pycsapi.models.connect_footprint_indicator_data import (
    ConnectFootprintIndicatorData,
)
from pycsapi.models.connect_footprint_indicator_data_financial_indicator import (
    ConnectFootprintIndicatorDataFinancialIndicator,
)
from pycsapi.models.connect_footprint_indicator_data_financial_indicator_year import (
    ConnectFootprintIndicatorDataFinancialIndicatorYear,
)
from pycsapi.models.connect_footprint_indicator_data_footprint_data import (
    ConnectFootprintIndicatorDataFootprintData,
)
from pycsapi.models.connect_fresh_inv_completed_investigation import (
    ConnectFreshInvCompletedInvestigation,
)
from pycsapi.models.connect_fresh_inv_completed_investigation_contact_details import (
    ConnectFreshInvCompletedInvestigationContactDetails,
)
from pycsapi.models.connect_fresh_inv_completed_investigation_search_criteria import (
    ConnectFreshInvCompletedInvestigationSearchCriteria,
)
from pycsapi.models.connect_fresh_inv_completed_investigation_search_criteria_address import (
    ConnectFreshInvCompletedInvestigationSearchCriteriaAddress,
)
from pycsapi.models.connect_fresh_inv_completed_investigation_status import (
    ConnectFreshInvCompletedInvestigationStatus,
)
from pycsapi.models.connect_fresh_inv_create_investigation import (
    ConnectFreshInvCreateInvestigation,
)
from pycsapi.models.connect_fresh_inv_create_investigation_contact_info import (
    ConnectFreshInvCreateInvestigationContactInfo,
)
from pycsapi.models.connect_fresh_inv_create_investigation_contact_info_company import (
    ConnectFreshInvCreateInvestigationContactInfoCompany,
)
from pycsapi.models.connect_fresh_inv_create_investigation_search_criteria import (
    ConnectFreshInvCreateInvestigationSearchCriteria,
)
from pycsapi.models.connect_fresh_inv_create_investigation_search_criteria_address import (
    ConnectFreshInvCreateInvestigationSearchCriteriaAddress,
)
from pycsapi.models.connect_fresh_inv_investigation_company_data import (
    ConnectFreshInvInvestigationCompanyData,
)
from pycsapi.models.connect_fresh_inv_investigation_company_data_address import (
    ConnectFreshInvInvestigationCompanyDataAddress,
)
from pycsapi.models.connect_fresh_inv_investigation_confirmed import (
    ConnectFreshInvInvestigationConfirmed,
)
from pycsapi.models.connect_fresh_inv_investigation_contact_info import (
    ConnectFreshInvInvestigationContactInfo,
)
from pycsapi.models.connect_fresh_inv_investigation_contact_info_company import (
    ConnectFreshInvInvestigationContactInfoCompany,
)
from pycsapi.models.connect_fresh_inv_list_investigations import (
    ConnectFreshInvListInvestigations,
)
from pycsapi.models.connect_fresh_inv_list_investigations_contact_details import (
    ConnectFreshInvListInvestigationsContactDetails,
)
from pycsapi.models.connect_fresh_inv_list_investigations_orders import (
    ConnectFreshInvListInvestigationsOrders,
)
from pycsapi.models.connect_fresh_inv_list_investigations_search_criteria import (
    ConnectFreshInvListInvestigationsSearchCriteria,
)
from pycsapi.models.connect_fresh_inv_list_investigations_status import (
    ConnectFreshInvListInvestigationsStatus,
)
from pycsapi.models.connect_full_finance_data import ConnectFullFinanceData
from pycsapi.models.connect_full_finance_data_financial_indicator import (
    ConnectFullFinanceDataFinancialIndicator,
)
from pycsapi.models.connect_full_finance_data_financial_indicator_year import (
    ConnectFullFinanceDataFinancialIndicatorYear,
)
from pycsapi.models.connect_full_finance_data_footprint_data import (
    ConnectFullFinanceDataFootprintData,
)
from pycsapi.models.connect_full_finance_data_footprint_data_year import (
    ConnectFullFinanceDataFootprintDataYear,
)
from pycsapi.models.connect_identity_aml_multi_bureau_search_request import (
    ConnectIdentityAMLMultiBureauSearchRequest,
)
from pycsapi.models.connect_identity_aml_search_request import (
    ConnectIdentityAMLSearchRequest,
)
from pycsapi.models.connect_identity_action import ConnectIdentityAction
from pycsapi.models.connect_identity_address import ConnectIdentityAddress
from pycsapi.models.connect_identity_address1 import ConnectIdentityAddress1
from pycsapi.models.connect_identity_address_list import ConnectIdentityAddressList
from pycsapi.models.connect_identity_aml_common_search_criteria import (
    ConnectIdentityAmlCommonSearchCriteria,
)
from pycsapi.models.connect_identity_aml_multi_bureau_search_criteria import (
    ConnectIdentityAmlMultiBureauSearchCriteria,
)
from pycsapi.models.connect_identity_aml_result_code import ConnectIdentityAmlResultCode
from pycsapi.models.connect_identity_aml_search_criteria import (
    ConnectIdentityAmlSearchCriteria,
)
from pycsapi.models.connect_identity_aml_search_result import (
    ConnectIdentityAmlSearchResult,
)
from pycsapi.models.connect_identity_aml_supplier_result import (
    ConnectIdentityAmlSupplierResult,
)
from pycsapi.models.connect_identity_aml_supplier_result_result_codes import (
    ConnectIdentityAmlSupplierResultResultCodes,
)
from pycsapi.models.connect_identity_bank_account_details import (
    ConnectIdentityBankAccountDetails,
)
from pycsapi.models.connect_identity_basic_response import ConnectIdentityBasicResponse
from pycsapi.models.connect_identity_batch_search_request import (
    ConnectIdentityBatchSearchRequest,
)
from pycsapi.models.connect_identity_cameo_response import ConnectIdentityCameoResponse
from pycsapi.models.connect_identity_common_result import ConnectIdentityCommonResult
from pycsapi.models.connect_identity_common_search_criteria import (
    ConnectIdentityCommonSearchCriteria,
)
from pycsapi.models.connect_identity_consumer_common_search_criteria import (
    ConnectIdentityConsumerCommonSearchCriteria,
)
from pycsapi.models.connect_identity_consumer_search_criteria import (
    ConnectIdentityConsumerSearchCriteria,
)
from pycsapi.models.connect_identity_consumer_search_result import (
    ConnectIdentityConsumerSearchResult,
)
from pycsapi.models.connect_identity_consumer_search_result_common import (
    ConnectIdentityConsumerSearchResultCommon,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result import (
    ConnectIdentityConsumerSearchResultConsumerResult,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_address import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_address_residents import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddressResidents,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_age_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_economic_activity_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_household_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_lifestage_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_mortgage_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_neighbourhood_definition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_occupation_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_property_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_shareholder_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_shareholder_composition_social_class_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionSocialClassComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_shareholder_composition_tenure_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionTenureComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_demographics_shareholder_composition_unemployment_composition import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderCompositionUnemploymentComposition,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_links import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_previous_address1 import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_score import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_accounts import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareAccounts,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_details import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_history import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHistory,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_holder_details import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetails,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_holder_details_address import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareHolderDetailsAddress,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_indebtedness import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareIndebtedness,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_summary import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSummary,
)
from pycsapi.models.connect_identity_consumer_search_result_consumer_result_applicant1_report_share_supplier_details import (
    ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareSupplierDetails,
)
from pycsapi.models.connect_identity_consumer_search_result_input import (
    ConnectIdentityConsumerSearchResultInput,
)
from pycsapi.models.connect_identity_consumer_search_result_input_common import (
    ConnectIdentityConsumerSearchResultInputCommon,
)
from pycsapi.models.connect_identity_consumer_search_result_input_common_person import (
    ConnectIdentityConsumerSearchResultInputCommonPerson,
)
from pycsapi.models.connect_identity_consumer_search_result_input_common_person_addresses import (
    ConnectIdentityConsumerSearchResultInputCommonPersonAddresses,
)
from pycsapi.models.connect_identity_consumer_search_result_input_consumer import (
    ConnectIdentityConsumerSearchResultInputConsumer,
)
from pycsapi.models.connect_identity_consumer_search_result_input_id_aml import (
    ConnectIdentityConsumerSearchResultInputIdAml,
)
from pycsapi.models.connect_identity_credit_report import ConnectIdentityCreditReport
from pycsapi.models.connect_identity_credit_score import ConnectIdentityCreditScore
from pycsapi.models.connect_identity_current_name import ConnectIdentityCurrentName
from pycsapi.models.connect_identity_date_type import ConnectIdentityDateType
from pycsapi.models.connect_identity_demographic import ConnectIdentityDemographic
from pycsapi.models.connect_identity_demographics_neighbourhood_definition import (
    ConnectIdentityDemographicsNeighbourhoodDefinition,
)
from pycsapi.models.connect_identity_demographics_property_composition import (
    ConnectIdentityDemographicsPropertyComposition,
)
from pycsapi.models.connect_identity_demographics_shareholder_composition import (
    ConnectIdentityDemographicsShareholderComposition,
)
from pycsapi.models.connect_identity_demographics_unemployment_composition import (
    ConnectIdentityDemographicsUnemploymentComposition,
)
from pycsapi.models.connect_identity_drivers_license import (
    ConnectIdentityDriversLicense,
)
from pycsapi.models.connect_identity_electricity_supplier import (
    ConnectIdentityElectricitySupplier,
)
from pycsapi.models.connect_identity_european_id_card import (
    ConnectIdentityEuropeanIDCard,
)
from pycsapi.models.connect_identity_gender import ConnectIdentityGender
from pycsapi.models.connect_identity_history_list_response import (
    ConnectIdentityHistoryListResponse,
)
from pycsapi.models.connect_identity_id_aml import ConnectIdentityIdAml
from pycsapi.models.connect_identity_id_aml_result import ConnectIdentityIdAmlResult
from pycsapi.models.connect_identity_identity_history_item import (
    ConnectIdentityIdentityHistoryItem,
)
from pycsapi.models.connect_identity_input_response import ConnectIdentityInputResponse
from pycsapi.models.connect_identity_insolvency_restriction import (
    ConnectIdentityInsolvencyRestriction,
)
from pycsapi.models.connect_identity_mapped_documents import (
    ConnectIdentityMappedDocuments,
)
from pycsapi.models.connect_identity_mapped_pep_match import (
    ConnectIdentityMappedPepMatch,
)
from pycsapi.models.connect_identity_mapped_result_code import (
    ConnectIdentityMappedResultCode,
)
from pycsapi.models.connect_identity_mapped_result_code_details import (
    ConnectIdentityMappedResultCodeDetails,
)
from pycsapi.models.connect_identity_mapped_sanction_detail import (
    ConnectIdentityMappedSanctionDetail,
)
from pycsapi.models.connect_identity_mapped_sanction_match import (
    ConnectIdentityMappedSanctionMatch,
)
from pycsapi.models.connect_identity_match_value import ConnectIdentityMatchValue
from pycsapi.models.connect_identity_multi_bureau_aml_search_result import (
    ConnectIdentityMultiBureauAmlSearchResult,
)
from pycsapi.models.connect_identity_multi_bureau_aml_supplier_result import (
    ConnectIdentityMultiBureauAmlSupplierResult,
)
from pycsapi.models.connect_identity_multi_bureau_aml_supplier_result_result_codes import (
    ConnectIdentityMultiBureauAmlSupplierResultResultCodes,
)
from pycsapi.models.connect_identity_ni_number import ConnectIdentityNINumber
from pycsapi.models.connect_identity_name import ConnectIdentityName
from pycsapi.models.connect_identity_passport import ConnectIdentityPassport
from pycsapi.models.connect_identity_pep_details import ConnectIdentityPepDetails
from pycsapi.models.connect_identity_pep_or_sanction import ConnectIdentityPepOrSanction
from pycsapi.models.connect_identity_pep_sanction_address import (
    ConnectIdentityPepSanctionAddress,
)
from pycsapi.models.connect_identity_pep_sanction_date import (
    ConnectIdentityPepSanctionDate,
)
from pycsapi.models.connect_identity_person import ConnectIdentityPerson
from pycsapi.models.connect_identity_picklist import ConnectIdentityPicklist
from pycsapi.models.connect_identity_picklist_inputs import (
    ConnectIdentityPicklistInputs,
)
from pycsapi.models.connect_identity_picklist_option import (
    ConnectIdentityPicklistOption,
)
from pycsapi.models.connect_identity_product import ConnectIdentityProduct
from pycsapi.models.connect_identity_reason_code import ConnectIdentityReasonCode
from pycsapi.models.connect_identity_reason_response import (
    ConnectIdentityReasonResponse,
)
from pycsapi.models.connect_identity_report_address import ConnectIdentityReportAddress
from pycsapi.models.connect_identity_report_alias import ConnectIdentityReportAlias
from pycsapi.models.connect_identity_report_associate import (
    ConnectIdentityReportAssociate,
)
from pycsapi.models.connect_identity_report_cifas import ConnectIdentityReportCifas
from pycsapi.models.connect_identity_report_credit_searches_at_current_address import (
    ConnectIdentityReportCreditSearchesAtCurrentAddress,
)
from pycsapi.models.connect_identity_report_demographics import (
    ConnectIdentityReportDemographics,
)
from pycsapi.models.connect_identity_report_electoral_roll_history import (
    ConnectIdentityReportElectoralRollHistory,
)
from pycsapi.models.connect_identity_report_history import ConnectIdentityReportHistory
from pycsapi.models.connect_identity_report_insolvency import (
    ConnectIdentityReportInsolvency,
)
from pycsapi.models.connect_identity_report_insolvency_at_address import (
    ConnectIdentityReportInsolvencyAtAddress,
)
from pycsapi.models.connect_identity_report_judgement import (
    ConnectIdentityReportJudgement,
)
from pycsapi.models.connect_identity_report_links import ConnectIdentityReportLinks
from pycsapi.models.connect_identity_report_matched_data import (
    ConnectIdentityReportMatchedData,
)
from pycsapi.models.connect_identity_report_notice import ConnectIdentityReportNotice
from pycsapi.models.connect_identity_report_residency_confirmation import (
    ConnectIdentityReportResidencyConfirmation,
)
from pycsapi.models.connect_identity_report_resident import (
    ConnectIdentityReportResident,
)
from pycsapi.models.connect_identity_report_rtr import ConnectIdentityReportRtr
from pycsapi.models.connect_identity_report_share_account import (
    ConnectIdentityReportShareAccount,
)
from pycsapi.models.connect_identity_report_summary_judgements import (
    ConnectIdentityReportSummaryJudgements,
)
from pycsapi.models.connect_identity_report_undeclared_address import (
    ConnectIdentityReportUndeclaredAddress,
)
from pycsapi.models.connect_identity_revalidate_request import (
    ConnectIdentityRevalidateRequest,
)
from pycsapi.models.connect_identity_search_result import ConnectIdentitySearchResult
from pycsapi.models.connect_identity_set_reason_request import (
    ConnectIdentitySetReasonRequest,
)
from pycsapi.models.connect_identity_share_account_default import (
    ConnectIdentityShareAccountDefault,
)
from pycsapi.models.connect_identity_share_account_delinquency import (
    ConnectIdentityShareAccountDelinquency,
)
from pycsapi.models.connect_identity_share_account_details import (
    ConnectIdentityShareAccountDetails,
)
from pycsapi.models.connect_identity_share_account_history import (
    ConnectIdentityShareAccountHistory,
)
from pycsapi.models.connect_identity_share_account_history_batch import (
    ConnectIdentityShareAccountHistoryBatch,
)
from pycsapi.models.connect_identity_share_account_holder_details import (
    ConnectIdentityShareAccountHolderDetails,
)
from pycsapi.models.connect_identity_share_account_supplier_details import (
    ConnectIdentityShareAccountSupplierDetails,
)
from pycsapi.models.connect_identity_summary import ConnectIdentitySummary
from pycsapi.models.connect_identity_summary_address import (
    ConnectIdentitySummaryAddress,
)
from pycsapi.models.connect_identity_summary_behavioural_data import (
    ConnectIdentitySummaryBehaviouralData,
)
from pycsapi.models.connect_identity_summary_card_data import (
    ConnectIdentitySummaryCardData,
)
from pycsapi.models.connect_identity_summary_ich import ConnectIdentitySummaryIch
from pycsapi.models.connect_identity_summary_in_debt import ConnectIdentitySummaryInDebt
from pycsapi.models.connect_identity_summary_links import ConnectIdentitySummaryLinks
from pycsapi.models.connect_identity_summary_share import ConnectIdentitySummaryShare
from pycsapi.models.connect_identity_summary_third_party import (
    ConnectIdentitySummaryThirdParty,
)
from pycsapi.models.connect_identity_supplier import ConnectIdentitySupplier
from pycsapi.models.connect_identity_supplier_details import (
    ConnectIdentitySupplierDetails,
)
from pycsapi.models.connect_identity_supplier_result import (
    ConnectIdentitySupplierResult,
)
from pycsapi.models.connect_identity_third_party_alerts import (
    ConnectIdentityThirdPartyAlerts,
)
from pycsapi.models.connect_identity_trans_union_result import (
    ConnectIdentityTransUnionResult,
)
from pycsapi.models.connect_identity_update_user_package import (
    ConnectIdentityUpdateUserPackage,
)
from pycsapi.models.connect_images_company_image_types import (
    ConnectImagesCompanyImageTypes,
)
from pycsapi.models.connect_images_company_image_types_inner import (
    ConnectImagesCompanyImageTypesInner,
)
from pycsapi.models.connect_images_company_images import ConnectImagesCompanyImages
from pycsapi.models.connect_images_company_images_company import (
    ConnectImagesCompanyImagesCompany,
)
from pycsapi.models.connect_images_company_images_data import (
    ConnectImagesCompanyImagesData,
)
from pycsapi.models.connect_images_company_images_document import (
    ConnectImagesCompanyImagesDocument,
)
from pycsapi.models.connect_images_company_images_local_properties import (
    ConnectImagesCompanyImagesLocalProperties,
)
from pycsapi.models.connect_indicator_data import ConnectIndicatorData
from pycsapi.models.connect_indicator_data_financial_indicator import (
    ConnectIndicatorDataFinancialIndicator,
)
from pycsapi.models.connect_indicator_data_footprint_data import (
    ConnectIndicatorDataFootprintData,
)
from pycsapi.models.connect_monitoring_add_company_to_portfolio_request import (
    ConnectMonitoringAddCompanyToPortfolioRequest,
)
from pycsapi.models.connect_monitoring_add_company_to_portfolio_response import (
    ConnectMonitoringAddCompanyToPortfolioResponse,
)
from pycsapi.models.connect_monitoring_all_notifications_events import (
    ConnectMonitoringAllNotificationsEvents,
)
from pycsapi.models.connect_monitoring_all_notifications_events_data import (
    ConnectMonitoringAllNotificationsEventsData,
)
from pycsapi.models.connect_monitoring_clear_companies_request import (
    ConnectMonitoringClearCompaniesRequest,
)
from pycsapi.models.connect_monitoring_clear_companies_response import (
    ConnectMonitoringClearCompaniesResponse,
)
from pycsapi.models.connect_monitoring_companies_in_a_portfolio import (
    ConnectMonitoringCompaniesInAPortfolio,
)
from pycsapi.models.connect_monitoring_companies_in_a_portfolio_data import (
    ConnectMonitoringCompaniesInAPortfolioData,
)
from pycsapi.models.connect_monitoring_company_events import (
    ConnectMonitoringCompanyEvents,
)
from pycsapi.models.connect_monitoring_company_events_data import (
    ConnectMonitoringCompanyEventsData,
)
from pycsapi.models.connect_monitoring_company_info import ConnectMonitoringCompanyInfo
from pycsapi.models.connect_monitoring_copy_and_move_companies_body_companies import (
    ConnectMonitoringCopyAndMoveCompaniesBodyCompanies,
)
from pycsapi.models.connect_monitoring_copy_and_move_companies_request import (
    ConnectMonitoringCopyAndMoveCompaniesRequest,
)
from pycsapi.models.connect_monitoring_copy_and_move_companies_response import (
    ConnectMonitoringCopyAndMoveCompaniesResponse,
)
from pycsapi.models.connect_monitoring_copy_and_move_companies_response_data import (
    ConnectMonitoringCopyAndMoveCompaniesResponseData,
)
from pycsapi.models.connect_monitoring_create_portfolio_request import (
    ConnectMonitoringCreatePortfolioRequest,
)
from pycsapi.models.connect_monitoring_create_portfolio_request_emails import (
    ConnectMonitoringCreatePortfolioRequestEmails,
)
from pycsapi.models.connect_monitoring_create_portfolio_response import (
    ConnectMonitoringCreatePortfolioResponse,
)
from pycsapi.models.connect_monitoring_delete_company_from_portfolio import (
    ConnectMonitoringDeleteCompanyFromPortfolio,
)
from pycsapi.models.connect_monitoring_delete_portfolio import (
    ConnectMonitoringDeletePortfolio,
)
from pycsapi.models.connect_monitoring_event_rules_response import (
    ConnectMonitoringEventRulesResponse,
)
from pycsapi.models.connect_monitoring_event_rules_response_inner import (
    ConnectMonitoringEventRulesResponseInner,
)
from pycsapi.models.connect_monitoring_get_company_from_portfolio import (
    ConnectMonitoringGetCompanyFromPortfolio,
)
from pycsapi.models.connect_monitoring_get_portfolio_by_id import (
    ConnectMonitoringGetPortfolioById,
)
from pycsapi.models.connect_monitoring_import_and_sync_portfolio_request import (
    ConnectMonitoringImportAndSyncPortfolioRequest,
)
from pycsapi.models.connect_monitoring_import_and_sync_portfolio_response import (
    ConnectMonitoringImportAndSyncPortfolioResponse,
)
from pycsapi.models.connect_monitoring_is_processed_request import (
    ConnectMonitoringIsProcessedRequest,
)
from pycsapi.models.connect_monitoring_is_processed_response import (
    ConnectMonitoringIsProcessedResponse,
)
from pycsapi.models.connect_monitoring_is_processed_response_data import (
    ConnectMonitoringIsProcessedResponseData,
)
from pycsapi.models.connect_monitoring_list_portfolio_event_rules import (
    ConnectMonitoringListPortfolioEventRules,
)
from pycsapi.models.connect_monitoring_list_portfolio_event_rules_inner import (
    ConnectMonitoringListPortfolioEventRulesInner,
)
from pycsapi.models.connect_monitoring_list_portfolios import (
    ConnectMonitoringListPortfolios,
)
from pycsapi.models.connect_monitoring_list_portfolios_data import (
    ConnectMonitoringListPortfoliosData,
)
from pycsapi.models.connect_monitoring_list_portfolios_data_emails import (
    ConnectMonitoringListPortfoliosDataEmails,
)
from pycsapi.models.connect_monitoring_list_portfolios_data_portfolios import (
    ConnectMonitoringListPortfoliosDataPortfolios,
)
from pycsapi.models.connect_monitoring_list_portfolios_data_shared_portfolios import (
    ConnectMonitoringListPortfoliosDataSharedPortfolios,
)
from pycsapi.models.connect_monitoring_list_sharing_permissions import (
    ConnectMonitoringListSharingPermissions,
)
from pycsapi.models.connect_monitoring_list_sharing_permissions_data import (
    ConnectMonitoringListSharingPermissionsData,
)
from pycsapi.models.connect_monitoring_list_sharing_permissions_data_user_permission import (
    ConnectMonitoringListSharingPermissionsDataUserPermission,
)
from pycsapi.models.connect_monitoring_monitored_countries_in_portfolio import (
    ConnectMonitoringMonitoredCountriesInPortfolio,
)
from pycsapi.models.connect_monitoring_paging import ConnectMonitoringPaging
from pycsapi.models.connect_monitoring_risk_summary import ConnectMonitoringRiskSummary
from pycsapi.models.connect_monitoring_share_portfolio_request import (
    ConnectMonitoringSharePortfolioRequest,
)
from pycsapi.models.connect_monitoring_share_portfolio_request_body import (
    ConnectMonitoringSharePortfolioRequestBody,
)
from pycsapi.models.connect_monitoring_share_portfolio_request_response import (
    ConnectMonitoringSharePortfolioRequestResponse,
)
from pycsapi.models.connect_monitoring_share_portfolio_request_response_data import (
    ConnectMonitoringSharePortfolioRequestResponseData,
)
from pycsapi.models.connect_monitoring_update_company_details_in_portfolio_request import (
    ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest,
)
from pycsapi.models.connect_monitoring_update_company_in_portfolio import (
    ConnectMonitoringUpdateCompanyInPortfolio,
)
from pycsapi.models.connect_monitoring_update_event_rules_body import (
    ConnectMonitoringUpdateEventRulesBody,
)
from pycsapi.models.connect_monitoring_update_event_rules_request import (
    ConnectMonitoringUpdateEventRulesRequest,
)
from pycsapi.models.connect_monitoring_update_portfolio_request import (
    ConnectMonitoringUpdatePortfolioRequest,
)
from pycsapi.models.connect_monitoring_update_portfolio_request_email import (
    ConnectMonitoringUpdatePortfolioRequestEmail,
)
from pycsapi.models.connect_monitoring_user_details import ConnectMonitoringUserDetails
from pycsapi.models.connect_monitoring_user_details_inner import (
    ConnectMonitoringUserDetailsInner,
)
from pycsapi.models.connect_protect_address import ConnectProtectAddress
from pycsapi.models.connect_protect_alerts_frequency import (
    ConnectProtectAlertsFrequency,
)
from pycsapi.models.connect_protect_audit_dto import ConnectProtectAuditDto
from pycsapi.models.connect_protect_audit_export_payload_dto import (
    ConnectProtectAuditExportPayloadDto,
)
from pycsapi.models.connect_protect_audit_export_request_dto import (
    ConnectProtectAuditExportRequestDto,
)
from pycsapi.models.connect_protect_audits_export_response_dto import (
    ConnectProtectAuditsExportResponseDto,
)
from pycsapi.models.connect_protect_create_investigation_query_dto import (
    ConnectProtectCreateInvestigationQueryDto,
)
from pycsapi.models.connect_protect_create_investigation_record_body import (
    ConnectProtectCreateInvestigationRecordBody,
)
from pycsapi.models.connect_protect_create_profile_dto import (
    ConnectProtectCreateProfileDto,
)
from pycsapi.models.connect_protect_create_schedule_request import (
    ConnectProtectCreateScheduleRequest,
)
from pycsapi.models.connect_protect_error_responses_access_forbidden import (
    ConnectProtectErrorResponsesAccessForbidden,
)
from pycsapi.models.connect_protect_get_investigation_file_body_dto import (
    ConnectProtectGetInvestigationFileBodyDto,
)
from pycsapi.models.connect_protect_investigation import ConnectProtectInvestigation
from pycsapi.models.connect_protect_investigation_file_response import (
    ConnectProtectInvestigationFileResponse,
)
from pycsapi.models.connect_protect_investigation_query import (
    ConnectProtectInvestigationQuery,
)
from pycsapi.models.connect_protect_investigation_response import (
    ConnectProtectInvestigationResponse,
)
from pycsapi.models.connect_protect_investigation_type import (
    ConnectProtectInvestigationType,
)
from pycsapi.models.connect_protect_list_all_investigations_current_alert import (
    ConnectProtectListAllInvestigationsCurrentAlert,
)
from pycsapi.models.connect_protect_problem_details import ConnectProtectProblemDetails
from pycsapi.models.connect_protect_profile import ConnectProtectProfile
from pycsapi.models.connect_protect_record import ConnectProtectRecord
from pycsapi.models.connect_protect_schedule import ConnectProtectSchedule
from pycsapi.models.connect_resource_not_found_error_response import (
    ConnectResourceNotFoundErrorResponse,
)
from pycsapi.models.connect_us_local_solutions_fresh_inv_create_investigation import (
    ConnectUSLocalSolutionsFreshInvCreateInvestigation,
)
from pycsapi.models.connect_us_local_solutions_fresh_inv_create_investigation_form_data import (
    ConnectUSLocalSolutionsFreshInvCreateInvestigationFormData,
)
from pycsapi.models.connect_us_local_solutions_fresh_inv_create_investigation_form_data_fi_body import (
    ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody,
)
from pycsapi.models.connect_update_fresh_investigation import (
    ConnectUpdateFreshInvestigation,
)
from pycsapi.models.connect_update_fresh_investigation_pending_info import (
    ConnectUpdateFreshInvestigationPendingInfo,
)
from pycsapi.models.consumer_common_address import ConsumerCommonAddress
from pycsapi.models.consumer_common_current_address import ConsumerCommonCurrentAddress
from pycsapi.models.consumer_common_name import ConsumerCommonName
from pycsapi.models.consumer_result_electoral_roll_history import (
    ConsumerResultElectoralRollHistory,
)
from pycsapi.models.consumer_result_history import ConsumerResultHistory
from pycsapi.models.consumer_result_history_address import ConsumerResultHistoryAddress
from pycsapi.models.consumer_result_insolvencies import ConsumerResultInsolvencies
from pycsapi.models.consumer_result_insolvencies_address import (
    ConsumerResultInsolvenciesAddress,
)
from pycsapi.models.consumer_result_insolvencies_restriction import (
    ConsumerResultInsolvenciesRestriction,
)
from pycsapi.models.consumer_result_judgements import ConsumerResultJudgements
from pycsapi.models.consumer_result_judgements_address import (
    ConsumerResultJudgementsAddress,
)
from pycsapi.models.consumer_result_link_aliases import ConsumerResultLinkAliases
from pycsapi.models.consumer_result_link_associates import ConsumerResultLinkAssociates
from pycsapi.models.consumer_result_links_undeclared_addresses import (
    ConsumerResultLinksUndeclaredAddresses,
)
from pycsapi.models.consumer_result_links_undeclared_addresses_supplier_details import (
    ConsumerResultLinksUndeclaredAddressesSupplierDetails,
)
from pycsapi.models.consumer_result_notices import ConsumerResultNotices
from pycsapi.models.consumer_result_report_summary import ConsumerResultReportSummary
from pycsapi.models.consumer_result_report_summary_address import (
    ConsumerResultReportSummaryAddress,
)
from pycsapi.models.consumer_result_report_summary_card_data import (
    ConsumerResultReportSummaryCardData,
)
from pycsapi.models.consumer_result_report_summary_credit_searches_at_current_address import (
    ConsumerResultReportSummaryCreditSearchesAtCurrentAddress,
)
from pycsapi.models.consumer_result_report_summary_impaired_credit_history import (
    ConsumerResultReportSummaryImpairedCreditHistory,
)
from pycsapi.models.consumer_result_report_summary_insolvency_at_address import (
    ConsumerResultReportSummaryInsolvencyAtAddress,
)
from pycsapi.models.consumer_result_report_summary_judgements import (
    ConsumerResultReportSummaryJudgements,
)
from pycsapi.models.consumer_result_report_summary_links import (
    ConsumerResultReportSummaryLinks,
)
from pycsapi.models.consumer_result_report_summary_matched_data import (
    ConsumerResultReportSummaryMatchedData,
)
from pycsapi.models.consumer_result_report_summary_residency import (
    ConsumerResultReportSummaryResidency,
)
from pycsapi.models.consumer_result_report_summary_third_party import (
    ConsumerResultReportSummaryThirdParty,
)
from pycsapi.models.consumer_search import ConsumerSearch
from pycsapi.models.country_option import CountryOption
from pycsapi.models.create_investigation_note_dto import CreateInvestigationNoteDto
from pycsapi.models.create_investigation_query_dto import CreateInvestigationQueryDto
from pycsapi.models.create_investigation_record_body import (
    CreateInvestigationRecordBody,
)
from pycsapi.models.create_schedule_dto import CreateScheduleDto
from pycsapi.models.creditsafe_fresh_investigation_global_data_core_attachment_binary_attachment import (
    CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment,
)
from pycsapi.models.creditsafe_global_data_address_criteria_schema import (
    CreditsafeGlobalDataAddressCriteriaSchema,
)
from pycsapi.models.creditsafe_global_data_address_data import (
    CreditsafeGlobalDataAddressData,
)
from pycsapi.models.creditsafe_global_data_address_data_report import (
    CreditsafeGlobalDataAddressDataReport,
)
from pycsapi.models.creditsafe_global_data_company import CreditsafeGlobalDataCompany
from pycsapi.models.creditsafe_global_data_company_activity_classification import (
    CreditsafeGlobalDataCompanyActivityClassification,
)
from pycsapi.models.creditsafe_global_data_company_data import (
    CreditsafeGlobalDataCompanyData,
)
from pycsapi.models.creditsafe_global_data_company_data_additional_data import (
    CreditsafeGlobalDataCompanyDataAdditionalData,
)
from pycsapi.models.creditsafe_global_data_company_status import (
    CreditsafeGlobalDataCompanyStatus,
)
from pycsapi.models.creditsafe_global_data_company_type import (
    CreditsafeGlobalDataCompanyType,
)
from pycsapi.models.creditsafe_global_data_core_attachment_binary_attachment import (
    CreditsafeGlobalDataCoreAttachmentBinaryAttachment,
)
from pycsapi.models.creditsafe_global_data_core_supplier_connector_consumer_report_response import (
    CreditsafeGlobalDataCoreSupplierConnectorConsumerReportResponse,
)
from pycsapi.models.creditsafe_global_data_countries_list import (
    CreditsafeGlobalDataCountriesList,
)
from pycsapi.models.creditsafe_global_data_country import CreditsafeGlobalDataCountry
from pycsapi.models.creditsafe_global_data_country_code import (
    CreditsafeGlobalDataCountryCode,
)
from pycsapi.models.creditsafe_global_data_currency import CreditsafeGlobalDataCurrency
from pycsapi.models.creditsafe_global_data_custom_data_entry_schema import (
    CreditsafeGlobalDataCustomDataEntrySchema,
)
from pycsapi.models.creditsafe_global_data_custom_data_schema import (
    CreditsafeGlobalDataCustomDataSchema,
)
from pycsapi.models.creditsafe_global_data_director_search_data import (
    CreditsafeGlobalDataDirectorSearchData,
)
from pycsapi.models.creditsafe_global_data_director_search_data_company import (
    CreditsafeGlobalDataDirectorSearchDataCompany,
)
from pycsapi.models.creditsafe_global_data_language import CreditsafeGlobalDataLanguage
from pycsapi.models.creditsafe_global_data_message import CreditsafeGlobalDataMessage
from pycsapi.models.creditsafe_global_data_message_code import (
    CreditsafeGlobalDataMessageCode,
)
from pycsapi.models.creditsafe_global_data_message_type import (
    CreditsafeGlobalDataMessageType,
)
from pycsapi.models.creditsafe_global_data_office_type import (
    CreditsafeGlobalDataOfficeType,
)
from pycsapi.models.creditsafe_global_data_query_match_type import (
    CreditsafeGlobalDataQueryMatchType,
)
from pycsapi.models.creditsafe_global_data_reports_additional_data import (
    CreditsafeGlobalDataReportsAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_advisor import (
    CreditsafeGlobalDataReportsAdvisor,
)
from pycsapi.models.creditsafe_global_data_reports_balance_sheet import (
    CreditsafeGlobalDataReportsBalanceSheet,
)
from pycsapi.models.creditsafe_global_data_reports_banker import (
    CreditsafeGlobalDataReportsBanker,
)
from pycsapi.models.creditsafe_global_data_reports_common_rating_value import (
    CreditsafeGlobalDataReportsCommonRatingValue,
)
from pycsapi.models.creditsafe_global_data_reports_company_activity import (
    CreditsafeGlobalDataReportsCompanyActivity,
)
from pycsapi.models.creditsafe_global_data_reports_company_activity_list import (
    CreditsafeGlobalDataReportsCompanyActivityList,
)
from pycsapi.models.creditsafe_global_data_reports_company_in_group import (
    CreditsafeGlobalDataReportsCompanyInGroup,
)
from pycsapi.models.creditsafe_global_data_reports_company_in_group_additional_data import (
    CreditsafeGlobalDataReportsCompanyInGroupAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_company_report import (
    CreditsafeGlobalDataReportsCompanyReport,
)
from pycsapi.models.creditsafe_global_data_reports_company_report_extra_section import (
    CreditsafeGlobalDataReportsCompanyReportExtraSection,
)
from pycsapi.models.creditsafe_global_data_reports_company_report_response import (
    CreditsafeGlobalDataReportsCompanyReportResponse,
)
from pycsapi.models.creditsafe_global_data_reports_company_status_description import (
    CreditsafeGlobalDataReportsCompanyStatusDescription,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_additional_information import (
    CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_credit_rating import (
    CreditsafeGlobalDataReportsConsumerConsumerCreditRating,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_credit_score import (
    CreditsafeGlobalDataReportsConsumerConsumerCreditScore,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_directorship import (
    CreditsafeGlobalDataReportsConsumerConsumerDirectorship,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_income import (
    CreditsafeGlobalDataReportsConsumerConsumerIncome,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_information import (
    CreditsafeGlobalDataReportsConsumerConsumerInformation,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_information_additional_data import (
    CreditsafeGlobalDataReportsConsumerConsumerInformationAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_payment_summary import (
    CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_remark_of_payment import (
    CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_consumer_report import (
    CreditsafeGlobalDataReportsConsumerConsumerReport,
)
from pycsapi.models.creditsafe_global_data_reports_consumer_criteria_set import (
    CreditsafeGlobalDataReportsConsumerCriteriaSet,
)
from pycsapi.models.creditsafe_global_data_reports_corporate_position import (
    CreditsafeGlobalDataReportsCorporatePosition,
)
from pycsapi.models.creditsafe_global_data_reports_corporate_position_additional_data import (
    CreditsafeGlobalDataReportsCorporatePositionAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_corporate_position_resigned import (
    CreditsafeGlobalDataReportsCorporatePositionResigned,
)
from pycsapi.models.creditsafe_global_data_reports_credit_rating import (
    CreditsafeGlobalDataReportsCreditRating,
)
from pycsapi.models.creditsafe_global_data_reports_director import (
    CreditsafeGlobalDataReportsDirector,
)
from pycsapi.models.creditsafe_global_data_reports_director_additional_data import (
    CreditsafeGlobalDataReportsDirectorAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_directors_director_report import (
    CreditsafeGlobalDataReportsDirectorsDirectorReport,
)
from pycsapi.models.creditsafe_global_data_reports_directors_director_report_response import (
    CreditsafeGlobalDataReportsDirectorsDirectorReportResponse,
)
from pycsapi.models.creditsafe_global_data_reports_directors_director_summary import (
    CreditsafeGlobalDataReportsDirectorsDirectorSummary,
)
from pycsapi.models.creditsafe_global_data_reports_directors_directorship import (
    CreditsafeGlobalDataReportsDirectorsDirectorship,
)
from pycsapi.models.creditsafe_global_data_reports_directors_directorship_additional_data import (
    CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_directors_directorships import (
    CreditsafeGlobalDataReportsDirectorsDirectorships,
)
from pycsapi.models.creditsafe_global_data_reports_directorship import (
    CreditsafeGlobalDataReportsDirectorship,
)
from pycsapi.models.creditsafe_global_data_reports_directorships import (
    CreditsafeGlobalDataReportsDirectorships,
)
from pycsapi.models.creditsafe_global_data_reports_employee_information import (
    CreditsafeGlobalDataReportsEmployeeInformation,
)
from pycsapi.models.creditsafe_global_data_reports_entity import (
    CreditsafeGlobalDataReportsEntity,
)
from pycsapi.models.creditsafe_global_data_reports_entity_full_name import (
    CreditsafeGlobalDataReportsEntityFullName,
)
from pycsapi.models.creditsafe_global_data_reports_entity_type import (
    CreditsafeGlobalDataReportsEntityType,
)
from pycsapi.models.creditsafe_global_data_reports_financial_ratios import (
    CreditsafeGlobalDataReportsFinancialRatios,
)
from pycsapi.models.creditsafe_global_data_reports_financial_value1_system_decimal import (
    CreditsafeGlobalDataReportsFinancialValue1SystemDecimal,
)
from pycsapi.models.creditsafe_global_data_reports_financial_value1_system_string import (
    CreditsafeGlobalDataReportsFinancialValue1SystemString,
)
from pycsapi.models.creditsafe_global_data_reports_gender import (
    CreditsafeGlobalDataReportsGender,
)
from pycsapi.models.creditsafe_global_data_reports_global_financials_ggs import (
    CreditsafeGlobalDataReportsGlobalFinancialsGGS,
)
from pycsapi.models.creditsafe_global_data_reports_id_type import (
    CreditsafeGlobalDataReportsIdType,
)
from pycsapi.models.creditsafe_global_data_reports_indicator_industry_comparison import (
    CreditsafeGlobalDataReportsIndicatorIndustryComparison,
)
from pycsapi.models.creditsafe_global_data_reports_indicators import (
    CreditsafeGlobalDataReportsIndicators,
)
from pycsapi.models.creditsafe_global_data_reports_indicators_inner import (
    CreditsafeGlobalDataReportsIndicatorsInner,
)
from pycsapi.models.creditsafe_global_data_reports_legal_form import (
    CreditsafeGlobalDataReportsLegalForm,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_company_basic_information import (
    CreditsafeGlobalDataReportsLtdCompanyBasicInformation,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_company_identification import (
    CreditsafeGlobalDataReportsLtdCompanyIdentification,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_company_summary import (
    CreditsafeGlobalDataReportsLtdCompanySummary,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_contact_information import (
    CreditsafeGlobalDataReportsLtdContactInformation,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_credit_score import (
    CreditsafeGlobalDataReportsLtdCreditScore,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_directors import (
    CreditsafeGlobalDataReportsLtdDirectors,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_directors_extra import (
    CreditsafeGlobalDataReportsLtdDirectorsExtra,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_extended_group_structure_extra import (
    CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_financial_statement import (
    CreditsafeGlobalDataReportsLtdFinancialStatement,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_group_structure import (
    CreditsafeGlobalDataReportsLtdGroupStructure,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_other_information import (
    CreditsafeGlobalDataReportsLtdOtherInformation,
)
from pycsapi.models.creditsafe_global_data_reports_ltd_share_capital_structure import (
    CreditsafeGlobalDataReportsLtdShareCapitalStructure,
)
from pycsapi.models.creditsafe_global_data_reports_other_financials import (
    CreditsafeGlobalDataReportsOtherFinancials,
)
from pycsapi.models.creditsafe_global_data_reports_previous_director import (
    CreditsafeGlobalDataReportsPreviousDirector,
)
from pycsapi.models.creditsafe_global_data_reports_previous_legal_form import (
    CreditsafeGlobalDataReportsPreviousLegalForm,
)
from pycsapi.models.creditsafe_global_data_reports_previous_name import (
    CreditsafeGlobalDataReportsPreviousName,
)
from pycsapi.models.creditsafe_global_data_reports_previous_value import (
    CreditsafeGlobalDataReportsPreviousValue,
)
from pycsapi.models.creditsafe_global_data_reports_profit_and_loss_figures import (
    CreditsafeGlobalDataReportsProfitAndLossFigures,
)
from pycsapi.models.creditsafe_global_data_reports_range_described_value1_system_string import (
    CreditsafeGlobalDataReportsRangeDescribedValue1SystemString,
)
from pycsapi.models.creditsafe_global_data_reports_report_additional_information import (
    CreditsafeGlobalDataReportsReportAdditionalInformation,
)
from pycsapi.models.creditsafe_global_data_reports_report_alternate_summary import (
    CreditsafeGlobalDataReportsReportAlternateSummary,
)
from pycsapi.models.creditsafe_global_data_reports_report_negative_information import (
    CreditsafeGlobalDataReportsReportNegativeInformation,
)
from pycsapi.models.creditsafe_global_data_reports_report_negative_information_extra import (
    CreditsafeGlobalDataReportsReportNegativeInformationExtra,
)
from pycsapi.models.creditsafe_global_data_reports_report_payment_data import (
    CreditsafeGlobalDataReportsReportPaymentData,
)
from pycsapi.models.creditsafe_global_data_reports_report_payment_data_extra import (
    CreditsafeGlobalDataReportsReportPaymentDataExtra,
)
from pycsapi.models.creditsafe_global_data_reports_report_section import (
    CreditsafeGlobalDataReportsReportSection,
)
from pycsapi.models.creditsafe_global_data_reports_share_class import (
    CreditsafeGlobalDataReportsShareClass,
)
from pycsapi.models.creditsafe_global_data_reports_share_class_additional_data import (
    CreditsafeGlobalDataReportsShareClassAdditionalData,
)
from pycsapi.models.creditsafe_global_data_reports_share_holder import (
    CreditsafeGlobalDataReportsShareHolder,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema import (
    CreditsafeGlobalDataSearchCriteriaSchema,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_base import (
    CreditsafeGlobalDataSearchCriteriaSchemaBase,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_country import (
    CreditsafeGlobalDataSearchCriteriaSchemaCountry,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_country_director import (
    CreditsafeGlobalDataSearchCriteriaSchemaCountryDirector,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_director import (
    CreditsafeGlobalDataSearchCriteriaSchemaDirector,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_query_string_schema import (
    CreditsafeGlobalDataSearchCriteriaSchemaQueryStringSchema,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_set import (
    CreditsafeGlobalDataSearchCriteriaSchemaSet,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_set_director import (
    CreditsafeGlobalDataSearchCriteriaSchemaSetDirector,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_value_schema1_creditsafe_global_data_company_status import (
    CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyStatus,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_value_schema1_creditsafe_global_data_company_type import (
    CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataCompanyType,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_value_schema1_creditsafe_global_data_office_type import (
    CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1CreditsafeGlobalDataOfficeType,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_value_schema1_system_boolean import (
    CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemBoolean,
)
from pycsapi.models.creditsafe_global_data_search_criteria_schema_value_schema1_system_string import (
    CreditsafeGlobalDataSearchCriteriaSchemaValueSchema1SystemString,
)
from pycsapi.models.creditsafe_global_data_search_response1_creditsafe_global_data_company import (
    CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataCompany,
)
from pycsapi.models.creditsafe_global_data_search_response1_creditsafe_global_data_director_search_data import (
    CreditsafeGlobalDataSearchResponse1CreditsafeGlobalDataDirectorSearchData,
)
from pycsapi.models.creditsafe_global_data_service_response import (
    CreditsafeGlobalDataServiceResponse,
)
from pycsapi.models.creditsafe_global_data_service_response1_creditsafe_global_data_services_be_data_service_raw_client_raw_wrapped_upp_response import (
    CreditsafeGlobalDataServiceResponse1CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse,
)
from pycsapi.models.creditsafe_global_data_services_be_data_service_raw_client_raw_wrapped_upp_response import (
    CreditsafeGlobalDataServicesBEDataServiceRawClientRawWrappedUPPResponse,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_additional_data_shareholder_detail import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderAdditionalDataShareholderDetail,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_beneficial_ownership_report import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderBeneficialOwnershipReport,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholder import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholder,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholder_and_beneficial_ownership_report import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderAndBeneficialOwnershipReport,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholder_report import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderReport,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholder_structure import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderStructure,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholder_summary import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholderSummary,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholding import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholding,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholding_additional_data import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdingAdditionalData,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_model_shareholder_shareholdings import (
    CreditsafeGlobalDataServicesDEDataServiceModelShareholderShareholdings,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_raw_client_company_bankruptcy_bankruptcy_report_response import (
    CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcyBankruptcyReportResponse,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_raw_client_company_bankruptcy_search_bankruptcy import (
    CreditsafeGlobalDataServicesDEDataServiceRawClientCompanyBankruptcySearchBankruptcy,
)
from pycsapi.models.creditsafe_global_data_services_de_data_service_raw_client_shareholders_shareholder_report_response import (
    CreditsafeGlobalDataServicesDEDataServiceRawClientShareholdersShareholderReportResponse,
)
from pycsapi.models.creditsafe_local_solutions_gb_land_registry import (
    CreditsafeLocalSolutionsGBLandRegistry,
)
from pycsapi.models.creditsafe_us_local_fi_response import CreditsafeUSLocalFIResponse
from pycsapi.models.creditsafe_us_local_fi_response_fresh_investigation_request_result import (
    CreditsafeUSLocalFIResponseFreshInvestigationRequestResult,
)
from pycsapi.models.delete_fresh_invetigations_by_order_id import (
    DeleteFreshInvetigationsByOrderId,
)
from pycsapi.models.delete_kyc_monitoring_profiles_response import (
    DeleteKYCMonitoringProfilesResponse,
)
from pycsapi.models.delete_kyc_monitoring_profiles_response_failed import (
    DeleteKYCMonitoringProfilesResponseFailed,
)
from pycsapi.models.delete_kyc_monitoring_profiles_resquest import (
    DeleteKYCMonitoringProfilesResquest,
)
from pycsapi.models.delete_kyc_profile_searches_by_profile_id_request_body import (
    DeleteKYCProfileSearchesByProfileIdRequestBody,
)
from pycsapi.models.delete_kyc_profile_searches_by_profile_id_response import (
    DeleteKYCProfileSearchesByProfileIdResponse,
)
from pycsapi.models.delete_kyc_profile_searches_by_profile_id_response_error import (
    DeleteKYCProfileSearchesByProfileIdResponseError,
)
from pycsapi.models.delete_kyc_profile_searches_by_profile_id_response_failed import (
    DeleteKYCProfileSearchesByProfileIdResponseFailed,
)
from pycsapi.models.delete_kyc_profiles import DeleteKYCProfiles
from pycsapi.models.delete_kyc_protect_schedules_response import (
    DeleteKYCProtectSchedulesResponse,
)
from pycsapi.models.delete_kyc_protect_schedules_response_failed import (
    DeleteKYCProtectSchedulesResponseFailed,
)
from pycsapi.models.delete_key_parties_response_by_profile_id import (
    DeleteKeyPartiesResponseByProfileId,
)
from pycsapi.models.delete_key_parties_response_by_profile_id_failed_object_response import (
    DeleteKeyPartiesResponseByProfileIdFailedObjectResponse,
)
from pycsapi.models.delete_key_parties_response_by_profile_id_failed_object_response_error import (
    DeleteKeyPartiesResponseByProfileIdFailedObjectResponseError,
)
from pycsapi.models.delete_key_party_by_id_no_content import DeleteKeyPartyByIdNoContent
from pycsapi.models.delete_key_party_search_contract_request import (
    DeleteKeyPartySearchContractRequest,
)
from pycsapi.models.delete_key_party_search_contract_request_items import (
    DeleteKeyPartySearchContractRequestItems,
)
from pycsapi.models.delete_key_party_search_contract_response import (
    DeleteKeyPartySearchContractResponse,
)
from pycsapi.models.delete_key_party_search_contract_response_error import (
    DeleteKeyPartySearchContractResponseError,
)
from pycsapi.models.delete_key_party_search_contract_response_failed import (
    DeleteKeyPartySearchContractResponseFailed,
)
from pycsapi.models.delete_key_party_search_contract_response_failed_item import (
    DeleteKeyPartySearchContractResponseFailedItem,
)
from pycsapi.models.delete_records_dto import DeleteRecordsDto
from pycsapi.models.details_addresses_body import DetailsAddressesBody
from pycsapi.models.download_attachment import DownloadAttachment
from pycsapi.models.download_attachment_response import DownloadAttachmentResponse
from pycsapi.models.file_download_response import FileDownloadResponse
from pycsapi.models.fresh_investigation_attachment_upload_for_order_request import (
    FreshInvestigationAttachmentUploadForOrderRequest,
)
from pycsapi.models.fresh_investigation_attachment_upload_for_order_response import (
    FreshInvestigationAttachmentUploadForOrderResponse,
)
from pycsapi.models.fresh_investigation_comments_for_order_request import (
    FreshInvestigationCommentsForOrderRequest,
)
from pycsapi.models.fresh_investigation_comments_for_order_response import (
    FreshInvestigationCommentsForOrderResponse,
)
from pycsapi.models.fresh_investigation_get_attachments_for_order_response import (
    FreshInvestigationGetAttachmentsForOrderResponse,
)
from pycsapi.models.fresh_investigation_get_attachments_for_order_response_attachments import (
    FreshInvestigationGetAttachmentsForOrderResponseAttachments,
)
from pycsapi.models.gb_local_solution_bank_verification_search_request import (
    GBLocalSolutionBankVerificationSearchRequest,
)
from pycsapi.models.gb_local_solution_bank_verification_search_response import (
    GBLocalSolutionBankVerificationSearchResponse,
)
from pycsapi.models.gb_local_solution_bank_verification_search_response_supplier_request_data import (
    GBLocalSolutionBankVerificationSearchResponseSupplierRequestData,
)
from pycsapi.models.gb_local_solution_bank_verification_search_response_supplier_response import (
    GBLocalSolutionBankVerificationSearchResponseSupplierResponse,
)
from pycsapi.models.gb_local_solution_cp_history_request_by_id_request import (
    GBLocalSolutionCPHistoryRequestByIdRequest,
)
from pycsapi.models.gb_local_solution_get_history_list_response import (
    GBLocalSolutionGetHistoryListResponse,
)
from pycsapi.models.gb_local_solution_get_history_request_response import (
    GBLocalSolutionGetHistoryRequestResponse,
)
from pycsapi.models.gb_local_solution_get_history_request_response_supplier_request_data import (
    GBLocalSolutionGetHistoryRequestResponseSupplierRequestData,
)
from pycsapi.models.gb_local_solution_get_history_request_response_supplier_response import (
    GBLocalSolutionGetHistoryRequestResponseSupplierResponse,
)
from pycsapi.models.gender_type import GenderType
from pycsapi.models.get_audits_response import GetAuditsResponse
from pycsapi.models.get_audits_response_items import GetAuditsResponseItems
from pycsapi.models.get_batch_uploads_download_errors_by_upload_id_response import (
    GetBatchUploadsDownloadErrorsByUploadIdResponse,
)
from pycsapi.models.get_batch_uploads_template_response import (
    GetBatchUploadsTemplateResponse,
)
from pycsapi.models.get_decision_engine_decision_outcome_response import (
    GetDecisionEngineDecisionOutcomeResponse,
)
from pycsapi.models.get_decision_engine_decision_outcome_response_decision_outcomes import (
    GetDecisionEngineDecisionOutcomeResponseDecisionOutcomes,
)
from pycsapi.models.get_decision_engine_decision_outcome_response_decision_outcomes_items import (
    GetDecisionEngineDecisionOutcomeResponseDecisionOutcomesItems,
)
from pycsapi.models.get_decision_engine_instances_response import (
    GetDecisionEngineInstancesResponse,
)
from pycsapi.models.get_decision_engine_instances_response_instances import (
    GetDecisionEngineInstancesResponseInstances,
)
from pycsapi.models.get_fresh_investigation_comments_by_order_id_response import (
    GetFreshInvestigationCommentsByOrderIdResponse,
)
from pycsapi.models.get_fresh_investigation_comments_by_order_id_response_comments import (
    GetFreshInvestigationCommentsByOrderIdResponseComments,
)
from pycsapi.models.get_individual_search_id_hits_response import (
    GetIndividualSearchIdHitsResponse,
)
from pycsapi.models.get_individual_search_id_hits_response_items import (
    GetIndividualSearchIdHitsResponseItems,
)
from pycsapi.models.get_individual_search_id_hits_response_superseded_hit import (
    GetIndividualSearchIdHitsResponseSupersededHit,
)
from pycsapi.models.get_investigation_file_body_dto import GetInvestigationFileBodyDto
from pycsapi.models.get_kyc_address_details_by_the_given_address_id_for_the_supplied_profile_id_user import (
    GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser,
)
from pycsapi.models.get_kyc_individual_search_response import (
    GetKYCIndividualSearchResponse,
)
from pycsapi.models.get_kyc_individual_search_response_items import (
    GetKYCIndividualSearchResponseItems,
)
from pycsapi.models.get_kyc_profile_attachment_details_by_attachment_id import (
    GetKYCProfileAttachmentDetailsByAttachmentId,
)
from pycsapi.models.get_kyc_profile_by_profile_id import GetKYCProfileByProfileId
from pycsapi.models.get_kyc_profile_details_by_profile_id import (
    GetKYCProfileDetailsByProfileId,
)
from pycsapi.models.get_kyc_profile_details_by_profile_id_turnover import (
    GetKYCProfileDetailsByProfileIdTurnover,
)
from pycsapi.models.get_kyc_profile_notes_by_note_id import GetKYCProfileNotesByNoteId
from pycsapi.models.get_kyc_profile_notes_by_note_id_request import (
    GetKYCProfileNotesByNoteIdRequest,
)
from pycsapi.models.get_kyc_profile_types import GetKYCProfileTypes
from pycsapi.models.get_kyc_profiles import GetKYCProfiles
from pycsapi.models.get_kyc_profiles_items import GetKYCProfilesItems
from pycsapi.models.get_kyc_protect_profile_id_note_id_response import (
    GetKYCProtectProfileIdNoteIdResponse,
)
from pycsapi.models.get_kyc_protect_profile_id_notes_response import (
    GetKYCProtectProfileIdNotesResponse,
)
from pycsapi.models.get_kyc_protect_profile_id_notes_response_items import (
    GetKYCProtectProfileIdNotesResponseItems,
)
from pycsapi.models.get_key_parties_response_by_profile_id import (
    GetKeyPartiesResponseByProfileId,
)
from pycsapi.models.get_key_parties_response_by_profile_id_items import (
    GetKeyPartiesResponseByProfileIdItems,
)
from pycsapi.models.get_key_parties_response_by_profile_id_items_address_response import (
    GetKeyPartiesResponseByProfileIdItemsAddressResponse,
)
from pycsapi.models.get_key_party_search_response import GetKeyPartySearchResponse
from pycsapi.models.get_kyc_protect_async_aml_job_criteria_response import (
    GetKycProtectAsyncAmlJobCriteriaResponse,
)
from pycsapi.models.get_kyc_protect_async_aml_job_item_response import (
    GetKycProtectAsyncAmlJobItemResponse,
)
from pycsapi.models.get_kyc_protect_async_aml_job_response import (
    GetKycProtectAsyncAmlJobResponse,
)
from pycsapi.models.get_kyc_protect_batch_uploads_by_upload_id_item_response import (
    GetKycProtectBatchUploadsByUploadIdItemResponse,
)
from pycsapi.models.get_kyc_protect_batch_uploads_by_uploads_response import (
    GetKycProtectBatchUploadsByUploadsResponse,
)
from pycsapi.models.get_profile_hits_by_profile_id_response import (
    GetProfileHitsByProfileIdResponse,
)
from pycsapi.models.get_profile_hits_by_profile_id_response_items import (
    GetProfileHitsByProfileIdResponseItems,
)
from pycsapi.models.get_profile_hits_by_profile_id_response_superseded_hit import (
    GetProfileHitsByProfileIdResponseSupersededHit,
)
from pycsapi.models.hits_hit_id_body import HitsHitIdBody
from pycsapi.models.id_enrichments_body import IdEnrichmentsBody
from pycsapi.models.idv_request_dto import IdvRequestDto
from pycsapi.models.idv_response_dto import IdvResponseDto
from pycsapi.models.idv_sources_dto import IdvSourcesDto
from pycsapi.models.individual_search_result_hit_response import (
    IndividualSearchResultHitResponse,
)
from pycsapi.models.individual_search_result_hit_response_aml_results import (
    IndividualSearchResultHitResponseAmlResults,
)
from pycsapi.models.individual_search_result_hit_summary_response import (
    IndividualSearchResultHitSummaryResponse,
)
from pycsapi.models.individual_search_update_hit_request import (
    IndividualSearchUpdateHitRequest,
)
from pycsapi.models.individuals_search_result_update_hits import (
    IndividualsSearchResultUpdateHits,
)
from pycsapi.models.inline_response200 import InlineResponse200
from pycsapi.models.inline_response2001 import InlineResponse2001
from pycsapi.models.inline_response20010 import InlineResponse20010
from pycsapi.models.inline_response20011 import InlineResponse20011
from pycsapi.models.inline_response20012 import InlineResponse20012
from pycsapi.models.inline_response20013 import InlineResponse20013
from pycsapi.models.inline_response20014 import InlineResponse20014
from pycsapi.models.inline_response20015 import InlineResponse20015
from pycsapi.models.inline_response20016 import InlineResponse20016
from pycsapi.models.inline_response2002 import InlineResponse2002
from pycsapi.models.inline_response2003 import InlineResponse2003
from pycsapi.models.inline_response2004 import InlineResponse2004
from pycsapi.models.inline_response2005 import InlineResponse2005
from pycsapi.models.inline_response2006 import InlineResponse2006
from pycsapi.models.inline_response2007 import InlineResponse2007
from pycsapi.models.inline_response2008 import InlineResponse2008
from pycsapi.models.inline_response2009 import InlineResponse2009
from pycsapi.models.inline_response201 import InlineResponse201
from pycsapi.models.inline_response204 import InlineResponse204
from pycsapi.models.inline_response404 import InlineResponse404
from pycsapi.models.inline_response4041 import InlineResponse4041
from pycsapi.models.inline_response409 import InlineResponse409
from pycsapi.models.international_age_algorithm import InternationalAgeAlgorithm
from pycsapi.models.international_age_algorithm_warning import (
    InternationalAgeAlgorithmWarning,
)
from pycsapi.models.international_enhanced_pep_database import (
    InternationalEnhancedPepDatabase,
)
from pycsapi.models.international_enhanced_pep_database_detail import (
    InternationalEnhancedPepDatabaseDetail,
)
from pycsapi.models.international_enhanced_pep_database_peps import (
    InternationalEnhancedPepDatabasePeps,
)
from pycsapi.models.international_sanctions import InternationalSanctions
from pycsapi.models.international_sanctions_detail import InternationalSanctionsDetail
from pycsapi.models.international_sanctions_detail_addresses import (
    InternationalSanctionsDetailAddresses,
)
from pycsapi.models.international_sanctions_detail_dates import (
    InternationalSanctionsDetailDates,
)
from pycsapi.models.international_sanctions_sanctions import (
    InternationalSanctionsSanctions,
)
from pycsapi.models.investigation import Investigation
from pycsapi.models.investigation_alert import InvestigationAlert
from pycsapi.models.investigation_alert_status import InvestigationAlertStatus
from pycsapi.models.investigation_note import InvestigationNote
from pycsapi.models.investigation_order_bys import InvestigationOrderBys
from pycsapi.models.investigation_query import InvestigationQuery
from pycsapi.models.investigation_record_dto import InvestigationRecordDto
from pycsapi.models.investigation_response import InvestigationResponse
from pycsapi.models.investigation_risk import InvestigationRisk
from pycsapi.models.investigation_risk_response import InvestigationRiskResponse
from pycsapi.models.investigation_status import InvestigationStatus
from pycsapi.models.investigation_type import InvestigationType
from pycsapi.models.job_enrichment_settings import JobEnrichmentSettings
from pycsapi.models.job_mapping_dto import JobMappingDto
from pycsapi.models.kyc_base_business_search_result_hit_summary_response import (
    KYCBaseBusinessSearchResultHitSummaryResponse,
)
from pycsapi.models.kyc_business_search_result_hit_summary_response import (
    KYCBusinessSearchResultHitSummaryResponse,
)
from pycsapi.models.kyc_get_search_businesses_by_search_id_hits_response import (
    KYCGetSearchBusinessesBySearchIdHitsResponse,
)
from pycsapi.models.kyc_get_search_businesses_by_search_id_hits_response_items import (
    KYCGetSearchBusinessesBySearchIdHitsResponseItems,
)
from pycsapi.models.kyc_get_search_businesses_by_search_id_hits_response_superseded_hit import (
    KYCGetSearchBusinessesBySearchIdHitsResponseSupersededHit,
)
from pycsapi.models.kyc_get_search_businesses_by_search_id_response import (
    KYCGetSearchBusinessesBySearchIdResponse,
)
from pycsapi.models.kyc_get_search_individual_by_search_id_response import (
    KYCGetSearchIndividualBySearchIdResponse,
)
from pycsapi.models.kycput_search_businesses_response import (
    KYCPUTSearchBusinessesResponse,
)
from pycsapi.models.kycput_search_businesses_response_failed import (
    KYCPUTSearchBusinessesResponseFailed,
)
from pycsapi.models.kycput_search_businesses_response_failed_item import (
    KYCPUTSearchBusinessesResponseFailedItem,
)
from pycsapi.models.kyc_post_individual_search_contract import (
    KYCPostIndividualSearchContract,
)
from pycsapi.models.kyc_profile_id_schedules_schedule_id_response import (
    KYCProfileIdSchedulesScheduleIdResponse,
)
from pycsapi.models.kyc_profile_schedule_response import KYCProfileScheduleResponse
from pycsapi.models.kyc_protect_base_individual_search_result_hit_summary_response import (
    KYCProtectBaseIndividualSearchResultHitSummaryResponse,
)
from pycsapi.models.kyc_protect_profile_details_note_by_note_id_not_found import (
    KYCProtectProfileDetailsNoteByNoteIdNotFound,
)
from pycsapi.models.kyc_protect_schedule_hit_response import (
    KYCProtectScheduleHitResponse,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response import (
    KYCPutSearchBusinessesBySearchIdHitsResponse,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response_failed import (
    KYCPutSearchBusinessesBySearchIdHitsResponseFailed,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response_failed_item import (
    KYCPutSearchBusinessesBySearchIdHitsResponseFailedItem,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response_items import (
    KYCPutSearchBusinessesBySearchIdHitsResponseItems,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response_successful import (
    KYCPutSearchBusinessesBySearchIdHitsResponseSuccessful,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_hits_response_superseded_hit import (
    KYCPutSearchBusinessesBySearchIdHitsResponseSupersededHit,
)
from pycsapi.models.kyc_put_search_businesses_by_search_id_response import (
    KYCPutSearchBusinessesBySearchIdResponse,
)
from pycsapi.models.kyc_put_search_individual_by_search_id_response import (
    KYCPutSearchIndividualBySearchIdResponse,
)
from pycsapi.models.key_party_by_id_return import KeyPartyByIdReturn
from pycsapi.models.key_party_by_id_return_address import KeyPartyByIdReturnAddress
from pycsapi.models.kyc_monitoring_kyc_alert_response import (
    KycMonitoringKycAlertResponse,
)
from pycsapi.models.kyc_protect_async_job_criteria_response import (
    KycProtectAsyncJobCriteriaResponse,
)
from pycsapi.models.kyc_protect_error_object import KycProtectErrorObject
from pycsapi.models.kyc_protect_get_customer_users_details_response import (
    KycProtectGetCustomerUsersDetailsResponse,
)
from pycsapi.models.kyc_protect_get_customer_users_details_response_items import (
    KycProtectGetCustomerUsersDetailsResponseItems,
)
from pycsapi.models.kyc_protect_get_individual_search_items import (
    KycProtectGetIndividualSearchItems,
)
from pycsapi.models.kyc_protect_get_my_user_details_response import (
    KycProtectGetMyUserDetailsResponse,
)
from pycsapi.models.kyc_protect_get_my_user_details_response_primary_contact import (
    KycProtectGetMyUserDetailsResponsePrimaryContact,
)
from pycsapi.models.kyc_protect_get_search_response import KycProtectGetSearchResponse
from pycsapi.models.kyc_protect_individual_search_response import (
    KycProtectIndividualSearchResponse,
)
from pycsapi.models.kyc_protect_post_post_individual_search_response import (
    KycProtectPostPostIndividualSearchResponse,
)
from pycsapi.models.kyc_protect_post_profiles_request import (
    KycProtectPostProfilesRequest,
)
from pycsapi.models.kyc_protect_post_profiles_request_details import (
    KycProtectPostProfilesRequestDetails,
)
from pycsapi.models.kyc_protect_post_profiles_request_details_assets_under_management import (
    KycProtectPostProfilesRequestDetailsAssetsUnderManagement,
)
from pycsapi.models.kyc_protect_post_profiles_request_details_turnover import (
    KycProtectPostProfilesRequestDetailsTurnover,
)
from pycsapi.models.kyc_protect_post_put_individual_search_request import (
    KycProtectPostPutIndividualSearchRequest,
)
from pycsapi.models.kyc_protect_problem_details import KycProtectProblemDetails
from pycsapi.models.kyc_protect_profile_address_response import (
    KycProtectProfileAddressResponse,
)
from pycsapi.models.kyc_protect_profile_assign_bulk_response import (
    KycProtectProfileAssignBulkResponse,
)
from pycsapi.models.kyc_protect_profile_attachment_response import (
    KycProtectProfileAttachmentResponse,
)
from pycsapi.models.kyc_protect_profile_conflict_response import (
    KycProtectProfileConflictResponse,
)
from pycsapi.models.kyc_protect_profile_created_response import (
    KycProtectProfileCreatedResponse,
)
from pycsapi.models.kyc_protect_profile_created_response_details import (
    KycProtectProfileCreatedResponseDetails,
)
from pycsapi.models.kyc_protect_profile_created_response_details_assets_under_management import (
    KycProtectProfileCreatedResponseDetailsAssetsUnderManagement,
)
from pycsapi.models.kyc_protect_profile_created_response_details_turnover import (
    KycProtectProfileCreatedResponseDetailsTurnover,
)
from pycsapi.models.kyc_protect_profile_details_response import (
    KycProtectProfileDetailsResponse,
)
from pycsapi.models.kyc_protect_profile_details_response_turnover import (
    KycProtectProfileDetailsResponseTurnover,
)
from pycsapi.models.kyc_protect_profile_get_attachment_response import (
    KycProtectProfileGetAttachmentResponse,
)
from pycsapi.models.kyc_protect_profile_get_details_address_response import (
    KycProtectProfileGetDetailsAddressResponse,
)
from pycsapi.models.kycprotect_schedules_body import KycprotectSchedulesBody
from pycsapi.models.kycprotect_schedules_body1 import KycprotectSchedulesBody1
from pycsapi.models.local_solutions_fr_bank_match import LocalSolutionsFRBankMatch
from pycsapi.models.local_solutions_fr_bank_match_entity import (
    LocalSolutionsFRBankMatchEntity,
)
from pycsapi.models.local_solutions_fr_bank_match_entity_additional_properties import (
    LocalSolutionsFRBankMatchEntityAdditionalProperties,
)
from pycsapi.models.local_solutions_fr_bank_match_entity_additional_properties_vat_request_info import (
    LocalSolutionsFRBankMatchEntityAdditionalPropertiesVatRequestInfo,
)
from pycsapi.models.local_solutions_fr_bank_match_entity_company import (
    LocalSolutionsFRBankMatchEntityCompany,
)
from pycsapi.models.local_solutions_fr_bank_match_entity_payment_identity import (
    LocalSolutionsFRBankMatchEntityPaymentIdentity,
)
from pycsapi.models.local_solutions_fr_bank_match_input import (
    LocalSolutionsFRBankMatchInput,
)
from pycsapi.models.local_solutions_fr_bank_match_input_company import (
    LocalSolutionsFRBankMatchInputCompany,
)
from pycsapi.models.local_solutions_fr_bank_match_input_payment_identity import (
    LocalSolutionsFRBankMatchInputPaymentIdentity,
)
from pycsapi.models.local_solutions_fr_bank_match_issuer_company import (
    LocalSolutionsFRBankMatchIssuerCompany,
)
from pycsapi.models.model1c736e import MODEL1c736e
from pycsapi.models.model1e2683 import MODEL1e2683
from pycsapi.models.model1e2683_items import MODEL1e2683Items
from pycsapi.models.model20274f import MODEL20274f
from pycsapi.models.model28cf8d import MODEL28cf8d
from pycsapi.models.model3eb319 import MODEL3eb319
from pycsapi.models.model3eb319_failed import MODEL3eb319Failed
from pycsapi.models.model4df4ca import MODEL4df4ca
from pycsapi.models.model4f561c import MODEL4f561c
from pycsapi.models.model5941c0 import MODEL5941c0
from pycsapi.models.model5b4b1c import MODEL5b4b1c
from pycsapi.models.model5bb0b0 import MODEL5bb0b0
from pycsapi.models.model5bdbb3 import MODEL5bdbb3
from pycsapi.models.model6bcc20 import MODEL6bcc20
from pycsapi.models.model7b2457 import MODEL7b2457
from pycsapi.models.model7b2457_items import MODEL7b2457Items
from pycsapi.models.model7c8060 import MODEL7c8060
from pycsapi.models.model7fba1c import MODEL7fba1c
from pycsapi.models.model8790cc import MODEL8790cc
from pycsapi.models.model931a1b import MODEL931a1b
from pycsapi.models.modelb33a65 import MODELb33a65
from pycsapi.models.mode_lcebf3b import MODELcebf3b
from pycsapi.models.mode_lcf4983 import MODELcf4983
from pycsapi.models.modele000b1 import MODELe000b1
from pycsapi.models.modelf6df8e import MODELf6df8e
from pycsapi.models.modelf73bb1 import MODELf73bb1
from pycsapi.models.modelf73bb1_items import MODELf73bb1Items
from pycsapi.models.match_rate import MatchRate
from pycsapi.models.match_type import MatchType
from pycsapi.models.one_of_creditsafe_global_data_company_data_vat_no import (
    OneOfCreditsafeGlobalDataCompanyDataVatNo,
)
from pycsapi.models.order_direction import OrderDirection
from pycsapi.models.post_kyc_keyparties_by_profile_id_address_contract_response import (
    PostKYCKeypartiesByProfileIdAddressContractResponse,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_address_request_contract_response import (
    PostKYCKeypartiesByProfileIdAddressRequestContractResponse,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_failed_add_key_party_contract_response import (
    PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_failed_response import (
    PostKYCKeypartiesByProfileIdFailedResponse,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_request import (
    PostKYCKeypartiesByProfileIdRequest,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_request_address import (
    PostKYCKeypartiesByProfileIdRequestAddress,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_request_items import (
    PostKYCKeypartiesByProfileIdRequestItems,
)
from pycsapi.models.post_kyc_keyparties_by_profile_id_response import (
    PostKYCKeypartiesByProfileIdResponse,
)
from pycsapi.models.post_kyc_keyparties_searches_link_by_profile_id_response import (
    PostKYCKeypartiesSearchesLinkByProfileIdResponse,
)
from pycsapi.models.post_kyc_keyparties_searches_link_by_profile_id_response_error import (
    PostKYCKeypartiesSearchesLinkByProfileIdResponseError,
)
from pycsapi.models.post_kyc_keyparties_searches_link_by_profile_id_response_failed import (
    PostKYCKeypartiesSearchesLinkByProfileIdResponseFailed,
)
from pycsapi.models.post_kyc_keyparties_searches_link_by_profile_id_response_failed_item import (
    PostKYCKeypartiesSearchesLinkByProfileIdResponseFailedItem,
)
from pycsapi.models.post_kyc_monitoring_profiles_bulk_response import (
    PostKYCMonitoringProfilesBulkResponse,
)
from pycsapi.models.post_kyc_monitoring_profiles_bulk_response_error import (
    PostKYCMonitoringProfilesBulkResponseError,
)
from pycsapi.models.post_kyc_monitoring_profiles_bulk_response_failed import (
    PostKYCMonitoringProfilesBulkResponseFailed,
)
from pycsapi.models.post_kyc_monitoring_profiles_bulk_resquest import (
    PostKYCMonitoringProfilesBulkResquest,
)
from pycsapi.models.post_kyc_profile_notes import PostKYCProfileNotes
from pycsapi.models.post_kyc_profile_notes_request import PostKYCProfileNotesRequest
from pycsapi.models.post_kyc_protect_schedules_request import (
    PostKYCProtectSchedulesRequest,
)
from pycsapi.models.post_kyc_protect_schedules_response import (
    PostKYCProtectSchedulesResponse,
)
from pycsapi.models.post_kyc_protect_schedules_response_failed import (
    PostKYCProtectSchedulesResponseFailed,
)
from pycsapi.models.post_kyc_protect_batch_uploads_request import (
    PostKycProtectBatchUploadsRequest,
)
from pycsapi.models.post_kyc_protect_batch_uploads_response import (
    PostKycProtectBatchUploadsResponse,
)
from pycsapi.models.problem_details import ProblemDetails
from pycsapi.models.profile_id_attachments_body import ProfileIdAttachmentsBody
from pycsapi.models.profile_id_keyparties_body import ProfileIdKeypartiesBody
from pycsapi.models.protect_batch_uploads_body import ProtectBatchUploadsBody
from pycsapi.models.put_batch_uploads_retry_by_id_response import (
    PutBatchUploadsRetryByIdResponse,
)
from pycsapi.models.put_individual_search_id_hits_by_hit_id_response import (
    PutIndividualSearchIdHitsByHitIdResponse,
)
from pycsapi.models.put_individual_search_id_hits_by_hit_id_response_superseded_hit import (
    PutIndividualSearchIdHitsByHitIdResponseSupersededHit,
)
from pycsapi.models.put_individual_search_id_hits_response import (
    PutIndividualSearchIdHitsResponse,
)
from pycsapi.models.put_individual_search_id_hits_response_error import (
    PutIndividualSearchIdHitsResponseError,
)
from pycsapi.models.put_individual_search_id_hits_response_failed import (
    PutIndividualSearchIdHitsResponseFailed,
)
from pycsapi.models.put_individual_search_id_hits_response_failed_item import (
    PutIndividualSearchIdHitsResponseFailedItem,
)
from pycsapi.models.put_individual_search_id_hits_response_successful import (
    PutIndividualSearchIdHitsResponseSuccessful,
)
from pycsapi.models.put_individual_search_id_hits_response_superseded_hit import (
    PutIndividualSearchIdHitsResponseSupersededHit,
)
from pycsapi.models.put_kyc_address_details_by_the_given_address_id_for_the_supplied_profile_id_user import (
    PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser,
)
from pycsapi.models.put_kyc_individual_search_by_search_id_request import (
    PutKYCIndividualSearchBySearchIdRequest,
)
from pycsapi.models.put_kyc_individual_search_request import (
    PutKYCIndividualSearchRequest,
)
from pycsapi.models.put_kyc_individual_search_request_items import (
    PutKYCIndividualSearchRequestItems,
)
from pycsapi.models.put_kyc_keyparties_by_profile_id_address_contract import (
    PutKYCKeypartiesByProfileIdAddressContract,
)
from pycsapi.models.put_kyc_keyparties_by_profile_id_failed_contract_response import (
    PutKYCKeypartiesByProfileIdFailedContractResponse,
)
from pycsapi.models.put_kyc_keyparties_by_profile_id_failed_response import (
    PutKYCKeypartiesByProfileIdFailedResponse,
)
from pycsapi.models.put_kyc_keyparties_by_profile_id_request import (
    PutKYCKeypartiesByProfileIdRequest,
)
from pycsapi.models.put_kyc_keyparties_by_profile_id_request_items import (
    PutKYCKeypartiesByProfileIdRequestItems,
)
from pycsapi.models.put_kyc_profile_assign import PutKYCProfileAssign
from pycsapi.models.put_kyc_profile_details_by_profile_id import (
    PutKYCProfileDetailsByProfileId,
)
from pycsapi.models.put_kyc_profile_details_by_profile_id_request import (
    PutKYCProfileDetailsByProfileIdRequest,
)
from pycsapi.models.put_kyc_profile_details_by_profile_id_request_assets_under_management import (
    PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement,
)
from pycsapi.models.put_kyc_profile_details_by_profile_id_request_turnover import (
    PutKYCProfileDetailsByProfileIdRequestTurnover,
)
from pycsapi.models.put_kyc_profile_details_note_by_note_id_response import (
    PutKYCProfileDetailsNoteByNoteIdResponse,
)
from pycsapi.models.put_kyc_profile_notes_by_note_id import PutKYCProfileNotesByNoteId
from pycsapi.models.put_kyc_profile_notes_by_note_id_request import (
    PutKYCProfileNotesByNoteIdRequest,
)
from pycsapi.models.put_kyc_protect_schedules_response import (
    PutKYCProtectSchedulesResponse,
)
from pycsapi.models.put_kyc_protect_schedules_response_error import (
    PutKYCProtectSchedulesResponseError,
)
from pycsapi.models.put_kyc_protect_schedules_response_failed import (
    PutKYCProtectSchedulesResponseFailed,
)
from pycsapi.models.put_kyc_protect_schedules_response_failed_item import (
    PutKYCProtectSchedulesResponseFailedItem,
)
from pycsapi.models.put_kyc_protect_schedules_response_successful import (
    PutKYCProtectSchedulesResponseSuccessful,
)
from pycsapi.models.put_kyc_search_individual_response import (
    PutKYCSearchIndividualResponse,
)
from pycsapi.models.put_kyc_search_individual_response_error import (
    PutKYCSearchIndividualResponseError,
)
from pycsapi.models.put_kyc_search_individual_response_failed import (
    PutKYCSearchIndividualResponseFailed,
)
from pycsapi.models.put_kyc_search_individual_response_failed_item import (
    PutKYCSearchIndividualResponseFailedItem,
)
from pycsapi.models.put_kyc_search_individual_response_successful import (
    PutKYCSearchIndividualResponseSuccessful,
)
from pycsapi.models.record import Record
from pycsapi.models.schedule import Schedule
from pycsapi.models.schedule_response import ScheduleResponse
from pycsapi.models.schedule_response_items import ScheduleResponseItems
from pycsapi.models.search_result_hits_address_response import (
    SearchResultHitsAddressResponse,
)
from pycsapi.models.search_result_hits_business_link_response import (
    SearchResultHitsBusinessLinkResponse,
)
from pycsapi.models.search_result_hits_contact_response import (
    SearchResultHitsContactResponse,
)
from pycsapi.models.search_result_hits_identifier_response import (
    SearchResultHitsIdentifierResponse,
)
from pycsapi.models.search_result_hits_individual_alias_response import (
    SearchResultHitsIndividualAliasResponse,
)
from pycsapi.models.search_result_hits_individual_link_response import (
    SearchResultHitsIndividualLinkResponse,
)
from pycsapi.models.search_result_hits_source_response import (
    SearchResultHitsSourceResponse,
)
from pycsapi.models.searches_bulk_body import SearchesBulkBody
from pycsapi.models.searches_bulk_body1 import SearchesBulkBody1
from pycsapi.models.searches_businesses_body import SearchesBusinessesBody
from pycsapi.models.searches_businesses_body1 import SearchesBusinessesBody1
from pycsapi.models.searches_link_body import SearchesLinkBody
from pycsapi.models.searches_link_body1 import SearchesLinkBody1
from pycsapi.models.source_type import SourceType
from pycsapi.models.standard import Standard
from pycsapi.models.uk_births_registry_database import UKBirthsRegistryDatabase
from pycsapi.models.uk_credit_bureau import UKCreditBureau
from pycsapi.models.uk_credit_header_aml import UKCreditHeaderAml
from pycsapi.models.uk_credit_header_aml_accounts_info import (
    UKCreditHeaderAmlAccountsInfo,
)
from pycsapi.models.uk_deceased_person_database import UKDeceasedPersonDatabase
from pycsapi.models.uk_edited_voters_database import UKEditedVotersDatabase
from pycsapi.models.uk_edited_voters_database_comments import (
    UKEditedVotersDatabaseComments,
)
from pycsapi.models.uk_edited_voters_database_match import UKEditedVotersDatabaseMatch
from pycsapi.models.uk_edited_voters_database_mis_match import (
    UKEditedVotersDatabaseMisMatch,
)
from pycsapi.models.uk_edited_voters_database_warning import (
    UKEditedVotersDatabaseWarning,
)
from pycsapi.models.uk_landline_telephone_database import UKLandlineTelephoneDatabase
from pycsapi.models.ukncoa import UKNCOA
from pycsapi.models.uk_national_identity_register import UKNationalIdentityRegister
from pycsapi.models.update_decision_engine_instance_request_body import (
    UpdateDecisionEngineInstanceRequestBody,
)
from pycsapi.models.update_decision_engine_instance_request_body_with_example import (
    UpdateDecisionEngineInstanceRequestBodyWithExample,
)
from pycsapi.models.update_investigation_records_dto import (
    UpdateInvestigationRecordsDto,
)
from pycsapi.models.update_investigation_request_dto import (
    UpdateInvestigationRequestDto,
)
from pycsapi.models.update_kyc_address_details_by_the_given_address_id_for_the_supplied_profile_id_user_request import (
    UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest,
)
from pycsapi.models.update_kyc_attachments_by_attachment_id import (
    UpdateKYCAttachmentsByAttachmentId,
)
from pycsapi.models.update_kyc_attachments_by_attachment_id_request import (
    UpdateKYCAttachmentsByAttachmentIdRequest,
)
from pycsapi.models.update_kyc_attchments_by_attachment_id import (
    UpdateKYCAttchmentsByAttachmentId,
)
from pycsapi.models.update_kyc_profile_by_profile_id import UpdateKYCProfileByProfileId
from pycsapi.models.update_kyc_profile_by_profile_id_request import (
    UpdateKYCProfileByProfileIdRequest,
)
from pycsapi.models.update_key_party_by_id import UpdateKeyPartyById
from pycsapi.models.update_key_party_by_id_address import UpdateKeyPartyByIdAddress
from pycsapi.models.update_kyc_alert_contract import UpdateKycAlertContract
from pycsapi.models.validate_id_body import ValidateIdBody
from pycsapi.models.web_api_models_searches_search_result_hits_business_hit_aml_results_response import (
    WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_business_search_result_hit_response import (
    WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_adverse_media_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_adverse_media_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesAdverseMediaEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_court_response import (
    WebApiModelsSearchesSearchResultHitsEntriesCourtResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_disqualified_director_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesDisqualifiedDirectorEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_enforcement_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_enforcement_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesEnforcementEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_events_hit_event_response import (
    WebApiModelsSearchesSearchResultHitsEntriesEventsHitEventResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_insolvency_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_insolvency_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesInsolvencyEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_pep_by_association_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_pep_by_association_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesPepByAssociationEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_pep_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesPepEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_pep_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesPepEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_position_response import (
    WebApiModelsSearchesSearchResultHitsEntriesPositionResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_profile_of_interest_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_profile_of_interest_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesProfileOfInterestEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_sanction_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_sanction_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesSanctionEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_state_owned_enterprise_entry_response import (
    WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_entries_state_owned_enterprise_entry_value_response import (
    WebApiModelsSearchesSearchResultHitsEntriesStateOwnedEnterpriseEntryValueResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_address_response import (
    WebApiModelsSearchesSearchResultHitsHitAddressResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_aml_results_peps_response import (
    WebApiModelsSearchesSearchResultHitsHitAmlResultsPepsResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_aml_results_sanctions_response import (
    WebApiModelsSearchesSearchResultHitsHitAmlResultsSanctionsResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_business_alias_response import (
    WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_business_link_response import (
    WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_contact_response import (
    WebApiModelsSearchesSearchResultHitsHitContactResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_identifier_response import (
    WebApiModelsSearchesSearchResultHitsHitIdentifierResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_individual_link_response import (
    WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_hit_source_response import (
    WebApiModelsSearchesSearchResultHitsHitSourceResponse,
)
from pycsapi.models.web_api_models_searches_search_result_hits_individual_hit_aml_results_response import (
    WebApiModelsSearchesSearchResultHitsIndividualHitAmlResultsResponse,
)
