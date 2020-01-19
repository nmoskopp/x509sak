#	x509sak - The X.509 Swiss Army Knife white-hat certificate toolkit
#	Copyright (C) 2018-2020 Johannes Bauer
#
#	This file is part of x509sak.
#
#	x509sak is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	x509sak is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with x509sak; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>

from x509sak.tests import BaseAnalyzerTest

class GeneratedSecurityAnalyzerTests(BaseAnalyzerTest):
	def test_generated_extension_AKI_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_Malformed_Undecodable")

	def test_generated_extension_AKI_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_Malformed_UnexpectedType")

	def test_generated_extension_AKI_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_Malformed_NonDEREncoding")

	def test_generated_extension_AKI_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_TrailingData")

	def test_generated_extension_BC_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_BC_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_BC_Malformed_Undecodable")

	def test_generated_extension_BC_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_BC_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_BC_Malformed_UnexpectedType")

	def test_generated_extension_BC_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_BC_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_BC_Malformed_NonDEREncoding")

	def test_generated_extension_BC_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_BC_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_BC_TrailingData")

	def test_generated_extension_CP_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CP_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CP_Malformed_Undecodable")

	def test_generated_extension_CP_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CP_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CP_Malformed_UnexpectedType")

	def test_generated_extension_CP_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CP_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CP_Malformed_NonDEREncoding")

	def test_generated_extension_CP_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CP_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CP_TrailingData")

	def test_generated_extension_CRLDP_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_Malformed_Undecodable")

	def test_generated_extension_CRLDP_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_Malformed_UnexpectedType")

	def test_generated_extension_CRLDP_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_Malformed_NonDEREncoding")

	def test_generated_extension_CRLDP_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_TrailingData")

	def test_generated_extension_EKU_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_EKU_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_EKU_Malformed_Undecodable")

	def test_generated_extension_EKU_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_EKU_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_EKU_Malformed_UnexpectedType")

	def test_generated_extension_EKU_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_EKU_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_EKU_Malformed_NonDEREncoding")

	def test_generated_extension_EKU_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_EKU_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_EKU_TrailingData")

	def test_generated_extension_IAN_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_IAN_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_IAN_Malformed_Undecodable")

	def test_generated_extension_IAN_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_IAN_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_IAN_Malformed_UnexpectedType")

	def test_generated_extension_IAN_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_IAN_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_IAN_Malformed_NonDEREncoding")

	def test_generated_extension_IAN_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_IAN_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_IAN_TrailingData")

	def test_generated_extension_KU_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_KU_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_KU_Malformed_Undecodable")

	def test_generated_extension_KU_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_KU_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_KU_Malformed_UnexpectedType")

	def test_generated_extension_KU_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_KU_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_KU_Malformed_NonDEREncoding")

	def test_generated_extension_KU_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_KU_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_KU_TrailingData")

	def test_generated_extension_NC_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NC_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NC_Malformed_Undecodable")

	def test_generated_extension_NC_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NC_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NC_Malformed_UnexpectedType")

	def test_generated_extension_NC_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NC_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NC_Malformed_NonDEREncoding")

	def test_generated_extension_NC_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NC_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NC_TrailingData")

	def test_generated_extension_NSCT_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NSCT_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NSCT_Malformed_Undecodable")

	def test_generated_extension_NSCT_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NSCT_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NSCT_Malformed_UnexpectedType")

	def test_generated_extension_NSCT_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NSCT_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NSCT_Malformed_NonDEREncoding")

	def test_generated_extension_NSCT_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_NSCT_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_NSCT_TrailingData")

	def test_generated_extension_SAN_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SAN_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SAN_Malformed_Undecodable")

	def test_generated_extension_SAN_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SAN_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SAN_Malformed_UnexpectedType")

	def test_generated_extension_SAN_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SAN_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SAN_Malformed_NonDEREncoding")

	def test_generated_extension_SAN_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SAN_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SAN_TrailingData")

	def test_generated_extension_SKI_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SKI_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SKI_Malformed_Undecodable")

	def test_generated_extension_SKI_wrong_type(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SKI_wrong_type.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SKI_Malformed_UnexpectedType")

	def test_generated_extension_SKI_non_der(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SKI_non_der.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SKI_Malformed_NonDEREncoding")

	def test_generated_extension_SKI_trailing_data(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_SKI_trailing_data.pem", expect_present = "X509Cert_Body_X509Exts_Ext_SKI_TrailingData")

	################################################################################################################################################################################

	def test_generated_ext_AKI_caname_dirname_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dirname_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DirectoryAddress_Empty")

	def test_generated_ext_AKI_caname_dns_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dns_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DNS_Malformed")

	def test_generated_ext_AKI_caname_dns_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dns_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DNS_Unexpected")

	def test_generated_ext_AKI_caname_dns_single_label(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dns_single_label.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DNS_SingleLabel")

	def test_generated_ext_AKI_caname_dns_wc_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dns_wc_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DNS_Wildcard_NotPermitted")

	def test_generated_ext_AKI_caname_dns_whitespace(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_dns_whitespace.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_DNS_OnlyWhitespace")

	def test_generated_ext_AKI_caname_edipartyname_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_edipartyname_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_EDIPartyName_Unexpected")

	def test_generated_ext_AKI_caname_email_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_email_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_Email_Malformed")

	def test_generated_ext_AKI_caname_email_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_email_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_Email_Unexpected")

	def test_generated_ext_AKI_caname_ip_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_ip_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_IPAddress_Malformed")

	def test_generated_ext_AKI_caname_ip_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_ip_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_IPAddress_Unexpected")

	def test_generated_ext_AKI_caname_ip_private(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_ip_private.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_IPAddress_PrivateAddressSpace")

	def test_generated_ext_AKI_caname_othername_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_othername_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_OtherName_Unexpected")

	def test_generated_ext_AKI_caname_registeredid_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_registeredid_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_RegisteredID_Unexpected")

	def test_generated_ext_AKI_caname_uri_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_uri_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_URI_Malformed")

	def test_generated_ext_AKI_caname_uri_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_uri_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_URI_Unexpected")

	def test_generated_ext_AKI_caname_uri_uncommon_scheme(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_uri_uncommon_scheme.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_URI_UncommonURIScheme")

	def test_generated_ext_AKI_caname_x400address_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_x400address_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_X400Address_Unexpected")

	def test_generated_ext_AKI_caname_x400address_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_AKI_caname_x400address_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_AKI_CAName_X400Address_Unexpected")

	def test_generated_ext_CRLDP_issuer_dirname_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dirname_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DirectoryAddress_Empty")

	def test_generated_ext_CRLDP_issuer_dns_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dns_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DNS_Malformed")

	def test_generated_ext_CRLDP_issuer_dns_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dns_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DNS_Unexpected")

	def test_generated_ext_CRLDP_issuer_dns_single_label(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dns_single_label.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DNS_SingleLabel")

	def test_generated_ext_CRLDP_issuer_dns_wc_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dns_wc_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DNS_Wildcard_NotPermitted")

	def test_generated_ext_CRLDP_issuer_dns_whitespace(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_dns_whitespace.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_DNS_OnlyWhitespace")

	def test_generated_ext_CRLDP_issuer_edipartyname_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_edipartyname_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_EDIPartyName_Unexpected")

	def test_generated_ext_CRLDP_issuer_email_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_email_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_Email_Malformed")

	def test_generated_ext_CRLDP_issuer_email_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_email_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_Email_Unexpected")

	def test_generated_ext_CRLDP_issuer_ip_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_ip_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_IPAddress_Malformed")

	def test_generated_ext_CRLDP_issuer_ip_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_ip_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_IPAddress_Unexpected")

	def test_generated_ext_CRLDP_issuer_ip_private(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_ip_private.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_IPAddress_PrivateAddressSpace")

	def test_generated_ext_CRLDP_issuer_othername_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_othername_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_OtherName_Unexpected")

	def test_generated_ext_CRLDP_issuer_registeredid_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_registeredid_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_RegisteredID_Unexpected")

	def test_generated_ext_CRLDP_issuer_uri_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_uri_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_URI_Malformed")

	def test_generated_ext_CRLDP_issuer_uri_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_uri_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_URI_Unexpected")

	def test_generated_ext_CRLDP_issuer_uri_uncommon_scheme(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_uri_uncommon_scheme.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_URI_UncommonURIScheme")

	def test_generated_ext_CRLDP_issuer_x400address_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_x400address_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_X400Address_Unexpected")

	def test_generated_ext_CRLDP_issuer_x400address_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_issuer_x400address_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_CRLIssuer_X400Address_Unexpected")

	def test_generated_ext_CRLDP_point_dirname_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dirname_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DirectoryAddress_Empty")

	def test_generated_ext_CRLDP_point_dns_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dns_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DNS_Malformed")

	def test_generated_ext_CRLDP_point_dns_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dns_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DNS_Unexpected")

	def test_generated_ext_CRLDP_point_dns_single_label(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dns_single_label.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DNS_SingleLabel")

	def test_generated_ext_CRLDP_point_dns_wc_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dns_wc_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DNS_Wildcard_NotPermitted")

	def test_generated_ext_CRLDP_point_dns_whitespace(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_dns_whitespace.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_DNS_OnlyWhitespace")

	def test_generated_ext_CRLDP_point_edipartyname_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_edipartyname_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_EDIPartyName_Unexpected")

	def test_generated_ext_CRLDP_point_email_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_email_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_Email_Malformed")

	def test_generated_ext_CRLDP_point_email_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_email_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_Email_Unexpected")

	def test_generated_ext_CRLDP_point_ip_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_ip_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_IPAddress_Malformed")

	def test_generated_ext_CRLDP_point_ip_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_ip_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_IPAddress_Unexpected")

	def test_generated_ext_CRLDP_point_ip_private(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_ip_private.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_IPAddress_PrivateAddressSpace")

	def test_generated_ext_CRLDP_point_othername_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_othername_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_OtherName_Unexpected")

	def test_generated_ext_CRLDP_point_registeredid_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_registeredid_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_RegisteredID_Unexpected")

	def test_generated_ext_CRLDP_point_uri_malformed(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_uri_malformed.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_URI_Malformed")

	def test_generated_ext_CRLDP_point_uri_uncommon_scheme(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_uri_uncommon_scheme.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_URI_UncommonURIScheme")

	def test_generated_ext_CRLDP_point_x400address_empty(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_x400address_empty.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_X400Address_Unexpected")

	def test_generated_ext_CRLDP_point_x400address_ok(self):
		self._test_examine_x509test_resultcode("certs/generated/ext_CRLDP_point_x400address_ok.pem", expect_present = "X509Cert_Body_X509Exts_Ext_CRLDP_PointName_X400Address_Unexpected")
