from auth import s

reports_payload = {
    "_search": "false",
    "nd": 1439582019852,
    "rows": 50,
    "page": 1,
    "sidx": "",
    "sord": "desc"
}

reports = s.post("https://mycw72.ecwcloud.com/portal9438/jsp/100mp/lab_reportsJson.jsp?", data=reports_payload).json()

for report in reports['rows']:

	single_report_payload = {
		"reason": report['cell'][2],
		"labId": report['id'],
		"result": report['cell'][3],
	}

	response = s.post("https://mycw72.ecwcloud.com/portal9438/jsp/100mp/getLabDetails.jsp?mainNav=MedRecords&ldpage=getLabDetails&pgId=lab_reports", data=single_report_payload)
	response = s.get("https://mycw72.ecwcloud.com/portal9438/jsp/100mp/renderFormData.jsp")

	with open("reports/%s.xml" % report['id'], "wb") as f: f.write(response.content)
	print("Saving report %s" % report['id'])