from auth import BASE_URL, s
import lxml.html

summary_payload = {
    "_search": "false",
    "nd": 1439575052983,
    "rows": 50,
    "page": 1,
    "sidx": "",
    "sord": "desc"
}

response = s.post(BASE_URL + "getVisitSummaryList.jsp?uid=127693", data=summary_payload)
doc = lxml.html.fromstring(response.content)

for row in doc.cssselect("row"):
    encounterid = row.get('id')

    response = s.get(BASE_URL + "renderVisitSummData.jsp?encounterid=%s" % encounterid)
    with open("visits/%s-1.html" % encounterid, "wb") as f: f.write(response.content)

    response = s.get(BASE_URL + "downloadVisitSummary.jsp?readable=true&encounterid=%s" % encounterid)
    with open("visits/%s-2.html" % encounterid, "wb") as f: f.write(response.content)

    response = s.get(BASE_URL + "downloadVisitSummary.jsp?encounterid=%s" % encounterid)
    with open("visits/%s.xml" % encounterid, "wb") as f: f.write(response.content)

    print("Saving visit %s" % encounterid)
    # time.sleep(1)