from misc import read_csv, generate_csv
import csv

backlink_list = read_csv('backlink.csv')

domain_list = []
with open('buyers_guide.csv', newline='') as csvfile:
        linereader = csv.reader(csvfile)
        for line in linereader:
            domain_list.append(line[0])

audit_domain_list = []
audit_backlink = []
for backlink in backlink_list:
    try:
        index = domain_list.index(backlink[3])
    except:
        index = None
    if index is not None:
        # {'backlink' : backlink, 'domain' : backlink[0]}
        audit_backlink.append(backlink)
        if backlink[3] not in audit_domain_list:
            audit_domain_list.append(domain_list[index])

with open('multiple_audit_backlinks_bg.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for backlink in audit_backlink:
        writer.writerow(backlink)

csv_columns = ['URL', 'Audited']
with open('audit_domains_bg.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for domain in audit_domain_list:
        writer.writerow({'URL': domain, 'Audited': 'Yes'})
    for domain in domain_list:
        writer.writerow({'URL': domain, 'Audited': 'No'})
