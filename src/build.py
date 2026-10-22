import csv,json,re
PAGE="https://watersystemguide.com/guides/hard-water-statistics/"
r=list(csv.DictReader(open('src/site.csv')))
FED=('U.S. EPA','USGS','CDC')
def stype(p):
    if p.startswith(FED): return 'us_federal_agency'
    if p.startswith(('Minnesota Pollution','Minnesota Department','Maryland Geological','Wisconsin DNR')): return 'us_state_agency'
    if p.startswith(('City of','Las Vegas','San Antonio','Citizens Energy','Austin Water','Seattle','Massachusetts Water','Portland Water','Denver Water','Madison Metropolitan','San Miguel')): return 'us_local_government_or_utility'
    if p.startswith(('World Health','WHO and UNICEF')): return 'intergovernmental_organization'
    if p.startswith(('Penn State','University of Minnesota')): return 'university'
    if p.startswith('Gallup'): return 'survey_publisher'
    if p.startswith(('Water Quality Association','Water Quality Research')): return 'industry_association_or_foundation'
    return 'other'
LIC={'us_federal_agency':'public_domain_us_federal',
 'us_state_agency':'government_fact_cite_source',
 'us_local_government_or_utility':'government_fact_cite_source',
 'intergovernmental_organization':'referenced_figure_source_copyright',
 'university':'referenced_figure_source_copyright',
 'survey_publisher':'referenced_figure_source_copyright',
 'industry_association_or_foundation':'referenced_figure_source_copyright'}
GEO={'Las Vegas':'Las Vegas Valley, NV, US','Phoenix':'Phoenix, AZ, US','San Antonio':'San Antonio, TX, US','Citizens Energy':'Indianapolis, IN, US','Tampa':'Tampa, FL, US','Austin':'Austin, TX, US','Seattle':'Seattle, WA, US','Massachusetts Water':'Boston area, MA, US','Portland':'Portland, OR, US','Minneapolis':'Minneapolis, MN, US','Denver':'Denver, CO, US','Maryland':'Maryland, US','Madison':'Madison area, WI, US','Waukesha':'Waukesha, WI, US','Wisconsin DNR':'Waukesha, WI, US','Lathrop':'Lathrop, CA, US','San Miguel':'San Miguel, CA, US','Minnesota':'Minnesota, US','University of Minnesota':'Minnesota, US','World Health':'Global','WHO and UNICEF':'Global'}
def geo(x):
    p=x['source_publisher']; s=x['statistic']
    if 'Morris' in s: return 'Morris, MN, US'
    if 'Waukesha' in s: return 'Waukesha, WI, US'
    if 'Minnesota' in s and p.startswith(('U.S.','USGS'))==False: return 'Minnesota, US'
    for k,v in GEO.items():
        if k in p: return v
    if x['section'].startswith('Hard water effects') and p.startswith('Water Quality Research'): return 'Laboratory test (US)'
    return 'United States'
TOPIC={'US hard water map':'hardness','How many homes':'hardness_prevalence','Water softener and home':'softener_adoption','Public water systems':'public_water_systems','Lead service':'lead_service_lines','PFAS':'pfas','Private wells':'private_wells','Chloride':'chloride_regulation','Salt use':'salt_use','Hard water effects':'appliances','Consumer concern':'consumer_concern','Global':'global_access'}
def topic(s):
    for k,v in TOPIC.items():
        if s.startswith(k): return v
NUM=re.compile(r'(?:\$|±)?\d[\d,]*(?:\.\d+)?(?:[–-]\d[\d,]*(?:\.\d+)?)?\s?(?:%|percent|million|billion|thousand|mg/L|µg/L|ppm|ppt|gallons?|grains? per gallon|gpg|g|pCi/L|tons|metric tons|people|years|percentage points|times)?')
FLAGS={
 'salt-08':'Contains a Water System Guide calculation (15.5M / 402,000 t, both USGS Minerals Yearbook 2023 Table 6), labelled as such on the live page and CSV since 2026-10-21.',
 'chloride-08':'Confirmed 2026-10-21: MMSD/AECOM 2015 study states 57% directly (Table 2-2: zeolite water softener contribution 80,500 lb/day, 57 %; text: an estimated 57% of the total chloride load). Not WSG arithmetic.',
 'hardness-05':'Source date recorded only as retrieval date (no publication date on MGS page).',
 'systems-05':'EPA ROE page footer says last updated 2023-10-04; FY2023 data. Re-check currency before press release.',
}
def yr(d):
    m=re.search(r'(19|20)\d\d',d); return m.group(0) if m else ''
out=[]
for x in r:
    st=stype(x['source_publisher']); fl=[]
    if x['id'] in FLAGS: fl.append(FLAGS[x['id']])
    if 'CDC' == x['source_publisher']: fl.append('CDC page blocks automated requests; verified via browser-style reader per WSG ledger.')
    if 'retrieved' in x['source_date'] and x['id']!='hardness-05': fl.append('No publication date on source; retrieval date only.')
    if st=='industry_association_or_foundation': fl.append('Industry-affiliated source; cite with that context.')
    m=NUM.search(x['statistic'])
    out.append(dict(id=x['id'],topic=topic(x['section']),section=x['section'],statistic=x['statistic'],
      geography=geo(x),year=yr(x['source_date']),source_date=x['source_date'],
      source_name=x['source_publisher'],source_title=x['source_title'],source_url=x['source_url'],
      source_type=st,source_license_note=LIC.get(st,'check'),
      verification_status='verified_against_primary_source_2026-10-11',review_flags=' | '.join(fl),
      wsg_page_url=PAGE,last_checked=x['retrieved']))
f=list(out[0])
w=csv.DictWriter(open('data.csv','w',newline=''),fieldnames=f);w.writeheader();w.writerows(out)
json.dump({'title':'Hard Water Map & Water Quality Statistics (2026)','publisher':'Water System Guide','version':'1.0.0','date':'2026-10-11','license':'CC-BY-4.0','source_page':PAGE,'records':out},open('data.json','w'),ensure_ascii=False,indent=1)
import collections
print(len(out),collections.Counter(o['source_type'] for o in out),sum(bool(o['review_flags']) for o in out),[o['id'] for o in out if o['source_license_note']=='check'])
